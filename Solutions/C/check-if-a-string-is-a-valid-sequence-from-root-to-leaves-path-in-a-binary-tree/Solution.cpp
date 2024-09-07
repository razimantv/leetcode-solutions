// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree

class Solution {
 public:
  bool work(TreeNode* root, vector<int>& arr, int i) {
    if (root == NULL or root->val != arr[i]) return false;
    if (i + 1 == arr.size()) return root->left == NULL and root->right == NULL;
    return work(root->left, arr, i + 1) or work(root->right, arr, i + 1);
  }
  bool isValidSequence(TreeNode* root, vector<int>& arr) {
    return work(root, arr, 0);
  }
};
