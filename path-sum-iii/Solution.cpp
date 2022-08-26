// https://leetcode.com/problems/path-sum-iii

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
 public:
  unordered_map<int, int> pref;
  Solution() { pref = {{0, 1}}; }
  int pathSum(TreeNode* root, int sum, int cum = 0) {
    if (root == NULL) return 0;
    cum += root->val;
    int ret = pref[cum - sum];
    ++pref[cum];
    if (root->left != NULL) ret += pathSum(root->left, sum, cum);
    if (root->right != NULL) ret += pathSum(root->right, sum, cum);
    --pref[cum];
    return ret;
  }
};
