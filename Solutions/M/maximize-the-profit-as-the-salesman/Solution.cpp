// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
 public:
  int maximizeTheProfit(int n, vector<vector<int>>& offers) {
    sort(offers.begin(), offers.end(),
         [&](const auto& o1, const auto& o2) { return o1[1] < o2[1]; });

    vector<int> dp(n + 1);
    for (int i = 1, j = 0, m = offers.size(); i <= n; ++i) {
      dp[i] = dp[i - 1];
      while (j < m and offers[j][1] == i - 1) {
        dp[i] = max(dp[i], dp[offers[j][0]] + offers[j][2]);
        ++j;
      }
    }
    return dp[n];
  }
};
