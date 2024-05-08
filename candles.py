def birthdayCakeCandles(candles):
    # Write your code here
    
    map_candle = {}
    
    for i in candles:
        if i in map_candle:
            map_candle[i] += 1
        else:
            map_candle[i] = 1
    
    print(max(map_candle.values()))

birthdayCakeCandles([3,2,2,1,3])