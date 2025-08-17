import math
from math import hypot

ca = float(input('Qual o cateto adjacente? '))
co = float(input('Qual o cateto oposto? '))
hipo = hypot(ca, co)
print(f'A hipotenusa é: {hipo}')

#O programa deve ler o cateto oposto, o cateto adjacente, e calcular a hipotenusa.