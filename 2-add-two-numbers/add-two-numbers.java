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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Create a dummy node to represent the head of the resulting linked list.
        ListNode dummy = new ListNode();
        
        // Create a current node pointer initialized to the dummy node.
        ListNode curr = dummy;
        
        // Initialize a variable to store the carry from addition.
        int carry = 0;

        // Iterate through the linked lists until both are null and there is no carry.
        while (l1 != null || l2 != null || carry != 0) {
            // Extract the values of the current nodes (or 0 if null).
            int v1 = (l1 != null) ? l1.val : 0;
            int v2 = (l2 != null) ? l2.val : 0;

            // Calculate the sum of values and the carry for the next iteration.
            int sum = v1 + v2 + carry;
            carry = sum / 10; // Get the carry for the next addition.
            int val = sum % 10; // Get the value to be stored in the new node.

            // Create a new node with the calculated value and attach it to the result list.
            curr.next = new ListNode(val);

            // Move the current pointer to the newly created node.
            curr = curr.next;

            // Move to the next nodes in the input lists if they are not null.
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        // Return the next node of the dummy node, which represents the head of the result list.
        return dummy.next;
    }
}
