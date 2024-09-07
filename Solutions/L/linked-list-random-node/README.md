# Linked list random node

[Problem link](https://leetcode.com/problems/linked-list-random-node)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/linked-list-random-node

class Solution {
 public:
  /** @param head The linked list's head.
      Note that the head is guaranteed to be not null, so it contains at least
     one node. */

  ListNode *l;
  int N;
  Solution(ListNode *head) {
    l = head;
    N = 0;
    while (head != nullptr) ++N, head = head->next;
  }

  /** Returns a random node's value. */
  int getRandom() {
    ListNode *c = l;
    int x = rand() % N;
    while (x--) c = c->next;
    return c->val;
  }
};

```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
