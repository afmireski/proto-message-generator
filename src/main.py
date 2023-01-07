from dtos.proto_message import ProtoMessage
from dtos.message_variables import MessageVariable


def read_path(msg: str, is_input: bool = False) -> str:
    path: str = str(input(f'{msg}\n>'))

    if len(path) == 0:
        raise IOError('O caminho não pode estar vazio')
    elif is_input and not path.__contains__('.ts'):
        raise IOError('Arquivos de entrada devem ser .ts')
    elif not is_input and not path.__contains__('.proto'):
        raise IOError('Arquivos de saída devem ser .proto')

    return path


def read_files(input_path: str, output_path: str):
    input_file = open(input_path, 'r')

    try:
        output_file = open(output_path, 'a')
    except FileNotFoundError:
        output_file = open(output_path, 'w')

    return input_file, output_file


def remove_unnecessary_chars(string: str) -> str:
    return string.strip(' ;\n').replace(':', '').replace('?', '').replace('!', '')


def is_class(line: str) -> bool:
    return not line.__contains__('import') and line.__contains__('class') and line.__contains__('{')


def is_interface(line: str) -> bool:
    return not line.__contains__('import') and line.__contains__('interface') and line.__contains__('{')


def is_var(line: str) -> bool:
    return not line.__contains__('import') and line.__contains__(':') and line.__contains__(';')


def generate_proto_message(input_file) -> ProtoMessage:
    message: ProtoMessage = ProtoMessage()
    i: int = 1

    lines = input_file.readlines()
    for line in lines:
        if is_class(line):
            temp = line.strip().split()

            class_index = temp.index('class')
            message = ProtoMessage(temp[class_index+1])
        elif is_interface(line):
            temp = line.strip().split()

            class_index = temp.index('interface')
            message = ProtoMessage(temp[class_index+1])
        elif is_var(line):
            temp = remove_unnecessary_chars(line).split()

            is_array = temp[1].__contains__('[]')
            temp[1] = temp[1].replace('[]', '')

            var: MessageVariable = MessageVariable(temp[1], temp[0], i, is_array)

            message.variables.append(var)

            i += 1

    if len(message.name) == 0:
        raise ValueError('Não foi identificada nenhuma classe')
    if len(message.variables) == 0:
        raise ValueError('Não foi identificada nenhuma variável')

    return message


def write_message(file, message: ProtoMessage):
    file.write(f'\nmessage {message.name} ' + '{\n')
    for var in message.variables:
        line: str = f'{var.var_type} {var.name} = {var.index};\n'
        if var.is_array:
            line = f'repeated {line}'
        line = f'\t{line}'

        file.write(line)
    file.write('}\n')


def main():
    input_path: str = read_path('Informe o caminho da entrada:', True)
    output_path: str = read_path('Informe o caminho da saída:')

    input_file, output_file = read_files(input_path, output_path)

    try:
        message: ProtoMessage = generate_proto_message(input_file)
        write_message(output_file, message)
    finally:
        input_file.close()
        output_file.close()


main()
