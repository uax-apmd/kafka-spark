from confluent_kafka import Producer
import sys
import logging

bootstrap_servers = "kafka:9092"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <topic>")
    sys.exit(1)

topic = sys.argv[1]

producer = Producer(
    {"bootstrap.servers": bootstrap_servers, "client.id": "python-console-producer"}
)

logging.info(
    "Console producer running. Sending messages to topic '%s'. Type messages and press Enter. CTRL+C to exit.",
    topic,
)

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            producer.produce(topic, value=line)
            producer.flush()
            logging.info("Sent message to topic '%s': %s", topic, line)
        except BufferError as e:
            logging.error("Buffer error while sending to topic '%s': %s", topic, e)
        except Exception as e:
            logging.error("Unexpected error while sending to topic '%s': %s", topic, e)

except KeyboardInterrupt:
    logging.info("Interrupted by user (CTRL+C).")

logging.info("Exiting producer for topic '%s'.", topic)
