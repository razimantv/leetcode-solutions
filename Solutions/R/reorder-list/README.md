# Reorder list

[Problem link](https://leetcode.com/problems/reorder-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reorder-list

class Solution {
 public:
  void reorderList(ListNode *head) {
    if (head == NULL or head->next == NULL or head->next->next == NULL) return;

    int N = 0;
    ListNode *cur = head;
    do {
      cur = cur->next;
      ++N;
    } while (cur != NULL);

    int M = (N + 1) / 2;
    cur = head;
    for (int i = 1; i < M; ++i) cur = cur->next;

    ListNode *n1 = cur->next, *n2 = n1->next, *temp;
    n1->next = NULL;
    cur->next = NULL;
    while (n2 != NULL) {
      temp = n2->next;
      n2->next = n1;
      n1 = n2;
      n2 = temp;
    }

    n2 = n1;
    n1 = head;
    for (int i = 0; i < M; ++i) {
      if (n2 == NULL) {
        break;
      }
      temp = n2->next;
      n2->next = n1->next;
      n1->next = n2;
      n1 = n2->next;
      n2 = temp;
    }
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
