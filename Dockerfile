FROM python:3.11-alpine3.15

WORKDIR /src
COPY src /src

EXPOSE 8000

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



