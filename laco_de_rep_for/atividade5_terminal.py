#Escreva um algoritmo que leia três notas de um aluno.
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: 
#Se a média for a partir de 7, aprovado; 
#Se a média for entre 5 e 6,9, o aluno está em recuperação; 
#Caso seja menor que 5, o aluno está reprovado.
import os 
os.system("cls")

notas = []
numero_notas = 3 

for i in range(numero_notas):
    while True:
        try:
            nota = float(input(f"Digite a sua {i + 1}ª nota."))
            if 0 <= nota  <= 10:
                notas.append(nota)
                break
            else:
                print("Nota invalida. Digite uma válida.") 
        except ValueError: 
            print("Nota invalide digite apenas numeros.")
media = sum(notas) / len(notas)

if media >= 7:
    status = "Aprovado"
elif media <= 5.0:
    status = "Reprovado"
else:
    status = "Recupeação"

print(f"Sua media final é {media:.1f} você está {status}.")