/*
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid = [[0,1],[1,0],[1,1],[1,0]]
Output: 1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.

Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
Output: 2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 2 0 
There are two islands in the grid. One island is marked by '1' and the other by '2'.

Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
0 ≤ grid[i][j] ≤ 1Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid = [[0,1],[1,0],[1,1],[1,0]]
Output: 1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.

Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
Output: 2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 2 0 
There are two islands in the grid. One island is marked by '1' and the other by '2'.

Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'0', '1'}
*/

// Back-end complete function Template for javascript

/**
 * @param {string[][]} grid
 * @returns {number}
*/
class Solution {
    isValid(x, y, n, m) { return (x >= 0 && x < n && y >= 0 && y < m); }

    // Function to find the number of islands.
    numIslands(grid) {
        // these lists are used to get row and column numbers of 8
        // neighbours of a given cell.
        let dx = new Array(-1, 0, 1, 0, 1, -1, -1, 1);
        let dy = new Array(0, -1, 0, 1, 1, 1, -1, -1);

        let n = grid.length;
        let m = grid[0].length;

        // boolean array to mark visited cells.
        // initially all cells are unvisited.
        let vis = new Array(n);
        for (let i = 0; i < n; i++) {
            vis[i] = new Array(m);
            vis[i].fill(false);
        }

        // using queue for BFS.
        let q = new Array();
        let ans = 0;
        let f = 0;

        // traversing over all cells of given matrix.
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                // if cell is unvisited and grid value is 1, we increment the
                // count and mark it as visited.
                if (!vis[i][j] && grid[i][j] == '1') {
                    ans++;
                    vis[i][j] = true;

                    // pushing it into the queue.
                    q.push(new Array(i, j));
                    while (q.length > f) {
                        let x = q[f][0];
                        let y = q[f][1];
                        f++;
                        for (let k = 0; k < 8; k++) {
                            // if row and column number is in range, grid value
                            // is 1 and cell is not yet visited,
                            if (this.isValid(x + dx[k], y + dy[k], n, m) &&
                                !vis[x + dx[k]][y + dy[k]] &&
                                grid[x + dx[k]][y + dy[k]] == '1') {
                                // we push the cell in queue and mark it
                                // visited.
                                q.push(new Array(x + dx[k], y + dy[k]));
                                vis[x + dx[k]][y + dy[k]] = true;
                            }
                        }
                    }
                }
            }
        }
        // returning the result.
        return ans;
    }
}
