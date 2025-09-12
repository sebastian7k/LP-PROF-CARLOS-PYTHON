import os
os.system("cls")
#captura de dados


num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: "))

#cauculos

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
produto = num1 / num2
maior = max(num1, num2)
menor = min(num1, num2)
iguais = num1 == num2

#resultados 

print(f"A soma é {soma}")
print(f"A subtração é {subtracao}")
print(f"A multiplicação é {multiplicacao}")
print(f"A divisão é {produto}")
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
print(f"Os números são iguais? {iguais}")
