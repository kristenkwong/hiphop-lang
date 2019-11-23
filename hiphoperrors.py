class hiphop_error():

    def __init__(self, error_type, line_num, error_msg):

        self.error_type = error_type
        self.line_num = line_num
        self.error_msg = error_msg

    def printError(self):
        print("{} (line {}): {}".format(self.error_type, self.line_num, self.error_msg))

