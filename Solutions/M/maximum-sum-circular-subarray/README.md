# Maximum sum circular subarray

[Problem link](https://leetcode.com/problems/maximum-sum-circular-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution {
 public:
  int maxSubarraySumCircular(vector<int>& A) {
    int N = A.size();
    vector<int> psum(N, 0);

    int best = A[0];
    for (int i = 0, cum = 0, minp = 0, maxp = 0; i < N; ++i) {
      psum[i] = maxp;
      cum += A[i];
      best = max(best, cum - minp);
      minp = min(minp, cum);
      maxp = max(maxp, cum);
    }

    for (int i = N - 1, cum = 0; i >= 0; --i) {
      cum += A[i];
      best = max(best, cum + psum[i]);
    }

    return best;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Cyclic array](/Collections/dynamic-programming.md#cyclic-array)
