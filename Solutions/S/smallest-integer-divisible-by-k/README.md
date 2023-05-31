# Smallest integer divisible by k

[Problem link](https://leetcode.com/problems/smallest-integer-divisible-by-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-integer-divisible-by-k

class Solution {
 public:
  int smallestRepunitDivByK(int K) {
    if (K % 2 == 0 or K % 5 == 0) return -1;
    int ret = 0, cur = 0;
    do {
      ++ret;
      cur = (cur * 10 + 1) % K;
    } while (cur);
    return ret;
  }
};
```