def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return arr[i]


arr = [3,1,3,4,2]
print(find_duplicate(arr))
arr1 = [2,4,7,2,8]
print(find_duplicate(arr1))