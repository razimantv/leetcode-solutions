# Word search ii

[Problem link](https://leetcode.com/problems/word-search-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-search-ii/

struct node {
  unordered_map<char, pair<node*, int>> children;
};

const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

class Solution {
  node trie;
  int m, n;
  void add(node* n, const string& s, int i) {
    if (!s[i]) {
      n->children['$'] = {nullptr, 1};
      return;
    }

    if (!n->children.count(s[i])) n->children[s[i]] = {new node, 0};
    ++n->children[s[i]].second;
    add(n->children[s[i]].first, s, i + 1);
  }

  int work(vector<vector<char>>& board, int i, int j, node* tn, string& s,
           vector<string>& ret) {
    char c = board[i][j];
    if (!tn->children.count(c)) return 0;

    s += c;
    board[i][j] = '#';
    auto& [next, val] = tn->children[c];

    int sub = 0;
    if (next->children.count('$')) {
      next->children.erase('$');
      ret.push_back(s);
      ++sub;
    }

    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii < 0 or ii >= m or jj < 0 or jj >= n) continue;
      int cur = work(board, ii, jj, next, s, ret);
      sub += cur;
    }

    if (!(val -= sub)) tn->children.erase(c);
    s.pop_back();
    board[i][j] = c;
    return sub;
  }

 public:
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    for (const string& w : words) add(&trie, w, 0);

    vector<string> ret;
    string temp;
    m = board.size(), n = board[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) work(board, i, j, &trie, temp, ret);
    return ret;
  }
};
```
### Solution_suboptimal.cpp
```cpp
// https://leetcode.com/problems/word-search-ii

class Solution {
 public:
  inline static vector<vector<int>> dir = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
  unordered_set<string> seen, pref, wordset;
  void dfs(vector<vector<char>>& board, int i, int j, string s, int M, int N) {
    s += board[i][j];
    if (!pref.count(s)) return;
    if (wordset.count(s)) seen.insert(s);
    board[i][j] = '#';
    for (auto d : dir) {
      int ii = i + d[0], jj = j + d[1];
      if (ii >= 0 and ii < M and jj >= 0 and jj < N and board[ii][jj] != '#')
        dfs(board, ii, jj, s, M, N);
    }
    board[i][j] = s.back();
    return;
  }
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    seen.clear();
    pref.clear();
    wordset.clear();

    for (auto w : words) {
      wordset.insert(w);
      string s = "";
      for (auto c : w) {
        s += c;
        pref.insert(s);
      }
    }

    int M = board.size(), N = board[0].size();
    for (int i = 0; i < M; i++)
      for (int j = 0; j < N; j++) dfs(board, i, j, "", M, N);

    vector<string> ret;
    for (auto s : seen) ret.push_back(s);
    return ret;
  }
};
```
## Tags

* [Trie](/Collections/trie.md#trie)
* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
