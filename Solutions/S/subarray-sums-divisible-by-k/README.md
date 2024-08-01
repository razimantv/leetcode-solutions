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

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
