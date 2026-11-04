import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def listar_funcionarios():
    cursor.execute("SELECT * FROM banco_usuarios")
    dados = cursor.fetchall()

    print("\n===== FUNCIONÁRIOS =====")
    for linha in dados:
        print(linha)


def listar_servicos():
    cursor.execute("SELECT * FROM banco_servicos")
    dados = cursor.fetchall()

    print("\n===== SERVIÇOS =====")
    for linha in dados:
        print(linha)


def listar_pecas():
    cursor.execute("SELECT * FROM banco_pecas")
    dados = cursor.fetchall()

    print("\n===== PEÇAS =====")
    for linha in dados:
        print(linha)


def listar_ordens():
    cursor.execute("SELECT * FROM banco_ordens_servico")
    dados = cursor.fetchall()

    print("\n===== ORDENS DE SERVIÇO =====")
    for linha in dados:
        print(linha)


def listar_os_servicos():
    cursor.execute("SELECT * FROM banco_os_servicos")
    dados = cursor.fetchall()

    print("\n===== SERVIÇOS DAS ORDENS =====")
    for linha in dados:
        print(linha)


def listar_os_pecas():
    cursor.execute("SELECT * FROM banco_os_pecas")
    dados = cursor.fetchall()

    print("\n===== PEÇAS DAS ORDENS =====")
    for linha in dados:
        print(linha)


def listar_pagamentos():
    cursor.execute("SELECT * FROM banco_pagamentos")
    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")
    for linha in dados:
        print(linha)


while True:
    print("\n===== MOTORUP - FUNCIONÁRIOS =====")
    print("1 - Listar funcionários")
    print("2 - Listar serviços")
    print("3 - Listar peças")
    print("4 - Listar ordens de serviço")
    print("5 - Listar serviços das ordens")
    print("6 - Listar peças das ordens")
    print("7 - Listar pagamentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_funcionarios()
    elif opcao == "2":
        listar_servicos()
    elif opcao == "3":
        listar_pecas()
    elif opcao == "4":
        listar_ordens()
    elif opcao == "5":
        listar_os_servicos()
    elif opcao == "6":
        listar_os_pecas()
    elif opcao == "7":
        listar_pagamentos()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()