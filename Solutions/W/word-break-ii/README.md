# Word break ii

[Problem link](https://leetcode.com/problems/word-break-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-break-ii

class Solution {
  vector<vector<int>> poss;
  vector<string> ans;
  string S;

 public:
  void work(int s, int e, string pref) {
    if (s == e) {
      ans.push_back(pref);
      return;
    }

    if (s) pref += ' ';
    for (int j : poss[s]) {
      work(j, e, pref + S.substr(s, j - s));
    }
  }
  vector<string> wordBreak(string s, vector<string>& wordDict) {
    S = s;
    unordered_set<string> prefixes, words;
    for (string& s : wordDict) {
      words.insert(s);
      for (int i = 1; i <= s.size(); ++i) prefixes.insert(s.substr(0, i));
    }

    poss.clear();
    poss.resize(s.size());
    vector<int> valid(s.size() + 1, 0);
    valid[s.size()] = 1;
    for (int i = s.size() - 1; i >= 0; --i) {
      string cur = "";
      for (int j = i; j < s.size(); ++j) {
        cur += s[j];
        if (!prefixes.count(cur)) break;
        if (words.count(cur) and valid[j + 1]) {
          poss[i].push_back(j + 1);
          valid[i] = 1;
        }
      }
    }

    if (!valid[0]) return {};
    work(0, s.size(), "");
    return ans;
  }
};
```