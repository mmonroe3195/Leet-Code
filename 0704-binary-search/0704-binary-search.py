import math

class Solution(object):
    
    #method one: using no helper method
    """def search(self, nums, target):
        if len(nums) == 0:
            return -1
        
        mid = int(math.floor((len(nums) - 1) / 2))
        if nums[mid] == target:
            return mid
        
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        
        right = self.search(nums[mid + 1:], target)
        
        if right == -1:
            return -1
        
        return mid + 1 + right"""
    
    #method two: using a helper function
    def searchHelper(self, nums, start, end, target):
        if start > end:
            return -1
            
        mid = (start + end) // 2
           
        if target == nums[mid]:
            return mid
            
        elif target < nums[mid]:
            return self.searchHelper(nums, start, mid - 1, target)
            
        return self.searchHelper(nums, mid + 1, end, target)
            
    def search(self, nums, target):
        return self.searchHelper(nums, 0, len(nums) - 1, target)