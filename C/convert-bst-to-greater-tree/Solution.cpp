// https://leetcode.com/problems/convert-bst-to-greater-tree

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
  int pref;
  TreeNode* convertBST(TreeNode* root, int start = 1) {
    if (root == nullptr) return nullptr;
    if (start == 1) pref = 0;
    convertBST(root->right, 0);
    root->val += pref;
    pref = root->val;
    convertBST(root->left, 0);
    return root;
  }
};
