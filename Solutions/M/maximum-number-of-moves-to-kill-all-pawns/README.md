# Maximum number of moves to kill all pawns

[Problem link](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

int seen[50][50], dp[1 << 16][16], N, fullmask, inv[1 << 16];
vector<vector<int>> dists;
pair<int, int> neigh[8] = {{1, 2},  {2, 1},  {-1, 2},  {-2, 1},
                           {1, -2}, {2, -1}, {-1, -2}, {-2, -1}};

class Solution {
 public:
  vector<int> get_dists(int x, int y, vector<vector<int>>& positions) {
    memset(seen, -1, sizeof seen);
    queue<pair<int, int>> bfsq;

    seen[x][y] = 0;
    bfsq.push({x, y});

    while (!bfsq.empty()) {
      auto [x, y] = bfsq.front();
      bfsq.pop();

      for (auto [dx, dy] : neigh) {
        int xx = x + dx, yy = y + dy;
        if (xx < 0 or xx >= 50 or yy < 0 or yy >= 50 or seen[xx][yy] != -1)
          continue;
        seen[xx][yy] = seen[x][y] + 1;
        bfsq.push({xx, yy});
      }
    }

    vector<int> ret;
    for (auto& pos : positions) ret.push_back(seen[pos[0]][pos[1]]);
    return ret;
  }

  int work(int mask, int pos, int player) {
    if (mask == fullmask) return 0;
    int& ret = dp[mask][pos];
    if (ret != -1) return ret;

    ret = player ? 0 : (1 << 30);
    int invmask = fullmask ^ mask;
    while (invmask) {
      int nextmask = invmask & -invmask, next = inv[nextmask];
      invmask ^= nextmask;
      int nextval = dists[pos][next] + work(mask | nextmask, next, player ^ 1);
      ret = player ? max(ret, nextval) : min(ret, nextval);
    }
    return ret;
  }
  int maxMoves(int kx, int ky, vector<vector<int>>& positions) {
    for (int i = 0; i < 16; ++i) inv[1 << i] = i;
    positions.push_back({kx, ky});

    dists.clear();
    for (auto& pos : positions)
      dists.push_back(get_dists(pos[0], pos[1], positions));

    N = positions.size();
    fullmask = (1 << N) - 1;
    memset(dp, -1, sizeof dp);
    return work(1 << (N - 1), N - 1, 1);
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Travelling salesman problem](/Collections/graph-theory.md#travelling-salesman-problem)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
