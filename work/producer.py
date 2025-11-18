from confluent_kafka import Producer
import sys

conf = {"bootstrap.servers": "kafka:9092", "client.id": "python-console-producer"}

producer = Producer(conf)

topic = "datosCSV"

print("Console producer running. Type messages and press Enter. CTRL+C to exit.\n")

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
