# Copy list with random pointer

[Problem link](https://leetcode.com/problems/copy-list-with-random-pointer)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/copy-list-with-random-pointer


class Solution {
 public:
  unordered_map<Node*, Node*> lookup;

  Node* copyRandomList(Node* head) {
    if (head == nullptr) return head;
    Node* cur = new Node(head->val);
    lookup[head] = cur;
    cur->next = copyRandomList(head->next);
    cur->random = lookup[head->random];
    return cur;
  }
};
```
## Tags

* [Pointers](/Collections/pointers.md#pointers)
* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
