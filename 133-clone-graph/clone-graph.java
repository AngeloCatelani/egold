/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
       public HashMap<Integer, Node> map = new HashMap<>();
    public Node cloneGraph(Node node) {
        //going to create a hashmap to store node,val and nodes
        //check if the node is already present in map 
        //if it is there return the node
        //else create a copy of that node
        //then add ithe copynode to map
        //run this for every neighbours of that node
   
        if(node == null)return null;
        if (map.containsKey(node.val)){
            return map.get(node.val);
        }
        Node copyNode = new Node(node.val,new ArrayList<Node>());
        map.put(node.val,copyNode);
        for(Node nei : node.neighbors){
            copyNode.neighbors.add(cloneGraph(nei));
        }
        return copyNode;
    }
}