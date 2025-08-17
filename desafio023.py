num = int(input('Digite um número: '))
u = num // 1 % 10
# u = num // 1 % 10
# num // 1 = o número inteiro completo (sem mudar nada)
# % 10 → pega o resto da divisão por 10, que é sempre o último dígito do número
# Ex: 1834 % 10 = 4 (último dígito)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}:')
print(f'Unidade: {u}.')
print(f'Dezena: {d}.')
print(f'Centena: {c}.')
print(f'Milhar: {m}.')


#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.