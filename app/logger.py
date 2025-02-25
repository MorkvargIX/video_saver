import logging
import colorlog

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(green)s %(message)s",
    datefmt=None,
    log_colors={
        "DEBUG":    "cyan",
        "INFO":     "cyan",
        "WARNING":  "yellow",
        "ERROR":    "red",
        "CRITICAL": "purple",
    }
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

