# selection sort

numList = [4,5,3,1,2]

def selectionSort(numList):
    for i in range(len(numList)):
        curr_min = i
        for j in range(i + 1, len(numList)):
            if numList[j] < numList[curr_min]:
                curr_min = j
        numList[i], numList[curr_min] = numList[curr_min], numList[i]
      
    return numList

sortedList = selectionSort(numList)
print(sortedList)
