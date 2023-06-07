// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution {
 public:
  int countNegatives(vector<vector<int>>& grid) {
    int ret{};
    for (int i = 0, m = grid.size(), n = grid[0].size(), j = n - 1; i < m;
         ++i) {
      while (j >= 0 and grid[i][j] < 0) --j;
      ret += n - j - 1;
    }
    return ret;
  }
};
