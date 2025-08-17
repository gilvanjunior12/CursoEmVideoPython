nome = input('Qual seu nome completo? ').strip()
# .strip() remove espaços antes e depois do nome

print(f'Muito prazer em te conhecer, {nome}!')

print(f'Seu primeiro nome é: {nome.split()[0]}')
# .split() divide o nome em palavras, [0] pega a primeira (primeiro nome)

print(f'Seu último nome é: {nome.split()[-1]}')
# .split() divide o nome em palavras, [-1] pega a última (último nome)



#O programa deverá ler o primeiro e último nome de uma pessoa.