class DB_Config:
    dbhost: str = 'pg-27a6b2a5-manjunatha-1738.aivencloud.com'
    dbport: int = 15659
    dbname: str = 'defaultdb'
    dbuser: str = 'avnadmin'
    dbpass: str = 'a37e8w81ho5i4766'


class SiteMonitorDataConfig:
    sitename: str
    status_code: int
    url: str
    has_regexp: bool


class SiteUrlAndMatcherConfig:
    source_url: str = 'http://google.com'
    website_matcher: str = 'google'


class KafkaProducerConfig:
    bootstrap_servers: str = 'localhost:9092'
    topic: str = 'monitor'


class KafkaConsumerConfig:
    bootstrap_servers: str = 'localhost:9092'
    topic: str = 'monitor'
