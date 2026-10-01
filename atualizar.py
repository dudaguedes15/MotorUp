import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


def atualizar_usuario():

    id = input("ID do usuário: ")

    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")

    cursor.execute(f'''
    UPDATE banco_usuarios
    SET nome = "{nome}",
        cpf = "{cpf}",
        telefone = "{telefone}",
        email = "{email}",
        senha = "{senha}"
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Usuário atualizado!")


def atualizar_veiculo():

    id = input("ID do veículo: ")

    usuario_id = input("Novo ID do usuário: ")
    placa = input("Nova placa: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    ano = input("Novo ano: ")
    cor = input("Nova cor: ")

    cursor.execute(f'''
    UPDATE banco_veiculos
    SET usuario_id = {usuario_id},
        placa = "{placa}",
        marca = "{marca}",
        modelo = "{modelo}",
        ano = {ano},
        cor = "{cor}"
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Veículo atualizado!")


def atualizar_servico():

    id = input("ID do serviço: ")

    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = input("Novo preço: ")
    tempo_estimado = input("Novo tempo estimado em minutos: ")

    cursor.execute(f'''
    UPDATE banco_servicos
    SET nome = "{nome}",
        descricao = "{descricao}",
        preco = {preco},
        tempo_estimado = {tempo_estimado}
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Serviço atualizado!")


def atualizar_peca():

    id = input("ID da peça: ")

    nome = input("Novo nome: ")
    codigo = input("Novo código: ")
    estoque = input("Novo estoque: ")
    preco = input("Novo preço: ")

    cursor.execute(f'''
    UPDATE banco_pecas
    SET nome = "{nome}",
        codigo = "{codigo}",
        estoque = {estoque},
        preco = {preco}
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Peça atualizada!")


def atualizar_ordem():

    id = input("ID da ordem de serviço: ")

    veiculo_id = input("Novo ID do veículo: ")
    funcionario_id = input("Novo ID do funcionário: ")
    data_entrada = input("Nova data de entrada: ")
    data_prevista = input("Nova data prevista: ")
    data_conclusao = input("Nova data de conclusão: ")
    status = input("Novo status: ")
    observacoes = input("Novas observações: ")

    cursor.execute(f'''
    UPDATE banco_ordens_servico
    SET veiculo_id = {veiculo_id},
        funcionario_id = {funcionario_id},
        data_entrada = "{data_entrada}",
        data_prevista = "{data_prevista}",
        data_conclusao = "{data_conclusao}",
        status = "{status}",
        observacoes = "{observacoes}"
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Ordem de serviço atualizada!")


def atualizar_os_servico():

    id = input("ID do serviço da ordem: ")

    ordem_servico_id = input("Novo ID da ordem: ")
    servico_id = input("Novo ID do serviço: ")
    quantidade = input("Nova quantidade: ")
    preco = input("Novo preço: ")

    cursor.execute(f'''
    UPDATE banco_os_servicos
    SET ordem_servico_id = {ordem_servico_id},
        servico_id = {servico_id},
        quantidade = {quantidade},
        preco = {preco}
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Serviço da ordem atualizado!")


def atualizar_os_peca():

    id = input("ID da peça da ordem: ")

    ordem_servico_id = input("Novo ID da ordem: ")
    peca_id = input("Novo ID da peça: ")
    quantidade = input("Nova quantidade: ")
    preco = input("Novo preço: ")

    cursor.execute(f'''
    UPDATE banco_os_pecas
    SET ordem_servico_id = {ordem_servico_id},
        peca_id = {peca_id},
        quantidade = {quantidade},
        preco = {preco}
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Peça da ordem atualizada!")


def atualizar_historico():

    id = input("ID do histórico: ")

    ordem_servico_id = input("Novo ID da ordem: ")
    status = input("Novo status: ")
    descricao = input("Nova descrição: ")
    data_hora = input("Nova data e hora: ")

    cursor.execute(f'''
    UPDATE banco_historico_os
    SET ordem_servico_id = {ordem_servico_id},
        status = "{status}",
        descricao = "{descricao}",
        data_hora = "{data_hora}"
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Histórico atualizado!")


def atualizar_pagamento():

    id = input("ID do pagamento: ")

    ordem_servico_id = input("Novo ID da ordem: ")
    valor = input("Novo valor: ")
    forma_pagamento = input("Nova forma de pagamento: ")
    status = input("Novo status: ")
    data_pagamento = input("Nova data de pagamento: ")

    cursor.execute(f'''
    UPDATE banco_pagamentos
    SET ordem_servico_id = {ordem_servico_id},
        valor = {valor},
        forma_pagamento = "{forma_pagamento}",
        status = "{status}",
        data_pagamento = "{data_pagamento}"
    WHERE id = {id}
    ''')

    conexao.commit()

    print("Pagamento atualizado!")


while True:

    print("\n===== ATUALIZAR MOTORUP =====")
    print("1 - Atualizar usuário")
    print("2 - Atualizar veículo")
    print("3 - Atualizar serviço")
    print("4 - Atualizar peça")
    print("5 - Atualizar ordem de serviço")
    print("6 - Atualizar serviço da ordem")
    print("7 - Atualizar peça da ordem")
    print("8 - Atualizar histórico")
    print("9 - Atualizar pagamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        atualizar_usuario()

    elif opcao == "2":
        atualizar_veiculo()

    elif opcao == "3":
        atualizar_servico()

    elif opcao == "4":
        atualizar_peca()

    elif opcao == "5":
        atualizar_ordem()

    elif opcao == "6":
        atualizar_os_servico()

    elif opcao == "7":
        atualizar_os_peca()

    elif opcao == "8":
        atualizar_historico()

    elif opcao == "9":
        atualizar_pagamento()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")


conexao.close()