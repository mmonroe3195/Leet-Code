class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        
        count = 0
        letterread = False
        
        for i in s:
            if i == ' ':
                if letterread:
                    break
                
            else:
                letterread = True
                count = count + 1
                
                
        return count