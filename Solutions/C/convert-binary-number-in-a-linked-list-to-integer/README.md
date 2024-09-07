# Convert binary number in a linked list to integer

[Problem link](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

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

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
