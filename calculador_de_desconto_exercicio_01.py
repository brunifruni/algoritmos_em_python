#algoritmo calculador de desconto
# determina quanto será descontado de um produto com base em um percentual informado, e qual será o valor final do produto após aplicar esse desconto.

preco = float(input('Digite o preço do produto: '))
percentual = float(input ('Digite o percentual de desconto (0-100): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f' O preço do produto é {preco}. Desconto de {percentual}%')
print(f'Valor calculado de desconto: {desconto}. Valor final do produto {final}')
