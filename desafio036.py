casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos você irá pagar? '))
mensalidade = casa / (anos * 12)
limite = salario * 0.3
if mensalidade > limite:
    print(f'Empréstimo aprovado! ')
else:
    print(f'A mensalidade será de: {mensalidade:.2f}.')





#Crie um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa deverá perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.