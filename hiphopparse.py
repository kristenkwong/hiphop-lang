# To parse a HIPHOP program
from hiphoptypes import *
import sys

class Parser():

    def __init__(self):

        return

    def parse(self, filename):

        f = open(filename, "r")
        lines = f.readlines()
        line_num = 1
        for line in lines:
            print("Parsing line {}: {}".format(line_num, line.strip()))

            tokens = line.split()
            if tokens[0] == "open":
                open_expr = is_open_expr(line)
                if (isinstance(open_expr, hiphop_error)):
                    error_out(open_expr, line_num)
                else:
                    val = open_expr.evaluate()
                    if (isinstance(val, hiphop_error)):
                        error_out(val, line_num)
            elif tokens[0] == "apply":
                apply_expr = is_apply_expr(line)
                if (isinstance(apply_expr, hiphop_error)):
                    error_out(apply_expr, line_num)
                else:
                    val = apply_expr.evaluate()
                    if (isinstance(val, hiphop_error)):
                        error_out(val, line_num)
            elif tokens[0] == "save":
                save_expr = is_save_expr(line)
                if (isinstance(save_expr, hiphop_error)):
                    error_out(save_expr, line_num)
                else:
                    val = save_expr.evaluate()
                    if (isinstance(val, hiphop_error)):
                        error_out(val, line_num)
            else:
                pass

            line_num += 1

def error_out(hiphop_error, line_num):
    hiphop_error.line_num = line_num
    hiphop_error.printError()
    sys.exit()