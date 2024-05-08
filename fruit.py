def countApplesAndOranges(s, t, a, b, apples, oranges):

    count_apple = 0
    count_orange = 0

    for apple in apples:
        if t >= (apple + a) and (apple + a) >= s:
            count_apple += 1

    for orange in oranges:
        if t >= (orange + b) and (orange + b) >= s:
            count_orange += 1

    print(count_apple)
    print(count_orange)


countApplesAndOranges(7,11,5,15,[-2, 2, 1],[5, -6])