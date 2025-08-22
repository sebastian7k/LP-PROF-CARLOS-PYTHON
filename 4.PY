import os
os.system("cls")
#solicitando um número ao usuário

numero = int(input("Digite um número: "))

#verificando se o número esta certo
if numero > 10:
    print("Maior que 10")
elif numero == 10:
    print("Menor ou igual a 10")
else:
    print("Menor que 10")
