nome = input('Digite seu nome completo: ')
print(f"""Seu nome com letras maiúsculas é: {nome.upper()}.
Seu nome com todas as letras minúsculas é: {nome.lower()}
Seu nome tem no total: {len(nome.replace(" ", ""))} letras (sem espaços).
Seu primeiro nome tem: {len(nome.strip().split()[0])} letras.""")


#Crie um programa que que leia o nome completo de uma pessoa.
#1- Apareça o nome com todas as letras maiúsculas
#2- Apareça o nome com todas as letras minúsculas
#3- Quantas letras no total (sem espaços)
#4- Apareça quantas letras tem o primeiro nome

#Obs: A última linha poderia ser: print(f'Seu primeiro nome tem: {len(nome.strip().split()[0])} letras.'). O strip
#Seria adicionado para garantir que não houvessem espaços.

#Obs: O strip só retira espaços do inicio e do fim, mantém os espaços entre as palavras. Usamos o replace para retirar
#os espaços. Substituimos os espaços por nada. Ou seja " " por "".
