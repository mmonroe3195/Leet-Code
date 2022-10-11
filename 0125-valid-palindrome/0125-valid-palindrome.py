import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        i = 0
        j = len(s) - 1
        
        if len(s) > 0:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        
        return True