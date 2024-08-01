# Minimum ascii delete sum for two strings

[Problem link](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution {
 public:
  // ChatGPT solution
  int minimumDeleteSum(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();

    // dp[i][j] represents the LCS of s1[0...i-1] and s2[0...j-1]
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    // Calculate the LCS
    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
        if (s1[i - 1] == s2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + static_cast<int>(s1[i - 1]);
        } else {
          dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }

    int totalAsciiSum = 0;
    // Calculate the sum of ASCII values of deleted characters
    for (char ch : s1) {
      totalAsciiSum += static_cast<int>(ch);
    }

    for (char ch : s2) {
      totalAsciiSum += static_cast<int>(ch);
    }

    // Subtract the sum of LCS characters' ASCII values from the total ASCII sum
    return totalAsciiSum - 2 * dp[m][n];
  }
};
```
## Tags

* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest common subsequence](/Collections/dynamic-programming.md#longest-common-subsequence)
