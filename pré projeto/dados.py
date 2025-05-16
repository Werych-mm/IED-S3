nomes = []
cidades = []
transportes = []

print("👾𝐖𝐄𝐋𝐂𝐎𝐌𝐄👾")
nome = input("Digite o ⋆.˚✮name✮˚.⋆ do usuário: ")
cidade = input("🌃𓍙.ೃ࿔*:･ Digite a cidade do usuário: ")
transporte_disponivel = input("O usuário possui algum tipo de transporte? 🚍🚛🚌🚲🛵(✅sim ou não❌) ")
tipo_transporte = {}

if transporte_disponivel == "sim":
    tipo_transporte["tipo"] = input("Qual o tipo de transporte que o usuário tem 🚍🚛🚌🚲🛵? ")
    tipo_transporte["capacidade"] = input("Quantas pessoas cabem no trasnporte do usuário? 👨‍👦‍👦 ")
    tipo_transporte["marca"] = input("Qual a marca do transporte do usuário? 📌 " )

else:
    tipo_transporte = None

nomes.append(nome)
cidades.append(cidade)
transportes.append(tipo_transporte)

print("📝Cadastro do usuário📝")
print(f"「 ✦ 𝐍𝐚𝐦𝐞 ✦ 」 {nomes[0]}")
print(f"✈︎Cidade: {cidades[0]}")

if transportes[0]:
    print("Transporte disponivel: Sim ✔️")
    print(f"Tipo de transporte: {transportes[0]['tipo']}")
    print(f"Capacidade: {transportes[0]['capacidade']}")
    print(f"Marca do transporte: {transportes[0]['marca']}")
else:
    print("Transporte disponivel: Não")
