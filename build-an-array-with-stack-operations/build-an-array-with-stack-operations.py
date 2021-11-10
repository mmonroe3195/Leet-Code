class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        arr = []
        
        for i in range(1, n + 1):
            
            arr.append("Push")
            
            if i not in target:
                arr.append("Pop")
                
            if i == target[-1]:
                break
                
        return arr