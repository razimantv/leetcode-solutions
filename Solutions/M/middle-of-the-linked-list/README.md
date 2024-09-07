# Middle of the linked list

[Problem link](https://leetcode.com/problems/middle-of-the-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/middle-of-the-linked-list

class Solution {
 public:
  ListNode* middleNode(ListNode* head) {
    ListNode *a = head, *b = head->next;
    while (1) {
      if (b == NULL)
        return a;
      else if (b->next == NULL)
        return a->next;
      a = a->next;
      b = b->next->next;
    }
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration) > [Slow and fast pointers](/Collections/linked-list.md#slow-and-fast-pointers)
