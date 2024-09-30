from typing import List

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        h1 = {i:0 for i in 'qwertyuiopasdfghjklzxcvbnm'}
        h2 = {i:0 for i in 'qwertyuiopasdfghjklzxcvbnm'}

        for i in s1:
            h1[i] += 1

        left = 0
        for right in range(len(s2)):
            if right - left == len(s1):
                if h1 == h2:
                    return True
                else:
                    h2[s2[left]] -=1
                    left +=1
            h2[s2[right]] += 1
        return False
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
                
            if nums[mid] > target:
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if nums[right] > target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

s = Solution()

print(s.search([1,2,3,4,5,6], 4))