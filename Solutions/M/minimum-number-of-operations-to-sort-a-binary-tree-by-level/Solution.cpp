// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class Solution {
 public:
  vector<vector<int>> atdepth;
  void dfs(TreeNode* root, int d) {
    if (atdepth.size() == d) atdepth.push_back({});
    atdepth[d].push_back(root->val);
    if (root->left) dfs(root->left, d + 1);
    if (root->right) dfs(root->right, d + 1);
  }
  int work(vector<int>& row) {
    auto sorted = row;
    sort(sorted.begin(), sorted.end());

    int n = row.size(), ret{};
    for (int& x : row)
      x = lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin();

    for (int i = 0; i < n; ++i) {
      if (row[i] == -1) continue;
      ret -= 2;
      for (int j = row[i]; j != -1;) {
        int nextj = row[j];
        row[j] = -1;
        j = nextj;
        ++ret;
      }
    }
    return ret;
  }
  int minimumOperations(TreeNode* root) {
    dfs(root, 0);
    int ret{};
    for (auto& row : atdepth) ret += work(row);
    return ret;
  }
};
