/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0,head);
        ListNode prev = dummy;
        ListNode curr = head;
        while(curr != null && curr.next != null){
            ListNode fast = curr.next.next;
            ListNode slow = curr.next;

            slow.next = curr;
            curr.next = fast;
            prev.next = slow;
          
            prev = curr;
            curr = fast;
        }
        return dummy.next;
    }
}
// Certainly! Let's go through the iterations of the `while` loop for the input linked list `[1,2,3,4]`:

// | Iteration | curr  | curr.next      | prev  | nextPair | second | second.next |
// |-----------|-------|----------------|-------|----------|--------|-------------|
// | Initial   | 1     | 2              | dummy |          |        |             |
// | 1         | 1     | 2              | dummy | 3        | 2      | 1           |
// | 2         | 3     | 4              | 2     | null     | 4      | 3           |

// In the initial state, `curr` points to the first node (1), and `curr.next` points to the second node (2). The `prev` pointer is initially set to the dummy node, and `nextPair` and `second` are yet to be defined.

// After the first iteration, `curr` is still 1, `curr.next` is 2, `prev` is the dummy node, `nextPair` points to 3, `second` is 2, and `second.next` is 1.

// After the second iteration, `curr` is now 3, `curr.next` is 4, `prev` is 2, `nextPair` is null (as there are no more pairs), `second` is 4, and `second.next` is 3.

// This process continues until there are no more pairs to swap.