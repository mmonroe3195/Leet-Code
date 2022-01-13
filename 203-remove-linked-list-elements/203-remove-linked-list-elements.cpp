/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        
        //handles the first element
        while(head && head->val == val)
            head = head->next;
            
        ListNode* current = head;
        
        while(current != nullptr){
            //checks if a value in the linked-list is the same as the val passed
            if(current->next && current->next->val == val)
                //removes the necessary value from the linked list  
                current->next = current->next->next;
            else
                current = current->next;
        }
        
         return head;
        
    }
        
        
};