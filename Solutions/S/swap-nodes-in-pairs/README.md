# Swap nodes in pairs

[Problem link](https://leetcode.com/problems/swap-nodes-in-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/swap-nodes-in-pairs

class Solution {
 public:
  ListNode* swapPairs(ListNode* head) {
    if (head == nullptr or head->next == nullptr) return head;
    auto n = swapPairs(head->next->next);
    head->next->next = head;
    swap(head->next, n);
    return n;
  }
};
```