FROM python:3.11-slim-buster


ENV PYTHONUNBRFFERED 1
ENV PYHTONDONTWRITEBYTECODE 1


RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y procps \ 
    && apt-get install -y sudo\
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /requirements.txt

# COPY --chown=g1tomer:g1tomer  /etc/ssl/certs/apache-selfsigned.crt /certs/apache-selfsigned.crt
# COPY /home/g1tomer/xxxtest.txt /xxxtest.txt
RUN pip install -r requirements.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed  -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed  -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed  -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed  -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed  -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /one

ENTRYPOINT [ "/entrypoint" ]

