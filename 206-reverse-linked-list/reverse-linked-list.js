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
var reverseList = function(head) {
   let prev = null;
    let curr = head;

    while (curr) {
        let nextTemp = curr.next; // Save next
        curr.next = prev;         // Reverse the link
        prev = curr;              // Move prev up
        curr = nextTemp;          // Move to next node
    }

    return prev; // New head of the reversed list
};