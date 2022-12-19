class MessageVariable:
    def __init__(self, var_type: str, name: str, index: int, is_array: bool = False):
        self.var_type = var_type
        self.name = name
        self.index = index
        self.is_array = is_array

