import  os 
os.system('cls' if os.name == 'nt' else 'clear')

#fazer um algoritmo que peça ao aluno uma nota  caso menor que 0 ou maior que 10 peça a nota novamente até que seja uma nota valida
#mostre a nota final usando while


nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota invalida.  Tente novamente.")
    nota = float(input("Digite uma nota entre 0 e 10: "))
print(f"Nota valida: {nota}")