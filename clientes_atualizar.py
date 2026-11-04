import sqlite3

conexao = sqlite3.connect("motorup.db")
cursor = conexao.cursor()

def atualizar_cliente():
    id = input("Digite o ID do cliente: ")
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
    print("Cliente atualizado!")


def atualizar_veiculo():
    id = input("Digite o ID do veículo: ")
    usuario_id = input("Novo ID do cliente: ")
    placa = input("Nova placa: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    ano = int(input("Novo ano: "))
    cor = input("Nova cor: ")

    cursor.execute("""
        UPDATE banco_veiculos
        SET usuario_id=?, placa=?, marca=?, modelo=?, ano=?, cor=?
        WHERE id=?
    """, (usuario_id, placa, marca, modelo, ano, cor, id))

    conexao.commit()
    print("Veículo atualizado!")


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


def atualizar_historico():
    id = input("Digite o ID do histórico: ")
    ordem_id = input("Novo ID da ordem: ")
    status = input("Novo status: ")
    descricao = input("Nova descrição: ")
    data_hora = input("Nova data e hora: ")

    cursor.execute("""
        UPDATE banco_historico_os
        SET ordem_servico_id=?, status=?, descricao=?, data_hora=?
        WHERE id=?
    """, (ordem_id, status, descricao, data_hora, id))

    conexao.commit()
    print("Histórico atualizado!")


while True:
    print("\n===== ATUALIZAR MOTORUP - CLIENTES =====")
    print("1 - Atualizar cliente")
    print("2 - Atualizar veículo")
    print("3 - Atualizar ordem de serviço")
    print("4 - Atualizar histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        atualizar_cliente()
    elif opcao == "2":
        atualizar_veiculo()
    elif opcao == "3":
        atualizar_ordem()
    elif opcao == "4":
        atualizar_historico()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()