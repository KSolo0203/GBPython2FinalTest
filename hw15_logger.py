import logging

FORMAT = "{levelname} - {asctime}\n{msg}"

logging.basicConfig(
    filename=f"{__name__}.log",
    filemode="a",
    encoding="utf-8",
    format=FORMAT,
    style="{",
    level=logging.INFO
)

hw15_logger = logging.getLogger("main")