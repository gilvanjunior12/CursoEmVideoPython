salario = float(input('Qual seu salário? ').strip().replace(',', '.'))
aumento_10 = salario + (salario * 10 / 100)  # 10% para salários > 1250
aumento_15 = salario + (salario * 15 / 100)  # 15% para salários <= 1250

if salario > 1250:
    print(f'Seu novo salário é de: R${aumento_10:.2f}.')
else:
    print(f'Seu novo salário é de: R${aumento_15:.2f}.')





#Escreva um programa que pergunte o salário de um funcionário, e calcule o valor do seu aumento.
#Salários superiores à 1250,00, terão aumento de 10%.
#Salários inferiores ou iguais, aumentarão em 15%.