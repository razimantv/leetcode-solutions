# Number of ways to assign edge weights ii

[Problem link](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)

## Reduction to finding path length

We need to count the number of ways to assign weights 1 or 2 to the edges between $u$ and $v$ such that the sum of weights is odd. If there are $d$ such edges, we can assign $d-1$ of them however we want. The odd sum then forces the value of the last edge.

- If $d = 0$, the answer is $0$.
- If $d > 0$, the answer is $2^{d-1} \pmod{10^9+7}$.

## Key Observations

1. **Path Distance in Trees**:
   The distance between any two nodes $u$ and $v$ in a rooted tree can be calculated using their depths and their **Lowest Common Ancestor (LCA)**:
   $$\text{dist}(u, v) = \text{depth}[u] + \text{depth}[v] - 2 \cdot \text{depth}[\text{LCA}(u, v)]$$
   Where $\text{depth}[x]$ is the distance from the root to node $x$.

2. **Query Efficiency**:
   Since we have multiple queries, we cannot afford to find the path by traversing the tree for each query. We need an efficient way to find the LCA. **Binary Lifting** allows us to find the LCA of any two nodes in $O(\log N)$ time after an $O(N \log N)$ preprocessing step.

## Algorithm

The algorithm is divided into three main parts: **Preprocessing**, **Binary Lifting Setup**, and **Answering Queries**.

### 1. Preprocessing (DFS)
We pick an arbitrary node (e.g., node $0$) as the root of the tree. We run a Depth-First Search (DFS) to:
- Compute the `depth` of each node.
- Identify the immediate parent of each node, which is stored in `par[0][u]`.

### 2. Binary Lifting Table Construction
To find the LCA in logarithmic time, we precompute the $2^i$-th ancestor for every node.
Let `par[i][u]` be the $2^i$-th ancestor of node `u`. 
We can compute this iteratively using the relation:
$$\text{par}[i][u] = \text{par}[i-1][\text{par}[i-1][u]]$$
This step takes $O(N \log N)$ time.

### 3. Finding the LCA
To find the LCA of $u$ and $v$:

1. **Equalize Depths**: If $\text{depth}[u] \neq \text{depth}[v]$, lift the deeper node up until both nodes are at the same depth. If $u$ and $v$ are now the same node, then this node is the LCA.
2. **Simultaneous Lift**: If they are not the same, lift both nodes up simultaneously as high as possible without them merging. We do this by iterating $i$ from the largest power of 2 down to $0$. If `par[i][u] != par[i][v]`, we set $u = \text{par}[i][u]$ and $v = \text{par}[i][v]$. After ths [process, $u$ and $v$ will be direct children of the LCA. Thus, the LCA is `par[0][u]`.

## Complexity Analysis

- **Time Complexity**:
  - **DFS & Graph Construction**: $O(N)$ as we traverse each node and edge once.
  - **Binary Lifting Table**: $O(N \log N)$ since we have $N$ nodes and $\approx \log_2(N)$ levels.
  - **Queries**: $O(Q \log N)$ where $Q$ is the number of queries. Each LCA query takes $O(\log N)$ steps because we jump up the tree using powers of 2.
  - **Total Time Complexity**: $\mathcal{O}((N + Q) \log N)$, which is highly efficient and easily runs within typical time limits (e.g., 1–2 seconds for $N, Q \le 10^5$).

- **Space Complexity**:
  - $\mathcal{O}(N \log N)$ to store the binary lifting table `par`.

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

const int nmax = 100000, mod = 1000000007;
vector<int> modpow;

class Solution {
public:
  vector<vector<int>> adj, par;
  vector<int> depth;

  vector<int> assignEdgeWeights(vector<vector<int>> &edges,
                                vector<vector<int>> &queries) {
    if (modpow.empty()) {
      modpow.push_back(1);
      for (int i = 0; i < nmax; ++i) {
        int x = modpow.back() << 1;
        if (x > mod)
          x -= mod;
        modpow.push_back(x);
      }
    }
    int n = edges.size() + 1;
    adj.resize(n);
    for (auto &e : edges) {
      int u = --e[0], v = --e[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    function<void(int, int)> dfs = [&](int u, int par) {
      for (int v : adj[u]) {
        if (v == par)
          continue;
        this->par[0][v] = u;
        depth[v] = depth[u] + 1;
        dfs(v, u);
      }
    };

    par = {vector<int>(n)};
    depth.resize(n);

    par[0][0] = -1;
    depth[0] = 0;
    dfs(0, -1);

    for (int i = 0, good = 1; good; ++i) {
      good = 0;
      par.push_back(vector<int>(n));
      for (int u = 0; u < n; ++u) {
        int pi = par[i][u];
        par[i + 1][u] = (pi == -1) ? -1 : par[i][pi];
        if (par[i + 1][u] != -1)
          good = 1;
      }
    }

    auto lca = [&](int u, int v) {
      if (depth[u] < depth[v])
        swap(u, v);
      int delta = depth[u] - depth[v];
      for (int i = par.size() - 1; i >= 0; --i)
        if (delta & (1 << i))
          u = par[i][u];
      if (u == v)
        return u;

      for (int i = par.size() - 1; i >= 0; --i)
        if (par[i][u] != par[i][v])
          u = par[i][u], v = par[i][v];
      return par[0][u];
    };

    vector<int> ret;
    for (auto &q : queries) {
      int u = --q[0], v = --q[1], w = lca(u, v);
      int d = depth[u] + depth[v] - 2 * depth[w];
      ret.push_back(d ? modpow[d - 1] : 0);
    }
    return ret;
  }
};
```
## Tags

* [Binary lifting](/Collections/binary-lifting.md#binary-lifting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Lowest common ancestor](/Collections/graph-theory.md#lowest-common-ancestor)
* [Tutorials](/Collections/tutorials.md#tutorials)
