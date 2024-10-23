/*
Given a single linked list, calculate the sum of the last n nodes.

Note: It is guaranteed that n <= number of nodes.

Examples:

Input: Linked List: 5->9->6->3->4->10, n = 3
Output: 17
Explanation: The sum of the last three nodes in the linked list is 3 + 4 + 10 = 17.

Input: Linked List: 1->2, n = 2
Output: 3
Explanation: The sum of the last two nodes in the linked list is 2 + 1 = 3.

Constraints:
1 <= number of nodes, n <= 10^5
1 <= node->data <= 10^3
*/

class Solution {
  public:
    // Function to calculate the sum of the last n nodes in a linked list
    int sumOfLastN_Nodes(struct Node* head, int n) {
        // If n is less than or equal to 0, return 0
        if (n <= 0)
            return 0;

        int sum = 0, temp = 0;
        struct Node *ref_ptr, *main_ptr;
        ref_ptr = main_ptr = head;

        // Calculate the sum of the first n nodes
        while (ref_ptr != NULL && n--) {
            sum += ref_ptr->data;
            ref_ptr = ref_ptr->next;
        }

        // Calculate the sum of the remaining nodes
        while (ref_ptr != NULL) {
            temp += main_ptr->data;
            sum += ref_ptr->data;
            main_ptr = main_ptr->next;
            ref_ptr = ref_ptr->next;
        }

        // Return the sum of the last n nodes
        return (sum - temp);
    }
};
