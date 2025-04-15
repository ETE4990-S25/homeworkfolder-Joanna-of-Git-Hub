import logging
import logging.handlers
from datetime import timedelta, datetime
import time
import freezegun
import json

# configurations for application
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
application = logging.getLogger("logger_application")
application.setLevel(logging.INFO)

a_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "application_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for ui
ui = logging.getLogger("logger_application.ui")
ui.setLevel(logging.CRITICAL)
ui.setLevel(logging.INFO)

ui_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "ui_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for utils
utils = logging.getLogger("logger_application.ui.utils")
utils.setLevel(logging.CRITICAL)
utils.setLevel(logging.INFO)

utils_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "utils_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# configuration for frontend
frontend = logging.getLogger("logger_application.ui.utils.frontend")
frontend.setLevel(logging.CRITICAL)
frontend.setLevel(logging.WARNING)
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
backend.setLevel(logging.INFO)

backend_handler = logging.handlers.TimedRotatingFileHandler(
        filename = "backend_archived_log.log",
        when = "D",
        backupCount = 3,
    )

# initializing formatter
formatting = logging.Formatter(
    fmt = ("%(asctime)s | %(levelname)s |"
           " %(message)s"
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
def error_log():
    with open("error_dictionary.json") as f:
        file = json.load(f)
    errors_dict = json.dumps(file, indent=2)

    levels = [application, ui, utils, frontend, backend]

# freezegun function
def main():
    with freezegun.freeze_time() as frozen:
        for i in range(10):
            frozen.tick(timedelta(hours = 24))
            time.sleep(0.1)
            application.info(f"INFO EXAMPLE") # the only info that shows up as is in the logs

            # These guys print the level and error name on the terminal
            # application.log(logging.CRITICAL, "No more disk space")

            # ui.critical("Computer Angry")
            # ui.error("file not found in directory")
            # application.warning("computer overheating")
            # application.info("You have turned on the computer")

            
            error_log()



if __name__ == "__main__":
    main()