import math

class Solution(object):
   import math

class Solution(object):
   def searchHelper(self, nums, target, start, stop):
        if start > stop and nums[0] != target:
            return -1
            
        mid = int(math.floor((start + stop) / 2))
        if nums[mid] == target:
            return mid
        
        elif target < nums[mid]:
            return self.searchHelper(nums, target, start, mid - 1)
        
        return self.searchHelper(nums, target, mid + 1, stop)

   def search(self, nums, target):
        return self.searchHelper(nums, target, 0, len(nums) - 1)
    