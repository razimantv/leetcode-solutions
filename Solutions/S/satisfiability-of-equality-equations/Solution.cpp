// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
 public:
  vector<int> par;
  int parent(int u) { return (par[u] == u) ? u : (par[u] = parent(par[u])); }
  bool equationsPossible(vector<string>& equations) {
    par.resize(26);
    iota(par.begin(), par.end(), 0);
    for (auto& e : equations) {
      if (e[1] == '!') continue;
      par[parent(e[0] - 'a')] = parent(e[3] - 'a');
    }
    for (auto& e : equations) {
      if (e[1] == '=') continue;
      if (parent(e[0] - 'a') == parent(e[3] - 'a')) return false;
    }
    return true;
  }
};
