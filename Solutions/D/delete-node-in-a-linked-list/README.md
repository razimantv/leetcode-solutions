# Delete node in a linked list

[Problem link](https://leetcode.com/problems/delete-node-in-a-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-node-in-a-linked-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  void deleteNode(ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration)
