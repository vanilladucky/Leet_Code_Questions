class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Slow is in the middle
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # Finished Reversing the second half of the list 
        
        left, right = head, prev
        while right:
            tmp_left = left.next
            tmp_right = right.next
            
            left.next = right
            right.next = tmp_left
            
            left, right = tmp_left, tmp_right
