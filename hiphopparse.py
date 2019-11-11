# To parse a HIPHOP program
from hiphoptypes import *
from hiphopinterp import Interpreter

class Parser():

    def __init__(self, interpreter):

        self.interpreter = interpreter 

    def parse(self, filename):

        f = open(filename, "r")
        lines = f.readlines()
        line_num = 1
        for line in lines:
            print(line.strip())


            open_expr = is_open_expr(line)
            if (isinstance(open_expr, hiphop_error)):
                open_expr.line_num = line_num
                open_expr.printError()
            else:
                self.interpreter.interp(open_expr)

            line_num += 1