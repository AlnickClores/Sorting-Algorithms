# quick sort

numList = [2, 1, 5, 3, 4]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)

sortedList = quickSort(numList)
print(sortedList)
