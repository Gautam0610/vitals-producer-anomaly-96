import os
import time
import random
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

output_topic = os.getenv("OUTPUT_TOPIC")
sasl_username = os.getenv("SASL_USERNAME")
sasl_password = os.getenv("SASL_PASSWORD")
interval_ms = int(os.getenv("INTERVAL_MS"))

producer = KafkaProducer(
    bootstrap_servers='your_bootstrap_servers',  # Replace with your Kafka brokers
    sasl_mechanism='PLAIN',
    security_protocol='SASL_SSL',
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password,
    value_serializer=lambda x: str(x).encode('utf-8')
)

def generate_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Normal body temp
    heart_rate = random.randint(60, 100)  # Normal heart rate
    systolic = random.randint(110, 140)  # Normal systolic pressure
    diastolic = random.randint(70, 90)  # Normal diastolic pressure
    breaths = random.randint(12, 20)  # Normal breaths per minute
    oxygen_saturation = random.randint(95, 100)  # Normal oxygen saturation
    blood_glucose = random.randint(70, 140)  # Normal blood glucose

    # Introduce anomalies
    if random.random() < 0.01:  # 1% chance of anomaly
        heart_rate = random.randint(150, 220)  # Extremely high heart rate
        breaths = random.randint(30, 50) # Extremely high breaths per minute

    return {
        "body_temp": body_temp,
        "heart_rate": heart_rate,
        "systolic": systolic,
        "diastolic": diastolic,
        "breaths": breaths,
        "oxygen_saturation": oxygen_saturation,
        "blood_glucose": blood_glucose
    }

if __name__ == "__main__":
    while True:
        vitals = generate_vitals()
        print(f"Sending vitals: {vitals}")
        producer.send(output_topic, value=vitals)
        time.sleep(interval_ms / 1000)
