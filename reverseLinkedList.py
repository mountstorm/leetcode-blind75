class Solution:
    def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        previous = None
        
        while current is not None:
            # save next node before we break the link
            nextNode = current.next
            # reverse the pointer
            current.next = previous
            # move the prev and curr one step forward
            previous = current
            current = nextNode
        # previous is now the new head    
        return previous