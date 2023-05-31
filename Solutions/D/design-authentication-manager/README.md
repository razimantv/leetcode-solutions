# Design authentication manager

[Problem link](https://leetcode.com/problems/design-authentication-manager)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-authentication-manager

class AuthenticationManager {
 public:
  int timeToLive;
  map<string, int> endtime;
  set<pair<int, string>> toremove;

  AuthenticationManager(int timeToLive) : timeToLive(timeToLive) {}

  void generate(string tokenId, int currentTime) {
    endtime[tokenId] = currentTime + timeToLive;
    toremove.insert({endtime[tokenId], tokenId});
  }

  void renew(string tokenId, int currentTime) {
    if (endtime.count(tokenId) and endtime[tokenId] > currentTime) {
      toremove.erase({endtime[tokenId], tokenId});
      endtime[tokenId] = currentTime + timeToLive;
      toremove.insert({endtime[tokenId], tokenId});
    }
  }

  int countUnexpiredTokens(int currentTime) {
    while (!toremove.empty() and toremove.begin()->first <= currentTime) {
      auto [t, token] = *toremove.begin();
      toremove.erase(toremove.begin());
      endtime.erase(token);
    }
    return endtime.size();
  }
};
```
## Tags

* [Design data structure](/README.md#Design_data_structure)
* [Priority queue](/README.md#Priority_queue) > [Key update using insert and remove on C++ set](/README.md#Priority_queue-Key_update_using_insert_and_remove_on_C___set)
