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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // Create a dummy node to simplify edge cases.
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Find the node at position 'left' and its predecessor.
        ListNode prevLeft = dummy;
        for (int i = 1; i < left; i++) {
            prevLeft = prevLeft.next;
        }

        // Find the node at position 'right' and its successor.
        ListNode rightNode = prevLeft;
        for (int i = 0; i < right - left + 2; i++) {
            rightNode = rightNode.next;
        }

        // Save the successor of 'rightNode' to reconnect later.
        ListNode nextNode = rightNode;

        // Reverse the sublist between 'left' and 'right'.
        ListNode reversedSublistHead = reverseList(prevLeft.next, rightNode);

        // Reconnect the reversed sublist with the original list.
        prevLeft.next = reversedSublistHead;
        while (reversedSublistHead.next != null) {
            reversedSublistHead = reversedSublistHead.next;
        }
        reversedSublistHead.next = nextNode;

        return dummy.next;
    }

    private ListNode reverseList(ListNode head, ListNode tail) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != tail) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        // After the loop, 'prev' will be the new head of the reversed list.
        return prev;
    }
}
