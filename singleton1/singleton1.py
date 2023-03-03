class Logger():

    def __init__(self, file_name):
        self.file_name = file_name

    def _write_log(self, level, msg):
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}]{1} \n".format(level, msg))

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warning(self, msg):
        self._write_log("WARNING", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)


# def critical_log_messages(msg):
#     with open("file.txt", "a") as log_file:
#         log_file.write("[CRITICAL]{0}\n".format(msg))


# def error_log_messages(msg):
#     with open("file.txt", "a") as log_file:
#         log_file.write("[ERRORs]{0}\n".format(msg))


# def warning_log_messages(msg):
#     with open("file.txt", "a") as log_file:
#         log_file.write("[WARNING]{0}\n".format(msg))


# def info_log_messages(msg):
#     with open("file.txt", "a") as log_file:
#         log_file.write("[INFO]{0}\n".format(msg))


# def debug_log_messages(msg):
#     with open("file.txt", "a") as log_file:
#         log_file.write("[DEBUG]{0}\n".format(msg))
