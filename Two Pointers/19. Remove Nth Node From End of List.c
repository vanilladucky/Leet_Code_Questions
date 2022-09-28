/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *dummy = (struct ListNode*)malloc(sizeof(struct ListNode)*30);
    dummy->next = head;
    struct ListNode *ptr1 = dummy;
    struct ListNode *ptr2 = dummy;
    int i = 0;
    
    for (i=0; i<n; i++){
        ptr2 = ptr2->next;
    }
    
    while (ptr2->next != NULL){
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    
    ptr1->next = ptr1->next->next;
    
    return dummy->next;
}
