# Smallest range ii

[Problem link](https://leetcode.com/problems/smallest-range-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-range-ii

class Solution {
 public:
  int smallestRangeII(vector<int>& A, int K) {
    sort(A.begin(), A.end());

    int best = A.back() - A[0];
    for (int i = 0, N = A.size(); i < N - 1; ++i)
      best =
          min(best, max(A[i] + K, A.back() - K) - min(A[0] + K, A[i + 1] - K));
    return best;
  }
};
```