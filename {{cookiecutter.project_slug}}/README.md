# {{cookiecutter.project_name}}

## Overview

The {{cookiecutter.project_name}} project is a python3/flask/flask-ask/dqlite/docker project.

## Developer Setup

The project is fully dockerised. There are a few ways to set this up on a Mac, but I'd recommend using `docker-machine`. You'll also need homebrew, VirtualBox, docker and docker-compose.

## Tests

Run tests with `make test`.

## Development Server

To run a development server, use `make run`. The server will be up on your docker VM (get this with `docker-machine ip default`), port 80.

## Changing Development Environment

If any of the libraries in `requirements.txt` or `dev_requirements.txt` are changed, `make bootstrap` will have to be rerun before they are reflected in runs of `make test` or `make run`.
