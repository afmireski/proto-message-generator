def read_path(msg: str, is_input: bool = False) -> str:
    path: str = str(input(f'{msg}\n>'))

    if len(path) == 0:
        raise IOError('O caminho não pode estar vazio')
    elif is_input and not path.__contains__('.ts'):
        raise IOError('Arquivos de entrada devem ser .ts')

    return path


def read_files(input_path, output_path):
    input_file = open(input_path, 'r')

    try:
        output_file = open(output_path, 'a')
    except FileNotFoundError:
        output_file = open(output_path, 'w')

    return input_file, output_file


def main():
    input_path: str = read_path('Informe o caminho da entrada:', True)
    output_path: str = read_path('Informe o caminho da saída:')

    input_file, output_file = read_files(input_path, output_path)

    input_file.close()
    output_file.close()


main()
