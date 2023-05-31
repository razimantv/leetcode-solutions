# Swap nodes in pairs

[Problem link](https://leetcode.com/problems/swap-nodes-in-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/swap-nodes-in-pairs

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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