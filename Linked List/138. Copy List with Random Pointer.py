class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copydict = {None:None}
        
        curr = head
        while curr:
            copydict[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            copydict[curr].next = copydict[curr.next]
            copydict[curr].random = copydict[curr.random]
            curr = curr.next
            
        return copydict[head]
