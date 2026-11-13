
import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


def usuarios():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE,
        telefone TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL
    )
    ''')


def atualizar_banco():
    cursor.execute("PRAGMA table_info(banco_usuarios)")
    colunas = cursor.fetchall()

    tipo_existe = False

    for coluna in colunas:
        if coluna[1] == "tipo":
            tipo_existe = True

    if tipo_existe == False:
        cursor.execute("""
        ALTER TABLE banco_usuarios
        ADD COLUMN tipo TEXT NOT NULL DEFAULT 'cliente'
        """)

    cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type = 'table' AND name = 'banco_funcionarios'
    """)

    tabela_existe = cursor.fetchone()

    if tabela_existe is not None:
        cursor.execute("""
        UPDATE banco_usuarios
        SET tipo = 'funcionario'
        WHERE id IN (
            SELECT usuario_id FROM banco_funcionarios
        )
        """)

    conexao.commit()


def veiculos():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_veiculos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        placa TEXT UNIQUE NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER,
        cor TEXT,
        FOREIGN KEY (usuario_id) REFERENCES banco_usuarios(id)
    )
    ''')


def servicos():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_servicos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        tempo_estimado INTEGER
    )
    ''')


def pecas():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_pecas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo TEXT UNIQUE,
        estoque INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    ''')


def ordens_servico():
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


def os_servicos():
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


def os_pecas():
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


def historico_os():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_historico_os(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ordem_servico_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        descricao TEXT,
        data_hora TEXT NOT NULL,
        FOREIGN KEY (ordem_servico_id) REFERENCES banco_ordens_servico(id)
    )
    ''')


def pagamentos():
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


usuarios()
atualizar_banco()

veiculos()
servicos()
pecas()
ordens_servico()
os_servicos()
os_pecas()
historico_os()
pagamentos()

conexao.commit()
conexao.close()

print("Banco de dados atualizado!")
