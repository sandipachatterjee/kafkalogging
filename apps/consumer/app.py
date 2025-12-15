import os, json
from kafka import KafkaConsumer

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "events")
GROUP = os.getenv("KAFKA_GROUP", "capstone-consumers")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP,
    group_id=GROUP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)

if __name__ == "__main__":
    print(f"Listening topic={TOPIC} bootstrap={BOOTSTRAP} group={GROUP}")
    for msg in consumer:
        print("consumed:", msg.value)
