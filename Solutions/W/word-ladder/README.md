# Word ladder

[Problem link](https://leetcode.com/problems/word-ladder)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-ladder

class Solution {
 public:
  int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    wordList.push_back(beginWord);

    int N = wordList.size(), L = beginWord.size(), end = -1;
    vector<vector<int>> adjlist(N);
    for (int i = 0; i < N; ++i) {
      if (wordList[i] == endWord) end = i;
      for (int j = 0; j < i; ++j) {
        int cnt = 0;
        for (int k = 0; k < L and cnt < 2; ++k)
          if (wordList[i][k] != wordList[j][k]) ++cnt;
        if (cnt == 1) {
          adjlist[i].push_back(j);
          adjlist[j].push_back(i);
        }
      }
    }
    if (end == -1) return 0;

    vector<int> depth(N, -1);
    queue<int> bfsq;

    bfsq.push(N - 1);
    depth[N - 1] = 1;
    while (!bfsq.empty()) {
      int u = bfsq.front();
      bfsq.pop();

      for (int v : adjlist[u]) {
        if (v == end) return depth[u] + 1;
        if (depth[v] != -1) continue;
        depth[v] = depth[u] + 1;
        bfsq.push(v);
      }
    }
    return 0;
  }
};
```