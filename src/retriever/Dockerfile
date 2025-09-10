FROM python:3.11

WORKDIR /app

COPY ../src/retriever ./src/retriever
RUN pip3 install -r ./src/retriever/requirements.txt
COPY ../src/utils/elasticsearch_util ./src/utils/elasticsearch_util
COPY ../src/utils/kafka_util ./src/utils/kafka_util
COPY ../src/utils/config_retriever.py ./src/utils/config_retriever.py
COPY ../src/utils/mongo ./src/utils/mongo
COPY ../src/utils/logger.py ./src/utils/logger.py

CMD ["python", "src/retriever/main.py"]