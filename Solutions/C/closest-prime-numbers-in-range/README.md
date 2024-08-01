# Closest prime numbers in range

[Problem link](https://leetcode.com/problems/closest-prime-numbers-in-range/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution {
 public:
  vector<int> closestPrimes(int left, int right) {
    vector<char> notprime(right + 1);
    vector<int> ret;
    for (int i = 2, prev = -1; i <= right; ++i) {
      if (notprime[i]) continue;
      if (i >= left) {
        if (ret.size() < 2)
          ret.push_back(i);
        else if (ret[1] - ret[0] > i - prev) {
          ret[0] = prev;
          ret[1] = i;
        }
      }
      prev = i;
      for (long long j = i * (long long)i; j <= right; j += i) notprime[j] = 1;
    }
    if (ret.size() < 2) return {-1, -1};
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
