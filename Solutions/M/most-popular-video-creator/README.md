# Most popular video creator

[Problem link](https://leetcode.com/problems/most-popular-video-creator/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/most-popular-video-creator/

class Solution {
 public:
  vector<vector<string>> mostPopularCreator(vector<string>& creators,
                                            vector<string>& ids,
                                            vector<int>& views) {
    unordered_map<string, tuple<long long, int, string>> seen;
    int n = creators.size();
    for (int i = 0; i < n; ++i) {
      string creator = creators[i], id = ids[i];
      int view = views[i];
      if (!seen.count(creator)) seen[creator] = {0, -1, ""};
      auto& [tot, best, bestid] = seen[creator];
      tot += view;
      if (best < view or (best == view and id < bestid))
        best = view, bestid = id;
    }

    vector<vector<string>> ret;
    long long maxtot = -1;
    for (auto& [k, v] : seen) {
      auto& [tot, best, bestid] = v;
      if (tot > maxtot)
        maxtot = tot, ret = {{k, bestid}};
      else if (tot == maxtot)
        ret.push_back({k, bestid});
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
