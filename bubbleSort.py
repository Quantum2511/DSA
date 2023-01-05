# Best case: O(n)
# Worst case: O(n^2)

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [3, 2, 5, 4, 1]
print(bubbleSort(arr))