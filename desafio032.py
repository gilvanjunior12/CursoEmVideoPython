ano = int(input('Digite o ano: ').strip())

if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    print('Ano bissexto!')
else:
    print('Ano não é bissexto!')


#Faça um aplicativo que verifique se um ano é bissexto.