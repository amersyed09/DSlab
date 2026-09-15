def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


n = int(input("enter no of array elements :"))

arr = list(map(int,input("enter array elements :").split()))


result = quickSort(arr, 0, n - 1)

print(f"sorted array {result}")
