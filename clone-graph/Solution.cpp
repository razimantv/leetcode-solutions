// https://leetcode.com/problems/clone-graph

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
  unordered_map<int, Node*> cache;

 public:
  Node* cloneGraph(Node* node) {
    if (node == NULL) return NULL;
    Node* ret = new Node(node->val);
    cache[node->val] = ret;
    for (auto next : node->neighbors) {
      if (!cache.count(next->val))
        next = cloneGraph(next);
      else
        next = cache[next->val];
      ret->neighbors.push_back(next);
    }
    return ret;
  }
};
