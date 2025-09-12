#escreva um algoritimo que solicite ao usuario  a nota de um aluno 
#caso seja menor que 0 ou maior que 10 solicite a nota novamente

import os 
os.system("cls")

print("Laço de repetição WHILE")
nota = float(input("Digite a sua nota: "))

tentativas = 0
max_tentativas = 3

while True:
    nota = float(input("digite a sua nota: "))
    if 0 <= nota <= 10:
          print(f"Sua nota é: {nota}")
          break
    else:
        tentativas += 1
        print(f"Nota inválida! A nota deve ser entre 0 e 10. {tentativas} de {max_tentativas} tentativas.")
        
        if tentativas >= max_tentativas:
            print("Número máximo de tentativas atingido. Encerrando o programa.")
            break
print ("Acabou")

