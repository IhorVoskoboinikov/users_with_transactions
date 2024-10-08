import json
import logging
from logging import Formatter
from datetime import datetime, timezone


class JsonFormatter(Formatter):
    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record):
        level = record.levelname
        log_time = datetime.fromtimestamp(record.created, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S %Z"
        )

        log_message = {"time": log_time, "level": level, "message": record.getMessage()}

        return json.dumps(log_message, ensure_ascii=False)


logger = logging.getLogger("my_logger")

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger.handlers = [handler]
logger.setLevel(logging.DEBUG)
