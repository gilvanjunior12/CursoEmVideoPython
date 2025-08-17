import random  # Importa o módulo random para gerar jogadas do computador aleatoriamente

# Lista com as opções do jogo
opcoes = ['Pedra', 'Papel', 'Tesoura']

# Mostra as opções para o jogador
print("""Faça sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

# Recebe a jogada do jogador
jogador = int(input('Digite o número referente à sua jogada: '))

# Verifica se o jogador digitou um número válido
if jogador not in [0, 1, 2]:
    print('Número inválido. Tente novamente!')  # Se digitou errado, avisa e não continua o jogo
else:
    # Gera a jogada do computador aleatoriamente (0, 1 ou 2)
    computador = random.randint(0, 2)

    # Mostra as jogadas do jogador e do computador
    print(f'Você jogou: {opcoes[jogador]}')
    print(f'O computador jogou: {opcoes[computador]}')

    # Verifica quem ganhou
    if jogador == computador:
        print('Empate!')  # Mesma jogada → empate
    elif (
            (jogador == 0 and computador == 2) or  # Pedra vence Tesoura
            (jogador == 1 and computador == 0) or  # Papel vence Pedra
            (jogador == 2 and computador == 1)  # Tesoura vence Papel
    ):
        print('Você ganhou!')  # Condições em que o jogador vence
    else:
        print('O computador ganhou!')  # Caso contrário, o computador vence

# Observação:
# Colocar todo o restante do jogo dentro do `else` garante que nada que dependa da variável
# 'computador' seja executado se o jogador digitou um número inválido.
# Assim, o programa não gera erro e só executa a lógica do jogo quando a jogada é válida.


#Faça um programa que jogue "Pedra, papel e tesoura" com você.

