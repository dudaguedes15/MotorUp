
import sqlite3

conexao = sqlite3.connect("motorup.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()


def cadastrar_funcionario():

    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    senha = input("Senha: ")

    cursor.execute('''
    INSERT INTO banco_usuarios
    (nome, cpf, telefone, email, senha)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, cpf, telefone, email, senha))

    conexao.commit()

    print("Funcionário cadastrado!")


def cadastrar_servico():

    nome = input("Nome do serviço: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")
    tempo_estimado = input("Tempo estimado em minutos: ")

    cursor.execute('''
    INSERT INTO banco_servicos
    (nome, descricao, preco, tempo_estimado)
    VALUES (?, ?, ?, ?)
    ''', (nome, descricao, preco, tempo_estimado))

    conexao.commit()

    print("Serviço cadastrado!")


def cadastrar_peca():

    nome = input("Nome da peça: ")
    codigo = input("Código: ")
    estoque = input("Estoque: ")
    preco = input("Preço: ")

    cursor.execute('''
    INSERT INTO banco_pecas
    (nome, codigo, estoque, preco)
    VALUES (?, ?, ?, ?)
    ''', (nome, codigo, estoque, preco))

    conexao.commit()

    print("Peça cadastrada!")


def cadastrar_ordem():

    veiculo_id = input("ID do veículo: ")
    funcionario_id = input("ID do funcionário: ")
    data_entrada = input("Data de entrada: ")
    data_prevista = input("Data prevista: ")
    status = input("Status: ")
    observacoes = input("Observações: ")

    cursor.execute('''
    INSERT INTO banco_ordens_servico
    (veiculo_id, funcionario_id, data_entrada, data_prevista, status, observacoes)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (veiculo_id, funcionario_id, data_entrada, data_prevista, status, observacoes))

    conexao.commit()

    print("Ordem de serviço cadastrada!")


def cadastrar_os_servico():

    ordem_servico_id = input("ID da ordem de serviço: ")
    servico_id = input("ID do serviço: ")
    quantidade = input("Quantidade: ")
    preco = input("Preço: ")

    cursor.execute('''
    INSERT INTO banco_os_servicos
    (ordem_servico_id, servico_id, quantidade, preco)
    VALUES (?, ?, ?, ?)
    ''', (ordem_servico_id, servico_id, quantidade, preco))

    conexao.commit()

    print("Serviço adicionado à ordem!")


def cadastrar_os_peca():

    ordem_servico_id = input("ID da ordem de serviço: ")
    peca_id = input("ID da peça: ")
    quantidade = input("Quantidade: ")
    preco = input("Preço: ")

    cursor.execute('''
    INSERT INTO banco_os_pecas
    (ordem_servico_id, peca_id, quantidade, preco)
    VALUES (?, ?, ?, ?)
    ''', (ordem_servico_id, peca_id, quantidade, preco))

    conexao.commit()

    print("Peça adicionada à ordem!")


def cadastrar_pagamento():

    ordem_servico_id = input("ID da ordem de serviço: ")
    valor = input("Valor: ")
    forma_pagamento = input("Forma de pagamento: ")
    status = input("Status: ")
    data_pagamento = input("Data do pagamento: ")

    cursor.execute('''
    INSERT INTO banco_pagamentos
    (ordem_servico_id, valor, forma_pagamento, status, data_pagamento)
    VALUES (?, ?, ?, ?, ?)
    ''', (ordem_servico_id, valor, forma_pagamento, status, data_pagamento))

    conexao.commit()

    print("Pagamento cadastrado!")


while True:

    print("\n===== MOTORUP - ÁREA DOS FUNCIONÁRIOS =====")
    print("1 - Cadastrar funcionário")
    print("2 - Cadastrar serviços")
    print("3 - Cadastrar peças")
    print("4 - Cadastrar ordem de serviço")
    print("5 - Adicionar serviço à ordem")
    print("6 - Adicionar peça à ordem")
    print("7 - Cadastrar pagamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario()

    elif opcao == "2":
        cadastrar_servico()

    elif opcao == "3":
        cadastrar_peca()

    elif opcao == "4":
        cadastrar_ordem()

    elif opcao == "5":
        cadastrar_os_servico()

    elif opcao == "6":
        cadastrar_os_peca()

    elif opcao == "7":
        cadastrar_pagamento()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")


conexao.close()
