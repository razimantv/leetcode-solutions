# Stone game iii

[Problem link](https://leetcode.com/problems/stone-game-iii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stone-game-iii/

class Solution {
 public:
  // Solution written entirely by ChatGPT
  string stoneGameIII(vector<int>& stoneValue) {
    int n = stoneValue.size();
    vector<int> dp(n + 1, 0);

    for (int i = n - 1; i >= 0; i--) {
      int take = 0;
      dp[i] = INT_MIN;

      for (int j = i; j < min(i + 3, n); j++) {
        take += stoneValue[j];
        dp[i] = max(dp[i], take - dp[j + 1]);
      }
    }

    if (dp[0] > 0)
      return "Alice";
    else if (dp[0] < 0)
      return "Bob";
    else
      return "Tie";
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/stone-game-iii/

class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            dp[i] = max(
                sum(stones[i:j+1]) - dp[j+1]
                for j in range(i, min(i + 3, n))
            )
        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Two player games](/Collections/two-player-games.md#two-player-games)
