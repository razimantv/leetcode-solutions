// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii


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
