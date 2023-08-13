# Double a number represented as a linked list

[Problem link](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class Solution {
 public:
  int work(ListNode* n) {
    int carry{};
    if (n->next) carry = work(n->next);
    n->val = n->val * 2 + carry;
    int ret = n->val / 10;
    n->val %= 10;
    return ret;
  }
  ListNode* doubleIt(ListNode* head) {
    ListNode* dummy = new ListNode(0, head);
    work(dummy);
    return dummy->val ? dummy : head;
  }
};
```
## Tags

* [Linked list](/README.md#Linked_list) > [Recursion](/README.md#Linked_list-Recursion)
