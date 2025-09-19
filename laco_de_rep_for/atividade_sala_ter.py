# Cardápio do restaurante
cardapio = {
    1: {"prato": "Picanha", "preco": 25.00},
    2: {"prato": "Lasanha", "preco": 20.00},
    3: {"prato": "Strogonoff", "preco": 18.00},
    4: {"prato": "Bife acebolado", "preco": 15.00},
    5: {"prato": "Pão com ovo", "preco": 5.00}
}

total_a_pagar = 0.0
pedidos = []

print("Bem-vindo ao restaurante!")

# Loop principal
while True:
    # Exibe o cardápio
    print("\nNosso cardápio:")
    for codigo, detalhes in cardapio.items():
        print(f"{codigo}: {detalhes['prato']} - R$ {detalhes['preco']:.2f}")

    try:
        # Solicita o código do prato
        escolha = int(input("\nDigite o código do prato que você deseja: "))

        # Usando match-case para verificar a escolha
        match escolha:
            case 1 | 2 | 3 | 4 | 5:
                prato_escolhido = cardapio[escolha]
                total_a_pagar += prato_escolhido["preco"]
                pedidos.append(prato_escolhido["prato"])
                print(f"Você adicionou '{prato_escolhido['prato']}' ao seu pedido.")
                print(f"Subtotal: R$ {total_a_pagar:.2f}")
            
            case _:
                print("Código inválido! Por favor, escolha uma opção do cardápio.")
                continue  # Volta ao início do loop sem perguntar se deseja continuar

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")
        continue

    # Pergunta se o cliente deseja continuar
    while True:
        continuar = input("Deseja escolher outro prato? (s/n): ").strip().lower()
        if continuar in ['s', 'sim']:
            break  # Volta para o início do loop principal
        elif continuar in ['n', 'não', 'nao']:
            print("\n=========================================")
            print("             Resumo do Pedido            ")
            print("=========================================")
            if pedidos:
                print("Pratos escolhidos:")
                for item in pedidos:
                    print(f"- {item}")
                print(f"\nTotal a pagar: R$ {total_a_pagar:.2f}")
            else:
                print("Nenhum pedido foi feito.")
            print("\nObrigado e bom apetite!")
            print("=========================================")
            exit()  # Encerra o programa
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
