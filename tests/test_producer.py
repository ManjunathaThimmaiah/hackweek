import asyncio
import pytest
from services.producer.kafka_producer import kafka_send
from services.monitor.web_monitor import website_monitor_data


def test_kafka_send_exceptions():
    # Given
    asyncio.run(kafka_send())

    # Then
    try:
        res = asyncio.run(kafka_send())
        assert False
    except:
        pytest.raises(Exception)
        assert False


def test_kafka_send():
    # Given
    stats = asyncio.run(website_monitor_data())

    # When
    res = asyncio.run(kafka_send(stats))

    # Then
    assert res == None
