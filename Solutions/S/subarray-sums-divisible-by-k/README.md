# Subarray sums divisible by k

[Problem link](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution {
public:
  int subarraysDivByK(vector<int> &nums, int k) {
    unordered_map<int, int> cnt{{0, 1}};
    int ret{};
    for (int i = 0, s = 0, n = nums.size(); i < n; ++i)
      ret += cnt[s = (s + nums[i] % k + k) % k]++;
    return ret;
  }
};
```
## Tags

* [Hashmap](/README.md#Hashmap)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
