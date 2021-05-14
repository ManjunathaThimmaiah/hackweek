import json
from aiokafka import AIOKafkaConsumer
from services.common.config import KafkaConsumerConfig

kafka_default_topic = KafkaConsumerConfig.topic


async def kafka_consumer_config():
    return AIOKafkaConsumer(
        kafka_default_topic,
        bootstrap_servers=KafkaConsumerConfig.bootstrap_servers,
        value_deserializer=lambda v: json.loads(v)
    )


async def consume():
    consumer = await kafka_consumer_config()
    await consumer.start()
    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.value)
            data = msg.value["data"]
            return data
    finally:
        await consumer.stop()
