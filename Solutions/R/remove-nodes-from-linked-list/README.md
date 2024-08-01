# Remove nodes from linked list

[Problem link](https://leetcode.com/problems/remove-nodes-from-linked-list/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class Solution {
 public:
  pair<int, ListNode*> work(ListNode* node) {
    if (!node) return {0, node};
    auto [val, next] = work(node->next);
    node->next = next;
    if (val > node->val)
      return {val, next};
    else
      return {node->val, node};
  }
  ListNode* removeNodes(ListNode* head) { return work(head).second; }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Recursion](/Collections/linked-list.md#recursion)
