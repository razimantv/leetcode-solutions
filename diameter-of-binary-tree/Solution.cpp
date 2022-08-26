// https://leetcode.com/problems/diameter-of-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
 public:
  pair<int, int> both(TreeNode* root) {
    if (root == NULL) return {0, 0};
    auto l = both(root->left), r = both(root->right);
    return {max(l.first, r.first) + 1,
            max(max(l.second, r.second), l.first + r.first + 1)};
  }
  int diameterOfBinaryTree(TreeNode* root) {
    if (root == NULL) return 0;
    return both(root).second - 1;
  }
};
