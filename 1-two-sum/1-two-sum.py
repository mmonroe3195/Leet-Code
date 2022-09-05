class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numdict = {}
        
        for i in range(len(nums)):
            if numdict.get(target - nums[i]) != None:
                return [numdict[target - nums[i]], i]
            
            numdict[nums[i]] = i