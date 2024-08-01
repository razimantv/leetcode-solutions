# Find the winner of the circular game

[Problem link](https://leetcode.com/problems/find-the-winner-of-the-circular-game)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-winner-of-the-circular-game

class Solution {
 public:
  int findTheWinner(int n, int k) {
    vector<int> players(n);
    iota(players.begin(), players.end(), 1);

    for (int i = 1, p = 0; i < n; ++i) {
      for (int j = 1; j < k; ++j) {
        p = (p + 1) % (players.size());
      }
      players.erase(players.begin() + (p % players.size()));
    }
    return players[0];
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
