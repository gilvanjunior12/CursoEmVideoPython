cidade = str(input('Qual o nome da sua cidade? ')).strip()
# input() lê o nome da cidade do usuário
# str() garante que o valor seja uma string (opcional aqui, pois input já retorna string)
# .strip() remove espaços extras no começo e no fim da string

print(cidade[:5].upper() == 'SANTO')
# cidade[:5] pega os primeiros 5 caracteres da string (fatiamento)
# .upper() transforma esses caracteres em maiúsculas para garantir a comparação consistente
# compara se os primeiros 5 caracteres, em maiúsculas, são iguais a 'SANTO'
# retorna True se começar com 'SANTO', ou False se não começar







#Crie um programa que leia o nome de uma cidade e te diga se a sua cidade começa ou não com a palavra santo.

