# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY . /usr/src/app
RUN pip install -r app/requirements/dev.txt

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker/dev/entrypoint.sh"]
