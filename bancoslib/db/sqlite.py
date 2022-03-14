import os

import sqlalchemy



def create_db_sqlite(path):
    
    
    
    # definindo string de conexao com o banco de dados sqlite
    str_conexao = "sqlite:///{path}"
        
    # carregando o dotenv
    str_conexao = str_conexao.format(path=os.path.join(path, "olist_oltp.db"))
    
    
    # criando a conexao com o banco de dados sqlite
    con = sqlalchemy.create_engine(str_conexao)

    return con



