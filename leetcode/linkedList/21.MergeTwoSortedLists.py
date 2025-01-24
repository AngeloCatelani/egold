def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = list1
    curr2 = list2
    head = ListNode()
    ans = ListNode()

    while curr1 or curr2:
        if curr1 is None:
            ans.next = curr2
            break
        elif curr2 is None:
            ans.next = curr1
            break
        else:
            if curr1.val < curr2.val:
                ans.next = curr1
                curr1 = curr1.next
            else:
                ans.next = curr2
                curr2 = curr2.next
        ans = ans.next
    return head.next
