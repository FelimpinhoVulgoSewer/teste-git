#print(input('Digite sua idade: ')) ; pode-se usar o input dentro do print pra ficar mais top
fita1 = input('Digite a fita 1: ')
fita2 = input('Digite a fita 2: ')

helice1 = fita1.upper()
helice2 = fita2.upper()


dict_fita = {
    'A': 1,
    'T': 1,
    'G': 2,
    'C': 2
}

if helice1.isalpha() and helice2.isalpha() and len(helice1) == len(helice2):
    erros = 0
    position = []
    for i in range(len(helice1)):
        if dict_fita[helice1[i]] != dict_fita[helice2[i]] or helice1[i] == helice2[i]:
            erros = erros + 1
            position.append(i)
    print('Quantidade de Erros: {}'.format(erros))
    print('Posição dos erros: {}'.format(position))

