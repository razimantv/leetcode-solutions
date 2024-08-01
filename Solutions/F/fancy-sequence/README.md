# Fancy sequence

[Problem link](https://leetcode.com/problems/fancy-sequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fancy-sequence

class Fancy {
 public:
  const int base = 131072, MOD = 1'000'000'007;
  vector<pair<int, int>> seg;
  int N;

  Fancy() {
    seg = vector<pair<int, int>>(base * 2, {1, 0});
    N = 0;
  }

  void append(int val) { seg[N++ + base] = {0, val}; }

  void update(int node, int L, int R, int l, int r, long long mult,
              long long add) {
    if (L == l and R == r) {
      seg[node].first = (seg[node].first * mult) % MOD;
      seg[node].second = (seg[node].second * mult + add) % MOD;
      return;
    } else if (L > r or R < l)
      return;

    int M = (L + R) >> 1;
    if (r <= M)
      update(node << 1, L, M, l, r, mult, add);
    else if (l > M)
      update((node << 1) | 1, M + 1, R, l, r, mult, add);
    else {
      update(node << 1, L, M, l, M, mult, add);
      update((node << 1) | 1, M + 1, R, M + 1, r, mult, add);
    }
  }

  void addAll(int inc) { update(1, 0, base - 1, 0, N - 1, 1, inc); }

  void multAll(int m) { update(1, 0, base - 1, 0, N - 1, m, 0); }

  int getIndex(int idx) {
    if (idx >= N) return -1;
    long long ret = 0;
    for (int pos = base + idx; pos; pos >>= 1)
      ret = (ret * seg[pos].first + seg[pos].second) % MOD;
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Composition of operations](/Collections/mathematics.md#composition-of-operations)
