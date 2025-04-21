import logging
import logging.handlers
from datetime import timedelta, datetime
import time
import freezegun
import json
import random

# configurations for application
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
application = logging.getLogger("logger_application")
application.setLevel(logging.INFO)
application.setLevel(logging.WARNING)
application.setLevel(logging.ERROR)
application.setLevel(logging.CRITICAL)

a_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "application_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for ui
ui = logging.getLogger("logger_application.ui")
ui.setLevel(logging.CRITICAL)
ui.setLevel(logging.INFO)
ui.setLevel(logging.WARNING)
ui.setLevel(logging.ERROR)

ui_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "ui_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for utils
utils = logging.getLogger("logger_application.ui.utils")
utils.setLevel(logging.CRITICAL)
utils.setLevel(logging.INFO)
utils.setLevel(logging.WARNING)
utils.setLevel(logging.ERROR)

utils_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "utils_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for frontend
frontend = logging.getLogger("logger_application.ui.utils.frontend")
frontend.setLevel(logging.CRITICAL)
frontend.setLevel(logging.WARNING)
frontend.setLevel(logging.ERROR)
frontend.setLevel(logging.INFO)

frontend_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "frontend_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for backend
backend = logging.getLogger("logger_application.ui.utils.backend")
backend.setLevel(logging.CRITICAL)
backend.setLevel(logging.WARNING)
backend.setLevel(logging.ERROR)
backend.setLevel(logging.INFO)

backend_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "backend_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# initializing formatter
formatting = logging.Formatter(
    fmt = ("%(asctime)s | %(name)s | " 
           "%(levelname)s | %(message)s"
    )
)

#adding handlers
a_handler.setFormatter(formatting)
ui_handler.setFormatter(formatting)
utils_handler.setFormatter(formatting)
frontend_handler.setFormatter(formatting)
backend_handler.setFormatter(formatting)
application.addHandler(a_handler)
ui.addHandler(ui_handler)
utils.addHandler(utils_handler)
frontend.addHandler(frontend_handler)
backend.addHandler(backend_handler)

#trying to use JSON to read/generate error messages
def error_log_json(level):
    with open("error_dictionary.json") as f:
        file = json.load(f)

    x = str(random.randint(1,4))

    for key, value in file[level].items():
        # if key == x:
        return file[level][key]

# freezegun function
def main():
    with freezegun.freeze_time() as frozen:
        for i in range(10):
            frozen.tick(timedelta(hours = 24))
            time.sleep(0.1)

            # These guys print the level and error name
            application.info(error_log_json("info"))
            ui.critical(error_log_json("critical"))
            utils.error(error_log_json("error"))
            frontend.warning(error_log_json("warning"))
            backend.critical(error_log_json("critical"))

            
            



if __name__ == "__main__":
    main()