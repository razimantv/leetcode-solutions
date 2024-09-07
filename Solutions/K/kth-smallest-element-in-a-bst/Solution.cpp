// https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution {
 public:
  pair<int, int> work(TreeNode* root, int k) {
    if (root == NULL) return {0, 0};
    auto l = work(root->left, k);
    if (l.first) return l;
    if (l.second == k - 1) return {1, root->val};
    auto r = work(root->right, k - 1 - l.second);
    if (r.first) return r;
    return {0, l.second + r.second + 1};
  }
  int kthSmallest(TreeNode* root, int k) { return work(root, k).second; }
};
