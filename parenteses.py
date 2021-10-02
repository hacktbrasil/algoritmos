
'''
()
)(
()()()()
((())())

- Primeiro sempre é abertura
- último sempre é fechamento
- Ao identificar um fechamento, ver se o anterior é uma abertura


- Contador começando do zero
- Loop na lista de caracteres
- Pra cada caractere:
    - Cada vez que receber um parêntese abrindo:
        - Aumento um contador
    - Cada vez que receber um parênteses fechando:
        - Decrementa o contador
    - Se o contador ficar negativo, retornar Falso
- Retorno Verdadeiro

'''

def parenteses_valido(texto):
    contador = 0

    for caractere in texto:
        if caractere == '(':
            contador += 1
        elif caractere == ')':
            contador -= 1

            if contador < 0:
                return False

    return contador == 0


def teste():
    testes = {
        '()': True,
        ')(': False,
        '()()()()': True,
        '((())())': True,
        '((())())(': False,
    }

    for texto, resultado_esperado in testes.items():
        resultado = parenteses_valido(texto)

        if resultado == resultado_esperado:
            print(f'CORRETO! {texto}')
        else:
            print(f'ERRADO: {texto}, deveria ser {resultado_esperado}')
