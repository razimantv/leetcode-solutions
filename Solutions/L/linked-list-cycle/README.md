# Linked list cycle

[Problem link](https://leetcode.com/problems/linked-list-cycle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/linked-list-cycle

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  bool hasCycle(ListNode *head) {
    ListNode *fast = head;
    while (1) {
      if (fast == nullptr or fast->next == nullptr) return false;
      fast = fast->next->next;
      head = head->next;
      if (fast == head) return true;
    }
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration) > [Slow and fast pointers](/README.md#Linked_list-Iteration-Slow_and_fast_pointers)
