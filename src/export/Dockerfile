FROM python:3.11

WORKDIR /app

COPY ./src/export ./src/export
RUN pip3 install -r /src/export/requirements.txt
COPY ../src/utils/elasticsearch_util /src/utils/elasticsearch_util
COPY ../src/utils/kafka_util /src/utils/kafka_util
COPY ../src/utils/config_retriever.py /src/utils/config_export.py
COPY ../src/utils/logger.py /src/utils/logger.py

CMD ["python", "main.py"]