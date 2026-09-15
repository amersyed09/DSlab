def insertionSort(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


n = int(input("enter no of array elements :"))

arr = list(map(int, input("enter array elements :").split()))


result = insertionSort(n, arr)

print(f"sorted array {result}")