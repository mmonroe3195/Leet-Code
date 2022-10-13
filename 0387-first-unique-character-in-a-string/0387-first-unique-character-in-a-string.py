class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #two O(n) loops = O(n) runtime
        
        #adding chars to dict
        chars = {}
        for i in s:
            if chars.get(i):
                chars[i] += 1
            
            else:
                chars[i] = 1
        
        #checking dict for first char without a repeat
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        
        return -1