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
    public ListNode mergeKLists(ListNode[] lists) {
        //going to have two function one will do merging and other will send arguments to the merge func
        //have interval start at 1;
        //have a while loop where interval < lists.length
        //and have i=0 i+interval < list.length;i+=interval*2
        //send list[i],lists[i+interval] to the merge fnc
        //in merge func check both list != null
        //then values if l1.val < l2.val => l1.next = merge(l1.next,l2)
        //opp of above statement
            if(lists.length == 0)return null;
      int interval =1;
      while(interval < lists.length){
          for(int i = 0; i+interval < lists.length ; i+=interval*2){
          lists[i]= merge(lists[i],lists[i+interval]);
          }
          interval *=2;
      }
      return lists[0];
      
    }
    private  ListNode merge(ListNode l1,ListNode l2){
        if(l1 == null)return l2;
        if(l2 == null)return l1;
        if(l1.val <= l2.val){
            l1.next = merge(l1.next,l2);
            return l1;
        }
        else{
            l2.next = merge(l1,l2.next);
            return l2;
        }
    }
}