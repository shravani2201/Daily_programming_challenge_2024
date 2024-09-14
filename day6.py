def find_zero_sum_subarrays(arr):
    subarr = []
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == 0:
                subarr.append((i, j))  
    return subarr

arr = [-3,1,2,-3,4,0]
result = find_zero_sum_subarrays(arr)


print(result)
