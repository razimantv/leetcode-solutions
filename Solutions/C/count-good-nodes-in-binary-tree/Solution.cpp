// https://leetcode.com/problems/count-good-nodes-in-binary-tree

class Solution {
 public:
  int goodNodes(TreeNode* root, int x = -99999) {
    if (!root) return 0;
    int ret = x <= root->val;
    x = max(x, root->val);
    return ret + goodNodes(root->left, x) + goodNodes(root->right, x);
  }
};
