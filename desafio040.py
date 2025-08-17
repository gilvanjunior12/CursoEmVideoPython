n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado! Estude mais no próximo ano.')
elif 7 > media >= 5:
    print('Você está de recuperação! ')
elif media >=7:
    print('Parabéns! Você foi aprovado.')



#Crie um programa que leia 2 notas de um aluno e calcule sua média.
#Se a média foi abaixo de 5, está reprovado.
#Se a média foi entre 5 e 6.9, está de recuperação.
#Se a média foi 7 ou superior, aprovado