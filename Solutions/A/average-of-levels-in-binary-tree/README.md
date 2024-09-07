# Average of levels in binary tree

[Problem link](https://leetcode.com/problems/average-of-levels-in-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/average-of-levels-in-binary-tree

class Solution {
 public:
  vector<double> tot;
  vector<int> cnt;

  vector<double> averageOfLevels(TreeNode* root, int level = 0) {
    if (root == nullptr) return {};
    if (tot.size() == level)
      tot.push_back(root->val), cnt.push_back(1);
    else
      tot[level] += root->val, ++cnt[level];
    averageOfLevels(root->left, level + 1);
    averageOfLevels(root->right, level + 1);

    if (level == 0) {
      for (int i = 0, n = tot.size(); i < n; ++i) tot[i] /= cnt[i];
      return tot;
    } else
      return {};
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Averaging from total and count](/Collections/averaging-from-total-and-count.md#averaging-from-total-and-count)
