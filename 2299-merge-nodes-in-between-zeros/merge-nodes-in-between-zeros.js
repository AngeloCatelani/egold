/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeNodes = function(head) {
    let dummy = new ListNode(-1);
    let curr = dummy
    let sum = 0;
    head = head.next;
    while(head){
        if(head.val == 0){
            curr.next = new ListNode(sum);
            curr = curr.next;
            sum = 0
        }
        else{
            sum += head.val
        }
        head = head.next;
    }
    return dummy.next;
};