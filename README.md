# hackoregon_housing

![PyPI version](https://badge.fury.io/py/2019-housing-backend.svg) | [![Build Status](https://travis-ci.org/hackoregon/2019-housing-backend.svg?branch=master)](https://travis-ci.org/hackoregon/2019-housing-backend)

This projects maps the state of the housing market in Oregon using data from Harvard Joint Center for Housing Studies, Neighborhood Change Database, and Home Mortgage Disclosure Act data.

# Documentation

The full documentation is at http://hackoregon.github.io/2019-housing-backend


# Features

> -   TODO (add what your project does)

# Data Sources

This API package in this repo is based on the Data Science work in the following projects:

* [2019-housing-data-science](https://github.com/hackoregon/2019-housing-data-science)

# Quickstart to install package in your own Django Project (Non-Hack Oregon Workflow)

* Install hackoregon_housing:  
  `pip install hackoregon_housing`

* Add subpackages to your `INSTALLED_APPS`:

  ```python
  INSTALLED_APPS = [     
                      ...     
                      'api',     
                      ...
                    ]
  ```

* Add hackoregon_housing's URL patterns:

  ```python
  from hackoregon_housing.api
  import urls as api_urls   

  urlpatterns = [     
                  ...     
                  url(r'^', include(api_urls)),     
                  ...
                ]
  ```

* Setup your database with a matching schema

* Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Credits

Tools used in rendering this package:

 * [Cookiecutter](https://github.com/audreyr/cookiecutter)
 * [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
