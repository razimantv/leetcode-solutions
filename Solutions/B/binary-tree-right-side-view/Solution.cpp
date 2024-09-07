// https://leetcode.com/problems/binary-tree-right-side-view

class Solution {
 public:
  vector<int> tree;
  vector<int> rightSideView(TreeNode* root, int level = 0) {
    if (root == nullptr) return {};

    if (tree.size() <= level)
      tree.push_back(root->val);
    else
      tree[level] = root->val;
    rightSideView(root->left, level + 1);
    rightSideView(root->right, level + 1);

    return level ? vector<int>() : tree;
  }
};
