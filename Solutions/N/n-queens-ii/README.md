# N queens ii

[Problem link](https://leetcode.com/problems/n-queens-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/n-queens-ii

class Solution {
 public:
  int totalNQueens(int n) {
    vector<int> perm(n);
    iota(perm.begin(), perm.end(), 0);

    int ret = 0, bad1 = -1, bad2 = -1, val1 = -1, val2 = -1;
    do {
      if (bad1 >= 0 and perm[bad1] == val1 and perm[bad2] == val2) continue;
      bad1 = -1;
      bool flag = true;
      for (int i = 0; flag and i < n; ++i) {
        for (int j = 0; flag and j < i; ++j) {
          if (abs(perm[i] - perm[j]) == abs(i - j)) {
            bad1 = i, bad2 = j, val1 = perm[i], val2 = perm[j];
            flag = false;
          }
        }
      }
      if (flag) ++ret;
    } while (next_permutation(perm.begin(), perm.end()));
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
