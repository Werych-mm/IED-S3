tarefas = []            # Lista principal de tarefas (espaço pra digitar a tarefa)
historico = []          # Pilha para desfazer tarefas (onde elas estarão armazenadas)
fila_execucao = []      # Fila para executar tarefas ("ordem que mostrará as tarefas")

def adicionar_tarefa(tarefa): #Cria uma função com o nome "adiconar_tarefa" através do comando "def" servindo para que o usuario possa adicionar tarefas
    tarefas.append(tarefa) #O append serve para adiconar algo a uma váriavel, ou seja, o que usuário digitar vai ser adicionada a variável "tarefa" 
    historico.append(tarefa) #aqui o que usúario digitou vai ser guardado a variavél "historico", para que possa ser removida ou mostrada depois
    fila_execucao.append(tarefa) #determina a ordem que as tarefas vão ser mostradas para o usuario
    print(f"Tarefa '{tarefa}' adicionada!\n") #mostra a mensagem "tarefa (o que o usuario digitou) adicionada!"

def desfazer_ultima_tarefa(): #Cria uma função com o nome "desfazer_ultima_tarefa" através do comando "def" servindo para que o usuario possa desfazer a ultima tarefa
    if historico: #inicia uma condição com a variavel "historico" para saber se ela está vazia
        ultima = historico.pop() #aqui ele iguala variavel "ultima" a variavel "historico", com a propriedade de "pop" que vai servir pra remover algum contéudo que esteja guarado nela 
        tarefas.remove(ultima) #se a condição for verdadeira, ele removera o ultimo contéudo adicionado que estiver na variavel "ultima"
        fila_execucao.remove(ultima) #remove o ultimo conteudo que estiver guardado na variavel "fila_execucao"
        print(f"Tarefa '{ultima}' desfeita!\n") #mostra para o usuario "tarefa (ultima que ele digitou) desfeita!"
    else: #se ela estiver vazia o conteúdo da variavel "ultima" não seja igual ao conteudo da variavel "historico" com a proprieda "pop".
        print("Nenhuma tarefa para desfazer.\n") #o programa vai mostrar na tela a mensagem "Nenhuma tarefa para desfazer." 

def atender_tarefa(): #Cria uma função com o nome "atender_tarefa" através do comando "def" servindo para o usuario inforar ao programa que a tarefa foi finalizada
    if fila_execucao: #inicia uma condição com a variavel "fila_execucao" para analisar se ela está vazia
        feita = fila_execucao.pop(0) #se elas forem iguais, o programa irá remover a primeira tarefa que foi digitada pelo usuário(através do comando "pop") e guardada na várivael"fila_execucão"
        tarefas.remove(feita) #remove essa tarefa no espaço de memória onde estavam guardadas todas as tarefas
        print(f"Tarefa '{feita}' atendida!\n") #O programa vai mostar na tela a mensagem "Tarefa (que estiver primeiro na fila) foi atendida"
    else: #se a várivael "fila_execucao" estiver vazia
        print("Nenhuma tarefa para atender.\n") #O programa vai mostrar a mensagem "Nenhuma tarefa para atender."

def mostrar_tarefas(): #Cria uma função com o nome "mostrar_tarefas" através do comando "def" servindo para que o usuario possa ver as tarefas que ele digitou
    print("\n📋 Lista de Tarefas:") #O programa vai mostar na tela a mensagem "📋 Lista de Tarefas:"
    for i, t in enumerate(tarefas): #Usa a estrutura for com 'enumerate' que serve para pegar o índice e o conteúdo de cada tarefa
        print(f"{i + 1}. {t}") #O programa vai mostrar as tarefas que o usuario digitou (o i +1 foi usado para a lista começar do 1) 
    print() #O programa vai mostrar uma linha em branco(feita para fins estéticos e visibilade do terminal melhor)

while True: #Uma estrutura de repetição que serve para manter o menu funcionando até a opção de saída ser escolhida
    print("1. Adicionar Tarefa") #O programa vai mostrar na tela a mensagem "1. Adicionar Tarefa"
    print("2. Desfazer Última Tarefa") #O programa vai mostrar na tela a mensagem "Desfazer Última Tarefa"
    print("3. Atender Tarefa (modo fila)") #O programa vai mostrar na tela a mensagem "3. Atender Tarefa (modo fila)"
    print("4. Mostrar Tarefas") #O programa vai mostrar na tela a mensagem "4. Mostrar Tarefas"
    print("5. Sair") #O programa vai mostrar na tela a mensagem "5. Sair"

    opcao = input("Escolha uma opção: ") #Cria uma variavel chamada "opcao" que é igualada ao valor que usuário digitar(através do comando "input") 

    if opcao == '1':  #Incia uma condição com a variavel "opcao" para saber se o número que o usuario digitou foi "1"
        tarefa = input("Digite a tarefa: ")  #Iguala a várivael "tarefa" ao usuário digitar(atráves do input)
        adicionar_tarefa(tarefa)  #Chama a função "adicionar_tarefa" para que o programa possa adicionar a várivael "tarefa" o que o usuário digitou
    elif opcao == '2':  #Caso o número que foi igualado a várivael opcao for "2"
        desfazer_ultima_tarefa()  # Chama a função "desfazer_ultima_tarefa" para desfazer a última tarefa digitada pelo úsuario
    elif opcao == '3':  #Caso o número que foi igualado a várivael "opcao" for "3"
        atender_tarefa()  # Chama a função "atender_tarefa" para atender/finalizar a primeira tarefa da fila da váriavel "fila_execucao"
    elif opcao == '4':  #Caso o número que foi igualado a várivael "opcao" for "4"
        mostrar_tarefas()  # Chama a função "mostrar_tarefas" que serve para exibir todas as tarefas que estão na váriavel "fila_execucao"
    elif opcao == '5':  #Caso o número que foi igualado a várivael "opcao" for "5"
        print("Saindo do programa...")  #O programa vai mostrar a mensagem  "Saindo do programa..."
        break  #Finaliza a estrutura de repetição e saí do programa
    else: #Caso o usúario tenha digitado qualquer outra coisa dos números citados acima
        print("Opção inválida!\n")  #O programa vai mostar a mensagem "Opção inválida!"