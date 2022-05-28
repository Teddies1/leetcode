/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head == NULL){
        return false;
    }
    if (head->next == NULL || head->next->next == NULL){
        return false;
    }
    struct ListNode *p = head;
    struct ListNode *q;
    
    q = p->next;
    
    while (p != NULL && q != NULL && q->next != NULL){
        if (p == q){
            return true;
        }
        p = p->next;
        q = q->next->next;
    }
    
    
    return false;
}