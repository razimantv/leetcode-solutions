# Linked list cycle ii

[Problem link](https://leetcode.com/problems/linked-list-cycle-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/linked-list-cycle-ii

class Solution {
 public:
  ListNode *detectCycle(ListNode *head) {
    if (head == NULL) return NULL;
    ListNode *slow = head, *fast = head;
    do {
      slow = slow->next;
      fast = fast->next;
      if (fast == NULL) return NULL;
      fast = fast->next;
      if (fast == NULL) return NULL;
    } while (slow != fast);
    fast = head;
    while (slow != fast) fast = fast->next, slow = slow->next;
    return slow;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration) > [Slow and fast pointers](/Collections/linked-list.md#slow-and-fast-pointers)
