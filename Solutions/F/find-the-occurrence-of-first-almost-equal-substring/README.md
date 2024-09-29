# Find the occurrence of first almost equal substring

[Problem link](https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
 public:
  int minStartingIndex(string s, string pattern) {
    // Converted from python by ChatGPT
    const int p = 43;
    const int mod = 1048901971;
    int m = s.length(), n = pattern.length();

    vector<long long> phashl(n, 0);
    long long h = 0;
    for (int i = 0; i < n; i++) {
      h = (h * p + (pattern[i] - 'a')) % mod;
      phashl[i] = h;
    }

    vector<long long> phashr(n, 0);
    vector<long long> ppows(n + 1, 1);
    h = 0;
    long long ppow = 1;
    for (int i = n - 1; i >= 0; i--) {
      h = (h + ppow * (pattern[i] - 'a')) % mod;
      ppow = (ppow * p) % mod;
      phashr[i] = h;
      ppows[n - i] = ppow;
    }

    vector<long long> shash(m + 1, 0);
    h = 0;
    for (int i = 0; i < m; i++) {
      h = (h * p + (s[i] - 'a')) % mod;
      shash[i + 1] = h;
    }

    for (int i = 0; i <= m - n; i++) {
      int start = 0, end = n + 1;

      while (end - start > 1) {
        int mid = (start + end) / 2;
        long long leftHash =
            (shash[i + mid] + mod - (ppows[mid] * shash[i]) % mod) % mod;
        if (leftHash == phashl[mid - 1]) {
          start = mid;
        } else {
          end = mid;
        }
      }
      int left = start;

      start = 0;
      end = n + 1;
      while (end - start > 1) {
        int mid = (start + end) / 2;
        long long rightHash =
            (shash[i + n] + mod - (ppows[mid] * shash[i + n - mid]) % mod) %
            mod;
        if (rightHash == phashr[n - mid]) {
          start = mid;
        } else {
          end = mid;
        }
      }
      int right = start;

      if (left + right >= n - 1) return i;
    }

    return -1;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Prefix/Suffix](/Collections/string.md#prefix-suffix)
* [Binary search](/Collections/binary-search.md#binary-search)
* [Sliding window](/Collections/sliding-window.md#sliding-window) > [String hashing](/Collections/sliding-window.md#string-hashing)
