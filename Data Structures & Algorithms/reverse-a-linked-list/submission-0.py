class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        return self.reverse(None, head)
    
    def reverse(self, prev, curr):
        if not curr:
            return prev
        
        nxt = curr.next
        curr.next = prev
        
        return self.reverse(curr, nxt)