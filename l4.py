import sys


def compress(gene: str):
    bit_str = ""
    for el in gene:
        if el == 'A':   # Соотносим буквы 'битам'
            bit_str += '00'
        elif el == 'C':
            bit_str += '01'
        elif el == 'G':
            bit_str += '10'
        elif el == 'T':
            bit_str += '11'
        else:
            print('Передан неверный ген ', gene)
            exit(1)
    return int(bit_str, base=2)     # Возвращаем десятичное число, переведенное из двоичного


def decompress(bit_string: str):
    i = 0
    gene = ''
    while i < len(bit_string):
        if bit_string[i] == '0' and bit_string[i+1] == '0':     # Соотносим 'биты' буквам
            gene += 'A'
        elif bit_string[i] == '0' and bit_string[i+1] == '1':
            gene += 'C'
        elif bit_string[i] == '1' and bit_string[i+1] == '0':
            gene += 'G'
        elif bit_string[i] == '1' and bit_string[i+1] == '1':
            gene += 'T'
        else:
            print("Передан не верный сжатый ген ", bit_string)
            exit(1)
        i += 2
    return gene


def dec_bin(x):     # Перевод из десятичного числа в двоичное
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = ('0' if x % 2 == 0 else '1') + res
        x //= 2
    return str(res)


print("Сжатый ген: ", compress('TAGGGATTAAC'), '\nИз числа в ген: ', decompress(dec_bin(compress('TAGGGATTAAC'))))
print('Размер сжатого гена: %s (байт)' % (sys.getsizeof(compress("TAGGGATTAAC"))),\
      '\nРазмер не сжатого гена: %s (байт)' % (sys.getsizeof(decompress(dec_bin(compress('TAGGGATTAAC'))))))



