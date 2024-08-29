/*
Given an array of integers arr, sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.

Examples :

Input: arr[] = [5, 5, 4, 6, 4]
Output: [4, 4, 5, 5, 6]
Explanation: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are the same the smaller element comes first. So 4 4 comes first then comes 5 5. Finally comes 6. The output is 4 4 5 5 6.
Input: arr[] = [9, 9, 9, 2, 5]
Output: [9, 9, 9, 2, 5]
Explanation: The highest frequency here is 3. Element 9 has the highest frequency So 9 9 9 comes first. Now both 2 and 5 have the same frequency. So we print smaller elements first. The output is 9 9 9 2 5.
Expected Time Complexity: O(n*logn)
Expected Space Complexity: O(n)

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i]≤ 105
*/
 java.util.*;

class Solution {
    // Function to sort the array according to frequency of elements.
    public ArrayList<Integer> sortByFreq(int arr[]) {
        // Step 1: Count the frequency of each element
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        // Step 2: Create a list from the map entries
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(frequencyMap.entrySet());
        
        // Step 3: Sort the list based on frequency (descending) and value (ascending)
        Collections.sort(entries, (a, b) -> {
            int freqComparison = b.getValue().compareTo(a.getValue()); // Compare frequencies in descending order
            if (freqComparison == 0) {
                return a.getKey().compareTo(b.getKey()); // Compare values in ascending order if frequencies are the same
            }
            return freqComparison;
        });
        
        // Step 4: Build the result list based on sorted entries
        ArrayList<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : entries) {
            int value = entry.getKey();
            int freq = entry.getValue();
            for (int i = 0; i < freq; i++) {
                result.add(value);
            }
        }
        
        return result;
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] arr1 = {5, 5, 4, 6, 4};
        System.out.println(solution.sortByFreq(arr1)); // Output: [4, 4, 5, 5, 6]

        int[] arr2 = {9, 9, 9, 2, 5};
        System.out.println(solution.sortByFreq(arr2)); // Output: [9, 9, 9, 2, 5]
    }
}
