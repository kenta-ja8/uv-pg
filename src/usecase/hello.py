from src.logger import logger
from src.config import Config
from src.client.hello import HelloClient


class HelloUsecase:
    config: Config
    helloClient: HelloClient

    def __init__(self, config: Config, helloClient: HelloClient):
        self.config = config
        self.helloClient = helloClient

    def say(self, userName: str, option1: str):
        greeting = self.helloClient.get_greeting()
        logger.info(
            f"{greeting} {self.config.SAMPLE_BASE_URL} by {userName} with {option1}"
        )
