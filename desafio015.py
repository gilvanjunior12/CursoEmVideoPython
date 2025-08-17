dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
total = (dias * 60) + (km * 0.15)
print(f'Você deverá pagar: R${total:.2f}.')






#O programa deve perguntar a quantidades de kms percorridos por um carro alugado
#Pergunte também a quantidade de dias que ele alugou
#Calcule o preço que ele deve pagar, sabendo que o carro custa 60 reais por dia, e 0,15 centavos por km rodado.