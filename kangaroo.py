def kangaroo(x1, v1, x2, v2):
    
    if x2 > x1 and v2 > v1:
        print('no')

    while x1 != x2:
        x1 += v1
        x2 += v2

        if x1 == x2:
            print('YES')
        
    print('NO')

kangaroo(0,2,1,3)