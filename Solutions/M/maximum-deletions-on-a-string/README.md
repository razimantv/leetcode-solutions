# Maximum deletions on a string

[Problem link](https://leetcode.com/problems/maximum-deletions-on-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
  // Canonical: String hash
  const long long P = 37, MOD = 1'000'000'007;
  vector<long long> fwhash, ppow;

  void buildfwhash(const string& s, int L) {
    fwhash = vector<long long>(L + 1, 0);
    ppow = vector<long long>(L + 1, 1);
    for (int i = 0; i < L; ++i) {
      fwhash[i + 1] = (fwhash[i] * P + (s[i] - 'a' + 1)) % MOD;
      ppow[i + 1] = (ppow[i] * P) % MOD;
    }
  }

  int hash(int i, int j) {
    int ret = fwhash[i + j] + MOD - (fwhash[i] * ppow[j]) % MOD;
    if (ret >= MOD) ret -= MOD;
    return ret;
  }

 public:
  int deleteString(string s) {
    int L = s.size();
    buildfwhash(s, L);
    vector<int> dp(L + 1);
    for (int i = L - 1; i >= 0; --i) {
      dp[i] = 1;
      for (int j = 1; i + 2 * j <= L; ++j) {
        int h1 = hash(i, j), h2 = hash(i + j, j);
        if (h1 == h2) dp[i] = max(dp[i], 1 + dp[i + j]);
      }
    }
    return dp[0];
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
