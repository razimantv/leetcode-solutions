# Neighboring bitwise xor

[Problem link](https://leetcode.com/problems/neighboring-bitwise-xor/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
 public:
  bool doesValidArrayExist(vector<int>& derived) {
    return !accumulate(derived.begin(), derived.end(), 0, bit_xor<void>());
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
