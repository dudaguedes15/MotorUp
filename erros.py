
import sqlite3


def tratar_erro(erro):
    if isinstance(erro, ValueError):
        print("Erro: digite um valor válido!")

    elif isinstance(erro, sqlite3.IntegrityError):
        print("Erro: esse dado já está cadastrado ou está sendo utilizado.")

    elif isinstance(erro, sqlite3.OperationalError):
        print("Erro ao executar a operação no banco de dados.")

    elif isinstance(erro, sqlite3.Error):
        print("Ocorreu um erro no banco de dados.")

    elif isinstance(erro, TypeError):
        print("Erro: tipo de dado inválido.")

    else:
        print("Ocorreu um erro:", erro)
