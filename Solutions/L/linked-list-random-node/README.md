# Linked list random node

[Problem link](https://leetcode.com/problems/linked-list-random-node)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/linked-list-random-node

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

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
