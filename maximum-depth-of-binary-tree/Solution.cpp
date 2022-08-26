// https://leetcode.com/problems/maximum-depth-of-binary-tree

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
  int maxDepth(TreeNode* root) {
    if (root == nullptr) return 0;
    int ret = 1;
    if (root->left != nullptr) ret = max(ret, maxDepth(root->left) + 1);
    if (root->right != nullptr) ret = max(ret, maxDepth(root->right) + 1);
    return ret;
  }
};
