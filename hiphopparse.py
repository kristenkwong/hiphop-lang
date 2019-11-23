# To parse a HIPHOP program
from hiphoptypes import *
from hiphoperrors import hiphop_error
import sys

class Parser():

    def __init__(self):

        return

    def parse_line(self, expr):

        tokens = expr.split()
        if tokens[0] == "open":
            open_expr = is_open_expr(expr)
            if (isinstance(open_expr, hiphop_error)):
                return open_expr
            else:
                val = open_expr.evaluate()
                return val
        elif tokens[0] == "apply":
            apply_expr = is_apply_expr(expr)
            if (isinstance(apply_expr, hiphop_error)):
                return apply_expr
            else:
                val = apply_expr.evaluate()
                if (isinstance(val, hiphop_error)):
                    return val
        elif tokens[0] == "save":
            save_expr = is_save_expr(expr)
            if (isinstance(save_expr, hiphop_error)):
                return save_expr
            else:
                val = save_expr.evaluate()
                if (isinstance(val, hiphop_error)):
                    return val
        elif tokens[0] == "apply-all":
            apply_all_expr = is_apply_all_expr(expr)
            if (isinstance(apply_all_expr, hiphop_error)):
                return apply_all_expr
            else:
                val = apply_all_expr.evaluate()
                if (isinstance(val, hiphop_error)):
                    return val 
        elif tokens[0] == "save-macro":
            save_macro = is_save_macro_expr(expr)
            if (isinstance(save_macro, hiphop_error)):
                return save_macro
            else: 
                val = save_macro.evaluate()
                if (isinstance(val, hiphop_error)):
                    return val
        else:
            return hiphop_error("ParseError", -1, "Unable to parse line")

    def parse(self, filename):

        f = open(filename, "r")
        lines = f.readlines()
        line_num = 1
        for line in lines:
            print("Parsing line {}: {}".format(line_num, line.strip()))
            parse_res = self.parse_line(line)
            if (isinstance(parse_res, hiphop_error)):
                error_out(parse_res, line_num)
            line_num += 1


def error_out(hiphop_error, line_num):
    hiphop_error.line_num = line_num
    hiphop_error.printError()
    sys.exit()