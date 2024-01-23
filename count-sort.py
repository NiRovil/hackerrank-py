def countSort(arr):

    dicionario = {}
    ponto_medio = len(arr)/2

    for index, conjunto in enumerate(arr):
        chave = int(conjunto[0])
        valor = "-" if index < ponto_medio else conjunto[1]
        
        if chave in dicionario.keys():
            dicionario[chave].append(valor)
        else:
            dicionario[chave] = [valor]

    resultado = [valor for chave in sorted(dicionario.keys()) for valor in dicionario[chave]] 

    print(' '.join(resultado))

arr = [['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], 
    ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], 
    ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], 
    ['4', 'the']]

countSort(arr)