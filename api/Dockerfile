
FROM python:3-alpine3.7

WORKDIR /app
RUN pip install pipenv

ADD . /app
RUN pip install $(pipenv lock --requirements)

CMD gunicorn -b '0.0.0.0:5000' app:app
