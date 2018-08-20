# StackOverflow-lite

StackOverflow-lite is a platform where people can ask questions and provide answers.

## Getting Started

You can clone the project using the link [Github repository](https://github.com/BarnaTB/StackOverflow-lite.git) and checkout the current output from [github pages]

## Prerequisites

The pages do not need much to be viewed as any web browser can view them from [this site](https://barnatb.github.io/StackOverflow-lite/) as long as they have internet access.

## Installing

    * Clone the project into your local repository using this command:

    `git clone https://github.com/BarnaTB/StackOverflow-lite.git`

    * Switch to the ft-api branch

    `git checkout ft-api`

    * Change directory to the cloned folder using the following command for Windows, Linux and MacOS

    `cd StackOverflow-lite`

    * If you do not have a virtual environment installed run the following command, else follow the next steps.
    `pip install virtualenv`

    * Create a virtual environment(for Windows, Linux and MacOS)

    `virtualenv venv`

    * Activate the virtual environment(Windows only)

    `source venv/Scripts/activate`

    and for Linux and MacOS

    `source venv/bin/activate`

    * Install the app dependencies.(for Windows, Linux and MacOS)

    `pip install -r requirements.txt`

    * Run the app(for Windows, Linux and MacOS)

    `python run.py`

    * Copy the url (http://127.0.0.1:5000/) into your Postman and to run any endpoint follow the table under the heading (**Endpoints**) with the url prefix (/api/v1) for each endpoint.

## Running the tests

    * To run the tests, switch to the ch-test-endpoints branch.

    `git checkout ch-test-endpoints`

    * If you don't have pytest installed, run the following command while the virtual environment is active

    `pip install pytest`

    * Run the tests.

    `py.test`

## Deployment

The pages are live on [github pages](https://barnatb.github.io/StackOverflow-lite/). They, however, have only been tested with Google Chrome and Mozilla Firefox so **no** assurance of perfomance in any other browser can be given.

## Built With

The project has been built with the following technologies so far:

    * HTML
    * CSS
    * Javascript

## Contributions

To contibute to the project, create a branch from the *develop* branch and make a PR after which your contributions may be merged into the **develop** branch

## Authors

Barnabas Tumuhairwe B

## Acknowledgements

Kudos to the developers at Andela for their unmatched support during the development of this project.
