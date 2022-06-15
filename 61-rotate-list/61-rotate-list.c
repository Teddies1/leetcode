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
    /* we want to create a circular linked list, and maintain a counter */
    while (head->next != NULL){
        head = head->next;
        count++;
    }
    head->next = temp;
    /*  
        notice that the head node to be returned is simply 
        (count - (k % count)) + 1 times of head = head->next;
    */
    int diff = k % count;
    
    for (int i = 0; i < count - diff; i++){
        head = head->next;
    }
    /* 
        increment the head by count-diff times, and set the head to be returned as head->next
        then, break the circular linked list
    */
    
    rotatehead = head->next;
    head->next = NULL;
    return rotatehead;
}