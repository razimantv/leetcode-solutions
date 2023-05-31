# Three equal parts

[Problem link](https://leetcode.com/problems/three-equal-parts)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/three-equal-parts

class Solution {
 public:
  vector<int> threeEqualParts(vector<int>& arr) {
    int n = arr.size();
    vector<int> lz(n + 1);
    for (int i = n - 1; i >= 0; --i)
      lz[i] = (arr[i] == 1 ? 0 : (1 + lz[i + 1]));
    if (lz[0] == n) return {0, 2};

    for (int i = lz[0]; i < n - 2; ++i) {
      int nz = i - lz[0] + 1, j = i + 1 + lz[i + 1] + nz;
      if (j >= n) break;
      int k = j + lz[j] + nz;
      if (k < n)
        continue;
      else if (k > n)
        break;

      bool flag = true;
      for (int zz = lz[0], ii = i + 1 + lz[i + 1], jj = j + lz[j];
           flag and jj < n; ++zz, ++ii, ++jj)
        if (arr[zz] != arr[ii] or arr[zz] != arr[jj]) flag = false;
      if (flag) return {i, j};
    }
    return {-1, -1};
  }
};
```