# Time based key value store

[Problem link](https://leetcode.com/problems/time-based-key-value-store)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/time-based-key-value-store

class TimeMap {
  unordered_map<string, map<int, string, greater<int>>> store;

 public:
  TimeMap() {}

  void set(string key, string value, int timestamp) {
    store[key][timestamp] = value;
  }

  string get(string key, int timestamp) {
    auto mit = store.find(key);
    if (mit == store.end()) return "";
    auto mit2 = mit->second.lower_bound(timestamp);
    if (mit2 == mit->second.end())
      return "";
    else
      return mit2->second;
  }
};

```