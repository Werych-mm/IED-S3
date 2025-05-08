tarefas = []            # Lista principal de tarefas (espaço pra digitar a tarefa)
historico = []          # Pilha para desfazer tarefas (onde elas estarão armazenadas)
fila_execucao = []      # Fila para executar tarefas ("ordem que mostrará as tarefas")

tarefas_completa = []   # Lista para armazenar tarefas incluindo as informações de prioridade e data

def adicionar_tarefa(tarefa): # Cria uma função com o nome "adicionar_tarefa" através do comando "def" servindo para que o usuario possa adicionar tarefas
    prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ") # Solicita ao usuário para digitar a prioridade da tarefa
    data = input("Digite a data de vencimento (formato: dd/mm/aaaa): ") # Solicita ao usuário para digitar a data de vencimento
    tarefa_completa = (tarefa, prioridade, data) # iguala a tupla(um tipo de lista que é imutavél) com tarefa, prioridade e data a váriavel "tarefa_completa"
    tarefas_completa.append(tarefa_completa) # Adiciona a tupla à lista "tarefa_completa"
    tarefas.append(tarefa) # O append serve para adicionar algo a uma variável, ou seja, o que usuário digitar vai ser adicionada à variável "tarefas"
    historico.append(tarefa) # Aqui o que o usuário digitou vai ser guardado na variável "historico", para que possa ser removido ou mostrado depois
    fila_execucao.append(tarefa) # Determina a ordem que as tarefas vão ser mostradas para o usuário
    print(f"Tarefa '{tarefa}' com prioridade '{prioridade}' e data '{data}' adicionada!\n") # Mostra a mensagem "Tarefa (que o usuario digitou) com prioridade (que o usuario digitou) e data (que o usuario digitou)' adicionada!"

def desfazer_ultima_tarefa(): # Cria uma função com o nome "desfazer_ultima_tarefa" através do comando "def" servindo para que o usuário possa desfazer a última tarefa
    if historico: # Inicia uma condição com a variável "historico" para saber se ela está vazia
        ultima = historico.pop() # Aqui ele iguala variável "ultima" à variável "historico", com a propriedade de "pop" que vai servir pra remover algum conteúdo que esteja guardado nela 
        tarefas.remove(ultima) # Se a condição for verdadeira, ele removerá o último conteúdo adicionado que estiver na variável "ultima"
        fila_execucao.remove(ultima) # Remove o último conteúdo que estiver guardado na variável "fila_execucao"
        print(f"Tarefa '{ultima}' desfeita!\n") # Mostra para o usuário "tarefa (última que ele digitou) desfeita!"
    else: # Se ela estiver vazia o conteúdo da variável "ultima" não será igual ao conteúdo da variável "historico" com a propriedade "pop".
        print("Nenhuma tarefa para desfazer.\n") # O programa vai mostrar na tela a mensagem "Nenhuma tarefa para desfazer."

def atender_tarefa(): # Cria uma função com o nome "atender_tarefa" através do comando "def" servindo para o usuário informar ao programa que a tarefa foi finalizada
    if fila_execucao: # Inicia uma condição com a variável "fila_execucao" para analisar se ela está vazia
        feita = fila_execucao.pop(0) # Se elas forem iguais, o programa irá remover a primeira tarefa que foi digitada pelo usuário (através do comando "pop") e guardada na variável "fila_execução"
        tarefas.remove(feita) # Remove essa tarefa no espaço de memória onde estavam guardadas todas as tarefas
        print(f"Tarefa '{feita}' atendida!\n") # O programa vai mostrar na tela a mensagem "Tarefa (que estiver primeiro na fila) foi atendida"
    else: # Se a variável "fila_execucao" estiver vazia
        print("Nenhuma tarefa para atender.\n") # O programa vai mostrar a mensagem "Nenhuma tarefa para atender."

def mostrar_tarefas(): # Cria uma função com o nome "mostrar_tarefas" através do comando "def" servindo para que o usuário possa ver as tarefas que ele digitou
    print("\n📋 Lista de Tarefas:") # O programa vai mostrar na tela a mensagem "📋 Lista de Tarefas:"
    for i, t in enumerate(tarefas_completa): # Agora, o programa vai enumerar as tarefas com prioridade e data
        tarefa, prioridade, data = t # Desempacota a tupla de cada tarefa para mostrar a tarefa, prioridade e data
        print(f"{i + 1}. {tarefa} - Prioridade: {prioridade} - Data: {data}") # O programa vai mostrar a mensagem "(tarefa que o úsario digitou) - Prioridade: (que o usuário digitou) - Data: (que o usu1ário digitou)"
    print() # O programa vai mostrar uma linha em branco (feita para fins estéticos e visibilidade do terminal melhor)

while True: # Uma estrutura de repetição que serve para manter o menu funcionando até a opção de saída ser escolhida
    print("1. Adicionar Tarefa") # O programa vai mostrar na tela a mensagem "1. Adicionar Tarefa"
    print("2. Desfazer Última Tarefa") # O programa vai mostrar na tela a mensagem "Desfazer Última Tarefa"
    print("3. Atender Tarefa (modo fila)") # O programa vai mostrar na tela a mensagem "3. Atender Tarefa (modo fila)"
    print("4. Mostrar Tarefas") # O programa vai mostrar na tela a mensagem "4. Mostrar Tarefas"
    print("5. Sair") # O programa vai mostrar na tela a mensagem "5. Sair"

    opcao = input("Escolha uma opção: ") # Cria uma variável chamada "opcao" que é igualada ao valor que o usuário digitar (através do comando "input")

    if opcao == '1':  # Inicia uma condição com a variável "opcao" para saber se o número que o usuário digitou foi "1"
        tarefa = input("Digite a tarefa: ")  # Iguala a variável "tarefa" ao que o usuário digitar (através do input)
        adicionar_tarefa(tarefa)  # Chama a função "adicionar_tarefa" para que o programa possa adicionar à variável "tarefas" o que o usuário digitou
    elif opcao == '2':  # Caso o número que foi igualado à variável "opcao" for "2"
        desfazer_ultima_tarefa()  # Chama a função "desfazer_ultima_tarefa" para desfazer a última tarefa digitada pelo usuário
    elif opcao == '3':  # Caso o número que foi igualado à variável "opcao" for "3"
        atender_tarefa()  # Chama a função "atender_tarefa" para atender/finalizar a primeira tarefa da fila da variável "fila_execucao"
    elif opcao == '4':  # Caso o número que foi igualado à variável "opcao" for "4"
        mostrar_tarefas()  # Chama a função "mostrar_tarefas" que serve para exibir todas as tarefas que estão na variável "tarefas_completa"
    elif opcao == '5':  # Caso o número que foi igualado à variável "opcao" for "5"
        print("Saindo do programa...")  # O programa vai mostrar a mensagem "Saindo do programa..."
        break  # Finaliza a estrutura de repetição e sai do programa
    else: # Caso o usuário tenha digitado qualquer outra coisa dos números citados acima
        print("Opção inválida!\n")  # O programa vai mostrar a mensagem "Opção inválida!"
