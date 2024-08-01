# Minimum number of flips to make the binary string alternating

[Problem link](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

class Solution {
 public:
  int minFlips(string s) {
    int N = s.size();
    vector<vector<int>> pref(2, vector<int>(N)), suf{pref};

    pref[s[0] ^ '0' ^ 1][0] = 1;
    for (int i = 1; i < N; ++i)
      for (int p = 0; p < 2; ++p)
        pref[p][i] = pref[p][i - 1] + 1 - (s[i] == ('0' ^ p ^ (i & 1)));

    suf[s[N - 1] ^ '0' ^ 1][N - 1] = 1;
    for (int i = N - 2; i >= 0; --i)
      for (int p = 0; p < 2; ++p)
        suf[p][i] = (suf[p ^ 1][i + 1]) + 1 - (s[i] == ('0' ^ p));

    int best = min(suf[0][0], suf[1][0]);
    for (int i = 1; i < N; ++i)
      for (int p = 0; p < 2; ++p)
        best = min(best, suf[p][i] + pref[((N - i) & 1) ^ p][i - 1]);
    return best;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Cyclic array](/Collections/dynamic-programming.md#cyclic-array)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
