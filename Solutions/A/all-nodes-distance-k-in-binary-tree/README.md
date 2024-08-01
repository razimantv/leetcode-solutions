# All nodes distance k in binary tree

[Problem link](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution {
 public:
  int work(TreeNode* root, int target, int k, int godepth, vector<int>& vals) {
    if (!root) return -1;
    int depth = -1;
    if (godepth < 0 and root->val == target) depth = 0, godepth = k;
    if (godepth == 0) {
      vals.push_back(root->val);
      return depth;
    } else if (godepth > 0) {
      work(root->left, target, k, godepth - 1, vals);
      work(root->right, target, k, godepth - 1, vals);
      return depth;
    }
    int child = work(root->left, target, k, godepth, vals);
    if (child >= 0) {
      int depth = child + 1;
      if (depth == k) vals.push_back(root->val);
      if (depth < k) work(root->right, target, k, k - depth - 1, vals);
      return depth;
    }
    child = work(root->right, target, k, godepth, vals);
    if (child >= 0) {
      int depth = child + 1;
      if (depth == k) vals.push_back(root->val);
      if (depth < k) work(root->left, target, k, k - depth - 1, vals);
      return depth;
    }
    return depth;
  }
  vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
    vector<int> ret;
    work(root, target->val, k, -1, ret);
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
