// https://leetcode.com/problems/substring-xor-queries/

class Solution {
 public:
  vector<vector<int>> substringXorQueries(string s,
                                          vector<vector<int>>& queries) {
    unordered_map<int, vector<int>> best;
    for (int i = 0, n = s.size(); i < n; ++i) {
      for (int j = i, pref = 0; j < n and j < i + 30; ++j) {
        pref = (pref << 1) | (s[j] - '0');
        if (!best.count(pref)) best[pref] = {i, j};
        if (!pref) break;
      }
    }

    vector<vector<int>> ret;
    for (auto& q : queries) {
      int x = q[0] ^ q[1];
      if (best.count(x))
        ret.push_back(best[x]);
      else
        ret.push_back({-1, -1});
    }
    return ret;
  }
};
