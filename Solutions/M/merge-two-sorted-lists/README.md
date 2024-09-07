# Merge two sorted lists

[Problem link](https://leetcode.com/problems/merge-two-sorted-lists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-two-sorted-lists

class Solution {
 public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode *ret = new ListNode, *cur = ret;
    while (l1 != nullptr or l2 != nullptr) {
      if (l1 == nullptr) {
        cur->next = l2;
        l2 = l2->next;
      } else if (l2 == nullptr or l1->val < l2->val) {
        cur->next = l1;
        l1 = l1->next;
      } else {
        cur->next = l2;
        l2 = l2->next;
      }
      cur = cur->next;
    }
    return ret->next;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Merge sort](/Collections/sorting.md#merge-sort)
* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
