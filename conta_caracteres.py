
def conta_caracteres(texto):
    caracteres_vistos = {}

    for caractere in texto:
        if caractere not in caracteres_vistos:
            caracteres_vistos[caractere] = 0
        
        caracteres_vistos[caractere] += 1

    return caracteres_vistos
