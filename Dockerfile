FROM python:3.8.2-alpine3.11

WORKDIR /app

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.11/main/ \
        mariadb-dev=10.4.13-r0 g++=9.2.0-r4

RUN mkdir /logs && chmod o+w /logs

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD python manage.py migrate && python manage.py runserver 0:8080
