
def run(funcao, testes):
    for inputs, esperado in testes.items():
        if type(inputs) != tuple:
            inputs = (inputs, )

        resposta = funcao(*inputs)

        print(f'{"CORRETO" if resposta == esperado else "ERRADO"}: {inputs}')
