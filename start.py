#!/usr/bin/env python3
import socket
import subprocess
import time
from settings import settings
from logger import logger


def wait_for_postgres():
    start_time = time.time()
    while time.time() - start_time < 60:
        try:
            with socket.create_connection((settings.POSTGRES_HOST, settings.POSTGRES_PORT), timeout=5):
                logger.info("PostgreSQL started")
                return True
        except (socket.timeout, ConnectionRefusedError):
            logger.info("Waiting for PostgreSQL...")
            time.sleep(1)
    raise TimeoutError("Timed out waiting for PostgreSQL")


def run_command(command):
    logger.info(f"Running command: {command}")
    process = subprocess.run(command, shell=True, check=True)
    if process.returncode != 0:
        raise RuntimeError(f"Command failed with return code {process.returncode}")


def main():
    wait_for_postgres()
    run_command('alembic upgrade head')
    run_command('uvicorn main:app --host 0.0.0.0 --port 8000')


if __name__ == "__main__":
    main()
