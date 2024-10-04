/*
Given a Circular Linked List. The task is to delete the given node, key in the circular linked list, and reverse the circular linked list.
Note:
  • You don't have to print anything, just return the head of the modified list in each function.
  • Nodes may consist of Duplicate values.
  • The key may or may not be present.
  
Examples:

Input: Linked List: 2 → 5 → 7 → 8 → 10, key = 8
2 → 5 → 7 → 8 → 10
↑________________↓
Output: 10 → 7 → 5 → 2 
Explanation: After deleting 8 from the given circular linked list, it has elements as 2, 5, 7, 10. Now, reversing this list will result in 10, 7, 5, 2 & the resultant list is also circular.

Input: Linked List: 1 → 7 → 8 → 10, key = 8
1 → 7 → 8 → 10
↑____________↓
Output: 10 → 7 → 1
Explanation: After deleting 8 from the given circular linked list, it has elements as 1, 7,10. Now, reversing this list will result in 10, 7, 1 & the resultant list is also circular.

Input: Linked List: 3 → 6 → 4 → 10, key = 9
Output: 10 → 4 → 6 → 3
Explanation: As there no key present in the list, so simply reverse the list & the resultant list is also circular.
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
2 <= number of nodes, key  <= 10^5
1 <= node -> data <= 10^5
*/

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Structure for the linked list node
struct Node {
    int data;
    struct Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

// Function to print nodes in a given circular linked list
void printList(struct Node *head) {
    if (head != NULL) {
        struct Node *temp = head;
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != head);
    } else {
        cout << "empty" << endl;
    }
    cout << endl;
}


// } Driver Code Ends
class Solution {
  public:
    // Function to reverse a circular linked list
    Node* reverse(Node* head) {
        if (head == NULL || head->next == head)
            return head;

        Node* prev = NULL;
        Node* current = head;
        Node* next;
        Node* init = head;

        do {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        } while (current != init);

        head->next = prev;
        head = prev;
        return head;
    }

    // Function to delete a node from the circular linked list
    Node* deleteNode(Node* head, int key) {
        if (head == NULL)
            return head;

        Node* current = head;
        Node* prev = NULL;

        // Finding the node to delete
        while (current->data != key) {
            if (current->next == head) {
                // Node with key not found in the list
                return head;
            }
            prev = current;
            current = current->next;
        }

        // Case 1: Only one node in the list
        if (current == head && current->next == head) {
            head = NULL;
            return head;
        }

        // Case 2: Deleting the head node
        if (current == head) {
            prev = head;
            while (prev->next != head) {
                prev = prev->next;
            }
            head = current->next;
            prev->next = head;
        }
        // Case 3: Deleting the last node
        else if (current->next == head) {
            prev->next = head;
        }
        // Case 4: Deleting a node in between
        else {
            prev->next = current->next;
        }

        return head;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;

        // Reading input into a vector
        while (ss >> number) {
            arr.push_back(number);
        }

        int key;
        cin >> key;
        cin.ignore();

        // Creating the circular linked list
        struct Node *head = new Node(arr[0]);
        struct Node *tail = head;
        for (int i = 1; i < arr.size(); ++i) {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }
        tail->next = head; // Make the list circular

        Solution ob;

        // Delete the node with the given key
        head = ob.deleteNode(head, key);

        // Reverse the circular linked list
        head = ob.reverse(head);

        // Print the modified list
        printList(head);
    }
    return 0;
}

// } Driver Code Ends
