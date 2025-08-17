import random
print('Escolhendo um número...')
sorteio = random.randint(0, 5)
escolhido = int(input('Qual número você acha que eu escolhi? ').strip())
if escolhido == sorteio:
    print('Você acertou!')
else:
    print('VocÊ errou!')



#Escreva um programa que faça "o computador" escolher um número entre 0 e 5.
#Depois, e usuário deverá tentar descobrir qual foi o número sorteado.
#Caso ele acerte, apareça uma mensagem de acerto, caso não, apareça uma de erro.