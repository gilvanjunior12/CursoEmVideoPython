import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
sorteio = [a1, a2, a3, a4]

random.shuffle(sorteio)

print(f'A ordem sorteada foi: {sorteio}.')




#O aplicativo deve ler o nome de 4 alunos e sortear uma ordem.