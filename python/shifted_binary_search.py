def search(nums, target: int) -> int:
        
        if(len(nums)) < 1:
            return -1
        
        if(len(nums) == 1 and nums[0] == target):
            return 0
        
        if(target == nums[len(nums)-1]):
            return len(nums) -1 
        
        if target == nums[0]:
            return 0
        left = 0
        right = len(nums) -1
        p = 0
        arr = []  #array that contains the target
        
        # Find pivot
        # while left < right:
            
        #     middle = (left + (right - left)) // 2
            
        #     if(nums[middle] > nums[right]):
        #         left = middle + 1
        #     else:
        #         right = middle

        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                p = i
        
        print(p)
        # to check which array to binary search
        # target at left array
        # if(nums[0] > nums[len(nums)-1]):
        #     if(target > nums[p] & target > nums[left]):
        #         right = p     
        #     # target at right array
        #     else:
        #         left = p+ 1

        # else:
        #     if(target > nums[p] & target > nums[left]):
        #         left = p + 1
        #         print(left)
        
        #     else:
        #         right = p

        
            
            
            
        while left <= right:
            print(left, right)
            middle = (left + right) // 2

            
            
            if(nums[middle] == target):
                return middle
            
        
            if(nums[middle] > target):
                right = middle - 1
            else:
                left = middle + 1                          
            
        
        return -1
            
print(search([1,3,5],3))