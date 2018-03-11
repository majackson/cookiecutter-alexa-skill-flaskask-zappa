# Cookiecutter Python Alexa skill template

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) project for building a Python-based Alexa skill, using [flask](http://flask.pocoo.org/), [flask-ask](https://github.com/johnwheeler/flask-ask), and [zappa](https://github.com/Miserlou/Zappa) for deployment to AWS Lambda.

The project is fully containerised with Docker config files, with entry points through a Makefile for testing, running locally, and rebuilding the environment. It would probably be trivial to adapt the project to not use Docker, if desired.

## Project setup
You'll need to have Docker and docker-compose installed to use the Makefile build process. On Mac, I recommend using VirtualBox, Homebrew and docker-machine for this.

After cutting your project, run `make bootstrap`. You should now be able to run the project locally with `make run`.

## Tests
Tests can be run by running `make test`.

## Deployment
Deployment to AWS Lambda is managed through a zappa project, which is already configured in the project. You'll need to add your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables to `production.env`. This file is excluded from git. You should then be able to do your initial deploy to Lambda by running `make zappa ZAPPA_CMD="deploy alexa"`. Subsequent updates to this same deployment can be performed with `make zappa ZAPPA_CMD="update alexa"`.

In order to hook up your deployed lambda function to Alexa, you'll need to jump through a few extra hoops in the Amazon Developer console. These are [described here](https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa), in the "Configure the skill in the Alexa developer console and test it" section.

## Databases
If your Alexa skill requires database access, the simplest thing is to bundle a SQLite database into the deployment package (simply drop the SQLite database somewhere in the project's file system to do this). However, since AWS Lambda execution environments are disposed of some time after execution, it's important to remember that changes to this database during execution will not necessarily be persisted across invocations. If you need only read-access to your SQLite database, this will not cause any problems. If you need to save data to your SQLite database from your Alexa invocations, and have that data be retrievable later, you'll need to use another option.

The simplest option for persisting database writes is to use something like [sqlalchemy-s3sqlite](https://github.com/cariaso/sqlalchemy-s3sqlite). This works by storing your SQLite database in an S3 bucket, copying it over to your function's execution workspace when invoked, and then copying it back to S3 at the end, if the database has been modified. This works quite well, and as long as you don't expect to have to deal with concurrent writes, is a good solution.

The full-fat option for database access is to use an Amazon RDS instance. This will give you full concurrent-write functionality, and probably be marginally faster than copying a database from S3. This is trivial to set up if you don't mind leaving your RDS instance open to connections from anywhere in the world, but if you want only your trusted Lambda function to have access, you'll need to jump through [a few VPC configuration hoops](https://gist.github.com/reggi/dc5f2620b7b4f515e68e46255ac042a7).
