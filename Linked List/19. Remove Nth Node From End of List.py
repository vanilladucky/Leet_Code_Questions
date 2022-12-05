class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        for i in range(n):
            right = right.next
            
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        
        return dummy.next
