/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *pre = NULL;
    struct ListNode *cur = head;
    struct ListNode *next = NULL;
    
    if(head == NULL){
        return NULL;
    }
    
    while(cur != NULL){   
        next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }    
    /*while(cur != NULL){   
        next = reverseList(cur->next);
        cur->next = pre;
        pre = cur;
        cur = next;
    }*/
    return pre;
}