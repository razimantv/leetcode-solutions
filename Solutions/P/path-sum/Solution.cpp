// https://leetcode.com/problems/path-sum

class Solution {
 public:
  bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    targetSum -= root->val;
    if (!targetSum and !root->left and !root->right) return true;
    return hasPathSum(root->left, targetSum) or
           hasPathSum(root->right, targetSum);
  }
};
