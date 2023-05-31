# Lru cache

[Problem link](https://leetcode.com/problems/lru-cache)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lru-cache

class LRUCache {
 public:
  set<pair<int, int>> old;
  map<int, int> val, time;
  int t, cap;
  LRUCache(int capacity) {
    cap = capacity;
    t = 0;
  }

  int get(int key) {
    if (val.count(key) == 0) return -1;
    old.erase({time[key], key});
    old.insert({time[key] = t++, key});
    return val[key];
  }

  void put(int key, int value) {
    if (time.count(key)) {
      old.erase({time[key], key});
    }

    val[key] = value;
    old.insert({time[key] = t++, key});

    if (old.size() > cap) {
      auto p = *old.begin();
      old.erase(old.begin());
      val.erase(p.second);
      time.erase(p.second);
    }
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
## Tags

* [Design data structure](/README.md#Design_data_structure)
* [Priority queue](/README.md#Priority_queue) > [Key update using insert and remove on C++ set](/README.md#Priority_queue-Key_update_using_insert_and_remove_on_C___set)
* [Hashmap](/README.md#Hashmap)
