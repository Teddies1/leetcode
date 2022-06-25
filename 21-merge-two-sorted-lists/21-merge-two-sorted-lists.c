/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    /*
    if (!list1){
        return list2;
    }
    if (!list2){
        return list1;
    }
    if (list1->val > list2->val){
        list2->next = mergeTwoLists(list1, list2->next);
        return list2;
    }
    else{
        list1->next = mergeTwoLists(list1->next, list2);
        return list1;
    }
    */
    struct ListNode dummy;
    struct ListNode *temp = &dummy;
    if (list1 == NULL && list2 == NULL){
        return NULL;
    }
    while(list1 != NULL && list2 != NULL){
        if (list1->val > list2->val){
            temp->next = list2;
            temp = temp->next;
            list2 = list2->next;
        }
        else{
            temp->next = list1;
            temp = temp->next;
            list1 = list1->next;
        }
    }
    while(list1 != NULL){
        temp->next = list1;
        temp = temp->next;
        list1 = list1->next;
    }
    while(list2 != NULL){
        temp->next = list2;
        temp = temp->next;
        list2 = list2->next;
    }
    return dummy.next;
}