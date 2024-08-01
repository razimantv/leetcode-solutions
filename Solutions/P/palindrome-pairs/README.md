# Palindrome pairs

[Problem link](https://leetcode.com/problems/palindrome-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/palindrome-pairs

const long long P = 37, mask = (1ll << 31) - 1;
class Solution {
  static vector<int> ppow;

 public:
  Solution() {
    if (!ppow.empty()) return;
    ppow.resize(301);
    ppow[0] = 1;
    for (int i = 1; i < 301; ++i) ppow[i] = (ppow[i - 1] * P) & mask;
  }

  vector<vector<int>> palindromePairs(vector<string>& words) {
    int W = words.size();
    vector<int> fwhash(W, -1), bwhash(W, -2);
    unordered_map<char, vector<int>> start, end;
    vector<int> empty;
    for (int i = 0; i < W; ++i) {
      int L = words[i].size();
      if (!L) {
        empty.push_back(i);
        continue;
      }
      start[words[i][0]].push_back(i);
      end[words[i][L - 1]].push_back(i);
      int cur = 0;
      for (int j = 0; j < L; ++j) cur = (cur * P + words[i][j] - 'a') & mask;
      fwhash[i] = cur;

      cur = 0;
      for (int j = L - 1; j >= 0; --j)
        cur = (cur * P + words[i][j] - 'a') & mask;
      bwhash[i] = cur;
    }

    vector<vector<int>> ret;
    if (!empty.empty()) {
      for (int i = 0, E = empty.size(); i < E; ++i)
        for (int j = 0; j < i; ++j) {
          ret.push_back({empty[i], empty[j]});
          ret.push_back({empty[j], empty[i]});
        }

      for (int i = 0; i < W; ++i)
        if (fwhash[i] == bwhash[i])
          for (int j : empty) {
            ret.push_back({i, j});
            ret.push_back({j, i});
          }
    }

    for (char c = 'a'; c <= 'z'; ++c)
      for (int i : start[c])
        for (int j : end[c]) {
          if (i == j) continue;
          int hash1 =
              (fwhash[j] + fwhash[i] * (long long)ppow[words[j].size()]) & mask;
          int hash2 =
              (bwhash[i] + bwhash[j] * (long long)ppow[words[i].size()]) & mask;
          if (hash1 == hash2) ret.push_back({i, j});
        }
    return ret;
  }
};

vector<int> Solution::ppow{};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Palindrome](/Collections/palindrome.md#palindrome) > [Hashing](/Collections/palindrome.md#hashing)
