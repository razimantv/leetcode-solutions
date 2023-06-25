// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
 public:
  vector<int> countServers(int ns, vector<vector<int>>& logs, int x,
                           vector<int>& queries) {
    int n = logs.size(), q = queries.size();
    vector<int> idx(n + q);
    iota(idx.begin(), idx.end(), 0);
    auto time = [&](int i) { return (i < n) ? logs[i][1] : queries[i - n]; };
    sort(idx.begin(), idx.end(), [&](int i, int j) {
      int ti = time(i), tj = time(j);
      return (ti == tj) ? (i < j) : (ti < tj);
    });

    int good{};
    unordered_map<int, int> last;
    set<pair<int, int>> toremove;
    for (int index : idx) {
      int t = time(index);
      while (!toremove.empty() and toremove.begin()->first < t - x) {
        auto [tt, ii] = *toremove.begin();
        toremove.erase(toremove.begin());
        --good;
        last.erase(ii);
      }
      if (index < n) {
        int server = logs[index][0];
        if (last.count(server)) {
          toremove.erase({last[server], server});
          --good;
        }
        toremove.insert({last[server] = t, server});
        ++good;
      } else {
        queries[index - n] = ns - good;
      }
    }
    return queries;
  }
};
