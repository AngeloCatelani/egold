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
        // Create a dummy node and link it to the head of the input list.
        ListNode dummy = new ListNode(0, head);
        
        // Create a pointer 'prev' initialized to the dummy node.
        ListNode prev = dummy;
        
        // Create a pointer 'curr' initialized to the head of the input list.
        ListNode curr = head;
        
        // Iterate through the list as long as there are at least two nodes to swap.
        while (curr != null && curr.next != null) {
            // Save pointers to the next pair and the second node in the pair.
            ListNode nextPair = curr.next.next;
            ListNode second = curr.next;

            // Reverse the pair by updating the next pointers.
            second.next = curr;
            curr.next = nextPair;
            prev.next = second;

            // Update the 'prev' and 'curr' pointers for the next iteration.
            prev = curr;
            curr = nextPair;
        }
        
        // Return the next node of the dummy node, which represents the new head of the modified list.
        return dummy.next;
    }
}
