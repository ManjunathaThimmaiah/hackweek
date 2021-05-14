import asyncio
from services.consumer.kafka_consumer import consume
from services.monitor.web_monitor import website_monitor_data
from db.db_communicator import database_writing
from services.common import logger
from services.producer.kafka_producer import kafka_send

log = logger.get_logger()


def aiven():
    stats = asyncio.run(website_monitor_data())
    asyncio.run(kafka_send(data=stats))


def start_consumer_new():
    data = asyncio.run(consume())
    asyncio.run(database_writing(data))


if __name__ == '__main__':
    start_consumer_new()
    aiven()
