





def import_query(path, **kwargs):
    """Função para importar uma query, recebendo varios argumentos

    Args:
        path (os): caminho de onde está armazenada a query sql
        
    Returns:
        query: retorna o resultado da query passada
    """
    with open(path, "r", **kwargs) as file_query:
        query = file_query.read()
    return query



def execute_many_sql(sql, con):
    """Função que recebe um sql uma conexao e verbose(opicional) e executa

    Args:
        sql (comando): parametro que recebe a query
        con (parametro): string de conexao com o banco de dados sqlite
    """

    for i in sql.split(";")[:-1]:
        con.execute(i)
        
