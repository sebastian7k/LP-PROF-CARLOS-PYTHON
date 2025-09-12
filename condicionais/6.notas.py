import os
os.system("cls")

#solicitando as notas dos alunos
num1 = float(input("Digite a primeiro numero: "))
num2 = float(input("Digite a segundo numero: "))
num3 = float(input("Digite a terceiro numero: "))

#calculando a média
media = (num1 + num2 + num3) / 3

#verificando a média
if media >= 7:
    print(f"A média é {media}. Aprovado")
else:
    print(f"A média é {media}. Reprovado")
    