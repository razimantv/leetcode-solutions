# Word ladder ii

[Problem link](https://leetcode.com/problems/word-ladder-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-ladder-ii

class Solution {
 public:
  bool hasedge(const string& s1, const string& s2) {
    for (int i = 0, bad = 0; s1[i]; ++i)
      if (s1[i] != s2[i])
        if (bad++) return false;
    return true;
  }
  vector<vector<string>> get(int u, vector<string>& wordList,
                             vector<vector<int>>& prev) {
    if (!u) return {{wordList[0]}};

    vector<vector<string>> ret;
    for (auto v : prev[u]) {
      for (auto& path : get(v, wordList, prev)) {
        ret.push_back(move(path));
        ret.back().push_back(wordList[u]);
      }
    }
    return ret;
  }
  vector<vector<string>> findLadders(string beginWord, string endWord,
                                     vector<string>& wordList) {
    if (find(wordList.begin(), wordList.end(), endWord) == wordList.end())
      return {};

    wordList.insert(wordList.begin(), beginWord);
    int E = find(wordList.begin(), wordList.end(), endWord) - wordList.begin();
    int W = wordList.size();
    vector<int> depth(W, -1);
    vector<vector<int>> prev(W);

    depth[0] = 0;
    prev[0] = {-1};
    queue<int> bfsq;
    bfsq.push(0);

    while (!bfsq.empty()) {
      auto word = bfsq.front();
      if (word == E) break;

      bfsq.pop();
      for (int w = 1; w < W; ++w) {
        if (!hasedge(wordList[word], wordList[w])) continue;
        auto& v2 = prev[w];
        if (v2.empty()) {
          bfsq.push(w);
          depth[w] = depth[word] + 1;
        }
        if (depth[w] == depth[word] + 1) v2.push_back(word);
      }
    }

    return get(E, wordList, prev);
  }
};
```