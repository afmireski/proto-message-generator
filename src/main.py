def read_path(msg: str, is_input: bool = False) -> str:
    path: str = str(input(f'{msg}\n>'))

    if len(path) == 0:
        raise IOError('O caminho não pode estar vazio')
    elif is_input and not path.__contains__('.ts'):
        raise IOError('Arquivos de entrada devem ser .ts')

    return path


def main():
    input_path: str = read_path('Informe o caminho da entrada:', True)
    output_path: str = read_path('Informe o caminho da saída:')

    print(f'Input: {input_path}')
    print(f'Output: {output_path}')


main()
