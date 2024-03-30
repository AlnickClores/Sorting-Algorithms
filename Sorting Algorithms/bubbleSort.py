# bubble sort

numList = [4,5,3,1,2]

def bubbleSort(numList):
    for i in range(len(numList)):
        for j in range(len(numList) - 1):
            if numList[j] > numList[j + 1]:
                numList[j + 1], numList[j] = numList[j], numList[j + 1]
    return numList

sortedList = bubbleSort(numList)
print(sortedList)
