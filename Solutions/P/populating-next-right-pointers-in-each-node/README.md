# Populating next right pointers in each node

[Problem link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
 public:
  Node* connect(Node* root, Node* next = NULL) {
    if (root == NULL) return root;
    root->next = next;
    if (root->left != NULL) {
      connect(root->left, root->right);
      connect(root->right, next == NULL ? NULL : next->left);
    }
    return root;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
