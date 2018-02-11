from setuptools import setup, find_packages

# import pypandoc


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='falcon-jsonify',
    author='Andrei Regiani',
    author_email='andrei.cpp@gmail.com',
    url='https://github.com/AndreiRegiani/falcon-jsonify',
    version='1.0',
    classifiers=classifiers,
    description='Falcon middleware to serialize/deserialize JSON with built-in input validation',
    # long_description = pypandoc.convert('README.md', 'rst'),
    keywords='falcon json jsonify validation validator middleware',
    packages=find_packages(include=('falcon_json*',)),
    install_requires=open('requirements.txt').read(),
    include_package_data=True,
    license='MIT',
)
