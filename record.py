def breakingRecords(scores):
    hs = scores[0]
    ls = scores[0]
    bs = []
    ws = []
    
    for i in range(len(scores)):
        if scores[i] > hs:
            bs.append(i)
            hs = scores[i]
            
        if scores[i] < ls:
            ws.append(i)
            ls = scores[i]

    
    return print(len(bs), len(ws))

breakingRecords([3,4,21,36,10,28,35,5,24,42])