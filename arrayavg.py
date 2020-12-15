def CalcAvg(initialArray):
    sum = 0
    avg = 0
    for x in range(len(initialArray)):
        sum = sum + initialArray[x]
    avg = sum/len(initialArray)
    return avg
