# Complement of base 10 integer

[Problem link](https://leetcode.com/problems/complement-of-base-10-integer)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/complement-of-base-10-integer

class Solution {
 public:
  int bitwiseComplement(int N) {
    int M = 1;
    do M <<= 1;
    while (M <= N);
    --M;
    return M ^ N;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
