# Everything responsible for saving the state of the program
# such as all identifiers
from hiphoperrors import hiphop_error

reserved_func_names = ["blur", "grayscale", "erode", "dilate",
                       "outline", "filtercolor", "scale", "crop", "impose", "reload"]

env_vars = {'wd': '"./'}


class var_dict():
    """
    Keeps track of ids holding images within the program.
    """

    def __init__(self):
        self.map = {}

    def add_var(self, id, img, path):
        self.map[id] = img
        self.map[id + 'p'] = path

    def get_var(self, id):

        return self.map.get(id, -1)

    def get_path(self, id):
        return self.map.get(id + 'p', -1)


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
