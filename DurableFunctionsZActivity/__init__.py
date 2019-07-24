import logging

def main(name: str) -> str:
    logging.warn(f"!!!Hello Activity: {name}")
    return f'Hello Activity: {name}!'