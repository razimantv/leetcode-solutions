// https://leetcode.com/problems/path-sum-ii

class Solution {
 public:
  vector<int> cur;
  vector<vector<int>> ret;
  vector<vector<int>> pathSum(TreeNode* root, int targetSum, int start = 1) {
    if (start and !root) return {};
    targetSum -= root->val;
    cur.push_back(root->val);
    if (targetSum == 0 and !root->left and !root->right) ret.push_back(cur);
    if (root->left) pathSum(root->left, targetSum, 0);
    if (root->right) pathSum(root->right, targetSum, 0);
    cur.pop_back();
    if (start)
      return ret;
    else
      return {};
  }
};
