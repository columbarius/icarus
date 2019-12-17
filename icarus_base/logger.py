import logging
from logging import getLogger, FileHandler, Formatter, StreamHandler
# from os import pa

LOG_FORMAT = Formatter("%(asctime)s [%(levelname)s]: %(message)s")
LOG_LEVEL = logging.WARNING
LOG_FILE = "./logs/icarus.log"

logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", datefmt='%Y/%m/%d %H:%M:%S', level=logging.ERROR)
console_logger = getLogger("console_logger")
console_handler = logging.StreamHandler()
console_logger.addHandler(console_handler)
console_logger.setLevel(LOG_LEVEL)
console_logger.propagate = True
icarus_logger = getLogger("icarus_logger")
icarus_logger.setLevel(LOG_LEVEL)
icarus_file_handler = FileHandler(LOG_FILE)
icarus_file_handler.setLevel(LOG_LEVEL)
icarus_file_handler.setFormatter(LOG_FORMAT)
icarus_logger.addHandler(icarus_file_handler)
icarus_logger.propagate = False



