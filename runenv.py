# Everything responsible for saving the state of the program
# such as all identifiers
from hiphoperrors import hiphop_error

reserved_func_names = ["blur", "grayscale", "erode", "dilate",
                       "outline", "filtercolor", "scale", "crop", "impose"]


class var_dict():
    """
    Keeps track of ids holding images within the program.
    """

    def __init__(self):
        self.map = {}

    def add_var(self, id, img):
        self.map[id] = img

    def get_var(self, id):

        return self.map.get(id, -1)


class macros_dict():
    """
    Keeps track of user defined macros in the program.
    """

    def __init__(self):
        self.map = {}

    def add_var(self, id, funcs):
        """
        funcs: list of lambda functions to save into macro
        """
        self.map[id] = funcs

    def get_var(self, id):
        return self.map.get(id, -1)


saved_vars = var_dict()
saved_macros = macros_dict()


def is_id_used(new_id):

    if (new_id in reserved_func_names):
        return False

    return True
