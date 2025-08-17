altura = float(input('Qual a sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal!')
elif 30 <= imc <= 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
else:
    print('IMC entre 25 e 30 (Sobrepeso).')





#O programa deverá ler a altura e peso de uma pessoa.
#Depois, calcular o IMC e mostre seu status de acordo com a seguinte tabela:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.05 e 25: Peso ideal
#De 30 até 40: Obesidade
#Acima de 40: Obesidade mórbida.