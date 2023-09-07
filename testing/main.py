f = open('BBG004731032.txt', 'r').readlines()
result = []
for i in range(len(f)):
    candle = f[i]
    candle = candle.split(',')
    candle =  [candle[0].split('=')[2], candle[2].split('=')[2], candle[4].split('=')[2], candle[6].split('=')[2],
            candle[8].split('=')[1],
            f"{candle[9].split('(')[1].strip()}:{candle[10].strip()}:{candle[11].strip()}:{candle[12].strip()}:{candle[13].strip()}"]
    result.append(int(candle[4]))

print(result)

