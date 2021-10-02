
// OPÇÃO 1: USANDO FUNÇÕES NATIVAS
const palindromo1 = (texto) => {
    return texto == texto.split().reverse().join()
}


// OPÇÃO 2: USANDO LOOP
const palindromo = (texto) => {
    let letra_esquerda = 0
    let letra_direita = texto.length - 1

    while(letra_direita > letra_esquerda) {
        if (texto[letra_direita] != texto[letra_esquerda]) return false

        letra_esquerda++
        letra_direita--
    }

    return true
}
