def dfs(matrix):
    # 1. Check for an empty graph.
    if not matrix:
        return []

    # 2. Initialize
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        # a. Check if visited
        if (i, j) in visited:
            return
		# b. Else add to visted
        visited.add((i, j))

        # c. Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # d. Add in your question-specific checks.
                traverse(next_i, next_j)

    # 3. For each point, traverse it.
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

This is a DFS Template to solve matrix questions:

def dfs(matrix):
    # 1. Check for an empty graph.
    if not matrix:
        return []

    # 2. Initialize
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        # a. Check if visited
        if (i, j) in visited:
            return
		# b. Else add to visted
        visited.add((i, j))

        # c. Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # d. Add in your question-specific checks.
                traverse(next_i, next_j)

    # 3. For each point, traverse it.
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
Use this template to addess the problem:

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not matrix:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)
Your runtime beats 98.84 % of python3 submissions

Complexity Analysis:
Time Complexity: since we keep a visited set for each ocean, we only visit a cell if it is not visited before. For each ocean, the worst case is mn thus totally O(mn)

Space Complexity: O(2mn + h) = O(mn).

For each DFS we need O(h) space used by the system stack, where h is the maximum depth of the recursion. In the worst case, O(h) = O(m*n).
Each visited set can have at maximum all cells from the matrix so O(mn). Two ocean means O(2mn).
329. Longest Increasing Path in a Matrix

Solution using the above template (LTE):

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Check edge case
        if not matrix:
            return 0

        # Initialize
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        visited = set()
        res = 0

        def dfs(i, j, visited):
            # Check if visited
            if (i, j) in visited:
                return 0
			visited.add((i, j))
            res = 1

            # work with neighbors
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]

                # for each direction we try to find a new count
                direction_count = 0
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[i][j] < matrix[next_i][next_j]:
                        direction_count = 1 + dfs(next_i, next_j, visited)

                res = max(direction_count, res)

            return res

        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col, visited), res)

        return res
Time Complexity: O(mn*mn)

Template with Memoization

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Check edge case
        if not matrix:
            return 0

        # Initialize
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        memo = [[-1] * cols for _ in range(rows)]
        res = 0

        def dfs(i, j, visited):
            # Check if visited
            if memo[i][j] != -1:
                return memo[i][j]

            res = 1

            # work with neighbors
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]

                # for each direction we try to find a new count
                direction_count = 0
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[i][j] < matrix[next_i][next_j]:
                        direction_count = 1 + dfs(next_i, next_j, visited)

                res = max(direction_count, res)

            memo[i][j] = res
            return res

        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col, memo), res)

        return res
Complexity Analysis:
Time Complexity: O(mn) each cell is visited once.

Space Complexity: O(mn + h) = O(mn).

For each DFS we need O(h) space used by the system stack, where h is the maximum depth of the recursion. In the worst case, O(h) = O(m*n).
Each visited set can have at maximum all cells from the matrix so 