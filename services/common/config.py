class DB_Config:
    dbhost: str = ''
    dbport: int = ''
    dbname: str = ''
    dbuser: str = ''
    dbpass: str = ''


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
