# Construa um algoritmo que calcule a média aritmética de vários valores inteiros 
# positivos, inseridos pelo usuário. 
# O final da leitura acontecerá quando for lido um valor negativo.
# Mostre a média aritmética dos números informados pelo usuário.
import os
os.system

val = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro pos:  "))
    if numero < 0: 
        break
    soma += numero
    val += 1
if val > 0:
    media = soma / val
    print(f"voce digitou {val} númeoros")
    print(f"A média aritimética é: {media:.2f}")
else:
    print("\nNehum número positivo foi digitado. Não ha nada há caucular")
    
os.system
    
