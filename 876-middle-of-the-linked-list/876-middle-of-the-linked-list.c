/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    int count = 0;
    struct ListNode *temp = head;
    
    while(temp != NULL){
        count++;
        temp = temp->next;
    }
    for (int i = 0; i < (count/2) ; i++){
        head = head->next;
    }
    return head;
    
}