/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    
    
    if (head == NULL){
        return NULL;
    }
    if (head->next == NULL){
        return head;
    }
    struct ListNode *next = head->next;
    struct ListNode *temp = head->next->next;
    next->next = head;
    head->next = swapPairs(temp);
    
    
    
    
    

   

    
    return next;
}