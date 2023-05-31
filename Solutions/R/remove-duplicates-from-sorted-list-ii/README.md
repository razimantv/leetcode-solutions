# Remove duplicates from sorted list ii

[Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

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
  ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr or head->next == nullptr) return head;
    if (head->val != head->next->val) {
      head->next = deleteDuplicates(head->next);
      return head;
    }
    int x = head->val;
    while (head != nullptr and head->val == x) head = head->next;
    return deleteDuplicates(head);
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Recursion](/README.md#Linked_list-Recursion)
