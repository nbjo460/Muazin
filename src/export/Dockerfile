FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./src/export ./src/export
COPY ../utils/elasticsearch_util utils/elasticsearch_util
COPY ../utils/kafka_util /utils/kafka_util

CMD ["python", "main.py"]