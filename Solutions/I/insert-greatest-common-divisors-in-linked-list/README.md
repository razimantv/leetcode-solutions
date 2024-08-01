# Insert greatest common divisors in linked list

[Problem link](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class Solution {
 public:
  ListNode* insertGreatestCommonDivisors(ListNode* head) {
    ListNode *next = head->next, *ret = head;
    while (next) {
      head->next = new ListNode(gcd(head->val, next->val), next);
      head = next;
      next = next->next;
    }
    return ret;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
