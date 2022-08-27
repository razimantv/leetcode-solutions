#include <filesystem>
#include <iostream>

int main() {
  using namespace std::filesystem;
  current_path("../Solutions");
  for (auto const& collection : directory_iterator{"."}) {
    if (!is_directory(collection)) continue;
    for (auto const& problem : directory_iterator{collection}) {
      if (!is_directory(problem) or !exists(path(problem) / "tags")) continue;
      std::cout << problem << '\n';
    }
  }
  return 0;
}

