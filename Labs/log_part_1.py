import logging
import logging.handlers
from datetime import timedelta, datetime
import time
import freezegun

# configurations for parent1
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
parent1 = logging.getLogger("logger_parent1")
parent1.setLevel(logging.INFO)
formatting = logging.Formatter(
    fmt = ("%(asctime)s | %(levelname)s"
           "%(message)s"
    )
)

parent1.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename = "parent1_archived_log.log",
        when = "D",
        backupCount = 3,
    )
)


# These guys print the level and error name on the terminal
# parent1.log(logging.CRITICAL, "No more disk space")

# parent1.critical("Computer Angry")
# parent1.error("file not found in directory")
# parent1.warning("computer overheating")
# parent1.info("You have turned on the computer")

