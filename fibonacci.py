import testlib


# Recursão, SEM programação dinâmica
# Tempo: O(2^n), Espaço: O(1)
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Recursão, COM programação dinâmica
# Tempo: O(n), Espaço: O(n)
def fibonacci2(n, cache=None):
    if not cache:
        cache = {
            0: 0,
            1: 1,
        }

    if n not in cache:
        cache[n] = fibonacci2(n - 1, cache) + fibonacci2(n - 2, cache)

    return cache[n]


# Bottom-up usando iteração (for loop) e tabela de hashes
# Tempo: O(n), Espaço: O(n)
def fibonacci3(n):
    memoria = {0: 0, 1: 1}

    for i in range(2, n + 1):
        memoria[i] = memoria[i - 1] + memoria[i - 2]

    return memoria[n]


# Bottom-up usando iteração e lista
# Tempo: O(n), Espaço: O(1)
def fibonacci4(n):
    memoria = [0, 1]

    for i in range(2, n + 1):
        penultimo, ultimo = memoria[0], memoria[1]

        memoria[0] = ultimo
        memoria[1] = ultimo + penultimo

    return memoria[1]


def test(fibonacci_function):
    sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]

    tests = {idx: number for idx, number in enumerate(sequence)}

    testlib.run(fibonacci_function, tests)
