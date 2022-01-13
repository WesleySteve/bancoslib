





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