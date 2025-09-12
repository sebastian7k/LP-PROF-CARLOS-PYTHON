import os 
os.system("cls")

nome = (input("Digite seu nome: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#cauculando a média

media = (nota1 + nota2) / 2
 
 #determinaindo o conceito

if media >= 9:
     conceito = "A"
elif media >= 7.5:
        conceito = "B"
elif media >= 6:
        conceito = "C"
elif media >= 4:
        conceito = "D"
else:
        conceito = "E"

#verificando aprovação

if conceito in ["A", "B", "C"]:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
    #mostrando os resultados
print(f"Nome: {nome}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")
