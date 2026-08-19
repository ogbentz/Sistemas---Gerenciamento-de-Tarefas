ARQUIVO = "tarefas.txt"


def carregar_tarefas():
    tarefas = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha:
                    dados = linha.split("|")

                    tarefa = {
                        "titulo": dados[0],
                        "descricao": dados[1],
                        "status": dados[2]
                    }

                    tarefas.append(tarefa)

    except FileNotFoundError:
        pass

    return tarefas


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(
                f"{tarefa['titulo']}|"
                f"{tarefa['descricao']}|"
                f"{tarefa['status']}\n"
            )


def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR TAREFA ---")

    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()

    if titulo == "":
        print("O título não pode ficar vazio.")
        return

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    print("\n--- LISTA DE TAREFAS ---")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status']}")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    try:
        numero = int(input("\nDigite o número da tarefa concluída: "))

        if numero < 1 or numero > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefas[numero - 1]["status"] = "Concluída"
        salvar_tarefas(tarefas)

        print("Tarefa marcada como concluída!")

    except ValueError:
        print("Digite apenas números.")


def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    try:
        numero = int(input("\nDigite o número da tarefa que deseja excluir: "))

        if numero < 1 or numero > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefa_removida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)

        print(
            f"A tarefa '{tarefa_removida['titulo']}' "
            "foi excluída com sucesso!"
        )

    except ValueError:
        print("Digite apenas números.")


def exibir_menu():
    print("\n==============================")
    print("   GERENCIADOR DE TAREFAS")
    print("==============================")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")
    print("==============================")


def main():
    tarefas = carregar_tarefas()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            excluir_tarefa(tarefas)

        elif opcao == "5":
            print("\nSistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()ARQUIVO = "tarefas.txt"


def carregar_tarefas():
    tarefas = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha:
                    dados = linha.split("|")

                    tarefa = {
                        "titulo": dados[0],
                        "descricao": dados[1],
                        "status": dados[2]
                    }

                    tarefas.append(tarefa)

    except FileNotFoundError:
        pass

    return tarefas


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(
                f"{tarefa['titulo']}|"
                f"{tarefa['descricao']}|"
                f"{tarefa['status']}\n"
            )


def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR TAREFA ---")

    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()

    if titulo == "":
        print("O título não pode ficar vazio.")
        return

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    print("\n--- LISTA DE TAREFAS ---")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status']}")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    try:
        numero = int(input("\nDigite o número da tarefa concluída: "))

        if numero < 1 or numero > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefas[numero - 1]["status"] = "Concluída"
        salvar_tarefas(tarefas)

        print("Tarefa marcada como concluída!")

    except ValueError:
        print("Digite apenas números.")


def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    try:
        numero = int(input("\nDigite o número da tarefa que deseja excluir: "))

        if numero < 1 or numero > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefa_removida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)

        print(
            f"A tarefa '{tarefa_removida['titulo']}' "
            "foi excluída com sucesso!"
        )

    except ValueError:
        print("Digite apenas números.")


def exibir_menu():
    print("\n==============================")
    print("   GERENCIADOR DE TAREFAS")
    print("==============================")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")
    print("==============================")


def main():
    tarefas = carregar_tarefas()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            excluir_tarefa(tarefas)

        elif opcao == "5":
            print("\nSistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
