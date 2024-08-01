# Design underground system

[Problem link](https://leetcode.com/problems/design-underground-system)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-underground-system

class UndergroundSystem {
 public:
  unordered_map<string, int> stationmap;
  unordered_map<int, pair<int, int>> userstatus;
  map<pair<int, int>, pair<int, double>> travelstats;

  UndergroundSystem() {}

  void checkIn(int id, string stationName, int t) {
    int station;
    if (stationmap.count(stationName))
      station = stationmap[stationName];
    else
      station = stationmap[stationName] = stationmap.size();
    userstatus[id] = {station, t};
  }

  void checkOut(int id, string stationName, int t) {
    int station;
    if (stationmap.count(stationName))
      station = stationmap[stationName];
    else
      station = stationmap[stationName] = stationmap.size();

    auto [start, tstart] = userstatus[id];
    auto &[cnt, ttot] = travelstats[{start, station}];
    ++cnt;
    ttot += t - tstart;
  }

  double getAverageTime(string startStation, string endStation) {
    auto [cnt, ttot] =
        travelstats[{stationmap[startStation], stationmap[endStation]}];
    return ttot / cnt;
  }
};
```
## Tags

* [Averaging from total and count](/Collections/averaging-from-total-and-count.md#averaging-from-total-and-count)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Coordinate compression](/Collections/hashmap.md#coordinate-compression)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
