import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()


def cadastrar_usuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    senha = input("Senha: ")

    cursor.execute(f'''
    INSERT INTO banco_usuarios
    (nome, cpf, telefone, email, senha)
    VALUES
    ("{nome}", "{cpf}", "{telefone}", "{email}", "{senha}")
    ''')

    conexao.commit()
    print("Usuário cadastrado!")


def cadastrar_veiculo():
    usuario_id = input("ID do usuário: ")
    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cor = input("Cor: ")

    cursor.execute(f'''
    INSERT INTO banco_veiculos
    (usuario_id, placa, marca, modelo, ano, cor)
    VALUES
    ({usuario_id}, "{placa}", "{marca}", "{modelo}", {ano}, "{cor}")
    ''')

    conexao.commit()
    print("Veículo cadastrado!")


def cadastrar_servico():
    nome = input("Nome do serviço: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")
    tempo_estimado = input("Tempo estimado em minutos: ")

    cursor.execute(f'''
    INSERT INTO banco_servicos
    (nome, descricao, preco, tempo_estimado)
    VALUES
    ("{nome}", "{descricao}", {preco}, {tempo_estimado})
    ''')

    conexao.commit()
    print("Serviço cadastrado!")


def cadastrar_peca():
    nome = input("Nome da peça: ")
    codigo = input("Código: ")
    estoque = input("Quantidade em estoque: ")
    preco = input("Preço: ")

    cursor.execute(f'''
    INSERT INTO banco_pecas
    (nome, codigo, estoque, preco)
    VALUES
    ("{nome}", "{codigo}", {estoque}, {preco})
    ''')

    conexao.commit()
    print("Peça cadastrada!")


def cadastrar_ordem():
    veiculo_id = input("ID do veículo: ")
    funcionario_id = input("ID do funcionário: ")
    data_entrada = input("Data de entrada: ")
    data_prevista = input("Data prevista: ")
    status = input("Status: ")
    observacoes = input("Observações: ")

    cursor.execute(f'''
    INSERT INTO banco_ordens_servico
    (veiculo_id, funcionario_id, data_entrada, data_prevista, status, observacoes)
    VALUES
    ({veiculo_id}, {funcionario_id}, "{data_entrada}", "{data_prevista}", "{status}", "{observacoes}")
    ''')

    conexao.commit()
    print("Ordem de serviço cadastrada!")


def cadastrar_os_servico():
    ordem_servico_id = input("ID da ordem de serviço: ")
    servico_id = input("ID do serviço: ")
    quantidade = input("Quantidade: ")
    preco = input("Preço: ")

    cursor.execute(f'''
    INSERT INTO banco_os_servicos
    (ordem_servico_id, servico_id, quantidade, preco)
    VALUES
    ({ordem_servico_id}, {servico_id}, {quantidade}, {preco})
    ''')

    conexao.commit()
    print("Serviço da ordem cadastrado!")


def cadastrar_os_peca():
    ordem_servico_id = input("ID da ordem de serviço: ")
    peca_id = input("ID da peça: ")
    quantidade = input("Quantidade: ")
    preco = input("Preço: ")

    cursor.execute(f'''
    INSERT INTO banco_os_pecas
    (ordem_servico_id, peca_id, quantidade, preco)
    VALUES
    ({ordem_servico_id}, {peca_id}, {quantidade}, {preco})
    ''')

    conexao.commit()
    print("Peça da ordem cadastrada!")


def cadastrar_historico():
    ordem_servico_id = input("ID da ordem de serviço: ")
    status = input("Status: ")
    descricao = input("Descrição: ")
    data_hora = input("Data e hora: ")

    cursor.execute(f'''
    INSERT INTO banco_historico_os
    (ordem_servico_id, status, descricao, data_hora)
    VALUES
    ({ordem_servico_id}, "{status}", "{descricao}", "{data_hora}")
    ''')

    conexao.commit()
    print("Histórico cadastrado!")


def cadastrar_pagamento():
    ordem_servico_id = input("ID da ordem de serviço: ")
    valor = input("Valor: ")
    forma_pagamento = input("Forma de pagamento: ")
    status = input("Status: ")
    data_pagamento = input("Data do pagamento: ")

    cursor.execute(f'''
    INSERT INTO banco_pagamentos
    (ordem_servico_id, valor, forma_pagamento, status, data_pagamento)
    VALUES
    ({ordem_servico_id}, {valor}, "{forma_pagamento}", "{status}", "{data_pagamento}")
    ''')

    conexao.commit()
    print("Pagamento cadastrado!")


cadastrar_usuario()
cadastrar_veiculo()
cadastrar_servico()
cadastrar_peca()
cadastrar_ordem()
cadastrar_os_servico()
cadastrar_os_peca()
cadastrar_historico()
cadastrar_pagamento()


conexao.close()