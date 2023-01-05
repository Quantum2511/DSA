# Best case: O(n)
# Worst case: O(n^2)

def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr 

arr = [3, 2, 5, 4, 1, 6]
print(insertSort(arr))