class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # would be easy to do in O(nlog(n))
        # sort list -> iterate through to see missing number range
        # this way is better though
        return sum(range(len(nums) + 1)) - sum(nums)
        