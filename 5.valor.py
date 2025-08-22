import os
os.system("cls")
#solicitando as notas dos alunos
num1 = float(input("Digite a primeiro numero: "))
num2 = float(input("Digite a segundo numero: "))

#calculando a média
media = (num1 + num2) / 2
soma = num1 + num2
produto = num1 * num2

#descobrir o menor valor =

menor = num1 if num1 < num2 else num2
maior = num1 if num1 > num2 else num2

#mostrando os resultados
print(f"A média é {media}")
print(f"A soma é {soma}")
print(f"O produto é {produto}")
print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")
