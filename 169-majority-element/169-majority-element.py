class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        index = 0
        half_size = len(nums) // 2 + 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1
                
            if count >= half_size:
                return nums[i]
        
        return nums[len(nums) - 1]
                
            
            