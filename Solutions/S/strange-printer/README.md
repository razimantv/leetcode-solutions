# Strange printer

[Problem link](https://leetcode.com/problems/strange-printer/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/strange-printer/

class Solution {
 public:
  // ChatGPT solution
  int strangePrinter(string s) {
    int n = s.length();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    for (int i = n - 1; i >= 0; i--) {
      dp[i][i] = 1;  // Base case: single character requires one turn
      for (int j = i + 1; j < n; j++) {
        if (s[i] == s[j]) {
          dp[i][j] = dp[i][j - 1];  // Same character, no extra turn needed
        } else {
          int minTurns = INT_MAX;
          for (int k = i; k < j; k++) {
            minTurns = std::min(minTurns, dp[i][k] + dp[k + 1][j]);
          }
          dp[i][j] = minTurns;
        }
      }
    }

    return dp[0][n - 1];
  }
};
```
## Tags

* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
