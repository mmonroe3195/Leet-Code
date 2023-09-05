class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # O(n) time complexity and O(n) space complexity
        """
        dict = {}
        for i in nums:
             if dict.get(i):
                 return True
            
             dict[i] = 1"""
        
        # O(nlogn) time complexity and O(1) space complexity
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False      
        
            
            