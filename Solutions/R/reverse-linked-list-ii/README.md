# Reverse linked list ii

[Problem link](https://leetcode.com/problems/reverse-linked-list-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-linked-list-ii

class Solution {
 public:
  ListNode* reverseBetween(ListNode* head, int left, int right) {
    ListNode dummy(0, head);
    ListNode* n1 = &dummy;
    for (int i = 1; i < left; ++i) n1 = n1->next;
    ListNode *n2 = n1->next, *n3 = n2->next;
    for (int i = left; i < right; ++i) {
      auto temp = n3->next;
      n3->next = n2;
      n2 = n3;
      n3 = temp;
    }
    n1->next->next = n3;
    n1->next = n2;
    return dummy.next;
  }
};
```