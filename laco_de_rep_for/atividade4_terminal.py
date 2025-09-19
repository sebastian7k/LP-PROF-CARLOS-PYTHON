import os
os.system('cls' if os.name == 'nt' else 'clear')

#Crie um programa que solicite ao usuário seu login e uma senha.  
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 
#O programa deve solicitar o login e senha apenas três
#vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.

login_correto = "admin"
senha_correta = "1234"

tentativa =  0
max_tentativas = 3

for tentativa in range (max_tentativas): 
    print(f"---Tentaviva{tentativa + 1} de {max_tentativas}---")
    login = input ("Digite seu Login:")
    senha = input ("Digite sua Senha:")
    if login_correto == login and senha == senha_correta:
        print(f"\n>> Acesso concedido! Bem vindo {login_correto}!")
        break
    else:
        tentativas_restantantes = max_tentativas - (tentativa + 1)
        if tentativa > 0:
            print(f"\n>> Login ou senha incorretos. Você tem mais {tentativas_restantantes} tentiva(s).\n ")
else:
    print("\n>> Número máximo de tentativas atingido. Acesso bloqueado.")