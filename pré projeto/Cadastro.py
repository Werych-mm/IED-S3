usuarios = []  # Lista principal

def adicionarpessoa():
    nome = input("Nome do usuário: ")
    cidade = input("Cidade: ")
    transporte_disponivel = input("Possui transporte? (sim/não): ")
    
    transporte = None
    if transporte_disponivel == "sim":
        transporte = {
            "tipo": input("Tipo do transporte: "),
            "capacidade": input("Capacidade: "),
            "marca": input("Marca: ")
        }

    usuario = {
        "nome": nome,
        "cidade": cidade,
        "transporte": transporte
    }

    usuarios.append(usuario)  # Adiciona o dicionário na lista

# Exibir todos os usuários cadastrados
def listar_usuarios():
    print("\n📝 Lista de Usuários 📝")
    for i, usuario in enumerate(usuarios):
        print(f"\nUsuário {i + 1}")
        print(f"Nome: {usuario['nome']}")
        print(f"Cidade: {usuario['cidade']}")
        if usuario['transporte']:
            print("Transporte: Sim")
            print(f" - Tipo: {usuario['transporte']['tipo']}")
            print(f" - Capacidade: {usuario['transporte']['capacidade']}")
            print(f" - Marca: {usuario['transporte']['marca']}")
        else:
            print("Transporte: Não")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionarpessoa()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")
