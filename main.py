import logging

# logging.info("hi info here")
# logging.critical("very bad ")
#
# create a logger
#
mylogger = logging.getLogger('My_logger')
mylogger.warning("from mylogger warning") # still posted on terminal
mylogger.info("should not appear on terminal")
mylogger.error("errors!")
mylogger.critical("OOPS! failed")

# handler is logging destination, aka file path
myhandler = logging.FileHandler("nancy.log")
mylogger.addHandler(myhandler)

#
# set a custom Formatter for handler, so that log file is easy to read
#
formatter = logging.Formatter(logging.BASIC_FORMAT)
myhandler.setFormatter(formatter)

mylogger.setLevel(logging.WARNING)

#
# with a file handler, logging is posted to the file instead
#
mylogger.debug("debugging is not on file")
mylogger.info('THis is not on file, level too low')
mylogger.error('How about some errors on file')
mylogger.warning("warning should be on file")
mylogger.critical("All files are gone!!!")

