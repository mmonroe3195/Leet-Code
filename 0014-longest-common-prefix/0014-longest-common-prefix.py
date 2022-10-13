class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for str in strs:
            if len(prefix) == 0:
                return ""
            for n in range(len(str)):
                if len(prefix) > n and str[n] != prefix[n]:
                    prefix = prefix[:n]
                    break
            
            #if the current string being compared is shorter than the prefix, the current prefix needs to be shortened
            if len(str) < prefix:
                prefix = prefix[:len(str)]
        
        return prefix
                