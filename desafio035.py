r1 = float(input('Qual o comprimento da primeira reta? ').strip())
r2 = float(input('Qual o comprimento da segunda reta? ').strip())
r3 = float(input('Qual o comprimento da terceira reta? ').strip())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você formou um triângulo')
else:
    print('Não é possível formar um triângulo')




#Desenvolva um programa que leia o comprimento de 3 retas e diga se ele pode ou não formar um triângulo.

