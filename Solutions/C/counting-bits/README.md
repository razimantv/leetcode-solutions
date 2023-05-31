# Counting bits

[Problem link](https://leetcode.com/problems/counting-bits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/counting-bits

class Solution {
 public:
  vector<int> countBits(int num) {
    vector<int> ret(num + 1);
    for (int i = 1; i <= num; ++i) {
      ret[i] = ((i & 1) ? ret[i - 1] + 1 : ret[i >> 1]);
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation)
* [Suboptimal solution](/README.md#Suboptimal_solution)
