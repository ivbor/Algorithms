import matplotlib.pyplot as plt
import matplotlib.animation as animation


class KnapsackProblem:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(weights)
        self.dp = [[0] * (self.capacity + 1)
                   for _ in range(self.num_items + 1)]

    def solve(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        # Adjust window size for larger display

        # Create a table with headers for weights and values
        headers = [f'W={w}' for w in range(self.capacity + 1)]
        rows = [f'Item {i}\n(w={self.weights[i]}, v={self.values[i]})'
                for i in range(self.num_items)]

        # Initialize table data with headers intact
        table_data = [[''] * (self.capacity + 1)
                      for _ in range(self.num_items)]
        for r in range(self.num_items):
            table_data[r] = [0] * (self.capacity + 1)

        ax.axis('tight')
        ax.axis('off')
        table_plot = ax.table(
            cellText=table_data,
            rowLabels=rows,
            colLabels=headers,
            loc='center',
            cellLoc='center',
        )

        # Increase font size and cell size for better visibility
        table_plot.auto_set_font_size(False)
        table_plot.set_fontsize(7)
        table_plot.scale(0.8, 1.5)  # Scale up the table

        def update(frame):
            i, w = frame
            if self.weights[i - 1] <= w:
                self.dp[i][w] = max(self.dp[i - 1][w],
                                    self.dp[i - 1][w - self.weights[i - 1]]
                                    + self.values[i - 1])
            else:
                self.dp[i][w] = self.dp[i - 1][w]

            # Update table cells (avoid updating headers)
            for r in range(1, self.num_items + 1):
                # Skip the first row (header)
                for c in range(self.capacity + 1):
                    # Skip the first column (header)
                    table_plot[(r, c)].get_text().set_text(f"{self.dp[r][c]}")
                    table_plot[(r, c)].set_facecolor("white")

            # Highlight the current cell
            table_plot[(i, w)].set_facecolor("yellow")
            ax.set_title(f"Knapsack Capacity: {w}, Item: {i}", fontsize=14)

        frames = [(i, w) for i in range(1, self.num_items + 1)
                  for w in range(self.capacity + 1)]
        animation.FuncAnimation(
            fig, update, frames=frames, repeat=False)
        plt.show()


# Input data
weights = [2, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 16
knapsack = KnapsackProblem(weights, values, capacity)
knapsack.solve()
