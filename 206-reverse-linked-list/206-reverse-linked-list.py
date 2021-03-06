# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):      
    def reverseHelper(self, head, prev):
            if head.next:
                first =  self.reverseHelper(head.next, head)
                head.next = prev
                return first
            
            else:
                head.next = prev
                return head
            

            
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        return self.reverseHelper(head, None)