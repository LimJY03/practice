def binary_search(target, sorted_arr):
    left = 0
    right = len(sorted_arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        if sorted_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1 #to tell that the target does not exist in the list
print(binary_search(9, [1,3,5,7,9]))