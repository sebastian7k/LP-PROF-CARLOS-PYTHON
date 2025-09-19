import os
os.system('cls' if os.name == 'nt' else 'clear')

#Escreva um algoritmo que solicite duas notas para um aluno. 
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Calcule e mostre a média aritmética do aluno.

nota1 = float(input("Digite a primeira nota entre 0 e 10: "))
nota2 = float(input("Digite a segunda nota entre 0 e 10: "))
while nota1 < 0 or nota1 > 10:
    print("Nota invalida.  Tente novamente.")
    nota1 = float(input("Digite a primeira nota entre 0 e 10: "))
while nota2 < 0 or nota2 > 10:
    print("Nota invalida.  Tente novamente.")
    nota2 = float(input("Digite a segunda nota entre 0 e 10: "))
    media = (nota1 + nota2) / 2
print(f"A sua média é : {media}")