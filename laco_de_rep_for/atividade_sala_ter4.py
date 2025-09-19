# Faça um algoritmo que leia uma quantidade não
# determinada de números inteiros positivos. Calcule: 
# a.quantidade de números pares e ímpares;  
# b.média de valores pares   
# b.média geral dos números lidos.  
# O número que encerrará a leitura será o número zero

print("Algoritimo de numeros impares ")

par = 0
impar = 0
soma_par = 0
soma_impar= 0
quant_par = 0
quant_impar = 0 

while True:
    numero = int(input("Digite um numero"))
    if numero == 0:
         break
    if numero%2==0:
        par += 1
        soma_par += numero
        media_par = soma_par / quant_par
    else:
        impar += 1
        soma_impar += numero
        media_impar = soma_impar / quant_par
print(f"Quantidade de números pares: {quant_par}. ")
print(f"A soma de numeros pares:{soma_par} ")
print(f"A media de numeros par é ")
print(f"Quantidade de números impares: {quant_impar}}.")
