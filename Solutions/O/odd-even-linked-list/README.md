# Odd even linked list

[Problem link](https://leetcode.com/problems/odd-even-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/odd-even-linked-list

class Solution {
 public:
  ListNode* oddEvenList(ListNode* head) {
    if (head == NULL or head->next == NULL) return head;
    ListNode *oddhead = head, *oddtail = head, *evenhead = head->next,
             *eventail = head->next;
    while (1) {
      if (eventail->next == NULL) return head;
      oddtail->next = eventail->next;
      oddtail = oddtail->next;
      eventail->next = oddtail->next;
      oddtail->next = evenhead;
      if (eventail->next == NULL) return head;
      eventail = eventail->next;
    }
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
