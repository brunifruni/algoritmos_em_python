soma = 0 #variavel acumuladora
cont = 1 #variavel de contagem das notas
while (cont <= 5):
  x = float(input(f'Digite a {cont}ª nota:'))
  soma = soma + x
  cont = cont + 1
media = soma / 5
print(f'Média final: {media}') #fora do laço para calcular somente uma so vez la no final
