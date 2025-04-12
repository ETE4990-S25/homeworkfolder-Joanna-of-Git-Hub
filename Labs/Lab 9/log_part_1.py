import logging
import logging.handlers
from datetime import timedelta, datetime
import time
import freezegun

# configurations for parent1
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
parent1 = logging.getLogger("logger_parent1")
parent1.setLevel(logging.INFO)

parent1.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename = "parent1_archived_log.log",
        when = "D",
        backupCount = 3,
    )
)

# configuration for child1
child1 = logging.getLogger("logger_parent1.child1")
child1.setLevel(logging.CRITICAL)
child1.setLevel(logging.INFO)

child1.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename = "child1_archived_log.log",
        when = "D",
        backupCount = 3,
    )
)

formatting = logging.Formatter(
    fmt = ("%(asctime)s | %(levelname)s"
           "%(message)s"
    )
)

# freezegun function
def main():
    with freezegun.freeze_time() as frozen:
        for i in range(10):
            frozen.tick(timedelta(hours = 24))
            time.sleep(0.1)
            parent1.info(f"INFO EXAMPLE")

# These guys print the level and error name on the terminal
# parent1.log(logging.CRITICAL, "No more disk space")

# parent1.critical("Computer Angry")
# parent1.error("file not found in directory")
# parent1.warning("computer overheating")
# parent1.info("You have turned on the computer")

