// https://leetcode.com/problems/merge-intervals

class Solution {
 public:
  vector<vector<int>> merge(vector<vector<int>>& I) {
    sort(I.begin(), I.end());
    vector<vector<int>> ret;
    for (int i = 0, N = I.size(); i < N;) {
      int s = I[i][0], e = I[i][1];
      for (++i; i < N and I[i][0] <= e; ++i) e = max(e, I[i][1]);
      ret.push_back({s, e});
    }
    return ret;
  }
};
