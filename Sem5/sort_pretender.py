def main():
    qtd_pretendentes = int(input())
    pretendentes = {}
    for vezes in range(qtd_pretendentes):
        nome, sobrenome, altura, peso = input().split()
        dif_peso,dif_alt = abs(int(peso)-75), abs(int(altura)-180)
        chave = dif_peso if int(peso) <= 75 else int(peso)
        if dif_alt not in pretendentes:
            pretendentes[dif_alt] = {chave:{sobrenome:[nome]}}
        else:
            if chave not in pretendentes[dif_alt]:
                pretendentes[dif_alt][chave] = {sobrenome:[nome]}
            else:
                if sobrenome not in pretendentes[dif_alt][chave]:
                    pretendentes[dif_alt][chave][sobrenome] = [nome]
                else:
                    pretendentes[dif_alt][chave][sobrenome].append(nome)

    for height in sorted(pretendentes.keys()):
        for weight in sorted(pretendentes[height].keys()):
            for surname in sorted(pretendentes[height][weight].keys()):
                print(surname,end=", ")
                for name in sorted(pretendentes[height][weight][surname]):
                    print(name)

main()
