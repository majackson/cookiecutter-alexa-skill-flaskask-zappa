FROM python:3.6
ENV PYTHONUNBUFFERED 1

# install packages
RUN apt-get update
RUN apt-get install -y netcat ntpdate
RUN pip install virtualenv

RUN mkdir /code
WORKDIR /code

ADD . /code/

RUN python3 -m venv ~/.venvs/{{cookiecutter.project_slug}}venv && \
    . ~/.venvs/{{cookiecutter.project_slug}}venv/bin/activate && \
    pip install -r requirements.txt && \
    pip install -r dev_requirements.txt

