// https://leetcode.com/problems/delete-node-in-a-bst

class Solution {
 public:
  TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == NULL) return NULL;
    if (key < root->val) {
      root->left = deleteNode(root->left, key);
      return root;
    }
    if (key > root->val) {
      root->right = deleteNode(root->right, key);
      return root;
    }

    if (root->left == NULL)
      return root->right;
    else if (root->right == NULL)
      return root->left;

    TreeNode* cur = root->left;
    while (cur->right != NULL) cur = cur->right;
    cur->right = root->right;

    return root->left;
  }
};
