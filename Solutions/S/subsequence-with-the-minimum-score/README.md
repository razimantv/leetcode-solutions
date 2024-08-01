# Subsequence with the minimum score

[Problem link](https://leetcode.com/problems/subsequence-with-the-minimum-score/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution {
 public:
  int minimumScore(string s, string t) {
    int m = s.size(), n = t.size();
    // how many characters of s do you need
    // to make first x characters of t its subsequence
    vector<int> left(n + 1, m + 1), right(n + 1, m + 1);
    left[0] = right[0] = 0;
    for (int i = 0, j = 0; i < n and j < m; ++i, ++j) {
      while (j < m and t[i] != s[j]) ++j;
      left[i + 1] = j + 1;
    }
    for (int i = 0, j = 0; i < n and j < m; ++i, ++j) {
      while (j < m and t[n - 1 - i] != s[m - 1 - j]) ++j;
      right[i + 1] = j + 1;
    }

    int ret = n;
    for (int i = n, j = 0; i >= 0; --i) {
      if (left[i] > m) continue;
      while (j <= n and left[i] + right[j] <= m) ++j;
      ret = min(ret, max(0, n - i - j + 1));
    }
    return ret;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
