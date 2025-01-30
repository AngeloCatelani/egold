def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head) # dummy->1    ->2  ->6->3
        current = head              # prev   curr  next
        
        prev = dummy
        while current:
            nxt = current.next
            if current.val == val: # dummy->1    ->2  ->6->3
                prev.next = nxt                 
                
                
                # prev   curr  next
            else:
                prev = current  # dummy->1    ->2  ->6    ->3
                                #       prev   curr  next
            current = nxt
        return dummy.next
