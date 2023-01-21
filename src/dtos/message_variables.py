class MessageVariable:
    def __init__(self, var_type: str, name: str, index: int, is_array: bool = False):
        self.var_type = self.__convert_type(var_type)
        self.name = name
        self.index = index
        self.is_array = is_array

    @staticmethod
    def __should_be_string(var_type: str) -> bool:
        return var_type == 'string' or var_type == 'Date' or var_type.lower().__contains__('enum') \
            or var_type.lower().__contains__('keyof typeof')

    def __convert_type(self, var_type: str) -> str:
        if self.__should_be_string(var_type):
            return 'string'
        elif var_type == 'number':
            return 'int32'
        elif var_type == 'boolean':
            return 'bool'
        else:
            return var_type

    def __str__(self):
        return f'{self.var_type}|{self.name}|{self.index}|{self.is_array}'
