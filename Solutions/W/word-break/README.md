# Word break

[Problem link](https://leetcode.com/problems/word-break)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-break

class Solution {
  struct trie {
    bool end{false};
    unordered_map<char, trie*> next;
  };

  trie head;

  void add(const string& s) {
    trie* cur = &head;
    for (char c : s) {
      if (!cur->next.count(c)) cur->next[c] = new trie;
      cur = cur->next[c];
    }
    cur->end = true;
  }

 public:
  bool wordBreak(string s, vector<string>& wordDict) {
    for (const string& word : wordDict) add(word);

    int N = s.size();
    vector<bool> poss(N + 1, false);
    poss[N] = true;

    for (int i = N - 1; i >= 0; --i) {
      trie* cur = &head;
      for (int j = i; j < N; ++j) {
        if (!cur->next.count(s[j])) break;
        cur = cur->next[s[j]];
        if (cur->end and poss[j + 1]) {
          poss[i] = true;
          break;
        }
      }
    }
    return poss[0];
  }
};
```