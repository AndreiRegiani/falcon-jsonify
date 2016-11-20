import json
import re

import falcon


class Middleware(object):

    def __init__(self, help_messages=True):
        self.debug = bool(help_messages)


    def bad_request(self, title, description):
        if self.debug:
            raise falcon.HTTPBadRequest(title, description)
        else:
            raise falcon.HTTPBadRequest()


    def get_json(self, field, dtype=None, min=None, max=None, default=None, match=None):
        value = None

        if default:
            value = default

        elif not field in self.req.json:
            self.bad_request("Missing JSON field",
                             "Field '{}' is required".format(field))
        else:
            value = self.req.json[field]

        # built-in validations
        err_title = "Validation error"

        if dtype:
            if dtype == str and type(value) == unicode:
                pass

            elif type(value) is not dtype:
                msg = "Data type for '{}' is '{}' but should be '{}'"
                self.bad_request(err_title,
                                 msg.format(field, type(value).__name__,  dtype.__name__))

        if type(value) == unicode:
            if min and len(value) < min:
                self.bad_request(err_title,
                                 "Minimum length for '{}' is '{}'".format(field, min))

            if max and len(value) > max:
                self.bad_request(err_title,
                                 "Maximum length for '{}' is '{}'".format(field, max))

        elif type(value) in (int, float):
            if min and value < min:
                self.bad_request(err_title,
                                 "Minimum value for '{}' is '{}'".format(field, min))

            if max and value > max:
                self.bad_request(err_title,
                                 "Maximum value for '{}' is '{}'".format(field, max))

        if match and not re.match(match, re.escape(value)):
            self.bad_request(err_title,
                             "'{}' does not match Regex: {}".format(field, match))

        return value


    def process_request(self, req, resp):
        if not req.content_length:
            return

        body = req.stream.read()
        req.json = {}
        self.req = req
        req.get_json = self.get_json

        try:
            req.json = json.loads(body.decode('utf-8'))

        except ValueError:
            self.bad_request("Malformed JSON", "Syntax error")

        except UnicodeDecodeError:
            self.bad_request("Invalid encoding", "Could not decode as UTF-8")


    def process_response(self, req, resp, resource, req_succeeded):
        try:
            resp.data = json.dumps(resp.json)
        except AttributeError:
            pass
