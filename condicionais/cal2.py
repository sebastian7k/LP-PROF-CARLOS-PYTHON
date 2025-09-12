# Calculadora simples

import os
os.system

print(" Calculadora Simples")
print(" Operações: +  -  *  /")

# Pega os valores

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Faz o cálculo
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operador inválido!"

print(f"Resultado: {resultado}")
