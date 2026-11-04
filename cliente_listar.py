import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def listar_clientes():
    cursor.execute("SELECT * FROM banco_usuarios")
    dados = cursor.fetchall()

    print("\n===== CLIENTES =====")
    for linha in dados:
        print(linha)


def listar_veiculos():
    cursor.execute("SELECT * FROM banco_veiculos")
    dados = cursor.fetchall()

    print("\n===== VEÍCULOS =====")
    for linha in dados:
        print(linha)


def listar_ordens():
    cursor.execute("SELECT * FROM banco_ordens_servico")
    dados = cursor.fetchall()

    print("\n===== ORDENS DE SERVIÇO =====")
    for linha in dados:
        print(linha)


def listar_historico():
    cursor.execute("SELECT * FROM banco_historico_os")
    dados = cursor.fetchall()

    print("\n===== HISTÓRICO DE SERVIÇO =====")
    for linha in dados:
        print(linha)


def listar_pagamentos():
    cursor.execute("SELECT * FROM banco_pagamentos")
    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")
    for linha in dados:
        print(linha)


while True:
    print("\n===== MOTORUP - CLIENTES =====")
    print("1 - Listar clientes")
    print("2 - Listar veículos")
    print("3 - Listar ordens de serviço")
    print("4 - Listar histórico")
    print("5 - Listar pagamentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_clientes()
    elif opcao == "2":
        listar_veiculos()
    elif opcao == "3":
        listar_ordens()
    elif opcao == "4":
        listar_historico()
    elif opcao == "5":
        listar_pagamentos()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()