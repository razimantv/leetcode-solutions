# Remove nth node from end of list

[Problem link](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-nth-node-from-end-of-list

class Solution {
 public:
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *n1 = head, *n2 = n1;
    for (int i = 0; i < n; ++i) n2 = n2->next;
    if (n2 == nullptr) return n1->next;
    n2 = n2->next;
    while (n2 != nullptr) n1 = n1->next, n2 = n2->next;
    n1->next = n1->next->next;
    return head;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration) > [Slow and fast pointers](/Collections/linked-list.md#slow-and-fast-pointers)
