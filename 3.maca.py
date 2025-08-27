import os
os.system("cls")

#pedindo maçãs

qtdm = int(input("Digite a quantidade de maçãs desejada"))

#verificando o preço unitario das maçãs

if qtdm < 12:
    preco = 1.30
else:
    preco = 1.00

#calculando o preço total
total = qtdm * preco
#mostrando o preço total
print(f"O preço total é R$ {total:.2f}")