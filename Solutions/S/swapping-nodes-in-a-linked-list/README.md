# Swapping nodes in a linked list

[Problem link](https://leetcode.com/problems/swapping-nodes-in-a-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list

class Solution {
 public:
  ListNode* swapNodes(ListNode* head, int k) {
    int n = 0;
    ListNode* cur = head;
    while (cur != nullptr) ++n, cur = cur->next;

    if (n == 2 * k - 1) return head;

    ListNode *node1 = head, *node2 = head;
    for (int i = 0; i < k - 1; ++i) node1 = node1->next;
    for (int i = 0; i < n - k; ++i) node2 = node2->next;

    swap(node1->val, node2->val);
    return head;
  }
};
```