# Jump game vii

[Problem link](https://leetcode.com/problems/jump-game-vii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game-vii

class Solution {
 public:
  void update(vector<char>& seg, int node, int l, int r, int L, int R) {
    // std::cout << node << " " << l << " " << r << " " << L << " " << R <<
    // "\n";
    if (l == L and r == R) {
      seg[node] = 1;
      return;
    }
    int M = (L + R) >> 1;
    if (r <= M)
      update(seg, node << 1, l, r, L, M);
    else if (l >= M)
      update(seg, (node << 1) | 1, l, r, M, R);
    else
      update(seg, node << 1, l, M, L, M),
          update(seg, (node << 1) | 1, M, r, M, R);
  }
  bool query(vector<char>& seg, int pos) {
    while (pos) {
      if (seg[pos]) return true;
      pos >>= 1;
    }
    return false;
  }

  bool canReach(string s, int minJump, int maxJump) {
    int N = s.size(), base = 1;
    if (s[N - 1] != '0') return false;
    while (base < N) base <<= 1;
    vector<char> seg(base << 1);
    seg[base] = 1;
    for (int i = 0; i < N; ++i) {
      if (s[i] != '0' or !query(seg, base + i)) continue;
      // cout << i;
      if (i == N - 1) return true;
      if (i + minJump >= N) continue;
      update(seg, 1, i + minJump, min(i + maxJump + 1, N), 0, base);
    }
    return false;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
