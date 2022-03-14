import os

import dotenv
import sqlalchemy



def create_db_sqlite(dotenv_path=os.path.expanduser("~/.env")):
    
    if (dotenv_path != "~/.env"):
    
        # definindo string de conexao com o banco de dados sqlite
        str_conexao = "sqlite:///{path}"
        
        # carregando o dotenv
   # str_conexao = str_conexao.format(path=os.path.join(DATA_OLTP_DIR, "olist_oltp.db"))
        str_conexao = str_conexao.format(
                path=os.path.join(dotenv.load_dotenv(dotenv_path), "olist_oltp.db"))
    
    # criando a conexao com o banco de dados sqlite
    con = sqlalchemy.create_engine(str_conexao)

    return con



