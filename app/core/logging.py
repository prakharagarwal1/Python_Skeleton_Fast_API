import logging
import colorlog


handler = colorlog.StreamHandler()

handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(asctime)s | %(log_color)s%(levelname)s%(reset)s | "
        "%(name)s | %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
)

logger = logging.getLogger("ai_assistant")
logger.setLevel(logging.DEBUG)

logger.handlers.clear()
logger.addHandler(handler)
logger.propagate = False


# import logging

# logger = logging.getLogger("ai_assistant")

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
# )