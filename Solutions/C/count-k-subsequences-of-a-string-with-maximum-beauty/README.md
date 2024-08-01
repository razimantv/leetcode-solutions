# Count k subsequences of a string with maximum beauty

[Problem link](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

class Solution {
 public:
  const long long MOD = 1'000'000'007ll;

  long long choose(int n, int r) {
    long long ret{1};
    for (int i = 0; i < r; ++i) ret = (ret * (n - i)) / (i + 1);
    return ret;
  }

  int countKSubsequencesWithMaxBeauty(string s, int k) {
    unordered_map<char, int> cnt;
    for (char c : s) ++cnt[c];
    if (cnt.size() < k) return 0;

    vector<int> counts;
    for (auto [k, v] : cnt) counts.push_back(v);
    sort(counts.begin(), counts.end(), greater<int>());

    long long ret{1ll}, last{}, needlast{};
    for (int i = 0, n = counts.size(); i < n; ++i) {
      if (i < k) ret = (ret * counts[i]) % MOD;
      if (i and (counts[i] != counts[i - 1])) {
        if (i >= k) break;
        last = 0;
      }
      ++last;
      if (i == k - 1) needlast = last;
    }
    ret = (ret * choose(last, needlast)) % MOD;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
