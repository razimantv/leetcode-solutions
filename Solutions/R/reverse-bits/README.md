# Reverse bits

[Problem link](https://leetcode.com/problems/reverse-bits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-bits

class Solution {
 public:
  uint32_t reverseBits(uint32_t n) {
    uint32_t ret = 0, o = 1;
    for (int i = 0; i < 32; i++)
      if (n & (o << i)) ret |= (o << (31 - i));
    return ret;
  }
};
```