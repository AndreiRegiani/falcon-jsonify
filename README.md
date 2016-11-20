# falcon-jsonify

 [Falcon](https://github.com/falconry/falcon) middleware to serialize/deserialize JSON with built-in input validation.

```
pip install falcon-jsonify
```

Add the middleware into your project:

```python
import falcon_jsonify
falcon.API(middleware=[falcon_jsonify.Middleware(help_messages=True)])
```

## Getting Started


### Responses

```python
resp.json = {"my_field": "Hello World"}
```

### Requests

```python
value = req.get_json('my_field')  # required field
```
* Response `400 Bad Request` is returned if field does not exist in the request body.
* Full deserialized dict can be accesed at `req.json` *(without validations)*, e.g. `req.json['my_field']`.


### Built-in validations

* `dtype`, `min`, `max`

```python
req.get_json('name', dtype=str, min=1, max=16)  # min/max char length
req.get_json('age', dtype=int, min=18, max=99)  # min/max numeric value
req.get_json('amount', dtype=float, min=0.0)
req.get_json('approved', dtype=bool)
```
* Response `400 Bad Request` is returned if a validation fails.

### Additional parameters ###

* `default`, `match`

```python
# make a field optional with default value
req.get_json('country_code', dtype=str, default="USA", max=3, min=3)

# custom validation with Regular Expressions
req.get_json('email', match="[^@]+@[^@]+\.[^@]+")
```

### Error responses

Example:

```javascript
HTTP/1.1 400 Bad Request

{
  "title": "Validation error",
  "description": "Minimum value for 'age' is '18'"
}
```

For proprietary APIs on production environment set `Middleware(help_messages=False)` to hide such error messages *(missing fields, validation checks, malformed JSON)*. For public APIs it's nice to keep them enabled.
