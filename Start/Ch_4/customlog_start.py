# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def my_func():
    logging.debug("This is a logging message for a function!", extra=extdata)

# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
datestr = "%d/%m/%Y %I:%M:%S %p"
extdata = {"user": "shaun@fufilmentcrowd.com"}
logging.basicConfig(filename="output.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format=fmtstr,
                    datefmt=datestr)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)
my_func()
