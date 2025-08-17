import random

opcoes = ['Pedra', 'Papel', 'Tesoura']

print("""Faça sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

jogador = int(input('Digite o número referente à sua jogada: '))

if jogador not in [0, 1, 2]:
    print('Número inválido. Tente novamente!')
else:
    computador = random.randint(0, 2)

    print(f'Você jogou: {opcoes[jogador]}')
    print(f'O computador jogou: {opcoes[computador]}')

    if jogador == computador:
        print('Empate!')
    elif (
            (jogador == 0 and computador == 2) or
            (jogador == 1 and computador == 0) or
            (jogador == 2 and computador == 1)
    ):
        print('Você ganhou!')
    else:
        print('O computador ganhou!')
