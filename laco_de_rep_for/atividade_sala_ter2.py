# Escreva um algoritmo que pergunte ao usuário se deseja inserir
# mais uma nota, 
# se a resposta do usuário for “N”, 
# o programa fará a média aritmética das notas informadas 
# e mostrará a média aritmética para o usuário.
# Obs.: Use um contador dentro do laço de repetição para contar a
# quantidade de iterações (loops).

import os
os.system


soma_notas = 0.0
contador = 0


while True:
    try:
        nota=float(input(f"Digite a nota #{contador + 1 }:"))
        soma_notas += nota 
        contador += 1 
            
        resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
            
        if resposta == 'N':
            if contador > 0:
                media = soma_notas / contador
                print(f"\nVocê inseriu {contador}nota(s).")
                print(f"A média aritmética das notas é:{media:.2f}")
            else:
                print("Nenhuma nota foi insrida>")
            break
        elif resposta != 'S':
            print("Resposta Inválida. Digite apenas 'S' ou 'N'")
        
    except ValueError:
        print("Porfavor, insita uma nota válida(número)")