FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && mkdir /code \
    && mkdir /backup \
    && apt-get install -y cron
WORKDIR /code
ADD requirements.txt /code/
ADD cron/django-conf /etc/cron.d/
ADD cron /code/cron/
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt \
    && chmod +x /code/cron/init.sh \
    && /code/cron/init.sh
