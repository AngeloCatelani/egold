public class Solution {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Create a list of lists to represent the adjacency list.
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }
//  System.out.print(adj);[[], []]
        // Add edges to the adjacency list.
        for (int i = 0; i < prerequisites.length; i++) {
            adj.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
// System.out.print(adj);[[], [0]]
        // Create a visited array to track the visited nodes.
        int[] visited = new int[numCourses];
// System.out.print(visited); 1 1
        // Iterate over all the nodes.
        for (int i = 0; i < numCourses; i++) {
            // If the node is not visited, then check if it is part of a cycle.
            if (visited[i] == 0) {
                if (isCyclic(adj, visited, i)) {
                    return false;
                }
            }
        }
        // Print the 'visited' array
for (int i = 0; i < visited.length; i++) {
    System.out.print(visited[i] + " ");
}

// To print a newline at the end for better formatting
System.out.println();
        return true;
    }

    private boolean isCyclic(List<List<Integer>> adj, int[] visited, int curr) {
        // If the node is already visited twice, then there is a cycle.
        if (visited[curr] == 2) {
            return true;
        }

        // Mark the node as being visited twice.
        visited[curr] = 2;

        // Iterate over all the neighbors of the current node.
        for (int neighbor : adj.get(curr)) {
            // If the neighbor is not visited, then recursively check if it is part of a cycle.
            if (visited[neighbor] != 1) {
                if (isCyclic(adj, visited, neighbor)) {
                    return true;
                }
            }
        }
       
        visited[curr] = 1;
        return false;
    }}