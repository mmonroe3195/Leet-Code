class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #runtime is O(n)
        s = s.lower()
        
        #removes all whitespace and non-alphanumeric chars
        s = re.sub(r'[\W_]', '', s) 
        print(s)
        
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
            
        return True