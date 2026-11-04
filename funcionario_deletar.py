import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def deletar_funcionario():
    id = input("Digite o ID do funcionário: ")

    cursor.execute(
        "DELETE FROM banco_usuarios WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Funcionário deletado!")
    else:
        print("Funcionário não encontrado!")


def deletar_servico():
    id = input("Digite o ID do serviço: ")

    cursor.execute(
        "DELETE FROM banco_servicos WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Serviço deletado!")
    else:
        print("Serviço não encontrado!")


def deletar_peca():
    id = input("Digite o ID da peça: ")

    cursor.execute(
        "DELETE FROM banco_pecas WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Peça deletada!")
    else:
        print("Peça não encontrada!")


def deletar_ordem():
    id = input("Digite o ID da ordem de serviço: ")

    cursor.execute(
        "DELETE FROM banco_ordens_servico WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Ordem de serviço deletada!")
    else:
        print("Ordem não encontrada!")


def deletar_os_servico():
    id = input("Digite o ID do serviço da ordem: ")

    cursor.execute(
        "DELETE FROM banco_os_servicos WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Serviço da ordem deletado!")
    else:
        print("Registro não encontrado!")


def deletar_os_peca():
    id = input("Digite o ID da peça da ordem: ")

    cursor.execute(
        "DELETE FROM banco_os_pecas WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Peça da ordem deletada!")
    else:
        print("Registro não encontrado!")


def deletar_pagamento():
    id = input("Digite o ID do pagamento: ")

    cursor.execute(
        "DELETE FROM banco_pagamentos WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Pagamento deletado!")
    else:
        print("Pagamento não encontrado!")


while True:
    print("\n===== DELETAR MOTORUP - FUNCIONÁRIOS =====")
    print("1 - Deletar funcionário")
    print("2 - Deletar serviço")
    print("3 - Deletar peça")
    print("4 - Deletar ordem de serviço")
    print("5 - Deletar serviço da ordem")
    print("6 - Deletar peça da ordem")
    print("7 - Deletar pagamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deletar_funcionario()
    elif opcao == "2":
        deletar_servico()
    elif opcao == "3":
        deletar_peca()
    elif opcao == "4":
        deletar_ordem()
    elif opcao == "5":
        deletar_os_servico()
    elif opcao == "6":
        deletar_os_peca()
    elif opcao == "7":
        deletar_pagamento()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()