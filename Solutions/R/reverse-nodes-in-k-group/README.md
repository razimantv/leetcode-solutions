# Reverse nodes in k group

[Problem link](https://leetcode.com/problems/reverse-nodes-in-k-group)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-nodes-in-k-group

class Solution {
 public:
  ListNode* reverseKGroup(ListNode* head, int k) {
    if (k == 1) return head;

    ListNode dummy(0, head);
    ListNode *cur = &dummy, temp;
    while (1) {
      auto temp = cur->next;
      for (int i = 0; i < k; ++i, temp = temp->next)
        if (!temp) return dummy.next;

      ListNode *f = cur->next, *l = f;
      for (int i = 1; i < k; ++i) {
        temp = l->next->next;
        l->next->next = f;
        f = l->next;
        l->next = temp;
      }

      cur->next = f;
      cur = l;
    }
    return dummy.next;
  }
};
```