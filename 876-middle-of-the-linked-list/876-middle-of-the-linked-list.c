/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    
    // okay-ish solution, but it is o(2n)
    /*
    int count = 0;
    struct ListNode *temp = head;
   
    while(temp != NULL){
        count++;
        temp = temp->next;
    }
    for (int i = 0; i < (count/2); i++){
        head = head->next;
    }
    return head;
    */
    
    //o(n)
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
    
    
    
    
}