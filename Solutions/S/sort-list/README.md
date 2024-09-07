# Sort list

[Problem link](https://leetcode.com/problems/sort-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-list

class Solution {
 public:
  ListNode *sortList(ListNode *head, int N = -1, ListNode *end = nullptr,
                     int level = 1) {
    if (head == nullptr or N == 0 or N == 1)
      return head;
    else if (N == -1) {
      ListNode *cur = head;
      N = 1;
      while (cur->next != nullptr) ++N, cur = cur->next;
      if (N == 1) return head;
    }

    ListNode *n1 = head, *n2 = head;
    for (int i = 1; i < N / 2; ++i) n2 = n2->next;
    n2->next = sortList(n2->next, N - N / 2, end, level + 1);
    n2 = n2->next;
    n1 = sortList(n1, N / 2, n2, level + 1);
    ListNode *mid = n2, *cur;

    if (n1->val < n2->val) {
      head = n1;
      n1 = n1->next;
    } else {
      head = n2;
      n2 = n2->next;
    }
    cur = head;

    while (n1 != mid or n2 != end) {
      if (n1 == mid or (n2 != end and n2->val < n1->val))
        cur->next = n2, n2 = n2->next, cur = cur->next;
      else
        cur->next = n1, n1 = n1->next, cur = cur->next;
    }
    cur->next = end;

    return head;
  }
};
```