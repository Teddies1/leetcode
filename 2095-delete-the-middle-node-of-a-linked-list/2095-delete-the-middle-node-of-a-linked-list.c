/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* locatepre(struct ListNode *head){
    int count = 0;
    struct ListNode* temp = head;
    while(temp != NULL){
        count++;
        temp = temp->next;
    }
    for (int i = 0; i < (count/2)-1; i++){
        head = head->next;
    } 
    return head;
}
struct ListNode* deleteMiddle(struct ListNode* head){
    if(head->next == NULL || head == NULL){
        return NULL;
    }
    
    struct ListNode *pre = locatepre(head);
    struct ListNode *mid = pre->next;
    
    pre->next = mid->next;
    return head;
}