# Merge k sorted lists

[Problem link](https://leetcode.com/problems/merge-k-sorted-lists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-k-sorted-lists

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

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Sorting](/Collections/sorting.md#sorting) > [Merge sort](/Collections/sorting.md#merge-sort)
* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
