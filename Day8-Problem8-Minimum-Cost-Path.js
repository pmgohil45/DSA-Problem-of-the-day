/*
Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

Examples :

Input: grid = {{9,4,9,9},{6,7,6,4},{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10

The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.

Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7

The minimum cost is- 4 + 3 + 7 = 14.

Expected Time Complexity: O(n2*log(n))
Expected Auxiliary Space: O(n2) 

Constraints:
   1 ≤ n ≤ 500
   1 ≤ cost of cells ≤ 500
*/

// Solve Using JavaScript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    // Helper function to swap elements at two indices
    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    // Function to get the parent index
    parent(i) {
        return Math.floor((i - 1) / 2);
    }

    // Function to get the left child index
    left(i) {
        return 2 * i + 1;
    }

    // Function to get the right child index
    right(i) {
        return 2 * i + 2;
    }

    // Function to insert a new element into the heap
    insert(key) {
        this.heap.push(key);
        let index = this.heap.length - 1;

        // Heapify up
        while (index !== 0 && this.heap[this.parent(index)][0] > this.heap[index][0]) {
            this.swap(index, this.parent(index));
            index = this.parent(index);
        }
    }

    // Function to remove and return the smallest element (the root) from the heap
    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapify(0);

        return root;
    }

    // Function to heapify down the element at index i
    heapify(i) {
        const left = this.left(i);
        const right = this.right(i);
        let smallest = i;

        if (left < this.heap.length && this.heap[left][0] < this.heap[smallest][0]) {
            smallest = left;
        }

        if (right < this.heap.length && this.heap[right][0] < this.heap[smallest][0]) {
            smallest = right;
        }

        if (smallest !== i) {
            this.swap(i, smallest);
            this.heapify(smallest);
        }
    }

    // Check if the heap is empty
    isEmpty() {
        return this.heap.length === 0;
    }
}

class Solution {
    // Function to return the minimum cost to reach the bottom-right cell from top-left cell.
    minimumCostPath(grid, n) {
        // Directions for the four possible moves (right, left, down, up)
        const directions = [
            [0, 1],  // Right
            [0, -1], // Left
            [1, 0],  // Down
            [-1, 0]  // Up
        ];

        // Initialize the min-heap
        const pq = new MinHeap();
        pq.insert([grid[0][0], 0, 0]);  // Starting from the top-left corner

        // Distance matrix to store the minimum cost to reach each cell
        const dist = Array.from({ length: n }, () => Array(n).fill(Infinity));
        dist[0][0] = grid[0][0];

        // Loop until the queue is empty
        while (!pq.isEmpty()) {
            const [cost, x, y] = pq.extractMin();

            // If we have reached the bottom-right cell, return the cost
            if (x === n - 1 && y === n - 1) {
                return cost;
            }

            // Check all possible directions (up, down, left, right)
            for (const [dx, dy] of directions) {
                const nx = x + dx;
                const ny = y + dy;

                // Check if the new position is within the bounds of the grid
                if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                    const newCost = cost + grid[nx][ny];

                    // If a cheaper path is found, update the distance matrix and push to priority queue
                    if (newCost < dist[nx][ny]) {
                        dist[nx][ny] = newCost;
                        pq.insert([newCost, nx, ny]);
                    }
                }
            }
        }

        // Return the cost to reach the bottom-right cell
        return dist[n - 1][n - 1];
    }
}

// Solve Using Python
/*

import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        
        # Directions for up, down, left, right moves
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority queue to store the cells with their accumulated cost
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))  # (cost, x, y)
        
        # Distance matrix to store minimum cost to reach each cell
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        
        # While there are cells to process
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we have reached the bottom-right corner
            if x == n - 1 and y == n - 1:
                return cost
            
            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    # If a cheaper cost path is found, update and push to queue
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        # Return the minimum cost to reach bottom-right cell
        return dist[n - 1][n - 1]

*/
