def find_missing(arr):
    n = len(arr)+1
    sum_of_n = (n*(n+1))//2
    sum_of_arr = sum(arr)
    return sum_of_n-sum_of_arr
arr = [1,2,4,5]
print(find_missing(arr))
arr1 = [2, 3, 4, 5]
print(find_missing(arr1))