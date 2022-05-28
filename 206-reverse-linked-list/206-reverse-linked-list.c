/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/*
    first we set pre to NULL.
    the idea is that we keep pointing cur->next backwards towards pre.
    we keep doing this until cur == NULL, which is the terminating statement.
    then, pre will be the new head node, and the LL is reverse since all the links-
    point backwards, and eventually towards the original NULL pointer.
    
    NULL    1 -> 2 -> 3 -> 4 -> NULL
    p       c    n
    
    NULL <- 1    2 -> 3 -> 4 -> NULL
            p    c    n
            
    NULL <- 1 <- 2    3 -> 4 -> NULL
                 p    c    n
                 
    NULL <- 1 <- 2 <- 3    4 -> NULL
                      p    c    n
                      
    NULL <- 1 <- 3 <- 3 <- 4    NULL 
                           p    c
    */

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *pre = NULL;
    struct ListNode *cur = head;
    struct ListNode *next = NULL;
    
    if(head == NULL){
        return NULL;
    }
    
    while(cur != NULL){   
        //establish the next node
        next = cur->next;
        
        //break link to next and point it to pre
        cur->next = pre;
        
        //set cur node to pre
        pre = cur;
        
        //set next node to cur
        cur = next;
    }    
    return pre;
}