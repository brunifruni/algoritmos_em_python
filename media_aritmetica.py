#Obter as duas notas de provas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#Calcular a média aritmética
media = (nota1 + nota2)/2

#Se a média for igual ou maior que 7, o aluno foi aprovado
if media >= 7:
    print("Aprovado")
#Se não, ele foi reprovado
else:
    print("Reprovado")
