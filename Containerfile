FROM python:3.6-slim

RUN apt update ; apt install -y build-essential

RUN pip install --no-cache-dir \
    "django~=2.0" djangorestframework requests \
    cython pystemmer "spacy~=2.0" \
    gunicorn

RUN python -m spacy download es

WORKDIR /app
COPY Servidor .

RUN python manage.py migrate
RUN python manage.py collectstatic --clear --noinput
RUN python fichero.py

EXPOSE 8000
CMD ["gunicorn", "servidor.wsgi:application"]
