class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        # Calculate the length of the machines list.
        machine_count = len(machines)

        # Compute total dresses and the expected dresses per machine, along with a remainder.
        total_dresses, remainder = divmod(sum(machines), machine_count)

        # If there is a remainder, we can't equally distribute dresses to all machines.
        if remainder:
            return -1

        # Initialize variables for the answer and the running balance.
        max_moves = 0
        balance = 0

        # Iterate over each machine.
        for dresses_in_machine in machines:
            # Calculate the number of dresses to move for this machine to reach the expected count.
            dresses_to_move = dresses_in_machine - total_dresses

            # Increment the balance, which represents the ongoing "debt" or "surplus" from left to right.
            balance += dresses_to_move

            # The maximum number of moves required is the maximum of three values:
            # 1. Current max_moves (the max encountered so far)
            # 2. The absolute balance (as we may need to move dresses across multiple machines)
            # 3. Dresses to move for the current machine (as it may require a lot of adding/removing)
            max_moves = max(max_moves, abs(balance), dresses_to_move)

        # Return the maximum number of moves needed to balance all machines.
        return max_moves