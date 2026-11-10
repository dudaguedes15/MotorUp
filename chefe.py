
import sqlite3

conexao = sqlite3.connect("motorup.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()


def cadastrar_servico():
    nome = input("Nome do serviço: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    tempo = int(input("Tempo estimado em minutos: "))

    cursor.execute("""
    INSERT INTO banco_servicos
    (nome, descricao, preco, tempo_estimado)
    VALUES (?, ?, ?, ?)
    """, (nome, descricao, preco, tempo))

    conexao.commit()
    print("Serviço cadastrado!")


def listar_servicos():
    cursor.execute("SELECT * FROM banco_servicos")
    dados = cursor.fetchall()

    print("\n===== SERVIÇOS =====")

    for linha in dados:
        print(linha)


def atualizar_servico():
    id_servico = input("ID do serviço: ")
    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    tempo = int(input("Novo tempo estimado: "))

    cursor.execute("""
    UPDATE banco_servicos
    SET nome=?, descricao=?, preco=?, tempo_estimado=?
    WHERE id=?
    """, (nome, descricao, preco, tempo, id_servico))

    conexao.commit()
    print("Serviço atualizado!")


def deletar_servico():
    id_servico = input("ID do serviço: ")

    try:
        cursor.execute(
            "DELETE FROM banco_servicos WHERE id=?",
            (id_servico,)
        )

        conexao.commit()
        print("Operação de exclusão realizada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Esse serviço está vinculado a uma ordem de serviço.")


def cadastrar_peca():
    nome = input("Nome da peça: ")
    codigo = input("Código: ")
    estoque = int(input("Quantidade em estoque: "))
    preco = float(input("Preço: "))

    cursor.execute("""
    INSERT INTO banco_pecas
    (nome, codigo, estoque, preco)
    VALUES (?, ?, ?, ?)
    """, (nome, codigo, estoque, preco))

    conexao.commit()
    print("Peça cadastrada!")


def listar_pecas():
    cursor.execute("SELECT * FROM banco_pecas")
    dados = cursor.fetchall()

    print("\n===== PEÇAS =====")

    for linha in dados:
        print(linha)


def atualizar_peca():
    id_peca = input("ID da peça: ")
    nome = input("Novo nome: ")
    codigo = input("Novo código: ")
    estoque = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))

    cursor.execute("""
    UPDATE banco_pecas
    SET nome=?, codigo=?, estoque=?, preco=?
    WHERE id=?
    """, (nome, codigo, estoque, preco, id_peca))

    conexao.commit()
    print("Peça atualizada!")


def deletar_peca():
    id_peca = input("ID da peça: ")

    try:
        cursor.execute(
            "DELETE FROM banco_pecas WHERE id=?",
            (id_peca,)
        )

        conexao.commit()
        print("Operação de exclusão realizada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Essa peça está vinculada a uma ordem de serviço.")



def listar_pagamentos_gerente():
    cursor.execute("SELECT * FROM banco_pagamentos")
    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")

    for linha in dados:
        print(linha)


def faturamento():
    cursor.execute("SELECT valor, status FROM banco_pagamentos")
    dados = cursor.fetchall()

    total = 0

    for linha in dados:
        if linha[1].lower() == "pago":
            total = total + linha[0]

    print("\n===== FATURAMENTO =====")
    print("Total recebido: R$", total)



def relatorio_ordens():
    cursor.execute("SELECT * FROM banco_ordens_servico")
    dados = cursor.fetchall()

    print("\n===== RELATÓRIO DE ORDENS =====")

    for linha in dados:
        print(linha)



def menu_servicos_gerente():
    while True:
        print("\n===== GERENCIAR SERVIÇOS =====")
        print("1 - Cadastrar serviço")
        print("2 - Listar serviços")
        print("3 - Atualizar serviço")
        print("4 - Deletar serviço")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_servico()

            case "2":
                listar_servicos()

            case "3":
                atualizar_servico()

            case "4":
                deletar_servico()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_pecas_gerente():
    while True:
        print("\n===== GERENCIAR PEÇAS =====")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Atualizar peça")
        print("4 - Deletar peça")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_peca()

            case "2":
                listar_pecas()

            case "3":
                atualizar_peca()

            case "4":
                deletar_peca()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_financeiro():
    while True:
        print("\n===== CONTROLE FINANCEIRO =====")
        print("1 - Listar pagamentos")
        print("2 - Ver faturamento")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_pagamentos_gerente()

            case "2":
                faturamento()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_gerente():
    while True:
        print("\n===== MOTORUP - ÁREA DO GERENTE =====")
        print("1 - Gerenciar serviços")
        print("2 - Gerenciar peças")
        print("3 - Controle financeiro")
        print("4 - Relatório de ordens de serviço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                menu_servicos_gerente()

            case "2":
                menu_pecas_gerente()

            case "3":
                menu_financeiro()

            case "4":
                relatorio_ordens()

            case "0":
                print("Saindo da área do gerente!")
                break

            case _:
                print("Opção inválida!")


menu_gerente()

conexao.close()
