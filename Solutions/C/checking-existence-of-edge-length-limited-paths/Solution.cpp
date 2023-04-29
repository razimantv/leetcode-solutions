// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution {
 public:
  vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edges,
                                         vector<vector<int>>& queries) {
    vector<int> par(n);
    iota(par.begin(), par.end(), 0);
    function<int(int)> parent = [&](int u) {
      return (u == par[u]) ? u : (par[u] = parent(par[u]));
    };

    sort(edges.begin(), edges.end(),
         [&](auto& e1, auto& e2) { return e1[2] < e2[2]; });
    int q = queries.size(), e = edges.size();
    vector<int> index(q);
    iota(index.begin(), index.end(), 0);
    sort(index.begin(), index.end(),
         [&](int i, int j) { return queries[i][2] < queries[j][2]; });
    vector<bool> ret(q);

    int i{};
    for (int ind : index) {
      auto& query = queries[ind];
      int u = query[0], v = query[1], w = query[2];
      while (i < e and edges[i][2] < w) {
        int p1 = parent(edges[i][0]), p2 = parent(edges[i][1]);
        par[p2] = p1;
        ++i;
      }
      ret[ind] = (parent(u) == parent(v));
    }
    return ret;
  }
};
