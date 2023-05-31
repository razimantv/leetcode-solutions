# Odd even linked list

[Problem link](https://leetcode.com/problems/odd-even-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/odd-even-linked-list

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
  ListNode* oddEvenList(ListNode* head) {
    if (head == NULL or head->next == NULL) return head;
    ListNode *oddhead = head, *oddtail = head, *evenhead = head->next,
             *eventail = head->next;
    while (1) {
      if (eventail->next == NULL) return head;
      oddtail->next = eventail->next;
      oddtail = oddtail->next;
      eventail->next = oddtail->next;
      oddtail->next = evenhead;
      if (eventail->next == NULL) return head;
      eventail = eventail->next;
    }
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration)
