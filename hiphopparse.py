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
            open_expr.evaluate()
        elif tokens[0] == "reload":
            load_expr = is_load_expr(expr)
            load_expr.evaluate()
        elif tokens[0] == "apply":
            apply_expr = is_apply_expr(expr)
            apply_expr.evaluate()
        elif tokens[0] == "save":
            save_expr = is_save_expr(expr)
            save_expr.evaluate()
        elif tokens[0] == "apply-all":
            apply_all_expr = is_apply_all_expr(expr)
            apply_all_expr.evaluate()
        elif tokens[0] == "save-macro":
            save_macro = is_save_macro_expr(expr)
            save_macro.evaluate()
        elif tokens[0] == "set":
            set_expr = is_set_expr(expr)
            set_expr.evaluate()
        elif tokens[0] == "get":
            get_expr = is_get_expr(expr)
            get_expr.get()
        # elif is_identifier(expr):
        #    pass
        else:
            raise hiphop_error("ParseError", "Unable to parse line")

    def parse(self, filename):

        try:
            f = open(filename, "r")
            lines = f.readlines()
        except FileNotFoundError:
            raise file_error("FileNotFoundError",
                             'File "{}" does not exist'.format(filename))
        line_num = 1
        for line in lines:
            #print("Parsing line {}: {}".format(line_num, line.strip()))
            try:
                self.parse_line(line)
            except hiphop_error as e:
                e.line_num = line_num
                raise e
            except hiphop_eval_error as e:
                e.line_num = line_num
                raise e
            line_num += 1
