// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

class Solution {
 public:
  long long kthLargestLevelSum(TreeNode* root, int k) {
    vector<long long> tot;
    function<void(TreeNode*, int)> dfs = [&](TreeNode* root, int level) {
      if (!root) return;
      if (level == tot.size()) tot.push_back({});
      tot[level] += root->val;
      dfs(root->left, level + 1);
      dfs(root->right, level + 1);
    };

    dfs(root, 0);
    if (tot.size() < k) return -1;
    nth_element(tot.begin(), tot.begin() + k - 1, tot.end(),
                greater<long long>());
    return tot[k - 1];
  }
};
