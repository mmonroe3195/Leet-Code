class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        #adding availible chars from magazine to dict
        chars = {}
        for i in magazine:
            if chars.get(i):
                chars[i] += 1
            
            else:
                chars[i] = 1
                
        #checking if every char needed for the randsom note is availible
        for i in ransomNote:
            if not chars.get(i) or chars[i] == 0:
                return False
            
            else:
                chars[i] -= 1
        
        return True