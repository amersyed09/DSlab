def selectionSort(n,arr):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j 

        arr[i],arr[min] = arr[min],arr[i]

    return arr

n = int(input("enter no of array elements :"))

arr = list(map(int,input("enter array elements :").split()))


result = selectionSort(n,arr)

print(f"sorted array {result}")
    