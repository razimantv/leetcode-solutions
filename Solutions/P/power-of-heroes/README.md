# Power of heroes

[Problem link](https://leetcode.com/problems/power-of-heroes/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/power-of-heroes/

class Solution {
 public:
  int sumOfPower(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    // sum_{i<j} a_i a_j² 2^(max(j-i-1,0))
    // sum_j a_j² sum_{i<j} a_i 2^...
    const int MOD = 1'000'000'007;
    auto mul = [&](int x, int y) { return (x * 1ll * y) % MOD; };
    auto inc = [&](int& x, int y) { x = (x + 0ll + y) % MOD; };

    int ret{};
    for (int i = 0, n = nums.size(), prev = 0; i < n; ++i) {
      int x = nums[i], xsq = mul(x, x);
      inc(ret, mul(xsq, x + prev));
      inc(prev, prev + x);
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Mathematics](/README.md#Mathematics) > [Closed form expressions](/README.md#Mathematics-Closed_form_expressions)
* [Dynamic programming](/README.md#Dynamic_programming) > [Complexity reduction with algebra](/README.md#Dynamic_programming-Complexity_reduction_with_algebra)
