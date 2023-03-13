// https://leetcode.com/problems/symmetric-tree

class Solution {
 public:
  bool work(TreeNode* n1, TreeNode* n2) {
    if (!n1 and !n2) return true;
    return n1 and n2 and (n1->val == n2->val) and work(n1->left, n2->right) and
           work(n1->right, n2->left);
  }
  bool isSymmetric(TreeNode* root) { return work(root, root); }
};
