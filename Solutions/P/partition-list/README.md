# Partition list

[Problem link](https://leetcode.com/problems/partition-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-list

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
  ListNode* partition(ListNode* head, int x) {
    ListNode *h1 = new ListNode, *h2 = new ListNode, *c1 = h1, *c2 = h2;
    while (head != nullptr) {
      if (head->val >= x)
        c2->next = head, c2 = c2->next;
      else
        c1->next = head, c1 = c1->next;
      head = head->next;
    }
    c1->next = h2->next;
    c2->next = nullptr;
    return h1->next;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
