# Path sum iii

[Problem link](https://leetcode.com/problems/path-sum-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/path-sum-iii

class Solution {
 public:
  unordered_map<int, int> pref;
  Solution() { pref = {{0, 1}}; }
  int pathSum(TreeNode* root, int sum, int cum = 0) {
    if (root == NULL) return 0;
    cum += root->val;
    int ret = pref[cum - sum];
    ++pref[cum];
    if (root->left != NULL) ret += pathSum(root->left, sum, cum);
    if (root->right != NULL) ret += pathSum(root->right, sum, cum);
    --pref[cum];
    return ret;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
* [Hashmap](/Collections/hashmap.md#hashmap)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
