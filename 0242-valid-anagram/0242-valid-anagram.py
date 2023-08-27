class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        """nlog(n) solution"""
        """
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        
        return False"""
    
        # O(n)
        s_dict = {}
        t_dict = {}
        
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else: 
                s_dict[i] = 1
                
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else: 
                t_dict[i] = 1
                
        if t_dict == s_dict:
            return True
        
        return False