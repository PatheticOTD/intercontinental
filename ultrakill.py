def searchInsert(self, nums, target):
    left = 0
    right = len(nums)-1
    while True:
        middle = (right + left) // 2
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        elif target == nums[middle]:
            return middle
        elif right - left == 1:
            return left
        
        if target > nums[middle]:
            left = middle
        else:right = middle
    
    
    
if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))