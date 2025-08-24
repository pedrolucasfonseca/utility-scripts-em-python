tarefas = []

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    elif escolha == "2":
        print("\nLista de tarefas:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
    elif escolha == "3":
        num = int(input("Digite o número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida!")
        else:
            print("Número inválido.")
    elif escolha == "4":
        print("Saindo...")
        exit()
    else:
        print("Opção Inválida.")
