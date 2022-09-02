class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        chars = [0 for i in range(26)]
        
        for i in s:
            chars[ord(i) - 97] += 1
        
        print(chars)
            
           
        for i in t:
            chars[ord(i) - 97] -= 1
            
        if chars != [0 for i in range(26)]:
            return False
        
        return True
        
        