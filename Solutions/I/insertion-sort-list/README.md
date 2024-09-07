# Insertion sort list

[Problem link](https://leetcode.com/problems/insertion-sort-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/insertion-sort-list

class Solution {
 public:
  ListNode *insertionSortList(ListNode *head) {
    if (head == nullptr or head->next == nullptr) return head;
    ListNode *dummy = new ListNode;
    for (ListNode *cur = head; cur != nullptr;) {
      for (ListNode *cur2 = dummy;; cur2 = cur2->next) {
        if (cur2->next == nullptr or cur2->next->val > cur->val) {
          swap(cur->next, cur2->next);
          swap(cur, cur2->next);
          break;
        }
      }
    }
    return dummy->next;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
