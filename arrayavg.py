def CalcAvg(initialArray):
    sum = 0
    avg = 0
    for x in range(len(initialArray)):
        sum = sum + initialArray[x]
    avg = sum/len(initialArray)
    return avg


def GreaterVals(initialArray):
    newArray = []
    avg = CalcAvg(initialArray)
    for x in range(len(initialArray)):
        if(initialArray[x] > avg):
            newArray.append(initialArray[x])
    return newArray
