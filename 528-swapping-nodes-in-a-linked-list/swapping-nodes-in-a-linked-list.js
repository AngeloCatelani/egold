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
   let left = null, right = null, cur = head;

        while (cur) {
            if (right) {
                right = right.next;
            }
            if (k === 1) {
                left = cur;
                right = head;
            }
            k--;
            cur = cur.next;
        }

        [left.val, right.val] = [right.val, left.val];
        return head;
    } 
