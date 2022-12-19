class MessageVariable:
    def __init__(self, var_type: str, name: str, index: int, is_array: bool = False):
        self.var_type = self.convert_type(var_type)
        self.name = self.convert_name(name)
        self.index = index
        self.is_array = is_array

    @staticmethod
    def convert_type(var_type: str) -> str:
        if var_type == 'string' or var_type.lower().__contains__('enum'):
            return 'string'
        elif var_type == 'number':
            return 'int32'
        elif var_type == 'boolean':
            return 'bool'
        else:
            return var_type

    @staticmethod
    def convert_name(name: str) -> str:
        if name.__contains__("Input"):
            name.replace("Input", "Request")
        elif name.__contains__("Output"):
            name.replace("Output", "Response")
        return name


