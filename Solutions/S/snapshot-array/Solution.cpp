// https://leetcode.com/problems/snapshot-array/

class SnapshotArray {
 public:
  vector<map<int, int>> history;
  unordered_map<int, int> current;
  int snap_id;
  SnapshotArray(int length)
      : history(length, map<int, int>{{-1, 0}}), snap_id(0) {}

  void set(int index, int val) { current[index] = val; }

  int snap() {
    for (auto& [k, v] : current) history[k][snap_id] = v;
    current.clear();
    return snap_id++;
  }

  int get(int index, int snap_id) {
    auto mit = history[index].upper_bound(snap_id);
    return (--mit)->second;
    return 0;
  }
};
