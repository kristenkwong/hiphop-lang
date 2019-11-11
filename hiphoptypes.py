import re 

"""
<HHE> ::= apply <func> <args> to <id>
        | open "<filename>" as <id>
        | save <id> as "filename>"
        | <id>
        | <num>

<args> ::= <arg>
         | <arg> <args>
         | 

<arg> ::= NUMBER

<id> ::= STRING 
"""

def is_open_expr(expr_str):
    # For one line of the program, if valid program return object,
    # otherwise False 

    match_filename = re.findall('(?<=open ")(.*)(?=" as)', expr_str)
    match_id = re.findall('(?<=open ")*(?<=" as )(.*)$', expr_str)
    if (len(match_filename) != 1 or len(match_id) != 1):
        return hiphop_error("ParserError", -1, 'Invalid syntax for `open` expression.')
    else:
        return open_expr(match_filename, match_id)

class open_expr():

    def __init__(self, filename, id):

        self.filename = filename 
        self.id = id 


class save_expr():

    def __init__(self, id, filename):

        self.id = id 
        self.filename = filename

class apply_expr():

    def __init__(self, funcname, args, img):

        """
        funcname: function to call when expression is evaluated
        args: list of arguments going into the function 
        img: img expression
        """

        self.funcname = funcname 
        self.args = args 
        self.img = img 

class identifier():

    def __init__(self, boundvar):

        self.boundvar = boundvar 

    def get_value(self):

        return self.boundvar

class hiphop_error():

    def __init__(self, error_type, line_num, error_msg):

        self.error_type = error_type
        self.line_num = line_num
        self.error_msg = error_msg

    def printError(self):
        print("{} (line {}): {}".format(self.error_type, self.line_num, self.error_msg))

