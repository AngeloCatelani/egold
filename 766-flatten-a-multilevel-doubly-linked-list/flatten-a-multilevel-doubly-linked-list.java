/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/
//  1---2---3---4---5---6--NULL  [Level 0]
//          |
//          7---8---9---10--NULL [Level 1]
//              |
//              11--12--NULL     [Level 2]
class Solution {
   public Node flatten(Node head) {
    if (head == null) {
        return head;
    }
    
    Stack<Node> stack = new Stack<>();
    
    Node dummy = new Node();
    Node res = dummy;
    
    stack.push(head);
    
    while (!stack.isEmpty()) {
        Node current = stack.pop();
        
        if (current.next != null) {
            stack.push(current.next);
        }
        if (current.child != null) {
            stack.push(current.child);
        }
        
        current.prev = dummy;
        current.child = null;
        dummy.next = current;
        dummy = dummy.next;
    }
    
    res.next.prev = null;
    return res.next;
}

}
//Time: we are traversing the LL once → O(N)
// Space: we are creating a new LL with the same number of elements → O(N)