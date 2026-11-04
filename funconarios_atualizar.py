import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def atualizar_funcionario():
    id = input("Digite o ID do funcionário: ")
    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")

    cursor.execute("""
        UPDATE banco_usuarios
        SET nome=?, cpf=?, telefone=?, email=?, senha=?
        WHERE id=?
    """, (nome, cpf, telefone, email, senha, id))

    conexao.commit()
    print("Funcionário atualizado!")


def atualizar_servico():
    id = input("Digite o ID do serviço: ")
    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    tempo = int(input("Novo tempo estimado: "))

    cursor.execute("""
        UPDATE banco_servicos
        SET nome=?, descricao=?, preco=?, tempo_estimado=?
        WHERE id=?
    """, (nome, descricao, preco, tempo, id))

    conexao.commit()
    print("Serviço atualizado!")


def atualizar_peca():
    id = input("Digite o ID da peça: ")
    nome = input("Novo nome: ")
    codigo = input("Novo código: ")
    estoque = int(input("Novo estoque: "))
    preco = float(input("Novo preço: "))

    cursor.execute("""
        UPDATE banco_pecas
        SET nome=?, codigo=?, estoque=?, preco=?
        WHERE id=?
    """, (nome, codigo, estoque, preco, id))

    conexao.commit()
    print("Peça atualizada!")


def atualizar_ordem():
    id = input("Digite o ID da ordem: ")
    veiculo_id = input("Novo ID do veículo: ")
    funcionario_id = input("Novo ID do funcionário: ")
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
          data_prevista, status, observacoes, id))

    conexao.commit()
    print("Ordem atualizada!")


def atualizar_os_servico():
    id = input("Digite o ID do registro: ")
    ordem_id = input("Novo ID da ordem: ")
    servico_id = input("Novo ID do serviço: ")
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))

    cursor.execute("""
        UPDATE banco_os_servicos
        SET ordem_servico_id=?, servico_id=?, quantidade=?, preco=?
        WHERE id=?
    """, (ordem_id, servico_id, quantidade, preco, id))

    conexao.commit()
    print("Serviço da ordem atualizado!")


def atualizar_os_peca():
    id = input("Digite o ID do registro: ")
    ordem_id = input("Novo ID da ordem: ")
    peca_id = input("Novo ID da peça: ")
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))

    cursor.execute("""
        UPDATE banco_os_pecas
        SET ordem_servico_id=?, peca_id=?, quantidade=?, preco=?
        WHERE id=?
    """, (ordem_id, peca_id, quantidade, preco, id))

    conexao.commit()
    print("Peça da ordem atualizada!")


def atualizar_pagamento():
    id = input("Digite o ID do pagamento: ")
    ordem_id = input("Novo ID da ordem: ")
    valor = float(input("Novo valor: "))
    forma = input("Nova forma de pagamento: ")
    status = input("Novo status: ")
    data = input("Nova data de pagamento: ")

    cursor.execute("""
        UPDATE banco_pagamentos
        SET ordem_servico_id=?, valor=?, forma_pagamento=?,
            status=?, data_pagamento=?
        WHERE id=?
    """, (ordem_id, valor, forma, status, data, id))

    conexao.commit()
    print("Pagamento atualizado!")


while True:
    print("\n===== ATUALIZAR MOTORUP - FUNCIONÁRIOS =====")
    print("1 - Atualizar funcionário")
    print("2 - Atualizar serviço")
    print("3 - Atualizar peça")
    print("4 - Atualizar ordem de serviço")
    print("5 - Atualizar serviço da ordem")
    print("6 - Atualizar peça da ordem")
    print("7 - Atualizar pagamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        atualizar_funcionario()
    elif opcao == "2":
        atualizar_servico()
    elif opcao == "3":
        atualizar_peca()
    elif opcao == "4":
        atualizar_ordem()
    elif opcao == "5":
        atualizar_os_servico()
    elif opcao == "6":
        atualizar_os_peca()
    elif opcao == "7":
        atualizar_pagamento()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()