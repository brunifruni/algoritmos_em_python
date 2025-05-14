print ('Escolha o que deseja comprar: ')
print ('1 - Maçã')
print ('2 - Laranja')
print ('3 - Banana')

produto = int (input('Digite a opção desejada: '))
qtd = int(input('Quantas unidades?'))

if (produto == 1):
  pagar = qtd * 2.3 #2.30 é o valor de 1 maça
  print(f'Você comprou {qtd} maçãs. O total a pagar é de R$ {pagar}')
else:
  if (produto == 2):
    pagar = qtd * 3.6 #preço da laranja
    print(f'Você comprou {qtd} laranjas. O total a pagar é de R$ {pagar}')
  else:
    if (produto == 3):
      pagar = qtd * 1.85
      print(f'Você comprou {qtd} bananas. O total a pagar é de R$ {pagar}')
    else:
      print('Produto inexistente')
