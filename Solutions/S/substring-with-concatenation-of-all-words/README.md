# Substring with concatenation of all words

[Problem link](https://leetcode.com/problems/substring-with-concatenation-of-all-words)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution {
 public:
  vector<int> findSubstring(string s, vector<string>& words) {
    int L = words[0].size(), N = s.size(), W = words.size();

    long long p = 354745078340568241, npow = 1;
    for (int i = 0; i < L; ++i) npow = (npow * 26) % p;

    unordered_map<long long, int> hashmap;
    vector<int> allow(W);
    for (int i = 0; i < W; ++i) {
      long long hash = 0;
      for (char c : words[i]) hash = (hash * 26 + (c - 'a')) % p;
      if (!hashmap.count(hash)) hashmap[hash] = i;
      ++allow[hashmap[hash]];
    }

    vector<int> startword(N, -1);
    long long phash = 0;
    for (int i = 0; s[i]; ++i) {
      phash = (phash * 26 + (s[i] - 'a')) % p;
      if (i >= L) phash = (phash + p - (npow * (s[i - L] - 'a')) % p) % p;
      if (i >= L - 1 and hashmap.count(phash))
        startword[i - L + 1] = hashmap[phash];
    }

    vector<int> ret;
    for (int i = 0; i < L; ++i) {
      vector<int> cnt(W);
      for (int j = i, k = i, jj = 0, kk = 0; k < N; k += L, ++kk) {
        if (startword[k] == -1) {
          while (j < k) --cnt[startword[j]], j += L, ++jj;
          j += L, ++jj;
        } else if (++cnt[startword[k]] > allow[startword[k]]) {
          while (--cnt[startword[j]] < allow[startword[j]]) j += L, ++jj;
          j += L, ++jj;
        }
        if (kk - jj == W - 1) ret.push_back(j);
      }
    }
    return ret;
  }
};
```