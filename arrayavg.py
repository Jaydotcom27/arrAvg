initialArray = [1, 2, 3]


def CalcSum(initialArray):
    sum = 0
    for x in range(len(initialArray)):
        sum = sum + initialArray[x]
    return sum


def CalcAvg(initialArray, sum):
    return sum/len(initialArray)


def getGreater(initialArray, avg):
    newArray = []
    for x in range(len(initialArray)):
        if (initialArray[x] > avg):
            newArray.append(initialArray[x])
    return newArray


print(getGreater([4, 7, 2], 4.333333333333333))
