// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

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
  int best(TreeNode* root, int l, int r) {
    int ret = max(root->val - l, r - root->val);

    l = min(l, root->val);
    r = max(r, root->val);
    if (root->left != nullptr) ret = max(ret, best(root->left, l, r));
    if (root->right != nullptr) ret = max(ret, best(root->right, l, r));
    return ret;
  }
  int maxAncestorDiff(TreeNode* root) {
    return best(root, root->val, root->val);
  }
};
