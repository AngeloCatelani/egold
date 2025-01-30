def isPalindrome( head) -> bool:
        # converting to array
        arr =[]
        while head:
            arr.append(head.val)
            head = head.next
        l=0
        r = len(arr)-1
        while l<=r:
            if arr[l] !=arr[r]:
                return False
            else:
                l+=1
                r-=1
        return True


# second solution
# spaceO(1)
        fast = head
        slow = head

        while fast and fast.next: #fast !=null and fast.next !=null
          fast = fast.next.next # shifts by 2places
          slow = slow.next # shifts by one place
        #                        l         r
        # reversing half of list 1->2->2<-1
        prev = None
        while slow: # slow will be the midpoint go till end of the node
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # prev will be the end value and slow will be null

        l = head
        r = prev
        while r:
            if l.val !=r.val:
                return False
            l = l.next
            r = r.next
        return True
        