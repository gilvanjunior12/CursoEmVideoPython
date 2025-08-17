from datetime import date

atual = date.today().year

nasc = int(input('Em que ano você nasceu?'))
idade = atual - nasc
if 0 <= idade <=9:
    print(f'Você está na categoria "MIRIM".')
elif 10 <= idade <= 14:
    print(f'Você está na categoria "INFANTIL".')
elif 15<= idade <=19:
    print(f'Você está na categoria "JUNIOR".')
elif idade == 20:
    print(f'Você está na categoria "SENIOR".')
elif idade > 20:
    print('VocÊ está na categoria "MASTER".')


#Faça um programa que leia o ano de nascimento de um atleta e mostre a sua categoria:
#até 9 anos é mirim
#Até 14 é infantil
#Até 19 é Junior
#Até 20 é Senior
#Acima de 20 é Master