// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

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
  TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned,
                          TreeNode* target) {
    if (original == nullptr)
      return original;
    else if (original == target)
      return cloned;
    auto ret = getTargetCopy(original->left, cloned->left, target);
    if (ret != nullptr) return ret;
    return getTargetCopy(original->right, cloned->right, target);
  }
};
