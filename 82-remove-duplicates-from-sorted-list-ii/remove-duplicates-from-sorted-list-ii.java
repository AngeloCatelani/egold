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
    public ListNode deleteDuplicates(ListNode head) {
        // Create a dummy node and link it to the head of the input list.
        ListNode dummy = new ListNode(0, head);
        
        // Create a pointer 'prev' initialized to the dummy node.
        ListNode prev = dummy;
        
        // Create a pointer 'curr' initialized to the head of the input list.
        ListNode curr = head;
        
        // Iterate through the list until there are no more nodes to check.
        while (curr != null && curr.next != null) {
            // Check if the current node has a duplicate next node.
            if (curr.val == curr.next.val) {
                // Move 'curr' to the next non-duplicate node.
                while (curr.next != null && curr.val == curr.next.val) {
                    curr = curr.next;
                }
                
                // Update 'prev' to skip the duplicate nodes.
                prev.next = curr.next;
            } else {
                // Move 'prev' and 'curr' to the next nodes.
                prev = prev.next;
            }
            
            // Move 'curr' to the next node.
            curr = curr.next;
        }
        
        // Return the next node of the dummy node, which represents the new head of the modified list.
        return dummy.next;
    }
}
