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
         ListNode dummy = new ListNode(0, head);
        
        // Create a pointer 'prev' initialized to the dummy node.
        ListNode prev = dummy;
        
        // Create a pointer 'curr' initialized to the head of the input list.
        ListNode curr = head;
        while(curr != null && curr.next != null){
            if(curr.val == curr.next.val){
                while(curr.next != null && curr.val == curr.next.val){
                    curr =curr.next;
                }prev.next =  curr.next;
            }
            else{
                prev = prev.next;
            }
            curr = curr.next;
        }
        return dummy.next;
    }
}