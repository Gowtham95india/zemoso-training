import string
import itertools

cases = string.lowercase
keys = [''.join(_) for _ in itertools.product(cases, repeat = 3)]

cipher_file = open('_xor.txt', 'r')
cipher_lines = []
for i in cipher_file.readlines():
    line = i.strip()
    line = map(int, i.split(','))
    cipher_lines = line

print cipher_lines
