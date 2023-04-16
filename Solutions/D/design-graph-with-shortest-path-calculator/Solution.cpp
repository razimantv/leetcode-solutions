// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph {
 public:
  vector<vector<pair<int, int>>> adj;

  Graph(int n, vector<vector<int>>& edges) {
    adj.resize(n);
    for (auto& e : edges) adj[e[0]].push_back({e[1], e[2]});
  }

  void addEdge(vector<int> edge) { adj[edge[0]].push_back({edge[1], edge[2]}); }
  int shortestPath(int node1, int node2) {
    int inf = 1'000'000'000;
    vector<int> dist(adj.size(), inf);
    dist[node1] = 0;
    auto cmp = [&](int u, int v) {
      if (dist[u] != dist[v]) return dist[u] < dist[v];
      return u < v;
    };
    set<int, decltype(cmp)> djset(cmp);
    djset.insert(node1);
    while (!djset.empty()) {
      int u = *djset.begin();
      if (u == node2) return dist[u];
      djset.erase(djset.begin());
      for (auto [v, w] : adj[u]) {
        int newdist = dist[u] + w;
        if (newdist >= dist[v]) continue;
        if (djset.count(v)) djset.erase(v);
        dist[v] = newdist;
        djset.insert(v);
      }
    }
    return -1;
  }
};
