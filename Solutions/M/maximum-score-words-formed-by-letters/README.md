# Maximum score words formed by letters

[Problem link](https://leetcode.com/problems/maximum-score-words-formed-by-letters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-score-words-formed-by-letters

class Solution {
 public:
  int best(const vector<pair<int, vector<char>>> words, vector<char>& available,
           int start) {
    if (start == words.size()) return 0;
    int cur = best(words, available, start + 1);
    for (int i = 0; i < 26; ++i) {
      if ((available[i] -= words[start].second[i]) < 0) {
        while (i >= 0) {
          available[i] += words[start].second[i];
          --i;
        }
        return cur;
      }
    }
    cur = max(cur, best(words, available, start + 1) + words[start].first);
    for (int i = 0; i < 26; ++i) available[i] += words[start].second[i];
    return cur;
  }

  int maxScoreWords(vector<string>& words, vector<char>& letters,
                    vector<int>& score) {
    vector<pair<int, vector<char>>> words_processed;
    for (string& w : words) {
      int s = 0;
      vector<char> cnt(26);
      for (char c : w) {
        ++cnt[c - 'a'];
        s += score[c - 'a'];
      }
      words_processed.push_back({s, cnt});
    }

    vector<char> available(26);
    for (char c : letters) ++available[c - 'a'];
    return best(words_processed, available, 0);
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
