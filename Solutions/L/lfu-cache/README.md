# Lfu cache

[Problem link](https://leetcode.com/problems/lfu-cache/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lfu-cache/

class LFUCache {
 public:
  unordered_map<int, tuple<int, int, int>> val_freq_time;
  set<tuple<int, int, int>> s;
  int time, capacity;
  LFUCache(int capacity) : time(0), capacity(capacity) {}

  int get(int key) {
    if (!capacity) return -1;
    auto mit = val_freq_time.find(key);
    if (mit == val_freq_time.end()) return -1;
    auto& [v, f, t] = mit->second;
    s.erase({f, t, key});
    ++f;
    t = ++time;
    s.insert({f, t, key});
    return v;
  }

  void put(int key, int value) {
    if (!capacity) return;

    auto mit = val_freq_time.find(key);
    auto& [v, f, t] = val_freq_time[key];
    if (mit == val_freq_time.end()) {
      if (s.size() == capacity) {
        auto [fr, tr, kr] = *s.begin();
        val_freq_time.erase(kr);
        s.erase(s.begin());
      }
    } else {
      s.erase({f, t, key});
    }

    v = value;
    ++f;
    t = ++time;
    s.insert({f, t, key});
  }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
