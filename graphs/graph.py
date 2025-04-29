from collections import deque

class GraphNode:

    def __init__(self, val):
        self.val = val
        self.neighbors = []
    
    def dfs(self, matrix, r, c, visited):
        # base case
        # out of bounds 
        if (r < 0 or c < 0 or
            r == len(matrix) or c == len(matrix[0]) or
            (r, c) in visited or
            matrix[r][c] == 1):
            return 0
        # reached end of matrix
        if r == len(matrix) - 1 and c == len(matrix[0]) - 1:
            return 1
        
        # add to visited
        visited.add((r, c))
        
        # recursively call in all directions
        count = 0
        count += self.dfs(matrix, r - 1, c, visited)
        count += self.dfs(matrix, r + 1, c, visited)
        count += self.dfs(matrix, r, c - 1, visited)
        count += self.dfs(matrix, r, c + 1, visited)

        # remove current cell from visited when backtracking
        visited.remove((r,c))

        return count

    def bfs(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        # set visited and queue
        visited = set()
        queue = deque()
        # add initial coordinates to visited and queue
        visited.add((0,0))
        queue.append((0,0))
        length = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # check if we made it to bottom right of matrix
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # we look in the other directions for neighbors
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                
                for dr, dc in neighbors:
                    # check if out of bounds, has been visited, or has value of 1
                    if (r+dr < 0 or c+dc < 0 or
                        r+dr >= ROWS or c+dc >= COLS or
                        (r+dr,c+dc) in visited or
                        matrix[r+dr][c+dc] == 1
                        ):
                        continue
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
            length += 1 
    
    def build_adj_list(edges):
        adj_list = {}

        for src, dst in edges:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []

            adj_list[src].append(dst)  
        
        return adj_list

    def dfs_adj_list(self, node, target, adj_list, visited):
        # base case 
        if node in visited:
            return 0 
        if node == target:
            return 1
        
        visited.add(node)
        count = 0
        for neighbor in adj_list[node]:
            count += self.dfs_adj_list(neighbor, target, adj_list, visited)
        visited.remove(node)

        return count
    
    def bfs_adj_list(self, node, target, adj_list):
        queue = deque()
        visited = set()
        queue.append(node)
        visited.add(node)

        length = 0 
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return length
                
                for neighbor in adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                
    

        


