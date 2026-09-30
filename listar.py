import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome NOT NULL,
    cpf UNIQUE,
    telefone TEXT NOT NULL,
    email UNIQUE NOT NULL,
    senha NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    placa UNIQUE NOT NULL,
    marca NOT NULL,
    modelo NOT NULL,
    ano INTEGER,
    cor TEXT,
    FOREIGN KEY (usuario_id) REFERENCES banco_usuarios(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_servicos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    tempo_estimado INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_pecas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome NOT NULL,
    codigo UNIQUE,
    estoque INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_ordens_servico(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    veiculo_id INTEGER NOT NULL,
    funcionario_id INTEGER,
    data_entrada TEXT NOT NULL,
    data_prevista TEXT,
    data_conclusao TEXT,
    status TEXT NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (veiculo_id) REFERENCES banco_veiculos(id),
    FOREIGN KEY (funcionario_id) REFERENCES banco_usuarios(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_os_servicos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ordem_servico_id INTEGER NOT NULL,
    servico_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (ordem_servico_id) REFERENCES banco_ordens_servico(id),
    FOREIGN KEY (servico_id) REFERENCES banco_servicos(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_os_pecas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ordem_servico_id INTEGER NOT NULL,
    peca_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (ordem_servico_id) REFERENCES banco_ordens_servico(id),
    FOREIGN KEY (peca_id) REFERENCES banco_pecas(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_historico_os(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ordem_servico_id INTEGER NOT NULL,
    status NOT NULL,
    descricao TEXT,
    data_hora TEXT NOT NULL,
    FOREIGN KEY (ordem_servico_id) REFERENCES banco_ordens_servico(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banco_pagamentos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ordem_servico_id INTEGER NOT NULL,
    valor REAL NOT NULL,
    forma_pagamento TEXT NOT NULL,
    status TEXT NOT NULL,
    data_pagamento TEXT,
    FOREIGN KEY (ordem_servico_id) REFERENCES banco_ordens_servico(id)
)
''')

conexao.commit()


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
    estoque = input("Estoque: ")
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

    print("Serviço adicionado à ordem!")


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

    print("Peça adicionada à ordem!")


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


def listar_usuarios():

    cursor.execute("SELECT * FROM banco_usuarios")

    dados = cursor.fetchall()

    print("\n===== USUÁRIOS =====")

    for usuario in dados:
        print(usuario)


def listar_veiculos():

    cursor.execute("SELECT * FROM banco_veiculos")

    dados = cursor.fetchall()

    print("\n===== VEÍCULOS =====")

    for veiculo in dados:
        print(veiculo)


def listar_servicos():

    cursor.execute("SELECT * FROM banco_servicos")

    dados = cursor.fetchall()

    print("\n===== SERVIÇOS =====")

    for servico in dados:
        print(servico)


def listar_pecas():

    cursor.execute("SELECT * FROM banco_pecas")

    dados = cursor.fetchall()

    print("\n===== PEÇAS =====")

    for peca in dados:
        print(peca)


def listar_ordens():

    cursor.execute("SELECT * FROM banco_ordens_servico")

    dados = cursor.fetchall()

    print("\n===== ORDENS DE SERVIÇO =====")

    for ordem in dados:
        print(ordem)


def listar_os_servicos():

    cursor.execute("SELECT * FROM banco_os_servicos")

    dados = cursor.fetchall()

    print("\n===== SERVIÇOS DAS ORDENS =====")

    for servico in dados:
        print(servico)


def listar_os_pecas():

    cursor.execute("SELECT * FROM banco_os_pecas")

    dados = cursor.fetchall()

    print("\n===== PEÇAS DAS ORDENS =====")

    for peca in dados:
        print(peca)


def listar_historico():

    cursor.execute("SELECT * FROM banco_historico_os")

    dados = cursor.fetchall()

    print("\n===== HISTÓRICO =====")

    for historico in dados:
        print(historico)


def listar_pagamentos():

    cursor.execute("SELECT * FROM banco_pagamentos")

    dados = cursor.fetchall()

    print("\n===== PAGAMENTOS =====")

    for pagamento in dados:
        print(pagamento)


while True:

    print("\n===== MOTORUP =====")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar veículo")
    print("3 - Cadastrar serviço")
    print("4 - Cadastrar peça")
    print("5 - Cadastrar ordem de serviço")
    print("6 - Adicionar serviço à ordem")
    print("7 - Adicionar peça à ordem")
    print("8 - Cadastrar histórico")
    print("9 - Cadastrar pagamento")
    print("10 - Listar usuários")
    print("11 - Listar veículos")
    print("12 - Listar serviços")
    print("13 - Listar peças")
    print("14 - Listar ordens de serviço")
    print("15 - Listar serviços das ordens")
    print("16 - Listar peças das ordens")
    print("17 - Listar histórico")
    print("18 - Listar pagamentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        cadastrar_veiculo()

    elif opcao == "3":
        cadastrar_servico()

    elif opcao == "4":
        cadastrar_peca()

    elif opcao == "5":
        cadastrar_ordem()

    elif opcao == "6":
        cadastrar_os_servico()

    elif opcao == "7":
        cadastrar_os_peca()

    elif opcao == "8":
        cadastrar_historico()

    elif opcao == "9":
        cadastrar_pagamento()

    elif opcao == "10":
        listar_usuarios()

    elif opcao == "11":
        listar_veiculos()

    elif opcao == "12":
        listar_servicos()

    elif opcao == "13":
        listar_pecas()

    elif opcao == "14":
        listar_ordens()

    elif opcao == "15":
        listar_os_servicos()

    elif opcao == "16":
        listar_os_pecas()

    elif opcao == "17":
        listar_historico()

    elif opcao == "18":
        listar_pagamentos()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")


conexao.close()