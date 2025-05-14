n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3)/3

if (media >= 7):
  print('Você passou nas matérias')
else:
  print('Você não passou')
###ou

#prof
n1 = float(input('Digite a nota da 1ª matéria: '))
n2 = float(input('Digite a nota da 2ª matéria: '))
n3 = float(input('Digite a nota da 3ª matéria: '))

if n1 >= 7 and n2 >= 7 and n3 >= 7:
  print('O aluno está aprovado!')
else:
  print('O aluno está reprovado!,')
