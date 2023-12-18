FROM python:3.12

WORKDIR /usr/src/app

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip

COPY /requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/

