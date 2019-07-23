import logging
import azure.functions as func


def main(context: str) -> str:
    logging.info("context" + context)
