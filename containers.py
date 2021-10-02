import testlib


def containers(text):
    FECHAMENTO = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    aberto = []

    for caractere in text:
        if caractere in FECHAMENTO:
            ultimo_aberto = aberto.pop() if aberto else None

            if ultimo_aberto != FECHAMENTO[caractere]:
                return False

        else:
            aberto.append(caractere)

    return not aberto


def test():
    tests = {
        '(]': False,
        '()': True,
        '([)]': False,
        '[]{}()': True,
        '({[]})': True,
        ']()[': False,
        '{({}[])[[[{()}[]]()]]}': True,
    }

    testlib.run(containers, tests)
