#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <unordered_set>
#include <vector>

namespace fs = std::filesystem;
using Dir = fs::directory_entry;
using Tag = std::vector<std::string>;
using Problem = std::pair<std::string, std::string>;

Tag get_tag_hierarchy(std::string tag_str) {
  std::istringstream iss(tag_str);
  Tag ret;
  std::string token;
  while (std::getline(iss, token, '>')) ret.push_back(token);
  return ret;
}

std::string sanitize(std::string str) {
  for (char& c : str)
    if (!isalnum(c)) c = '_';
  return str;
}

std::string create_readme_tagline(Tag& tag) {
  std::string ret;
  for (std::string tag_label; auto t : tag) {
    if (!ret.empty()) {
      ret += " > ";
      tag_label += "-";
    }
    tag_label += sanitize(t);
    ret += "[" + t + "](/README.md#" + tag_label + ")";
  }
  return ret;
}

auto get_code_files(const Dir& problem) {
  std::set<std::pair<std::string, fs::path>> codefiles;
  const std::unordered_set<std::string> code_extensions{".cpp", ".py", ".sh"};
  for (const auto& file : fs::directory_iterator{problem}) {
    std::string ext;
    if (file.is_regular_file() and file.path().has_extension() and
        code_extensions.count(ext = file.path().extension()))
      codefiles.insert({ext, file.path()});
  }
  return codefiles;
}

void process_problem(const Dir& problem,
                     std::map<Tag, std::set<Problem>>& tag_map) {
  std::string problemname = problem.path().filename(),
              problempath = problem.path().string();
  for (char& c : problemname)
    if (c == '-') c = ' ';
  problemname[0] = toupper(problemname[0]);
  if (exists(problem.path() / "README.md.base"))
    copy_file(problem.path() / "README.md.base", problem.path() / "README.md",
              fs::copy_options::overwrite_existing);

  std::ofstream readme(problem.path() / "README.md", std::ios::app);

  readme << "\n## Solutions\n\n";
  for (const auto& [ext, file] : get_code_files(problem)) {
    readme << "\n### " << file.filename().string() << "\n";
    readme << "```" << ext.substr(1) << "\n";
    std::ifstream code_file (file);
    for (std::string str; std::getline(code_file, str);) {
      readme << str << "\n";
    }
    readme << "```";
  }

  if (!exists(problem.path() / "tags")) {
    tag_map[{"Untagged"}].insert({problemname, problempath});
  } else {
    std::ifstream tags_file(problem.path() / "tags");
    readme << "\n## Tags\n\n";
    for (std::string tag_str; getline(tags_file, tag_str);) {
      if (tag_str.empty()) continue;
      auto tag = get_tag_hierarchy(tag_str);
      tag_map[tag].insert({problemname, problempath});
      readme << "* " << create_readme_tagline(tag) << "\n";
    }
  }
}

void print_tag_list(std::map<Tag, std::set<Problem>>& tag_map) {
  std::cout << "\n# Problems by tags\n";
  std::unordered_set<std::string> bad_tags{"Suboptimal solution", "Fraud",
                                           "Untagged"};
  for (std::vector<std::string> prev_tag; auto& [tag, problemlist] : tag_map) {
    if (bad_tags.count(tag[0])) continue;
    unsigned int level = 0;
    std::string tag_label;
    for (auto& token : prev_tag) {
      if (level == tag.size() or token != tag[level]) break;
      if (!tag_label.empty()) tag_label += '-';
      tag_label += sanitize(tag[level]);
      ++level;
    }
    while (level < tag.size()) {
      if (!tag_label.empty()) tag_label += '-';
      tag_label += sanitize(tag[level]);
      std::cout << "\n"
                << std::string(level + 2, '#') << " "
                << "<a name=\"" << tag_label << "\">" << tag[level] << "</a>\n";
      ++level;
    }

    for (auto& [name, path] : problemlist)
      std::cout << "* [" << name << "](" << path << ")\n";
    prev_tag = tag;
  }
  for (auto tag : bad_tags) {
    std::cout << "\n## " << tag << "\n";
    for (auto& [name, path] : tag_map[{tag}]) {
      std::cout << "* [" << name << "](" << path << ")\n";
    }
  }
}

int main() {
  fs::current_path("..");
  std::map<Tag, std::set<Problem>> tag_map;
  for (const auto& collection : fs::directory_iterator{"Solutions"}) {
    if (!is_directory(collection)) continue;
    for (const auto& problem : fs::directory_iterator{collection})
      if (is_directory(problem)) process_problem(problem, tag_map);
  }

  print_tag_list(tag_map);
  return 0;
}
