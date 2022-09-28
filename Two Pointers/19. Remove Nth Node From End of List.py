# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head) # In case we need to remove the head node in the case of [1, 2], n = 2
        first, second = dummy, dummy
        
        for i in range(n):
            second = second.next
        
        while second.next:
            first, second = first.next, second.next
        
        first.next = first.next.next # First element is the element before the node that has to be removed
        
        return dummy.next
