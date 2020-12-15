initialArray = [1, 2, 3]


def CalcSum(initialArray):
    sum = 0
    for x in range(len(initialArray)):
        sum = sum + initialArray[x]
    return sum


sum = CalcSum(initialArray)


def CalcAvg(initialArray, sum):
    return sum/len(initialArray)
