
UM_A_VINTE = {
    0: '',
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
}

DEZENA = {
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa',
}

CENTENA = {
    1: 'cento',
    2: 'duzentos',
    3: 'trezentos',
    4: 'quatrocentos',
    5: 'quinhentos',
    6: 'seicentos',
    7: 'setecentos',
    8: 'oitocentos',
    9: 'novecentos',
}


def num_texto(num):
    if num < 20:
        return UM_A_VINTE[num]

    if num < 100:
        return num_composto_texto(num, 10)

    if num == 100:
        return 'cem'

    if num < 1000:
        return num_composto_texto(num, 100)

    else:
        separador = ' mil, ' if num % 1000 > 0 else ' mil'
        return num_texto(num // 1000) + separador + num_texto(num % 1000)


def num_composto_texto(num, divisor):
    mapas = {
        10: DEZENA,
        100: CENTENA,
    }

    mapa = mapas[divisor]

    principal = mapa[num // divisor]
    separador = ' e ' if num % divisor > 0 else ''
    resto = num_texto(num % divisor)
    return principal + separador + resto


if __name__ == '__main__':
    import sys
    print(num_texto(num=int(sys.argv[1])))
