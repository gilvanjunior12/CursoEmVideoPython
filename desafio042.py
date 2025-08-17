r1 = float(input('Qual o comprimento da primeira reta? ').strip())
r2 = float(input('Qual o comprimento da segunda reta? ').strip())
r3 = float(input('Qual o comprimento da terceira reta? ').strip())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você formou um triângulo')
    if r1 == r2 == r3:
        print('Tipo: Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tipo: Isósceles')
    else:
        print('Tipo: Escaleno')
else:
    print('Não é possível formar um triângulo')


#Refaça o desafio 035:
#Porém, acrescentando o recurso de mostrar que tipo de triangulo será formado.
#Equilaterio
#Isosceles
#Escaleno