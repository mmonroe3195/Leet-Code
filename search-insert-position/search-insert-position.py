class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        
        for i in reversed(range(nums[0], target)):
            if i in nums:
                return nums.index(i) + 1
            
        if target < nums[0]:
            return 0
        
        return len(nums)