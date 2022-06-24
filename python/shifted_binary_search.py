def shifted_binary_search(target, shifted_arr):
    
    left = 0
    right = len(shifted_arr)-1
    
    while(left <= right):
        mid = (left+right) // 2
        if shifted_arr[mid] == target:
            return mid
        # target in 'not shifted zone'
        elif shifted_arr[mid] > shifted_arr[left]:
            if target < shifted_arr[mid] & target >= shifted_arr[left]:
                right = mid - 1
            else:
                left = mid + 1
                
        # target in shifted zone 
        else:
            if target > shifted_arr[mid] & target <= shifted_arr[right]:
                left = mid + 1
            else:
                right - mid - 1

    return -1
    



print(shifted_binary_search(21, [9,19,21,2,5]))
print(shifted_binary_search(14, [2,3,5,6,7,14,0,1]))
    




