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
// The problem statement is asking you to create a deep copy (clone) of a connected undirected graph. The graph is represented using a custom class called `Node`, which has the following properties:

// - `val`: An integer value associated with each node.
// - `neighbors`: A list of neighboring nodes, which are other nodes that are connected to the current node.

// Here's a step-by-step explanation of the problem:

// 1. You're given a reference to a node in the original graph. This reference will always be the first node with `val = 1`.

// 2. Your task is to create a deep copy of the entire graph, which means duplicating each node and its neighbors while preserving the structure of the graph.

// 3. You should return the reference to the cloned graph, which is essentially a reference to the first node in the cloned graph with `val = 1`.

// 4. The graph is represented in the test case using an adjacency list. An adjacency list is a collection of unordered lists where each list describes the set of neighbors of a node in the graph. In the context of this problem, the adjacency list represents which nodes are connected to each node in the graph.

// For example, consider a simple undirected graph:

// ```
// Original Graph:
// 1 - 2
// |   |
// 4 - 3
// ```

// In this example:

// - Node 1 has neighbors 2, 4.
// - Node 2 has neighbors 1, 3.
// - Node 3 has neighbors 2, 4.
// - Node 4 has neighbors 1, 3.

// Your task is to create a deep copy of this graph while maintaining the same connections:

// ```
// Cloned Graph:
// 1 - 2
// |   |
// 4 - 3
// ```

// To solve this problem, you'll likely need to use a depth-first search (DFS) or breadth-first search (BFS) approach to traverse the original graph and create the corresponding nodes and connections in the cloned graph.

// Once you've created the cloned graph, you return a reference to the first node (with `val = 1`) in the cloned graph.

// The problem often appears on coding challenge platforms like LeetCode, and you're required to implement a solution that can create the cloned graph based on the given adjacency list representation.
class Solution {
    // Create a HashMap to map original nodes to their cloned nodes.
    public HashMap<Integer, Node> map = new HashMap<>();

    // The main function for cloning the graph.
    public Node cloneGraph(Node node) {
        // If the input node is null, return null (base case).
        if (node == null) return null;
        
        // If the cloned node already exists in the map, return it.
        if (map.containsKey(node.val)) return map.get(node.val);
        
        // Create a new cloned node with the same value as the original node.
        Node newNode = new Node(node.val, new ArrayList<Node>());
        
        // Add the new cloned node to the map.
        map.put(node.val, newNode);
        // System.out.print(map);
        // Recursively clone the neighbors of the original node.
        for (Node neighbor : node.neighbors) {
            // Add the cloned neighbor to the neighbors list of the new node.
            newNode.neighbors.add(cloneGraph(neighbor));
        }
        
        // Return the new cloned node.
        return newNode;
    }
}
//hashmap
//old     new
// 1 ->   1
// 2 ->   2
// 4 -> 4
//3 -> 3
