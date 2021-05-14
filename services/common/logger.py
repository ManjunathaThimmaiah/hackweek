import logging

loggers = {}


def get_logger():
    global loggers
    if len(loggers):
        return loggers["logger"]
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    logger.addHandler(console)
    loggers["logger"] = logger
    return logger
