// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

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
 public:
  vector<int> adj[100001];
  void bfs(TreeNode* root) {
    queue<TreeNode*> bfsq;
    bfsq.push(root);
    while (!bfsq.empty()) {
      auto u = bfsq.front();
      bfsq.pop();
      vector<TreeNode*> vec{u->left, u->right};
      for (auto v : vec) {
        if (v) {
          adj[u->val].push_back(v->val);
          adj[v->val].push_back(u->val);
          bfsq.push(v);
        }
      }
    }
  }

  int dfs2(int u, int par) {
    int d = 0;
    for (int v : adj[u])
      if (v != par) d = max(d, 1 + dfs2(v, u));
    // cout << u << " " << par << " " << d << "\n";
    return d;
  }
  int amountOfTime(TreeNode* root, int start) {
    bfs(root);
    return dfs2(start, -1);
  }
};
