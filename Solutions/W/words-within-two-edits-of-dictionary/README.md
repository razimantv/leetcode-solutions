# Words within two edits of dictionary

[Problem link](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution {
 public:
  vector<string> twoEditWords(vector<string>& queries,
                              vector<string>& dictionary) {
    unordered_set<string> good;
    int L = queries[0].size();
    for (const string& w : dictionary) {
      for (int i = 0; i < L; ++i) {
        string ww = w;
        for (char c = 'a'; c <= 'z'; ++c) {
          ww[i] = c;
          good.insert(ww);
        }
      }
    }

    vector<string> ret;
    for (const string& w : queries) {
      for (int i = 0; i < L; ++i) {
        string ww = w;
        for (char c = 'a'; c <= 'z'; ++c) {
          ww[i] = c;
          if (good.count(ww)) {
            ret.push_back(w);
            goto BPP;
          }
        }
      }
    BPP:;
    }
    return ret;
  }
};
```
## Tags

* [Meet in the middle](/Collections/meet-in-the-middle.md#meet-in-the-middle)
