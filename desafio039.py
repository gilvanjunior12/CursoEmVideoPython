from datetime import date

atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos, em {atual}.')

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')


#Faça um programa que leia a idade de uma pessoa.
#De acordo com a idade, o programa deverá dizer:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo.
#O programa também deverá o tempo que falta ou que passou.