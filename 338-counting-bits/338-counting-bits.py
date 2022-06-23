class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(n + 1):
            ans.append(str(bin(i))[2:].count("1"))
        
        return ans