class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        odd, even = head, head.next
        even_start = head.next

        while even and even.next:
            tmp = even.next
            even.next = even.next.next
            odd.next = tmp

            even = even.next
            odd = odd.next

        odd.next = even_start

        return head
