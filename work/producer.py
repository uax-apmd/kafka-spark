from confluent_kafka import Producer
import sys

bootstrap_servers = "kafka:9092"

producer = Producer(
    {"bootstrap.servers": bootstrap_servers, "client.id": "python-console-producer"}
)

topic = "datosCSV"

print(
    f"Console producer running. Type messages and press Enter to send to topic {topic}. CTRL+C to exit."
)

try:
    for line in sys.stdin:

        line = line.strip()
        if not line:
            continue

        producer.produce(topic, value=line)
        producer.flush()

        print(f"Sent: {line}")

except KeyboardInterrupt:
    pass

print("Exiting producer.")
