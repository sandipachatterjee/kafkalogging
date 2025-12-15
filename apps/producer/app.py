import os, json, time, random
from datetime import datetime
from kafka import KafkaProducer

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "events")

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    acks="all",
)

def make_event():
    return {
        "id": random.randint(100000, 999999),
        "ts": datetime.utcnow().isoformat() + "Z",
        "type": random.choice(["login", "purchase", "heartbeat"]),
        "value": random.random(),
    }

if __name__ == "__main__":
    while True:
        event = make_event()
        producer.send(TOPIC, event)
        producer.flush()
        print("sent:", event)
        time.sleep(2)
