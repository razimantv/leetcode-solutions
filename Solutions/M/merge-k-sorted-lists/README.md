# Merge k sorted lists

[Problem link](https://leetcode.com/problems/merge-k-sorted-lists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-k-sorted-lists

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
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode head, *tail = &head;
    auto cmp = [](const ListNode* n1, const ListNode* n2) {
      return n1->val < n2->val;
    };
    multiset<ListNode*, decltype(cmp)> m(cmp);
    for (auto n : lists)
      if (n) m.insert(n);
    while (!m.empty()) {
      auto n = *m.begin();
      m.erase(m.begin());
      tail->next = n;
      tail = n;
      if (n->next) m.insert(n->next);
    }
    tail->next = nullptr;
    return head.next;
  }
};
```
## Tags

* [Sorting](/README.md#Sorting) > [Custom](/README.md#Sorting-Custom)
* [Priority queue](/README.md#Priority_queue)
* [Sorting](/README.md#Sorting) > [Merge sort](/README.md#Sorting-Merge_sort)
* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration)
