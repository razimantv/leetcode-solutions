# Split linked list in parts

[Problem link](https://leetcode.com/problems/split-linked-list-in-parts)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/split-linked-list-in-parts

class Solution {
 public:
  vector<ListNode*> splitListToParts(ListNode* head, int k) {
    if (k == 1)
      return {head};
    else if (!head)
      return vector<ListNode*>(k);

    ListNode* dummy = head;
    int N = 0;
    while (dummy) ++N, dummy = dummy->next;

    vector<ListNode*> ret;
    while (k) {
      int cur = N / k;
      if (N % k) ++cur;
      ret.push_back(head);
      for (int i = 1; i < cur; ++i) head = head->next;
      if (head) dummy = head->next, head->next = nullptr, head = dummy;

      --k;
      N -= cur;
    }
    return ret;
  }
};
```