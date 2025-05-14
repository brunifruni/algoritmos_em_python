nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))

if nome == 'Bruna':
  print ('Olá, Bruna!')
elif idade < 18:
  print('Você não é a Bruna e é menor de idade')
elif idade > 100:
  print('Diferente de você, a Bruna não é imortal')
