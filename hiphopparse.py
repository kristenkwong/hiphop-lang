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
        else:
            raise hiphop_error("ParseError","Unable to parse line")

    def parse(self, filename):

        try:
            f = open(filename, "r")
            lines = f.readlines()
        except FileNotFoundError:
            raise hiphop_error("FileNotFoundError", "File does not exist")
        line_num = 1
        for line in lines:
            print("Parsing line {}: {}".format(line_num, line.strip()))
            try:
                self.parse_line(line)
            except hiphop_error as e:
                e.line_num = line_num
                raise e
            except hiphop_eval_error as e:
                e.line_num = line_num
                raise e
            line_num += 1
