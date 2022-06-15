/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    struct ListNode *temp = head;
    struct ListNode *rotatehead = NULL;
    if (head == NULL){
        return NULL;
    }
    int count = 1;
    while (head->next != NULL){
        head = head->next;
        count++;
    }
    head->next = temp;
    int diff = k % count;
    
    for (int i = 0; i < count - diff; i++){
        head = head->next;
    }
    rotatehead = head->next;
    head->next = NULL;
    return rotatehead;
}