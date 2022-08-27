// https://leetcode.com/problems/count-number-of-ways-to-place-houses

class Solution {
 public:
  int countHousePlacements(int n) {
    vector<int> dp(n + 1);
    dp[0] = 1, dp[1] = 2;
    const int MOD = 1'000'000'007;
    for (int i = 2; i <= n; ++i) dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    return (dp.back() * (long long)dp.back()) % MOD;
  }
};
