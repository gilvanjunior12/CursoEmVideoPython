largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = altura * largura
tinta = area / 2
print(f'A área da parede é de: {area:.2f}, ou seja, você precisará de {tinta:.2f} litros de tinta para pintar toda a parede.')


#Faça um programa que leia a largura e altura duma parede em metros, e calcule sua área.
#Também calcule a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta
#uma área de 2m quadrados.