# Find a value of a mysterious function closest to target

[Problem link](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target

class Solution {
 public:
  const int L = 25;
  vector<int> numtovec(int N) {
    vector<int> ret(L, 0);
    for (int i = 0; i < L; ++i) {
      if (!(N & (1 << i))) ret[i] = 1;
    }
    return ret;
  }
  int vectonum(const vector<int>& v) {
    int ret = (1 << L) - 1;
    for (int i = 0; i < L; ++i) {
      if (v[i]) ret ^= (1 << i);
    }
    return ret;
  }

  int closestToTarget(vector<int>& arr, int target) {
    int N = arr.size(), best = 1 << L;
    auto cur = numtovec((1 << L) - 1);
    for (int i = 0, j = -1; i < N; ++i) {
      if (i > 0) {
        auto rem = numtovec(arr[i - 1]);
        for (int l = 0; l < L; ++l) cur[l] -= rem[l];
      }
      while (j < N - 1 and vectonum(cur) >= target) {
        auto rem = numtovec(arr[++j]);
        for (int l = 0; l < L; ++l) cur[l] += rem[l];
      }
      best = min(best, abs(target - vectonum(cur)));
      if (j > i) {
        auto rem = numtovec(arr[j]);
        for (int l = 0; l < L; ++l) cur[l] -= rem[l];
        best = min(best, abs(target - vectonum(cur)));
        for (int l = 0; l < L; ++l) cur[l] += rem[l];
      }
    }
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
