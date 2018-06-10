
FROM python:3-alpine3.7

WORKDIR /app
RUN pip install pipenv

ADD . /app
RUN pip install $(pipenv lock --requirements)

CMD flask run --host 0.0.0.0
