dist = float(input('Qual a distância da sua viagem? ').strip())
curta = dist * 0.50
longa = dist * 0.45
if dist <= 200:
    print(f'Você deve: R${curta:.2f} reais.')
else:
    print(f'Você deve: R${longa:.2f} reais.')




#Desenvolva um programa que leia a distância de uma viagem em km.
#Calcule o preço da passagem:
#Se a viagem for até 200km, o km custa 50 centavos
#A a viagem for mais longa, 45 centavos.