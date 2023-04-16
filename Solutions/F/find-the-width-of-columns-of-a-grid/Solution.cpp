// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
 public:
  vector<int> findColumnWidth(vector<vector<int>>& grid) {
    int n = grid[0].size();
    vector<int> ret(n);
    for (auto& row : grid)
      for (int i = 0; i < n; ++i)
        ret[i] = max(ret[i], (int)to_string(row[i]).size());
    return ret;
  }
};
