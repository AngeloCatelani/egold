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
    public int getDecimalValue(ListNode head) {
        //have stringbuilder add to it
        //then convert to number
        //then check the binary number to number
        StringBuilder s = new StringBuilder();
        while(head != null){
            s.append(head.val);
            head = head.next;
        }
        // System.out.println(s.toString());
       
        //  System.out.println(number);
         // convert binary string to decimal integer
        int decimalValue = Integer.parseInt(s.toString(), 2);
        
        return decimalValue;
        
    }
}