# Best poker hand

[Problem link](https://leetcode.com/problems/best-poker-hand)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-poker-hand

class Solution {
 public:
  string bestHand(vector<int>& ranks, vector<char>& suits) {
    bool flag = true;
    for (int i = 1; i < 5; ++i)
      if (suits[i] != suits[0]) flag = false;
    if (flag) return "Flush";

    sort(ranks.begin(), ranks.end());
    for (int i = 2; i < 5; ++i)
      if (ranks[i] == ranks[i - 2]) return "Three of a Kind";

    for (int i = 1; i < 5; ++i)
      if (ranks[i] == ranks[i - 1]) return "Pair";

    return "High Card";
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
