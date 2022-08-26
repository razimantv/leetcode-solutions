// https://leetcode.com/problems/n-ary-tree-level-order-traversal

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
  vector<vector<int>> levelOrder(Node* root) {
    if (!root) return {};

    vector<vector<int>> ret;
    vector<Node*> cur{root};
    while (!cur.empty()) {
      vector<Node*> next;
      ret.push_back({});
      for (auto n : cur) {
        ret.back().push_back(n->val);
        for (auto nn : n->children) next.push_back(nn);
      }
      cur = next;
    }
    return ret;
  }
};
