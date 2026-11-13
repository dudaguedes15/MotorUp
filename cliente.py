
import sqlite3

conexao = sqlite3.connect("motorup.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()


def cadastrar_cliente():
    
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    senha = input("Senha: ")

    try:
        cursor.execute("""
        INSERT INTO banco_usuarios
        (nome, cpf, telefone, email, senha, tipo)
        VALUES (?, ?, ?, ?, ?, 'cliente')
        """, (nome, cpf, telefone, email, senha))

        conexao.commit()
        print("Cliente cadastrado!")

    except sqlite3.IntegrityError:
        print("CPF ou email já cadastrado!")


def cadastrar_veiculo():

    usuario_id = input("ID do cliente: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'cliente'
    """, (usuario_id,))

    if cursor.fetchone() is None:
        print("Cliente não encontrado!")
        return

    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")

    try:
        cursor.execute("""
        INSERT INTO banco_veiculos
        (usuario_id, placa, marca, modelo, ano, cor)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (usuario_id, placa, marca, modelo, ano, cor))

        conexao.commit()
        print("Veículo cadastrado!")

    except sqlite3.IntegrityError:
        print("Essa placa já está cadastrada!")


def listar_clientes():
    cursor.execute("""
    SELECT * FROM banco_usuarios
    WHERE tipo = 'cliente'
    """)
    dados = cursor.fetchall()

    print("\n===== CLIENTES =====")

    if dados:
        for linha in dados:
            print(linha)
    else:
        print("Nenhum cliente cadastrado!")


def listar_veiculos():
    cursor.execute("""
    SELECT banco_veiculos.*
    FROM banco_veiculos
    INNER JOIN banco_usuarios
    ON banco_veiculos.usuario_id = banco_usuarios.id
    WHERE banco_usuarios.tipo = 'cliente'
    """)
    dados = cursor.fetchall()

    print("\n===== VEÍCULOS =====")

    if dados:
        for linha in dados:
            print(linha)
    else:
        print("Nenhum veículo cadastrado!")


def listar_ordens():
    cursor.execute("SELECT * FROM banco_ordens_servico")
    dados = cursor.fetchall()

    print("\n===== ORDENS DE SERVIÇO =====")

    if dados:
        for linha in dados:
            print(linha)
    else:
        print("Nenhuma ordem cadastrada!")


def listar_historico():
    cursor.execute("SELECT * FROM banco_historico_os")
    dados = cursor.fetchall()

    print("\n===== HISTÓRICO DE SERVIÇO =====")

    if dados:
        for linha in dados:
            print(linha)
    else:
        print("Nenhum histórico cadastrado!")


def listar_pagamentos():
    cursor.execute("SELECT * FROM banco_pagamentos")
    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")

    if dados:
        for linha in dados:
            print(linha)
    else:
        print("Nenhum pagamento cadastrado!")


def atualizar_cliente():

    id_cliente = input("Digite o ID do cliente: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'cliente'
    """, (id_cliente,))

    if cursor.fetchone() is None:
        print("Cliente não encontrado!")
        return

    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")

    try:
        cursor.execute("""
        UPDATE banco_usuarios
        SET nome=?, cpf=?, telefone=?, email=?, senha=?
        WHERE id=? AND tipo='cliente'
        """, (nome, cpf, telefone, email, senha, id_cliente))

        conexao.commit()
        print("Cliente atualizado!")

    except sqlite3.IntegrityError:
        print("Esse CPF ou email já está cadastrado!")


def atualizar_veiculo():

    id_veiculo = input("Digite o ID do veículo: ")

    cursor.execute("""
    SELECT id FROM banco_veiculos
    WHERE id = ?
    """, (id_veiculo,))

    if cursor.fetchone() is None:
        print("Veículo não encontrado!")
        return

    usuario_id = input("Novo ID do cliente: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'cliente'
    """, (usuario_id,))

    if cursor.fetchone() is None:
        print("Cliente não encontrado!")
        return

    placa = input("Nova placa: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    ano = int(input("Novo ano: "))
    cor = input("Nova cor: ")

    try:
        cursor.execute("""
        UPDATE banco_veiculos
        SET usuario_id=?, placa=?, marca=?, modelo=?, ano=?, cor=?
        WHERE id=?
        """, (usuario_id, placa, marca, modelo, ano, cor, id_veiculo))

        conexao.commit()
        print("Veículo atualizado!")

    except sqlite3.IntegrityError:
        print("Essa placa já está cadastrada!")


def atualizar_ordem():

    id_ordem = input("Digite o ID da ordem: ")

    cursor.execute("""
    SELECT id FROM banco_ordens_servico
    WHERE id = ?
    """, (id_ordem,))

    if cursor.fetchone() is None:
        print("Ordem não encontrada!")
        return

    veiculo_id = input("Novo ID do veículo: ")

    cursor.execute("""
    SELECT id FROM banco_veiculos
    WHERE id = ?
    """, (veiculo_id,))

    if cursor.fetchone() is None:
        print("Veículo não encontrado!")
        return

    funcionario_id = input("Novo ID do funcionário: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'funcionario'
    """, (funcionario_id,))

    if cursor.fetchone() is None:
        print("Funcionário não encontrado!")
        return

    data_entrada = input("Nova data de entrada: ")
    data_prevista = input("Nova data prevista: ")
    status = input("Novo status: ")
    observacoes = input("Novas observações: ")

    cursor.execute("""
    UPDATE banco_ordens_servico
    SET veiculo_id=?, funcionario_id=?, data_entrada=?,
        data_prevista=?, status=?, observacoes=?
    WHERE id=?
    """, (veiculo_id, funcionario_id, data_entrada,
          data_prevista, status, observacoes, id_ordem))

    conexao.commit()
    print("Ordem atualizada!")


def atualizar_historico():

    id_historico = input("Digite o ID do histórico: ")

    cursor.execute("""
    SELECT id FROM banco_historico_os
    WHERE id = ?
    """, (id_historico,))

    if cursor.fetchone() is None:
        print("Histórico não encontrado!")
        return

    ordem_id = input("Novo ID da ordem: ")

    cursor.execute("""
    SELECT id FROM banco_ordens_servico
    WHERE id = ?
    """, (ordem_id,))

    if cursor.fetchone() is None:
        print("Ordem não encontrada!")
        return

    status = input("Novo status: ")
    descricao = input("Nova descrição: ")
    data_hora = input("Nova data e hora: ")

    cursor.execute("""
    UPDATE banco_historico_os
    SET ordem_servico_id=?, status=?, descricao=?, data_hora=?
    WHERE id=?
    """, (ordem_id, status, descricao, data_hora, id_historico))

    conexao.commit()
    print("Histórico atualizado!")


def deletar_cliente():

    id_cliente = input("Digite o ID do cliente: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'cliente'
    """, (id_cliente,))

    if cursor.fetchone() is None:
        print("Cliente não encontrado!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_usuarios
        WHERE id = ? AND tipo = 'cliente'
        """, (id_cliente,))

        conexao.commit()
        print("Cliente deletado!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem registros vinculados a esse cliente.")


def deletar_veiculo():

    id_veiculo = input("Digite o ID do veículo: ")

    cursor.execute("""
    SELECT id FROM banco_veiculos
    WHERE id = ?
    """, (id_veiculo,))

    if cursor.fetchone() is None:
        print("Veículo não encontrado!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_veiculos
        WHERE id = ?
        """, (id_veiculo,))

        conexao.commit()
        print("Veículo deletado!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem ordens vinculadas a esse veículo.")


def deletar_ordem():

    id_ordem = input("Digite o ID da ordem de serviço: ")

    cursor.execute("""
    SELECT id FROM banco_ordens_servico
    WHERE id = ?
    """, (id_ordem,))

    if cursor.fetchone() is None:
        print("Ordem não encontrada!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_ordens_servico
        WHERE id = ?
        """, (id_ordem,))

        conexao.commit()
        print("Ordem de serviço deletada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem registros vinculados a essa ordem.")


def deletar_historico():

    id_historico = input("Digite o ID do histórico: ")

    cursor.execute("""
    SELECT id FROM banco_historico_os
    WHERE id = ?
    """, (id_historico,))

    if cursor.fetchone() is None:
        print("Histórico não encontrado!")
        return

    cursor.execute("""
    DELETE FROM banco_historico_os
    WHERE id = ?
    """, (id_historico,))

    conexao.commit()
    print("Histórico deletado!")


def menu_cadastrar():

    while True:
        print("\n===== CADASTRAR =====")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar veículo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_cliente()

            case "2":
                cadastrar_veiculo()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_listar():

    while True:
        print("\n===== LISTAR =====")
        print("1 - Listar clientes")
        print("2 - Listar veículos")
        print("3 - Listar ordens de serviço")
        print("4 - Listar histórico")
        print("5 - Listar pagamentos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_clientes()

            case "2":
                listar_veiculos()

            case "3":
                listar_ordens()

            case "4":
                listar_historico()

            case "5":
                listar_pagamentos()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_atualizar():

    while True:
        print("\n===== ATUALIZAR =====")
        print("1 - Atualizar cliente")
        print("2 - Atualizar veículo")
        print("3 - Atualizar ordem de serviço")
        print("4 - Atualizar histórico")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                atualizar_cliente()

            case "2":
                atualizar_veiculo()

            case "3":
                atualizar_ordem()

            case "4":
                atualizar_historico()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_deletar():

    while True:
        print("\n===== DELETAR =====")
        print("1 - Deletar cliente")
        print("2 - Deletar veículo")
        print("3 - Deletar ordem de serviço")
        print("4 - Deletar histórico")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                deletar_cliente()

            case "2":
                deletar_veiculo()

            case "3":
                deletar_ordem()

            case "4":
                deletar_historico()

            case "0":
                break

            case _:
                print("Opção inválida!")


def menu_principal():

    while True:
        print("\n===== MOTORUP - ÁREA DO CLIENTE =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                menu_cadastrar()

            case "2":
                menu_listar()

            case "3":
                menu_atualizar()

            case "4":
                menu_deletar()

            case "0":
                print("Sistema encerrado!")
                break

            case _:
                print("Opção inválida!")


menu_principal()

conexao.close()
