# Best case: O(n)
# Worst case: O(n^2)

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

    return arr

arr = [3, 2, 5, 4, 1]
print(bubbleSort(arr))