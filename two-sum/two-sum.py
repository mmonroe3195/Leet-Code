import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old = copy.deepcopy(nums)
        nums.sort()
        num1 = 0
        num2 = 0
        
        
        for i in nums:
            if target - i in nums:
                num2 = target - i
                num1 = i
                break
        
        
        index1 = old.index(num1)
        index2 = old.index(num2)
        
        if index2 == index1:
            old.remove(num1)
            index2 = old.index(num1) + 1
        
        arr = [index1, index2]
        arr.sort()
        return arr
        
        
        