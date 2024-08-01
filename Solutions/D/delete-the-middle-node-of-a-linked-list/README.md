# Delete the middle node of a linked list

[Problem link](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

/** Definition for singly-linked list.
* struct ListNode {
*   int val;
*   ListNode* next;
*   ListNode() : val(0), next(nullptr) {}
*   ListNode(int x) : val(x), next(nullptr) {}
*   ListNode(int x, ListNode* next) : val(x), next(next) {}
};
**/

class Solution {
 public:
  ListNode* deleteMiddle(ListNode* head) {
    if (!head or !head->next) return nullptr;
    ListNode *p1 = head, *p2 = p1->next;
    while (1) {
      if (!p2->next) {
        p1->next = p1->next->next;
        break;
      }
      p2 = p2->next;
      if (!p2->next) {
        p1->next = p1->next->next;
        break;
      }
      p2 = p2->next;
      p1 = p1->next;
    }
    return head;
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration) > [Slow and fast pointers](/Collections/linked-list.md#slow-and-fast-pointers)
