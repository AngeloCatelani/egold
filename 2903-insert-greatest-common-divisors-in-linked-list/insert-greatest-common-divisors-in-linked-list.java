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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode current = head;
        while (current != null && current.next != null) {
            int newNodeVal = gcd(current.val, current.next.val);
            ListNode newNode = new ListNode(newNodeVal); // Create a new node with the GCD value
            newNode.next = current.next; // Link the new node to the current node's next
            current.next = newNode; // Link the current node to the new node
            current = newNode.next; // Move to the node after the new one
        }
        return head;
    }

    private int gcd(int a,int b){
      
        // Find Minimum of a and b
        int result = Math.min(a, b);
        while (result > 0) {
            if (a % result == 0 && b % result == 0) {
                break;
            }
            result--;
        }
 
        // Return gcd of a and b
        return result;

 
    }
}