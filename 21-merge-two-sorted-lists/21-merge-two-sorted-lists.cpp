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

    /* Helper method */
    void mergeHelper(ListNode* list1, ListNode* list2, ListNode* curr) {
        
        if (!list1 && !list2)
            return;
        
        if (!list1) {
            curr->next = list2;
            return;
        }
            
        if (!list2){
            curr->next = list1;
            return;
        }
        
        if (list1->val < list2->val) {
            ListNode* temp = list1->next;
            curr->next =  list1;
            curr = curr->next;
            mergeHelper(temp, list2, curr);
        }
        
        else {
            ListNode* temp = list2->next;
            curr->next = list2;
            curr = curr->next;
            mergeHelper(list1, temp, curr);
        }
        
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* head = nullptr;
        
        if (!list1 && !list2)
            return nullptr;
        
        if (!list1)
            return list2;
            
        if (!list2)
            return list1;
        
        if (list1->val < list2->val) {
            head = list1;
            mergeHelper(list1->next, list2, head);
        }
        
        else {
            head = list2;
            mergeHelper(list1, list2->next, head);
        }
        
        return head;
    }
    
    
};