
FIRST_TWENTY = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

TEN = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def num_text(num: int, recur=False) -> str:
    concat = ' ' if recur and num > 0 else ''

    if num < 20:
        return concat + FIRST_TWENTY[num]

    if num < 100:
        return concat + TEN[num // 10] + num_text(num % 10, True)

    if num < 1000:
        return concat + num_text(num // 100) + ' hundred' + num_text(num % 100, True)

    return num_text(num // 1000) + ' thousand' + num_text(num % 1000, True)


if __name__ == '__main__':
    import sys
    print(num_text(num=int(sys.argv[1])))
