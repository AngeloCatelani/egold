class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Helper function to calculate Manhattan distance
        def get_distance(i, j, x, y):
            return abs(i - x) + abs(j - y)

        # Perform a Breadth-First Search to find the shortest path
        def bfs(start_i, start_j, dest_i, dest_j):
            # Initialize the priority queue with the starting position
            # and with initial distance as the heuristic
            queue = [(get_distance(start_i, start_j, dest_i, dest_j), start_i, start_j)]
            # Distance dictionary keeps track of steps from the start
            distance = {start_i * column + start_j: 0}
            while queue:
                # Pop the position with lowest estimated cost
                _, curr_i, curr_j = heappop(queue)
                current_step = distance[curr_i * column + curr_j]
                if (curr_i, curr_j) == (dest_i, dest_j):
                    return current_step
                # Check all four adjacent neighbors
                for delta_i, delta_j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    # Validate next position and check if it's a tree
                    if 0 <= next_i < row and 0 <= next_j < column and forest[next_i][next_j] > 0:
                        next_position_key = next_i * column + next_j
                        if next_position_key not in distance or distance[next_position_key] > current_step + 1:
                            distance[next_position_key] = current_step + 1
                            heappush(queue, (distance[next_position_key] + get_distance(next_i, next_j, dest_i, dest_j), next_i, next_j))
            return -1

        row, column = len(forest), len(forest[0])
        # Extract the trees and their positions and sort them based on height
        trees = [(forest[i][j], i, j) for i in range(row) for j in range(column) if forest[i][j] > 1]
        trees.sort()
        current_i = current_j = total_steps = 0

        # Iterate through all trees in sorted order
        for _, target_i, target_j in trees:
            # Get the distance to the next tree
            steps_to_next_tree = bfs(current_i, current_j, target_i, target_j)
            # If a tree can't be reached, return -1
            if steps_to_next_tree == -1:
                return -1
            # Add the steps to the total steps and update current position
            total_steps += steps_to_next_tree
            current_i, current_j = target_i, target_j
        return total_steps