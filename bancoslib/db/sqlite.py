import os

import sqlalchemy


def create_db_sqlite(path, nome_banco):

    # definindo string de conexao com o banco de dados sqlite
    str_conexao = "sqlite:///{path}"

    # carregando o dotenv
    str_conexao = str_conexao.format(path=os.path.join(path, nome_banco + ".db"))

    # criando a conexao com o banco de dados sqlite
    con = sqlalchemy.create_engine(str_conexao)

    return con


def connect_db_sqlite(db_path, nome_banco=[]):
    """Função para se conectar com o banco de dados local sqlite

    Returns:
        con: retorna uma conexao com o banco de dados sqlite
    """

    # definindo string de conexao com o banco de dados sqlite
    str_conexao = "sqlite:///{db_path}"

    # definindo string de conexao com o banco de dados sqlite
    str_conexao = "sqlite:///{path}".format(path=os.path.join(db_path, nome_banco))

    # criando a conexao com o banco de dados sqlite
    con = sqlalchemy.create_engine(str_conexao)

    return con
