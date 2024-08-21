# heap sort

numList = [5,1,2,3,4]

def heapify(numList, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numList[left] > numList[largest]:
        largest = left

    if right < n and numList[right] > numList[largest]:
        largest = right

    if largest != i:
        numList[i], numList[largest] = numList[largest], numList[i] 

        heapify(numList, n, largest)

def heapSort(numList):
    n = len(numList)

    for i in range(n // 2 - 1, -1, -1):
        heapify(numList, n, i)

    for i in range(n-1, 0, -1):
        numList[i], numList[0] = numList[0], numList[i]
        heapify(numList, i, 0)
    
    return numList

sortedList = heapSort(numList)
print(sortedList)
