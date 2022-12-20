class ProtoMessage:
    def __init__(self, name: str = ''):
        self.name = self.convert_name(name)
        self.variables = []

    @staticmethod
    def convert_name(name: str) -> str:
        if name.__contains__("Input"):
            name = name.replace("Input", "Request")
        elif name.__contains__("Output"):
            name = name.replace("Output", "Response")
        return name

    def __str__(self):
        return f"{self.name}{self.variables.__str__()}"

