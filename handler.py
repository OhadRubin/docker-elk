import requests
import logging
from logstash import formatter
from loguru import logger


class LogstashFlaskHandler(logging.Handler):
    
    def __init__(self,
                 host="localhost",
                 port=5557,
                 username="your_username",
                 password="your_password"
                 
                 ) -> None:
        super(LogstashFlaskHandler, self).__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.formatter = formatter.LogstashFormatterVersion1()
        

    def emit(self, record):
        
        url = f'http://{self.host}:{self.port}/log'
        headers = {'Username': self.username, 'Password': self.password}
        requests.post(url, data=self.formatter.format(record), headers=headers)


handler = LogstashFlaskHandler(host='localhost',
                               port=5557,
                               username='your_username',
                               password='your_password')
logger.add(handler, format="{time} {level} {message}")
