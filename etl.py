import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:

    """
    Função que lê um arquivo csv e retorna uma lista de dicionarios

    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# vendas_itens: list[dict]

# vendas_itens = ler_csv(path_arquivo)
# print(vendas_itens)

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:

    """
    Função que filtra produtos onde entrega = True

    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:

    """
    Soma todos os produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues =filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)