import os
os.system("cls")

idade = int(input("Digite sua idade"))

if idade <16:
    print ("Voê não pode votar")    
elif (16<= idade <18) or idade >65:
    print ("Seu voto é opcional")
else: 
    print ("seu voto é obrigatorio")