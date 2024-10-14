import sys

import typer

from src.config import load_config
from src.logger import initialize_logger, logger
from src.client.hello import HelloClient
from src.usecase.hello import HelloUsecase

app = typer.Typer()


def main():
    config = load_config()
    initialize_logger()
    helloClient = HelloClient()
    helloUsecase = HelloUsecase(config, helloClient)

    option1: str = typer.Option("option1")

    def hello(
        name: str,
        option1: str = option1,
    ):
        # uv run main.py hello john --option1=optionxxx
        logger.info(f"hello {name} with {option1}")
        helloUsecase.say(name, option1)

    def err():
        # uv run main.py err
        logger.info("call err def")
        raise Exception("Error Example")

    _ = app.command()(hello)
    _ = app.command()(err)

    try:
        app(standalone_mode=False)
    except Exception as e:
        logger.error("Exception: %s", e, exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    logger.info("Start")
    main()
    logger.info("End")
