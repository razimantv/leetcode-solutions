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

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
