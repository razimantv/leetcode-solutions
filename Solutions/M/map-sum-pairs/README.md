# Map sum pairs

[Problem link](https://leetcode.com/problems/map-sum-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/map-sum-pairs

class MapSum {
 public:
  /** Initialize your data structure here. */

  unordered_map<string, int> m;
  MapSum() {}

  void insert(string key, int val) { m[key] = val; }

  int sum(string prefix) {
    int tot = 0, l = prefix.size();
    for (auto& [k, v] : m) {
      if (k.size() < l) continue;
      if (k.compare(0, l, prefix) == 0) tot += v;
    }
    return tot;
  }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```
## Tags

* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
* [Hashmap](/Collections/hashmap.md#hashmap)
