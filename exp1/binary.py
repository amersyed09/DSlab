def binarySearch(n,arr,key):
    low = 0
    high = n-1
    while low <= high:

        mid = (low + high)//2

        if key == arr[mid]:
            return mid 
        elif key > arr[mid]:
            low = mid +1 
        else:
            high = mid -1 

    return -1 

n = int(input("enter no of array elements :"))

arr = list(map(int,input("enter array elements :").split()))

key = int(input("enter key value to search:"))

result = binarySearch(n,arr,key)

if result == -1:
    print("element not found ")

else:
    print("element found at", result+1)
    