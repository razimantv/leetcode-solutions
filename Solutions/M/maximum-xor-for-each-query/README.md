# Maximum xor for each query

[Problem link](https://leetcode.com/problems/maximum-xor-for-each-query)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-xor-for-each-query

class Solution {
 public:
  vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
    int n = nums.size();
    for (int i = 1; i < n; ++i) {
      nums[i] ^= nums[i - 1];
    }

    vector<int> ret;
    while (!nums.empty()) {
      ret.push_back((nums.back() ^ ((1 << maximumBit) - 1)) &
                    ((1 << maximumBit) - 1));
      nums.pop_back();
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
