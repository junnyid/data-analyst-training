def solution(inputArray):
    maxSoFar = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if product > maxSoFar:
            maxSoFar = product
    return maxSoFar