usuarios = []

def adicionarpessoa():
    nome = input("﹒⌗﹒your name ⸝⸝: ")
    cidade = input("ᯓ ✈︎Cidade: ")
    transporte_disponivel = input("Possui transporte?🚌🚗🏍️🛵🚲 (sim/não): ")
    
    transporte = None
    if transporte_disponivel == "sim":
        transporte = {
            "tipo": input("Tipo do transporte 🚗🚘🚕: "),
            "capacidade": input("Capacidade📶: "),
            "marca": input("⌞Marca⌝: ")
        }

    usuario = {
        "nome": nome,
        "cidade": cidade,
        "transporte": transporte
    }

    usuarios.append(usuario)

def listar_usuarios():
    print("\n📝 Lista de Usuários 📝")
    for i, usuario in enumerate(usuarios):
        print(f"\n- ⭑𓂃 ⌗ USER 𖦹 🪷  {i + 1}")
        print(f"⋆˚࿔ 𝐧𝐚𝐦𝐞 𝜗𝜚˚⋆: {usuario['nome']}")
        print(f"🌃𓍙.ೃ࿔*Cidade: {usuario['cidade']}")
        if usuario['transporte']:
            print("Transporte: ✅️(ᵔᗜᵔ)")
            print(f" - 🔠Tipo🔠: {usuario['transporte']['tipo']}")
            print(f" - 🚚Capacidade🚚: {usuario['transporte']['capacidade']}")
            print(f" - 🏷️Marca🏷️: {usuario['transporte']['marca']}")
        else:
            print("Transporte: 🚫( ｡ •̀ ⤙ •́ ｡ )")

while True:
    print("MENU ☰")
    print("1️⃣. Adicionar usuário ✚")
    print("2️⃣. Listar usuários 💫")
    print("3️⃣. Sair 🔚")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionarpessoa()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        break
    else:
        print("�Opção inválida.�")

