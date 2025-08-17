num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:].upper()}')
else:
    print('Opção inválida.')



#Escreva um programa que leia um número inteiro qualquer e peça pro usuário escolher a base de conversão.
#-1 para binário, -2 para octal -3 para hexadecimal.