def bubbleSort(n,arr):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

n = int(input("enter no of array elements :"))

arr = list(map(int,input("enter array elements :").split()))


result = bubbleSort(n,arr)

print(f"sorted array {result}")
    