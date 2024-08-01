# Remove linked list elements

[Problem link](https://leetcode.com/problems/remove-linked-list-elements)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-linked-list-elements

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
  ListNode* removeElements(ListNode* head, int val) {
    if (head == NULL) return head;
    head->next = removeElements(head->next, val);
    return (head->val == val) ? head->next : head;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Recursion](/Collections/linked-list.md#recursion)
