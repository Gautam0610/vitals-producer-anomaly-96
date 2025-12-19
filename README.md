# Vitals Producer Anomaly

This project generates random vitals data with occasional anomalies and pushes it to a Kafka topic.

## Prerequisites

*   Python 3.6+
*   Kafka broker
*   `.env` file with the following variables:
    *   `OUTPUT_TOPIC`: Kafka topic to send data to
    *   `SASL_USERNAME`: SASL username for Kafka authentication
    *   `SASL_PASSWORD`: SASL password for Kafka authentication
    *   `INTERVAL_MS`: Interval in milliseconds between data generation

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/vitals-producer-anomaly-96.git
    cd vitals-producer-anomaly-96
    ```

2.  Install dependencies:

    ```bash
    pip install kafka-python python-dotenv
    ```

3.  Run the producer:

    ```bash
    python producer.py
    ```

## Docker

1.  Build the Docker image:

    ```bash
    docker build -t vitals-producer .
    ```

2.  Run the Docker container:

    ```bash
    docker run -d -e OUTPUT_TOPIC=<your_topic> -e SASL_USERNAME=<your_username> -e SASL_PASSWORD=<your_password> -e INTERVAL_MS=<interval_ms> vitals-producer
    ```