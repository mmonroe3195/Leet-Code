class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in nums:
            if dict.get(i):
                return True
            
            else:
                dict[i] = 1
        
        return False