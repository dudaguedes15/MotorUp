
import sqlite3

conexao = sqlite3.connect("motorup.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()


def cadastrar_usuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    senha = input("Senha: ")

    try:
        cursor.execute("""
        INSERT INTO banco_usuarios
        (nome, cpf, telefone, email, senha, tipo)
        VALUES (?, ?, ?, ?, ?, 'funcionario')
        """, (nome, cpf, telefone, email, senha))

        conexao.commit()
        print("Funcionário cadastrado!")

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


def cadastrar_peca():

    nome = input("Nome da peça: ")
    codigo = input("Código: ")
    estoque = int(input("Estoque: "))
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


def cadastrar_ordem():
    veiculo_id = input("ID do veículo: ")

    cursor.execute("""
    SELECT id FROM banco_veiculos
    WHERE id = ?
    """, (veiculo_id,))

    if cursor.fetchone() is None:
        print("Veículo não encontrado!")
        return

    funcionario_id = input("ID do funcionário: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'funcionario'
    """, (funcionario_id,))

    if cursor.fetchone() is None:
        print("Funcionário não encontrado!")
        return

    data_entrada = input("Data de entrada: ")
    data_prevista = input("Data prevista: ")
    status = input("Status: ")
    observacoes = input("Observações: ")

    cursor.execute("""
    INSERT INTO banco_ordens_servico
    (veiculo_id, funcionario_id, data_entrada,
    data_prevista, status, observacoes)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (veiculo_id, funcionario_id, data_entrada,
          data_prevista, status, observacoes))

    conexao.commit()

    print("Ordem de serviço cadastrada!")


def listar_usuarios():
    cursor.execute("""
    SELECT * FROM banco_usuarios
    WHERE tipo = 'cliente'
    """)
    clientes = cursor.fetchall()

    print("\n===== CLIENTES =====")
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print("Nenhum cliente cadastrado!")

    cursor.execute("""
    SELECT * FROM banco_usuarios
    WHERE tipo = 'funcionario'
    """)
    funcionarios = cursor.fetchall()

    print("\n===== FUNCIONÁRIOS =====")
    if funcionarios:
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Nenhum funcionário cadastrado!")


def listar_veiculos():
    cursor.execute("SELECT * FROM banco_veiculos")
    veiculos = cursor.fetchall()

    print("\n===== VEÍCULOS =====")
    if veiculos:
        for veiculo in veiculos:
            print(veiculo)
    else:
        print("Nenhum veículo cadastrado!")


def listar_servicos():
    cursor.execute("SELECT * FROM banco_servicos")
    servicos = cursor.fetchall()

    print("\n===== SERVIÇOS =====")
    if servicos:
        for servico in servicos:
            print(servico)
    else:
        print("Nenhum serviço cadastrado!")


def listar_pecas():
    cursor.execute("SELECT * FROM banco_pecas")
    pecas = cursor.fetchall()

    print("\n===== PEÇAS =====")
    if pecas:
        for peca in pecas:
            print(peca)
    else:
        print("Nenhuma peça cadastrada!")


def listar_ordens():
    cursor.execute("SELECT * FROM banco_ordens_servico")
    ordens = cursor.fetchall()

    print("\n===== ORDENS DE SERVIÇO =====")
    if ordens:
        for ordem in ordens:
            print(ordem)
    else:
        print("Nenhuma ordem cadastrada!")


def atualizar_usuario():
    id_usuario = input("ID do funcionário: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'funcionario'
    """, (id_usuario,))

    if cursor.fetchone() is None:
        print("Funcionário não encontrado!")
        return

    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")

    try:
        cursor.execute("""
        UPDATE banco_usuarios
        SET nome = ?, cpf = ?, telefone = ?, email = ?, senha = ?
        WHERE id = ? AND tipo = 'funcionario'
        """, (nome, cpf, telefone, email, senha, id_usuario))

        conexao.commit()
        print("Funcionário atualizado!")

    except sqlite3.IntegrityError:
        print("Esse CPF ou email já está cadastrado!")


def atualizar_veiculo():
    id_veiculo = input("ID do veículo: ")

    cursor.execute("""
    SELECT id FROM banco_veiculos
    WHERE id = ?
    """, (id_veiculo,))

    if cursor.fetchone() is None:
        print("Veículo não encontrado!")
        return

    placa = input("Nova placa: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    ano = int(input("Novo ano: "))
    cor = input("Nova cor: ")

    try:
        cursor.execute("""
        UPDATE banco_veiculos
        SET placa = ?, marca = ?, modelo = ?, ano = ?, cor = ?
        WHERE id = ?
        """, (placa, marca, modelo, ano, cor, id_veiculo))

        conexao.commit()
        print("Veículo atualizado!")

    except sqlite3.IntegrityError:
        print("Essa placa já está cadastrada!")


def atualizar_servico():
    id_servico = input("ID do serviço: ")

    cursor.execute("""
    SELECT id FROM banco_servicos
    WHERE id = ?
    """, (id_servico,))

    if cursor.fetchone() is None:
        print("Serviço não encontrado!")
        return

    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    tempo = int(input("Novo tempo estimado: "))

    cursor.execute("""
    UPDATE banco_servicos
    SET nome = ?, descricao = ?, preco = ?, tempo_estimado = ?
    WHERE id = ?
    """, (nome, descricao, preco, tempo, id_servico))

    conexao.commit()
    print("Serviço atualizado!")


def atualizar_peca():
    id_peca = input("ID da peça: ")

    cursor.execute("""
    SELECT id FROM banco_pecas
    WHERE id = ?
    """, (id_peca,))

    if cursor.fetchone() is None:
        print("Peça não encontrada!")
        return

    nome = input("Novo nome: ")
    codigo = input("Novo código: ")
    estoque = int(input("Novo estoque: "))
    preco = float(input("Novo preço: "))

    try:
        cursor.execute("""
        UPDATE banco_pecas
        SET nome = ?, codigo = ?, estoque = ?, preco = ?
        WHERE id = ?
        """, (nome, codigo, estoque, preco, id_peca))

        conexao.commit()
        print("Peça atualizada!")

    except sqlite3.IntegrityError:
        print("Esse código já está cadastrado!")


def atualizar_ordem():
    id_ordem = input("ID da ordem: ")

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
    SET veiculo_id = ?, funcionario_id = ?, data_entrada = ?,
    data_prevista = ?, status = ?, observacoes = ?
    WHERE id = ?
    """, (veiculo_id, funcionario_id, data_entrada,
          data_prevista, status, observacoes, id_ordem))

    conexao.commit()
    print("Ordem atualizada!")


def deletar_usuario():
    id_usuario = input("ID do funcionário: ")

    cursor.execute("""
    SELECT id FROM banco_usuarios
    WHERE id = ? AND tipo = 'funcionario'
    """, (id_usuario,))

    if cursor.fetchone() is None:
        print("Funcionário não encontrado!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_usuarios
        WHERE id = ? AND tipo = 'funcionario'
        """, (id_usuario,))

        conexao.commit()
        print("Funcionário deletado!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem ordens vinculadas a esse funcionário.")


def deletar_veiculo():
    id_veiculo = input("ID do veículo: ")

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


def deletar_servico():
    id_servico = input("ID do serviço: ")

    cursor.execute("""
    SELECT id FROM banco_servicos
    WHERE id = ?
    """, (id_servico,))

    if cursor.fetchone() is None:
        print("Serviço não encontrado!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_servicos
        WHERE id = ?
        """, (id_servico,))

        conexao.commit()
        print("Serviço deletado!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem ordens vinculadas a esse serviço.")


def deletar_peca():
    id_peca = input("ID da peça: ")

    cursor.execute("""
    SELECT id FROM banco_pecas
    WHERE id = ?
    """, (id_peca,))

    if cursor.fetchone() is None:
        print("Peça não encontrada!")
        return

    try:
        cursor.execute("""
        DELETE FROM banco_pecas
        WHERE id = ?
        """, (id_peca,))

        conexao.commit()
        print("Peça deletada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem ordens vinculadas a essa peça.")


def deletar_ordem():
    id_ordem = input("ID da ordem: ")

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
        print("Ordem deletada!")

    except sqlite3.IntegrityError:
        print("Não foi possível deletar! Existem registros vinculados a essa ordem.")


def menu_principal():
    while True:
        print("\n===== MOTORUP - ÁREA DO FUNCIONÁRIO =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":
                print("\n===== CADASTRAR =====")
                print("1 - Funcionário")
                print("2 - Veículo")
                print("3 - Serviço")
                print("4 - Peça")
                print("5 - Ordem de serviço")

                escolha = input("Escolha: ")

                match escolha:
                    case "1":
                        cadastrar_usuario()
                    case "2":
                        cadastrar_veiculo()
                    case "3":
                        cadastrar_servico()
                    case "4":
                        cadastrar_peca()
                    case "5":
                        cadastrar_ordem()
                    case _:
                        print("Opção inválida!")

            case "2":
                print("\n===== LISTAR =====")
                print("1 - Clientes e funcionários")
                print("2 - Veículos")
                print("3 - Serviços")
                print("4 - Peças")
                print("5 - Ordens de serviço")

                escolha = input("Escolha: ")

                match escolha:
                    case "1":
                        listar_usuarios()
                    case "2":
                        listar_veiculos()
                    case "3":
                        listar_servicos()
                    case "4":
                        listar_pecas()
                    case "5":
                        listar_ordens()
                    case _:
                        print("Opção inválida!")

            case "3":
                print("\n===== ATUALIZAR =====")
                print("1 - Funcionário")
                print("2 - Veículo")
                print("3 - Serviço")
                print("4 - Peça")
                print("5 - Ordem de serviço")

                escolha = input("Escolha: ")

                match escolha:
                    case "1":
                        atualizar_usuario()
                    case "2":
                        atualizar_veiculo()
                    case "3":
                        atualizar_servico()
                    case "4":
                        atualizar_peca()
                    case "5":
                        atualizar_ordem()
                    case _:
                        print("Opção inválida!")

            case "4":
                print("\n===== DELETAR =====")
                print("1 - Funcionário")
                print("2 - Veículo")
                print("3 - Serviço")
                print("4 - Peça")
                print("5 - Ordem de serviço")

                escolha = input("Escolha: ")

                match escolha:
                    case "1":
                        deletar_usuario()
                    case "2":
                        deletar_veiculo()
                    case "3":
                        deletar_servico()
                    case "4":
                        deletar_peca()
                    case "5":
                        deletar_ordem()
                    case _:
                        print("Opção inválida!")

            case "0":
                print("Sistema encerrado!")
                break

            case _:
                print("Opção inválida!")


menu_principal()
conexao.close()
