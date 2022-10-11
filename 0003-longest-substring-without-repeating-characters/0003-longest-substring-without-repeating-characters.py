class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        max_len = 0
        curr_len = 0
        i = 0
        
        while i != len(s):
            #checking if the current string char is already in the dict
            if s[i] in chars.keys():
                 #setting the new index based on where the last new substring starts
                 #uses sliding window technique
                i = chars[s[i]] + 1
                chars = {}
                chars[s[i]] = i

                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 1                
            
            else:
                chars[s[i]] = i
                curr_len += 1
            i += 1

        if curr_len > max_len:
            return curr_len
        
        return max_len