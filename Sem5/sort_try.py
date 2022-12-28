teste1=[2,
        ['Miguel Rocha 199 138',
        'Heitor Pereira 200 200']]

teste2=[7,
        ['Guido Batista 195 110',
        'Heitor Tostes 180 75',
        'Bruno Costa 180 75',
        'Joao Kleber 180 65',
        'Rafael Rodrigues 165 110',
        'Ricardo Neto 170 70',
        'Juca Carvalho 180 77']]

teste3=[10,
        ['William Cavalcante 101 152',
        'Lucas Costa 206 92',
        'Gabriel Pereira 203 168',
        'George Santos 228 184',
        'George Gomes 222 134',
        'Jack Santos 225 73',
        'Harry Oliveira 227 170',
        'Oliver Pereira 221 105',
        'Lucas Carvalho 130 43',
        'Thomas Morais 143 112']]

teste4=[10,
        ['Charlie Alpha 180 75',
        'Charlie Beta 180 77',
        'Charlie Gamma 180 73',
        'Charlie Delta 180 74',
        'Charlie Epsilon 180 46',
        'Rambo Alpha 180 71',
        'Rambo Beta 180 72',
        'Rambo Gamma 180 77',
        'Rambo Delta 180 78',
        'Rambo Epsilon 180 79']]

teste5=[5,
        ['Charlie Alpha 165 90',
        'Charlie Beta 165 90',
        'Charlie Gamma 165 90',
        'Charlie Delta 165 90',
        'Charlie Epsilon 165 90']]

teste6=[50,
        ['Bernardo Schmitz 165 90',
        'William Martins 112 48',
        'Arthur Melo 206 63',
        'William Cardoso 188 56',
        'William Ribeiro 165 51',
        'Gabriel Rodrigues 181 86',
        'Miguel Correia 226 87',
        'Arthur Santos 124 82',
        'Charlie Martins 198 76',
        'Charlie Cardoso 154 85',
        'Heitor Dias 208 43',
        'George Sousa 170 77',
        'Gabriel Cavalcante 111 91',
        'Jacob Morais 102 46',
        'Lucas Dias 120 32',
        'Matheus Costa 165 52',
        'Noah Fernandes 156 82',
        'Matheus Sousa 128 89',
        'Jack Martins 139 70',
        'Miguel Schmitz 158 50',
        'William Rocha 132 67',
        'Charlie Teixeira 166 76',
        'Gabriel Dias 166 97',
        'Gabriel Ribeiro 100 82',
        'Pedro Carvalho 145 55',
        'Jacob Barbosa 222 97',
        'William Sousa 140 86',
        'Heitor Cardoso 219 100',
        'Davi Cavalcante 187 57',
        'Charlie Carvalho 174 100',
        'Matheus Cardoso 226 41',
        'Davi Dias 137 56',
        'Matheus Pereira 225 89',
        'Miguel Cavalcante 198 30',
        'Heitor Rodrigues 131 80',
        'Jack Lima 131 58',
        'Charlie Santos 153 75',
        'George Dias 197 70',
        'Gabriel Carvalho 160 89',
        'Davi Costa 182 95',
        'Charlie Almeida 163 93',
        'Matheus Rodrigues 185 54',
        'Rafael Ribeiro 113 85',
        'Thomas Alves 220 66',
        'George Pereira 221 36',
        'Lucas Teixeira 212 76',
        'Davi Correia 165 38',
        'Heitor Lima 201 56',
        'Gabriel Lima 133 44',
        'Gabriel Cardoso 199 48']]
print(teste6)
def main(qtd,lista):
    qtd_pretendentes = qtd
    pretendentes = {}
    for vezes in range(qtd_pretendentes):
        nome,sobrenome,altura,peso = lista[vezes].split()
        dif_peso,dif_alt = abs(int(peso)-75) , abs(int(altura)-180)
        chave = dif_peso if int(peso)<=75 else int(peso)
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



main(teste1[0],teste1[1])
print()
main(teste2[0],teste2[1])
print()
main(teste3[0],teste3[1])
print()
main(teste4[0],teste4[1])
print()
main(teste5[0],teste5[1])
print()
main(teste6[0],teste6[1])

'''
Rocha, Miguel
Pereira, Heitor

Costa, Bruno
Tostes, Heitor
Kleber, Joao
Carvalho, Juca
Neto, Ricardo
Batista, Guido
Rodrigues, Rafael

Pereira, Gabriel
Costa, Lucas
Morais, Thomas
Pereira, Oliver
Gomes, George
Santos, Jack
Oliveira, Harry
Santos, George
Carvalho, Lucas
Cavalcante, William

Alpha, Charlie
Delta, Charlie
Gamma, Charlie
Beta, Rambo
Alpha, Rambo
Epsilon, Charlie
Beta, Charlie
Gamma, Rambo
Delta, Rambo
Epsilon, Rambo

Alpha, Charlie
Beta, Charlie
Delta, Charlie
Epsilon, Charlie
Gamma, Charlie

Rodrigues, Gabriel
Costa, Davi
Rodrigues, Matheus
Carvalho, Charlie
Cavalcante, Davi
Cardoso, William
Sousa, George
Teixeira, Charlie
Dias, Gabriel
Costa, Matheus
Ribeiro, William
Correia, Davi
Schmitz, Bernardo
Dias, George
Almeida, Charlie
Cavalcante, Miguel
Martins, Charlie
Cardoso, Gabriel
Carvalho, Gabriel
Lima, Heitor
Schmitz, Miguel
Fernandes, Noah
Melo, Arthur
Cardoso, Charlie
Santos, Charlie
Dias, Heitor
Teixeira, Lucas
Carvalho, Pedro
Cardoso, Heitor
Alves, Thomas
Sousa, William
Martins, Jack
Pereira, George
Barbosa, Jacob
Dias, Davi
Pereira, Matheus
Cardoso, Matheus
Correia, Miguel
Lima, Gabriel
Rocha, William
Lima, Jack
Rodrigues, Heitor
Sousa, Matheus
Santos, Arthur
Dias, Lucas
Ribeiro, Rafael
Martins, William
Cavalcante, Gabriel
Morais, Jacob
Ribeiro, Gabriel
'''