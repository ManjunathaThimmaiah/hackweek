from aiokafka import AIOKafkaProducer
from services.common.config import KafkaProducerConfig

kafka_default_topic = KafkaProducerConfig.topic


async def kafka_producer_config():
    return AIOKafkaProducer(
        bootstrap_servers=KafkaProducerConfig.bootstrap_servers)


async def kafka_send(data, topic=kafka_default_topic):
    producer = await kafka_producer_config()
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait(topic=topic, value=data)
        print("sending")
    except:
        print("logger due to kafka error")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.flush()
        await producer.stop()
