def addone(digits, num):
        digits[num] = 0
        
        if num - 1 < 0:
            digits[0] = 1
            digits.append(0)
            
        elif digits[num - 1] == 9:
            addone(digits, num - 1)
        
        else:
            digits[num - 1] = digits[num - 1] + 1
            
            
        return digits

class Solution(object):
        
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            
        else:
            digits = addone(digits, len(digits) - 1)
        
        return digits
    

    