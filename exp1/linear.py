def linearSearch(n,arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

n = int(input("enter no of array elements :"))

arr = list(map(int,input("enter array elements :").split()))

key = int(input("enter key value to search:"))

result = linearSearch(n,arr,key)

if result == -1:
    print("element not found ")

else:
    print("element found at", result+1)
    