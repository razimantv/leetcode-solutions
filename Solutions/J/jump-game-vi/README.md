# Jump game vi

[Problem link](https://leetcode.com/problems/jump-game-vi)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game-vi

class Solution {
 public:
  int maxResult(vector<int>& nums, int k) {
    int n = nums.size();
    set<pair<int, int>, greater<pair<int, int>>> best;
    best.insert({nums[n - 1], n - 1});

    for (int i = n - 2; i >= 0; --i) {
      auto [v, p] = *best.begin();
      if (p > i + k) {
        best.erase(best.begin());
        ++i;
        continue;
      }
      best.insert({nums[i] += v, i});
    }
    return nums[0];
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Right to left](/README.md#Array_scanning-Right_to_left)
* [Priority queue](/README.md#Priority_queue)
