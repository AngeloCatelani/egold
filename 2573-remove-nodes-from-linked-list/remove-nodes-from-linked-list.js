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
var removeNodes = function(head) {
    let stack = [];
        let cur = head;

        while (cur) {
            while (stack.length && cur.val > stack[stack.length - 1]) {
                stack.pop();
            }
            stack.push(cur.val);
            cur = cur.next;
        }

        let dummy = new ListNode();
        cur = dummy;

        for (let num of stack) {
            cur.next = new ListNode(num);
            cur = cur.next;
        }

        return dummy.next;
    }
