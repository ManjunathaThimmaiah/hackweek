import aiohttp
import json
import re
from typing import Optional
from services.common.config import *

url = SiteUrlAndMatcherConfig.source_url
regex = SiteUrlAndMatcherConfig.website_matcher
kafka_topic = KafkaProducerConfig.topic


async def website_monitor_data(url=url, regex: Optional[str] = regex):
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.request(method="GET", url=url)
            html = await response.text()
            matcher = None
            if regex is not None:
                matcher = re.search(regex, html) is not None

            data = {
                "data": {
                    "id": 1,
                    "status_code": response.status,
                    "url": url,
                    "regex_matching": matcher,
                }
            }
            return json.dumps(data).encode('utf-8')
        except TimeoutError:
            pass


# async def main(urls):
#     tasks = []
#     for url in urls:
#         tasks = await website_monitor_data(url)
#     await asyncio.gather(*tasks)
