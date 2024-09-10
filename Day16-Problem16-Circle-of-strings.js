/*
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first character of Y. If every string of the array can be chained with exactly two strings of the array(one with the first character and the second with the last character of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"

Examples

Input: arr[] = ["abc", "bcd", "cdf"]
Output: 0
Explaination: These strings can't form a circle because no string has 'd'at the starting index.

Input: arr[] = ["ab" , "bc", "cd", "da"]
Output: 1
Explaination: These strings can form a circle of strings.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints: 
1 ≤ length of strings ≤ 20
*/
class Solution {
    isCircle(arr) {
        let n = arr.length;
        if (n === 0) return 0;
        
        let adjList = new Array(26).fill(0).map(() => []);
        let inDegree = new Array(26).fill(0);
        let outDegree = new Array(26).fill(0);
        
        // Build the graph and count in-degree and out-degree
        for (let str of arr) {
            let first = str.charCodeAt(0) - 97;
            let last = str.charCodeAt(str.length - 1) - 97;
            adjList[first].push(last);
            outDegree[first]++;
            inDegree[last]++;
        }
        
        // Check if in-degree equals out-degree for each character
        for (let i = 0; i < 26; i++) {
            if (inDegree[i] !== outDegree[i]) {
                return 0;
            }
        }
        
        // Perform a DFS to check if the graph is strongly connected
        let visited = new Array(26).fill(false);
        
        // Find the first node with outgoing edges
        let start = -1;
        for (let i = 0; i < 26; i++) {
            if (outDegree[i] > 0) {
                start = i;
                break;
            }
        }
        
        if (start === -1) return 0;  // No outgoing edges, not a valid circle
        
        // Run DFS from the first node with an outgoing edge
        this.dfs(start, adjList, visited);
        
        // Check if all nodes with outgoing edges are visited
        for (let i = 0; i < 26; i++) {
            if (outDegree[i] > 0 && !visited[i]) {
                return 0;
            }
        }
        
        return 1;
    }
    
    // DFS function
    dfs(node, adjList, visited) {
        visited[node] = true;
        for (let neighbor of adjList[node]) {
            if (!visited[neighbor]) {
                this.dfs(neighbor, adjList, visited);
            }
        }
    }
}
