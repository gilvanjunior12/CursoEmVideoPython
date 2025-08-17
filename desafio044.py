print(f'{" LOJA DO JUNIOR ":=^40}')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista (dinheiro ou cheque)
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Escolha uma opção: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f}')
else:
    total = None
    print('OPÇÃO INVÁLIDA DE PAGAMENTO! Tente novamente.')

if total is not None:
    print(f'Sua compra de R${preço:.2f} irá custar: R${total:.2f}.')



#O programa deve calcular o valor a ser pago em um produto.
#Considerando o preço normal e a condição de pagamento:
#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros.









