// https://leetcode.com/problems/n-ary-tree-preorder-traversal

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
 public:
  vector<int> ret;
  vector<int> preorder(Node* root, int start = 1) {
    if (root == nullptr) return {};
    ret.push_back(root->val);
    for (auto n : root->children) preorder(n, 0);
    if (start) return ret;
    return {};
  }
};
