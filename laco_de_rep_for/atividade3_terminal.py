import os
os.system('cls' if os.name == 'nt' else 'clear')
#Crie um programa que solicite ao usuário seu login e
#uma senha. 
#O programa deve continuar pedindo o login e a senha
#até que ambos estejam corretos. 

login_correto = "admin"
senha_correto = "1234"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login == login_correto and senha_correto == senha:
        print("Login e senha corretos. Acesso concedido.")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")