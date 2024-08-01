# Minimum money required before transactions

[Problem link](https://leetcode.com/problems/minimum-money-required-before-transactions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution {
 public:
  long long minimumMoney(vector<vector<int>>& transactions) {
    long long bad{}, answer{};
    for (auto& t : transactions) {
      if (t[0] > t[1]) bad += t[0] - t[1];
    }

    for (auto& t : transactions) {
      long long current = bad;
      if (t[0] > t[1]) current -= t[0] - t[1];
      answer = max(answer, current + t[0]);
    }
    return answer;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
