/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    let l = null;
    let r = null;
    let curr = head;
    while(curr){
        if(r){
            r = r.next;
        }
        if(k === 1){
            l = curr
            r = head
        }
        k--;
        curr = curr.next;
    }
    [l.val,r.val] = [r.val,l.val];
    return head
};