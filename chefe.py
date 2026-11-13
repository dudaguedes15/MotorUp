from erros import tratar_erro
import sqlite3

conexao = sqlite3.connect("motorup.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()


def listar_clientes():
    cursor.execute("""
    SELECT id, nome, cpf, telefone, email
    FROM banco_usuarios
    WHERE tipo = 'cliente'
    ORDER BY nome
    """)

    dados = cursor.fetchall()

    print("\n===== CLIENTES CADASTRADOS =====")

    if len(dados) == 0:
        print("Nenhum cliente cadastrado!")
    else:
        for linha in dados:
            print("ID:", linha[0])
            print("Nome:", linha[1])
            print("CPF:", linha[2])
            print("Telefone:", linha[3])
            print("Email:", linha[4])
            print("------------------------")


def listar_funcionarios():
    cursor.execute("""
    SELECT id, nome, cpf, telefone, email
    FROM banco_usuarios
    WHERE tipo = 'funcionario'
    ORDER BY nome
    """)

    dados = cursor.fetchall()

    print("\n===== FUNCIONÁRIOS CADASTRADOS =====")

    if len(dados) == 0:
        print("Nenhum funcionário cadastrado!")
    else:
        for linha in dados:
            print("ID:", linha[0])
            print("Nome:", linha[1])
            print("CPF:", linha[2])
            print("Telefone:", linha[3])
            print("Email:", linha[4])
            print("------------------------")


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

    if len(dados) == 0:
        print("Nenhum serviço cadastrado!")
    else:
        for linha in dados:
            print(linha)


def atualizar_servico():
    id_servico = int(input("ID do serviço: "))

    cursor.execute(
        "SELECT id FROM banco_servicos WHERE id=?",
        (id_servico,)
    )

    if cursor.fetchone() is None:
        print("Serviço não encontrado!")
        return

    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    tempo = input("Novo tempo estimado: ")

    cursor.execute("""
    UPDATE banco_servicos
    SET nome=?, descricao=?, preco=?, tempo_estimado=?
    WHERE id=?
    """, (nome, descricao, preco, tempo, id_servico))

    conexao.commit()
    print("Serviço atualizado!")


def deletar_servico():
    id_servico = int(input("ID do serviço: "))

    cursor.execute(
        "SELECT id FROM banco_servicos WHERE id=?",
        (id_servico,)
    )

    if cursor.fetchone() is None:
        print("Serviço não encontrado!")
        return

    try:
        cursor.execute(
            "DELETE FROM banco_servicos WHERE id=?",
            (id_servico,)
        )

        conexao.commit()
        print("Serviço deletado!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Serviço vinculado a uma ordem.")


def cadastrar_peca():
    nome = input("Nome da peça: ")
    codigo = input("Código: ")
    estoque = int(input("Quantidade em estoque: "))
    preco = float(input("Preço: "))

    try:
        cursor.execute("""
        INSERT INTO banco_pecas
        (nome, codigo, estoque, preco)
        VALUES (?, ?, ?, ?)
        """, (nome, codigo, estoque, preco))

        conexao.commit()
        print("Peça cadastrada!")

    except sqlite3.IntegrityError:
        print("Esse código já está cadastrado!")


def listar_pecas():
    cursor.execute("SELECT * FROM banco_pecas")
    dados = cursor.fetchall()

    print("\n===== PEÇAS =====")

    if len(dados) == 0:
        print("Nenhuma peça cadastrada!")
    else:
        for linha in dados:
            print(linha)


def atualizar_peca():
    id_peca = input("ID da peça: ")

    cursor.execute(
        "SELECT id FROM banco_pecas WHERE id=?",
        (id_peca,)
    )

    if cursor.fetchone() is None:
        print("Peça não encontrada!")
        return

    nome = input("Novo nome: ")
    codigo = input("Novo código: ")
    try:
        estoque = int(input("Nova quantidade: "))

    except Exception as erro:
        tratar_erro(erro)
    return
    preco = float(input("Novo preço: "))

    try:
        cursor.execute("""
        UPDATE banco_pecas
        SET nome=?, codigo=?, estoque=?, preco=?
        WHERE id=?
        """, (nome, codigo, estoque, preco, id_peca))

        conexao.commit()
        print("Peça atualizada!")

    except sqlite3.IntegrityError:
        print("Esse código já está cadastrado!")


def deletar_peca():
    id_peca = input("ID da peça: ")

    cursor.execute(
        "SELECT id FROM banco_pecas WHERE id=?",
        (id_peca,)
    )

    if cursor.fetchone() is None:
        print("Peça não encontrada!")
        return

    try:
        cursor.execute(
            "DELETE FROM banco_pecas WHERE id=?",
            (id_peca,)
        )

        conexao.commit()
        print("Peça deletada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Essa peça está vinculada a uma ordem de serviço.")


def listar_pagamentos_gerente():
    cursor.execute("SELECT * FROM banco_pagamentos")
    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")

    if len(dados) == 0:
        print("Nenhum pagamento cadastrado!")
    else:
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
    print("Total recebido: R$", round(total, 2))


def relatorio_ordens():
    cursor.execute("""
    SELECT
        banco_ordens_servico.id,
        banco_usuarios.nome,
        banco_veiculos.placa,
        banco_veiculos.modelo,
        banco_ordens_servico.data_entrada,
        banco_ordens_servico.status,
        banco_ordens_servico.observacoes
    FROM banco_ordens_servico
    INNER JOIN banco_veiculos
    ON banco_ordens_servico.veiculo_id = banco_veiculos.id
    INNER JOIN banco_usuarios
    ON banco_veiculos.usuario_id = banco_usuarios.id
    ORDER BY banco_ordens_servico.id
    """)

    dados = cursor.fetchall()

    print("\n===== RELATÓRIO DE ORDENS =====")

    if len(dados) == 0:
        print("Nenhuma ordem de serviço cadastrada!")
    else:
        for linha in dados:
            print("ID da ordem:", linha[0])
            print("Cliente:", linha[1])
            print("Placa:", linha[2])
            print("Modelo:", linha[3])
            print("Data de entrada:", linha[4])
            print("Status:", linha[5])
            print("Observações:", linha[6])
            print("------------------------")


def menu_usuarios():
    while True:
        print("\n===== CONSULTAR USUÁRIOS =====")
        print("1 - Consultar clientes")
        print("2 - Consultar funcionários")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_clientes()

            case "2":
                listar_funcionarios()

            case "0":
                break

            case _:
                print("Opção inválida!")


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
        print("1 - Consultar clientes e funcionários")
        print("2 - Gerenciar serviços")
        print("3 - Gerenciar peças")
        print("4 - Controle financeiro")
        print("5 - Relatório de ordens de serviço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                menu_usuarios()

            case "2":
                menu_servicos_gerente()

            case "3":
                menu_pecas_gerente()

            case "4":
                menu_financeiro()

            case "5":
                relatorio_ordens()

            case "0":
                print("Saindo da área do gerente!")
                break

            case _:
                print("Opção inválida!")


menu_gerente()

conexao.close()
