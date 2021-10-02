import testlib


def palindromo1(texto):
    # OPÇÃO 1: USANDO FUNCIONALIDADE NATIVA
    return texto == texto[::-1]


def palindromo2(texto):
    # OPÇÃO 2: USANDO LOOP
    letra_esquerda = 0
    letra_direita = len(texto) - 1

    while letra_direita > letra_esquerda:
        if texto[letra_esquerda] != texto[letra_direita]:
            return False

        letra_esquerda += 1
        letra_direita -= 1

    return True


def test():
    testes = {
        '': True,
        'aaaa': True,
        '123 99 321': True,
        'abcba': True,
        'amor a roma': True,
        'hello world': False,
        'abacaxi': False,
    }

    testlib.run(palindromo1, testes)
