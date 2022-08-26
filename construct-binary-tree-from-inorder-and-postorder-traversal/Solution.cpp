// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

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
  unordered_map<int, int> in, post;

 public:
  TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder, int is = 0,
                      int ie = -1, int ps = 0, int pe = -1) {
    if (ie == -1) {
      if (inorder.empty())
        return NULL;
      else if (inorder.size() == 1) {
        return new TreeNode(inorder[0]);
      }
      ie = pe = inorder.size() - 1;
      in.clear();
      post.clear();
      for (int i = is; i <= ie; ++i) {
        in[inorder[i]] = post[postorder[i]] = i;
      }
    }

    TreeNode* ret = new TreeNode(postorder[pe]);
    int ip = in[ret->val];
    if (ip > is) {
      ret->left =
          buildTree(inorder, postorder, is, ip - 1, ps, ps + ip - is - 1);
    }
    if (ip < ie) {
      ret->right =
          buildTree(inorder, postorder, ip + 1, ie, pe + ip - ie, pe - 1);
    }
    return ret;
  }
};
