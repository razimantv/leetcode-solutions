// https://leetcode.com/problems/coin-change-2

class Solution {
 public:
  int change(int amount, vector<int>& coins) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;
    for (int c : coins) {
      for (int i = 0; i + c <= amount; i++) dp[i + c] += dp[i];
    }
    return dp.back();
  }
};
