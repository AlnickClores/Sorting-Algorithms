# merge sort

numList = [2, 1, 5, 3, 4]

def mergeSort(numList):
    if len(numList) > 1:
        mid = len(numList) // 2
        left_half = numList[:mid]
        right_half = numList[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numList[k] = left_half[i]
                i += 1
            else:
                numList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numList[k] = right_half[j]
            j += 1
            k += 1

    return numList

sortedList = mergeSort(numList)
print(sortedList)