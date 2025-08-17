preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print(f'O valor atual do produto é R${preço:.2f}. \n'
      f'Com o desconto de 5%, o produto custará: R${novo:.2f}.')


#Leia o valor de um produto, e calcule seu novo preço com 5% de desconto.