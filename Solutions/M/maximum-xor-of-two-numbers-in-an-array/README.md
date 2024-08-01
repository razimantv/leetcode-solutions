# Maximum xor of two numbers in an array

[Problem link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

class Solution {
 public:
  int findMaximumXOR(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int best = 0;
    for (int n : nums) {
      int cur = 0;
      for (int b = 30, p = 0; b >= 0; --b) {
        p |= (1 << b);
        if (!(n & (1 << b))) cur ^= (1 << b);
        auto elem = lower_bound(nums.begin(), nums.end(), cur);
        if (elem == nums.end() or ((*elem) ^ cur) & p) cur ^= (1 << b);
      }
      best = max(best, cur ^ n);
    }
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Build result bit-by-bit](/Collections/bitwise-operation.md#build-result-bit-by-bit)
* [Binary search](/Collections/binary-search.md#binary-search)
