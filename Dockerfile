FROM python:3-alpine

MAINTAINER Jean Souza <jean.azuos@gmail.com>

COPY app.py /app/
COPY cli /app/cli
COPY controller /app/controller
COPY model /app/model
COPY views /app/views
COPY static /app/static
COPY requirements.txt /app/

WORKDIR /app

RUN apk update && \
  apk add --no-cache \
    python3-dev \
    python3 && \
    pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]