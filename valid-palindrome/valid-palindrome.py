class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        new = ""
        
        for i in s:
            if i.isalnum():
               new = new + i
        
        
        for i in range(len(new)//2):
            if new[i] != new[-i-1]:
                return False
        return True