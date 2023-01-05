# Best case: O(n)
# Worst case: O(n^2)

def bubbleSort(arr):
    swapped = False
    for i in range(len(arr) - 1):

        for j in range(len(arr) - i - 1):
        
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    if not swapped: return 
    
arr = [3, 2, 5, 4, 1]
print(bubbleSort(arr))