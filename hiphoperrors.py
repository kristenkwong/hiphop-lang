class Error(Exception):
    """"base class for exceptions"""
    pass

class hiphop_error(Error):

    def __init__(self, error_type, error_msg):

        self.error_type = error_type
        self.line_num = -1
        self.error_msg = error_msg

    def printError(self):
        print("{} (line {}): {}".format(self.error_type, self.line_num, self.error_msg))

class hiphop_eval_error(Error):
    def __init__(self, error_type, error_msg):
        self.error_type = error_type
        self.msg = error_msg
        self.line_num = -1

class file_error(Error):
    def __init__(self, error_type, error_msg):
        self.error_type = error_type
        self.msg = error_msg