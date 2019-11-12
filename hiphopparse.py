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
                    open_expr.line_num = line_num
                    open_expr.printError()
                    sys.exit()
                else:
                    open_expr.evaluate()
            elif tokens[0] == "apply":
                apply_expr = is_apply_expr(line)
                if (isinstance(apply_expr, hiphop_error)):
                    apply_expr.line_num = line_num
                    apply_expr.printError()
                    sys.exit()
                else:
                    apply_expr.evaluate()
            elif tokens[0] == "save":
                save_expr = is_save_expr(line)
                if (isinstance(save_expr, hiphop_error)):
                    save_expr.line_num = line_num
                    save_expr.printError()
                    sys.exit()
                else:
                    save_expr.evaluate()
            else:
                pass

            line_num += 1