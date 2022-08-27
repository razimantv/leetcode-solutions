#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>

int main() {
  using namespace std::filesystem;
  current_path("../Solutions");

  std::map<std::string, std::set<std::pair<std::string, std::string>>>
      tagmap;
  for (auto const& collection : directory_iterator{"."}) {
    if (!is_directory(collection)) continue;
    for (auto const& problem : directory_iterator{collection}) {
      if (!is_directory(problem)) continue;
      std::string problemname = path(problem).filename();
      std::string problempath =
          path(collection).filename() / path(problem).filename();
      for (char& c : problemname)
        if (c == '-') c = ' ';
      problemname[0] = toupper(problemname[0]);
      if (!exists(path(problem) / "tags")) {
        tagmap["Untagged"].insert({problemname, problempath});
        continue;
      }
      std::ifstream tagsfile(path(path(problem) / "tags"));
      for (std::string tag; getline(tagsfile, tag);) {
        tagmap[tag].insert({problemname, problempath});
      }
    }
  }

  std::cout << "\n# Problems by tags\n";
  for (auto& [tag, problemlist] : tagmap) {
    if (tag == "Untagged") continue;
    std::cout << "\n## " << tag << "\n";
    for (auto& [name, path] : problemlist) {
      std::cout << "* [" << name << "](Solutions/" << path << ")\n";
    }
  }
  std::cout << "\n## Untagged\n";
  for (auto& [name, path] : tagmap["Untagged"]) {
    std::cout << "* [" << name << "](Solutions/" << path << ")\n";
    }
  return 0;
}
