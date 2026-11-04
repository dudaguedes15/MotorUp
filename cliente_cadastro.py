
import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()


def cadastrar_cliente():

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
    print("Cliente cadastrado!")


def cadastrar_veiculo():

    usuario_id = input("ID do cliente: ")
    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cor = input("Cor: ")

    cursor.execute('''
    INSERT INTO banco_veiculos
    (usuario_id, placa, marca, modelo, ano, cor)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (usuario_id, placa, marca, modelo, ano, cor))

    conexao.commit()
    print("Veículo cadastrado!")


def consultar_servicos():

    cursor.execute("SELECT * FROM banco_servicos")

    dados = cursor.fetchall()

    print("\n===== SERVIÇOS DISPONÍVEIS =====")

    for servico in dados:
        print("ID:", servico[0])
        print("Nome:", servico[1])
        print("Descrição:", servico[2])
        print("Preço:", servico[3])
        print("Tempo:", servico[4])
        print("-------------------")


def consultar_pecas():

    cursor.execute("SELECT * FROM banco_pecas")

    dados = cursor.fetchall()

    print("\n===== PEÇAS DISPONÍVEIS =====")

    for peca in dados:
        print("ID:", peca[0])
        print("Nome:", peca[1])
        print("Código:", peca[2])
        print("Estoque:", peca[3])
        print("Preço:", peca[4])
        print("-------------------")


def consultar_ordens():

    usuario_id = input("ID do cliente: ")

    cursor.execute('''
    SELECT banco_ordens_servico.*
    FROM banco_ordens_servico
    INNER JOIN banco_veiculos
    ON banco_ordens_servico.veiculo_id = banco_veiculos.id
    WHERE banco_veiculos.usuario_id = ?
    ''', (usuario_id,))

    dados = cursor.fetchall()

    for ordem in dados:
        print(ordem)


def consultar_historico():

    ordem_id = input("ID da ordem de serviço: ")

    cursor.execute('''
    SELECT * FROM banco_historico_os
    WHERE ordem_servico_id = ?
    ''', (ordem_id,))

    dados = cursor.fetchall()

    for historico in dados:
        print(historico)


def consultar_pagamentos():

    ordem_id = input("ID da ordem de serviço: ")

    cursor.execute('''
    SELECT * FROM banco_pagamentos
    WHERE ordem_servico_id = ?
    ''', (ordem_id,))

    dados = cursor.fetchall()

    for pagamento in dados:
        print(pagamento)


while True:

    print("\n===== MOTORUP - ÁREA DO CLIENTE =====")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar veículo")
    print("3 - Consultar serviços disponíveis")
    print("4 - Consultar peças")
    print("5 - Consultar ordens de serviço")
    print("6 - Consultar histórico")
    print("7 - Consultar pagamentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        cadastrar_veiculo()

    elif opcao == "3":
        consultar_servicos()

    elif opcao == "4":
        consultar_pecas()

    elif opcao == "5":
        consultar_ordens()

    elif opcao == "6":
        consultar_historico()

    elif opcao == "7":
        consultar_pagamentos()

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")


conexao.close()
