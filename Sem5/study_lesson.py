def busca(lista, valor_buscado):
    valores_nao_existentes = []
    for i in valor_buscado:
        if i not in lista:
            return "You died!"

    return valores_nao_existentes

def main():
    qtd_testes = int(input())
    for x in range(qtd_testes):
        plano = input()
