def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 1-2-3
    prev = None
    curr = head
    while curr:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


 