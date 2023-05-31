# Linked list cycle ii

[Problem link](https://leetcode.com/problems/linked-list-cycle-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/linked-list-cycle-ii

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
  ListNode *detectCycle(ListNode *head) {
    if (head == NULL) return NULL;
    ListNode *slow = head, *fast = head;
    do {
      slow = slow->next;
      fast = fast->next;
      if (fast == NULL) return NULL;
      fast = fast->next;
      if (fast == NULL) return NULL;
    } while (slow != fast);
    fast = head;
    while (slow != fast) fast = fast->next, slow = slow->next;
    return slow;
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration) > [Slow and fast pointers](/README.md#Linked_list-Iteration-Slow_and_fast_pointers)
