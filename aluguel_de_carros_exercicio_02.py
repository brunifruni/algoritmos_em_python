# calcula o valor total a ser pago pelo aluguel de um carro, com base nos quilômetros rodados e na quantidade de dias de aluguel.
km = int (input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias foram alugados?'))

preco = 60 * dias + 0.15 * km
print(f'Km={km}. Dias: {dias}.')
print(f'Valor a ser pago: {preco}')
