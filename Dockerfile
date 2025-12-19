FROM python:3.9-slim-buster

WORKDIR /app

COPY producer.py ./
COPY .env ./
COPY README.md ./

RUN pip install kafka-python python-dotenv

CMD ["python", "producer.py"]