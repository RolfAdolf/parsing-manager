# pull official base image
FROM python:3.10.12-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV HOME /parsing-manager-service/

WORKDIR $HOME


# Requirements are installed here to ensure they will be cached.
ENV REQUIREMENTS $HOME/requirements
RUN mkdir REQUIREMENTS
COPY ./requirements REQUIREMENTS
RUN pip install --upgrade pip
RUN pip install -r REQUIREMENTS/prod.txt


# Copy the service code and model
COPY ./src $HOME

# Copy the start script and change rights
COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
