# Merge in between linked lists

[Problem link](https://leetcode.com/problems/merge-in-between-linked-lists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-in-between-linked-lists

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
  ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
    ListNode* l1 = list1;
    for (int i = 1; i < a; ++i) l1 = l1->next;

    swap(l1->next, list2);
    while (l1->next) l1 = l1->next;
    for (int i = a; i < b; ++i) list2 = list2->next;
    l1->next = list2->next;
    return list1;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
