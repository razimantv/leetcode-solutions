// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal

class Solution {
 public:
  int pos;
  vector<int> flip;
  const vector<int> fail{-1}, empty{};
  vector<int> flipMatchVoyage(TreeNode *root, vector<int> &voyage,
                              int start = 1) {
    if (root == nullptr) return {};
    pos = start ? 0 : (pos + 1);
    if (root->val != voyage[pos]) return fail;

    if (root->left == nullptr and root->right == nullptr) return {};
    if (root->left == nullptr) swap(root->left, root->right);
    if (root->left->val != voyage[pos + 1]) {
      swap(root->left, root->right);
      flip.push_back(root->val);
    }
    if (flipMatchVoyage(root->left, voyage, 0) == fail) return fail;
    if (flipMatchVoyage(root->right, voyage, 0) == fail) return fail;
    return start ? flip : empty;
  }
};
