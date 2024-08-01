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

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
