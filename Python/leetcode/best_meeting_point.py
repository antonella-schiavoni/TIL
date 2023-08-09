"""
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
Example 2:

Input: grid = [[1,1]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
There will be at least two friends in the grid.
"""


def minTotalDistance(grid):
    if not grid or not grid[0]:
        return 0

    homes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                homes.append((i, j))

    homes.sort(key=lambda x: x[0])  # Sorting by x-coordinate
    median_x = homes[len(homes) // 2][0]

    homes.sort(key=lambda x: x[1])  # Sorting by y-coordinate
    median_y = homes[len(homes) // 2][1]

    return sum(abs(x - median_x) + abs(y - median_y) for x, y in homes)


if __name__ == '__main__':
    # Example
    grid = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    print(minTotalDistance(grid))  # This will print 6
