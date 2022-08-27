// https://leetcode.com/problems/validate-binary-search-tree

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
  bool isValidBST(TreeNode* root, TreeNode* l = nullptr,
                  TreeNode* r = nullptr) {
    if (l != nullptr and root->val <= l->val) return false;
    if (r != nullptr and root->val >= r->val) return false;
    if (root->left != nullptr and !isValidBST(root->left, l, root))
      return false;
    if (root->right != nullptr and !isValidBST(root->right, root, r))
      return false;
    return true;
  }
};
