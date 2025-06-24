class CellAutomaton:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_initial_state(self, state_matrix):
        self.grid = state_matrix

    def count_neighbors(self, row, col):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def step(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                if neighbors == 1:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
        self.grid = new_grid
