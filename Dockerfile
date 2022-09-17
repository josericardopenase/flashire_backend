FROM python

WORKDIR /usr/src/config

COPY Pipfile Pipfile.lock ./


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pipenv
RUN pip install -U gunicorn
RUN pip install -U psycopg2
RUN pipenv install --system

COPY . .

EXPOSE 8000

ENTRYPOINT gunicorn --bind 0.0.0.0:8000 config.wsgi