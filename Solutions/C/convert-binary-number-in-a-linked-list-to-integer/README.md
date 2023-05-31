# Convert binary number in a linked list to integer

[Problem link](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

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
  int getDecimalValue(ListNode* head) {
    int ret = 0;
    while (head != nullptr) ret = (ret << 1) | head->val, head = head->next;
    return ret;
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Iteration](/README.md#Linked_list-Iteration)
