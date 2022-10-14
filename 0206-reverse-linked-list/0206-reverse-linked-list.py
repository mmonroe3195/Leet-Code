# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseHelper(self, head, prev):
        if not head:
            return None
        
        if not head.next:
            head.next = prev
            return head
        
        temp = head.next
        head.next = prev
        return self.reverseHelper(temp, head)
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseHelper(head, None)
        