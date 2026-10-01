import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


def deletar_usuario():

    id = input("ID do usuário: ")

    cursor.execute(f'''
    DELETE FROM banco_usuarios
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Usuário excluído!")


def deletar_veiculo():

    id = input("ID do veículo: ")

    cursor.execute(f'''
    DELETE FROM banco_veiculos
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Veículo excluído!")


def deletar_servico():

    id = input("ID do serviço: ")

    cursor.execute(f'''
    DELETE FROM banco_servicos
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Serviço excluído!")


def deletar_peca():

    id = input("ID da peça: ")

    cursor.execute(f'''
    DELETE FROM banco_pecas
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Peça excluída!")


def deletar_ordem():

    id = input("ID da ordem de serviço: ")

    cursor.execute(f'''
    DELETE FROM banco_ordens_servico
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Ordem de serviço excluída!")


def deletar_os_servico():

    id = input("ID do serviço da ordem: ")

    cursor.execute(f'''
    DELETE FROM banco_os_servicos
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Serviço da ordem excluído!")


def deletar_os_peca():

    id = input("ID da peça da ordem: ")

    cursor.execute(f'''
    DELETE FROM banco_os_pecas
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Peça da ordem excluída!")


def deletar_historico():

    id = input("ID do histórico: ")

    cursor.execute(f'''
    DELETE FROM banco_historico_os
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Histórico excluído!")


def deletar_pagamento():

    id = input("ID do pagamento: ")

    cursor.execute(f'''
    DELETE FROM banco_pagamentos
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Pagamento excluído!")


while True:

    print("\n===== MOTORUP - DELETE =====")
    print("1 - Deletar usuário")
    print("2 - Deletar veículo")
    print("3 - Deletar serviço")
    print("4 - Deletar peça")
    print("5 - Deletar ordem de serviço")
    print("6 - Deletar serviço da ordem")
    print("7 - Deletar peça da ordem")
    print("8 - Deletar histórico")
    print("9 - Deletar pagamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deletar_usuario()

    elif opcao == "2":
        deletar_veiculo()

    elif opcao == "3":
        deletar_servico()

    elif opcao == "4":
        deletar_peca()

    elif opcao == "5":
        deletar_ordem()

    elif opcao == "6":
        deletar_os_servico()

    elif opcao == "7":
        deletar_os_peca()

    elif opcao == "8":
        deletar_historico()

    elif opcao == "9":
        deletar_pagamento()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")


conexao.close()