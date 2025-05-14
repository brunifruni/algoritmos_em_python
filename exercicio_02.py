km = int (input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias foram alugados?'))

preco = 60 * dias + 0.15 * km
print(f'Km={km}. Dias: {dias}.')
print(f'Valor a ser pago: {preco}')