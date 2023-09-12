FROM python:alpine3.7

COPY . /flaskapp

WORKDIR /flaskapp

RUN pip install pipenv

RUN pipenv --python python

RUN pipenv install

EXPOSE 5050

CMD pipenv run python ./app.py