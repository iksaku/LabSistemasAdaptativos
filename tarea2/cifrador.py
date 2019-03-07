# -*- coding: utf8 -*-

import sys

abc = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

hash_abc = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}

cesar3 = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'v',
    's': 'u',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c'
}


def cesar_cipher(file_content):
    for line in file_content:
        result = ''
        for letter in line:
            if letter in cesar3.keys():
                is_upper = letter == letter.upper()
                letter = cesar3[letter.lower()]
                if is_upper:
                    letter = letter.upper()
                result += letter
            else:
                result += ' '
        result += '\n\t'
    return result


def customizable_cipher(file_content, x=3):
    max_i = len(abc)
    for line in file_content:
        result = ''
        for letter in line:
            if letter in abc:
                is_upper = (letter == letter.upper())
                i = abc.index(letter.lower()) + x
                if (i >= max_i):
                    i -= max_i
                letter = abc[i]
                if is_upper:
                    letter = letter.upper()
                result += letter
            else:
                result += ' '
        result += '\n\t'
    return result


try:
    file = open(sys.argv[1])
    content = file.readlines()
    file.close()
except IndexError:
    print("[Error] Porfavor especifique el nombre del archivo a abrir.")
    quit(1)
except FileNotFoundError:
    print("[Error] El archivo '%s' no existe." % sys.argv[1])
    quit(1)

try:
    x = int(sys.argv[2])
except ValueError:
    print('No se especifico un desfase, utilizando el desfase predeterminado...')
    x = 3
except IndexError:
    print('No se especifico un desfase, utilizando el desfase predeterminado...')
    x = 3

print('Contenido del archivo:\n\t' + '\n\t'.join(content))
print('Contenido cifrado (cesar3):\n\t' + cesar_cipher(content))
print('Contenido cifrado (desfase de ' + str(x) + ' posiciones):\n\t' + customizable_cipher(content, x))