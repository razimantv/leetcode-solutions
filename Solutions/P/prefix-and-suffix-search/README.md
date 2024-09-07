# Prefix and suffix search

[Problem link](https://leetcode.com/problems/prefix-and-suffix-search)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/prefix-and-suffix-search

class WordFilter {
 public:
  unordered_map<string, int> prefmap, sufmap;
  unordered_map<int, unordered_map<int, int>> seen;

  WordFilter(vector<string>& words) {
    int W = words.size();
    for (int w = 0; w < W; ++w) {
      int L = words[w].size();
      vector<int> prefvec(L), sufvec(L);
      string pref, suf;
      for (int i = 0; i < L; ++i) {
        pref += words[w][i];
        suf += words[w][L - 1 - i];

        auto mit = prefmap.find(pref);
        if (mit == prefmap.end())
          prefvec[i] = prefmap[pref] = prefmap.size();
        else
          prefvec[i] = mit->second;

        mit = sufmap.find(suf);
        if (mit == sufmap.end())
          sufvec[i] = sufmap[suf] = sufmap.size();
        else
          sufvec[i] = mit->second;
      }
      for (auto& p : prefvec)
        for (auto& s : sufvec) seen[p][s] = w;
    }
  }

  int f(string pref, string suf) {
    reverse(suf.begin(), suf.end());
    auto mit = prefmap.find(pref);
    if (mit == prefmap.end()) return -1;
    auto mit2 = sufmap.find(suf);
    if (mit2 == sufmap.end()) return -1;

    int p = mit->second, s = mit2->second;
    auto mit3 = seen.find(p);
    auto mit4 = mit3->second.find(s);
    if (mit4 == mit3->second.end())
      return -1;
    else
      return mit4->second;
  }
};

```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Prefix/Suffix](/Collections/string.md#prefix-suffix)
