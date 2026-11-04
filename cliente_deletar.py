import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def deletar_cliente():
    id = input("Digite o ID do cliente: ")

    cursor.execute(
        "DELETE FROM banco_usuarios WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Cliente deletado!")
    else:
        print("Cliente não encontrado!")


def deletar_veiculo():
    id = input("Digite o ID do veículo: ")

    cursor.execute(
        "DELETE FROM banco_veiculos WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Veículo deletado!")
    else:
        print("Veículo não encontrado!")


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


def deletar_historico():
    id = input("Digite o ID do histórico: ")

    cursor.execute(
        "DELETE FROM banco_historico_os WHERE id=?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Histórico deletado!")
    else:
        print("Histórico não encontrado!")


while True:
    print("\n===== DELETAR MOTORUP - CLIENTES =====")
    print("1 - Deletar cliente")
    print("2 - Deletar veículo")
    print("3 - Deletar ordem de serviço")
    print("4 - Deletar histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deletar_cliente()
    elif opcao == "2":
        deletar_veiculo()
    elif opcao == "3":
        deletar_ordem()
    elif opcao == "4":
        deletar_historico()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()