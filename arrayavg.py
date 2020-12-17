def getGreaterThanAvg(initialArray):
    sum = 0
    newArray = []
    for x in range(len(initialArray)):
        sum = sum + initialArray[x]
    avg = sum/len(initialArray)
    for x in range(len(initialArray)):
        if(initialArray[x] > avg):
            newArray.append(initialArray[x])
    return newArray
