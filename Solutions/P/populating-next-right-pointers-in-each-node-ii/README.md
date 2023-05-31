# Populating next right pointers in each node ii

[Problem link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

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
  Node* connect(Node* root) {
    if (root == NULL) return root;
    for (vector<Node*> n{root}, n2; !n.empty(); n = n2, n2.clear()) {
      for (Node* next = NULL; !n.empty(); next = n.back(), n.pop_back()) {
        auto x = n.back();
        x->next = next;
        if (x->right != NULL) n2.push_back(x->right);
        if (x->left != NULL) n2.push_back(x->left);
      }
      reverse(n2.begin(), n2.end());
    }
    return root;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Iteration](/README.md#Tree-Binary_tree-Iteration)
