velocidade = float(input('Qual a velocidade do carro? ').strip())
diferença = velocidade - 80
multa = 7 * diferença
if velocidade >=81:
    print(f"""Você foi multado.
    Sua multa foi no valor de: {multa:.2f}.""")



#Escreva um programa que leia a velocidade de um carro.
#Se o carro ultrapassar 80km/h, aparece uma mensagem de multa.
#Caso não ultrapasse, não acontece nada.
#Se ele ultrapassou, vai levar uma multa que custa R$7,00 por cada km que ultrapassou do limite.