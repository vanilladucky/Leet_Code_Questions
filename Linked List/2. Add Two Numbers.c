/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* result = malloc(sizeof(struct ListNode)); 
    struct ListNode* ptr = result;
    result->val = 0;
    result->next = NULL;

    int carry = 0;
    
    while (l1 != NULL || l2!=NULL || carry !=0){
        
        int a = (l1 == NULL) ? 0 : l1->val;
        int b = (l2 == NULL) ? 0 : l2->val;
        ptr->val = a + b + carry;
        carry = ptr->val / 10;
        ptr->val = ptr->val %10;

        if(l1!=NULL){
            l1 = (l1->next ==NULL)? NULL: l1->next;
        }
        if(l2 !=NULL){
            l2 = (l2->next !=NULL)? l2->next: NULL;
        }

        if(l1 != NULL || l2!=NULL || carry !=0){
            ptr->next = malloc(sizeof(struct ListNode));
            ptr->next->next=NULL;
            ptr = ptr->next;
        }
        
    }
    return result;
}
