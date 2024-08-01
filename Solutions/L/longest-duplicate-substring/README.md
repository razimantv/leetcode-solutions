# Longest duplicate substring

[Problem link](https://leetcode.com/problems/longest-duplicate-substring)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-duplicate-substring

class Solution {
 public:
  long long modmult(long long a, long long b, long long M) {
    long long ret = 0;
    while (a) {
      if (a & 1) {
        ret += b;
        if (ret >= M) ret -= M;
      }
      b <<= 1;
      if (b >= M) b -= M;
      a >>= 1;
    }
    return ret;
  }
  int getindex(string S, int L) {
    const long long P = 31, M = 36028797018963913ll;
    long long Ppow = 1;
    set<long long> seen;
    vector<long long> pref(S.size() + 1, 0);
    for (int i = 0; i < S.size(); i++) {
      pref[i + 1] = (pref[i] * P + S[i] - 'a' + 3) % M;
      if (i < L) Ppow = (Ppow * P) % M;
      if (i + 1 < L) continue;
      long long cur = pref[i + 1] - modmult(pref[i + 1 - L], Ppow, M);
      if (cur < 0) cur += M;
      if (seen.count(cur)) return i - L + 1;
      seen.insert(cur);
    }
    return -1;
  }
  string longestDupSubstring(string S) {
    int start = 0, end = S.size(), pos = -1;
    while (start < end - 1) {
      int mid = (start + end) >> 1;
      int idx = getindex(S, mid);
      if (idx == -1)
        end = mid;
      else {
        start = mid;
        pos = idx;
      }
    }

    if (start == 0)
      return "";
    else
      return S.substr(pos, start);
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
