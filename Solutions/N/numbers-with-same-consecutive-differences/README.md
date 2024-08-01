# Numbers with same consecutive differences

[Problem link](https://leetcode.com/problems/numbers-with-same-consecutive-differences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/numbers-with-same-consecutive-differences

class Solution {
 public:
  vector<int> numsSameConsecDiff(int N, int K) {
    if (N == 1) return {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<int> ret = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (int i = 1; i < N; ++i) {
      vector<int> next;
      for (int n : ret) {
        int d = n % 10;
        if (d + K < 10) next.push_back(n * 10 + d + K);
        if (K and d >= K) next.push_back(n * 10 + d - K);
      }
      ret = next;
    }
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
