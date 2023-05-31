# Snapshot array

[Problem link](https://leetcode.com/problems/snapshot-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/snapshot-array

class SnapshotArray {
 public:
  vector<vector<pair<int, int>>> db;
  int N, snapid;

  SnapshotArray(int length) {
    N = length;
    db = vector<vector<pair<int, int>>>(N, vector<pair<int, int>>(1, {0, 0}));
    snapid = 0;
  }

  void set(int index, int val) {
    auto& [i, v] = db[index].back();
    if (i == snapid)
      v = val;
    else
      db[index].push_back({snapid, val});
  }

  int snap() { return snapid++; }

  int get(int index, int snap_id) {
    auto vit = lower_bound(db[index].begin(), db[index].end(),
                           make_pair(snap_id + 1, -1));
    return (--vit)->second;
  }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
```