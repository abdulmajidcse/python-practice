def insertion_sort(arr):
    # copy the original list
    arr2 = arr[:]
    for i in range(1, len(arr2)):
        value = arr2[i]
        j = i - 1
        while j >= 0 and arr2[j] > value:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = value
    return arr2

# Example usage
arr = [12, 11, 13, 5, 6]
print("Unsorted array is:", arr)
print("Sorted array is:", insertion_sort(arr))