nome = input('Digite seu nome: ').strip()
print('Analisando o nome Amanda: ')
print(f'A letra "A" apareceu  {nome.upper().count('A')} vezes')
print(f'A primeira letra "A" aparece na posição: {nome.upper().find('A')+1}')
print(f'A última letra "A" aparece na posição: {nome.upper().rfind('A')+1}')



#O programa deverá ler um nome e falar:
#Quantas vezes a letra "A" aparece;
#Em qual posição a primeira letra "A" apareceu;
#Em qual posição apareceu a última letra "A";