class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
              
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            
            elif len(stack) > 0:
                popped = stack.pop() 
                if popped == '(' and i != ')':
                    return False
                
                elif popped == '{' and i != '}':
                    return False
                
                elif popped == '[' and i != ']':
                    return False
            
            else:
                return False
                
        if len(stack) > 0:
            return False
        
        return True
        