import math

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        mid = int(math.floor((len(nums) - 1) / 2))
        if nums[mid] == target:
            return mid
        
        left = self.search(nums[:mid], target)
        
        if left != -1:
            return left
        
        right = self.search(nums[mid + 1:], target)
        
        if right == -1:
            return -1
        
        else:
            return mid + 1 + right