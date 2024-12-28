import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LongestCommonSubsequence:
    def __init__(self, str1, str2):
        # Initialize the strings, lengths, and a DP table
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)
        self.dp = [[0 for i in range(self.n)] for _ in range(self.m)]

    def solve(self):
        # Prepare the figure and axis
        fig, ax = plt.subplots()
        table = np.zeros((self.m, self.n), dtype=int)
        ax.axis('tight')
        ax.axis('off')
        # Create a table visualization component
        table_plot = ax.table(
            cellText=table.astype(str),  # Initialize with zeros in string format
            rowLabels=list(self.str1),  # Empty label at start for row labels
            colLabels=list(self.str2),  # Empty label at start for column labels
            loc="center",
            cellLoc="center",
        )
        # Create frames for animation representing each cell processing step
        frames = [(i, j) for i in range(self.m) for j in range(self.n)]

        def update(frame):
            # Extract frame coordinates
            i, j = frame
            # Update DP table based on LCS logic
            if self.str1[i - 1] == self.str2[j - 1]:
                self.dp[i][j] = self.dp[i - 1][j - 1] + 1
            else:
                self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])

            # Update the table cells for the visualization
            for x in range(self.m):
                for y in range(self.n):
                    # Update cell text with current DP table value
                    table_plot[x + 1, y].get_text().set_text(str(self.dp[x][y]))
                    # Reset cell color to white
                    table_plot[x + 1, y].set_facecolor("white")
            
            # Highlight the currently processed cell in the table
            table_plot[i + 1, j].set_facecolor("yellow")
            # Update the title to show the characters being compared
            ax.set_title(f"Comparing: '{self.str1[i]}' and '{self.str2[j]}'")

        # Create an animation object
        ani = animation.FuncAnimation(fig, update, frames=frames, repeat=False)
        # Display the visualization
        plt.show()

# Example usage
str1 = "helloworld"
str2 = "playword"
lcs = LongestCommonSubsequence(str1, str2)
lcs.solve()
