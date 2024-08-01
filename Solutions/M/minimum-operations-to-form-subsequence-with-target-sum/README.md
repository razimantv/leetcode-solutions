# Minimum operations to form subsequence with target sum

[Problem link](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

class Solution {
 public:
  int minOperations(vector<int>& nums, int target) {
    if (accumulate(nums.begin(), nums.end(), 0ll) < target) return -1;
    multiset<int> have(nums.begin(), nums.end()), need;
    unordered_map<int, int> invpow;
    for (int i = 0; i < 31; ++i) {
      if (target & (1 << i)) need.insert(1 << i);
      invpow[1 << i] = i;
    }

    int ret{};
    while (!have.empty()) {
      int x = *have.begin(), y = *need.begin();
      have.erase(have.begin());
      if (x == y) {
        need.erase(need.begin());
      } else if (x < y) {
        if (!have.empty() and *have.begin() == x) {
          have.erase(have.begin());
          have.insert(x << 1);
        }
      } else {
        need.erase(need.begin());
        while (y < x) {
          have.insert(y);
          y <<= 1;
          ++ret;
        }
      }

      if (need.empty()) break;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
