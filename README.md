# StackOverflow-lite

StackOverflow-lite is a platform where people can ask questions and provide answers.

## Travis-CI

[![Build Status](https://travis-ci.org/BarnaTB/StackOverflow-lite.svg?branch=ch-test-endpoints)](https://travis-ci.org/BarnaTB/StackOverflow-lite)

## Coveralls

[![Coverage Status](https://coveralls.io/repos/github/BarnaTB/StackOverflow-lite/badge.svg?branch=ch-test-endpoints)](https://coveralls.io/github/BarnaTB/StackOverflow-lite?branch=ch-test-endpoints)

## Code Climate

[![Maintainability](https://api.codeclimate.com/v1/badges/30514c2cf23246636552/maintainability)](https://codeclimate.com/github/BarnaTB/StackOverflow-lite/maintainability)

## Getting Started

You can clone the project using the link [Github repository](https://github.com/BarnaTB/StackOverflow-lite.git).

## Prerequisites

The pages do not need much to be viewed as any web browser can view them from [this site](https://barnatb.github.io/StackOverflow-lite/) as long as they have internet access.

## Installing

* Clone the project into your local repository using this command:

    `git clone https://github.com/BarnaTB/StackOverflow-lite.git`

* Switch to the master branch

    `git checkout master`

## Features

* Post a question
* Fetch a single question
* Fetch all questions
* Post an answer

## Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/questions|Create a question
GET|api/v1/questions/questionId|Fetch a specific question
GET|api/v1/questions|Fetch all questions
POST|/questions/questionId/answers|Add an answer

## Tools Used

* [Flask](http://flask.pocoo.org/) - Web microframework for Python
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python

## Running the tests

There are currently no automated tests for this project.

## Deployment

The pages are live on [github pages](https://barnatb.github.io/StackOverflow-lite/). They, however, have only been tested with Google Chrome and Mozilla Firefox so **no** assurance of perfomance in any other browser can be given.

## Built With

The project has been built with the following technologies so far:

* HTML
* CSS
* Javascript
* Python/Flask

## Contributions

To contibute to the project, create a branch from the *develop* branch and make a PR after which your contributions may be merged into the **develop** branch

## Authors

Barnabas Tumuhairwe B

## Acknowledgements

Kudos to the developers at Andela for their unmatched support during the development of this project.
