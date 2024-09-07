# Delete node in a linked list

[Problem link](https://leetcode.com/problems/delete-node-in-a-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-node-in-a-linked-list

class Solution {
 public:
  void deleteNode(ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
