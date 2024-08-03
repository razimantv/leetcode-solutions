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
using TaggedProblemCollection = std::map<Tag, std::set<Problem>>;
using TaggedHierarchicalCollection =
    std::map<std::string, TaggedProblemCollection>;

Tag get_tag_hierarchy(std::string tag_str) {
  /**
   * Converts a string of tags separated by '>' into a vector of tags.
   * @param tag_str: A string of tags separated by '>'.
   * @return: A vector of tags.
   */
  std::istringstream iss(tag_str);
  Tag ret;
  std::string token;
  while (std::getline(iss, token, '>')) ret.push_back(token);
  return ret;
}

std::string sanitize(std::string str) {
  /**
   * Converts a string to a format that can be used as an anchor in markdown.
   * @param str: The string to be converted.
   * @return: The converted string.
   */
  for (char& c : str) c = isalnum(c) ? tolower(c) : '-';
  return str;
}

std::string readme_filename(std::string parent_tag) {
  /**
   * Converts a parent tag to a markdown filename.
   * @param parent_tag: The tag.
   * @return: The markdown filename.
   */
  return "Collections/" + sanitize(parent_tag) + ".md";
}

std::string create_readme_tagline(Tag& tag) {
  /**
   * Converts a vector of tags into a markdown tagline.
   * @param tag: A vector of tags.
   * @return: A markdown tagline.
   */
  std::string ret;
  for (auto t : tag) {
    if (!ret.empty()) ret += " > ";
    auto tag_label = sanitize(t);
    ret += "[" + t + "](/" + readme_filename(tag[0]) + "#" + tag_label + ")";
  }
  return ret;
}

auto get_code_files(const Dir& problem) {
  /**
   * Returns a set of .cpp/.py/.sh files in a problem directory.
   * @param problem: The problem directory.
   * @return: A set of code files.
   */
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

void process_problem(
    const Dir& problem,
    TaggedHierarchicalCollection& tagged_hierarchical_collection) {
  /**
   * Processes a problem directory and updates the tag map.
   * @param problem: The problem directory.
   * @param tag_map: The tag map.
   */
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
    std::ifstream code_file(file);
    for (std::string str; std::getline(code_file, str);) {
      readme << str << "\n";
    }
    readme << "```";
  }

  if (!exists(problem.path() / "tags")) {
    tagged_hierarchical_collection["Untagged"][{"Untagged"}].insert(
        {problemname, problempath});
  } else {
    std::ifstream tags_file(problem.path() / "tags");
    readme << "\n## Tags\n\n";
    for (std::string tag_str; getline(tags_file, tag_str);) {
      if (tag_str.empty()) continue;
      auto tag = get_tag_hierarchy(tag_str);
      tagged_hierarchical_collection[tag[0]][tag].insert(
          {problemname, problempath});
      readme << "* " << create_readme_tagline(tag) << "\n";
    }
  }
}

void create_readme(std::string filename,
                   TaggedProblemCollection& problem_collection) {
  /**
   * Creates a README file for a tag.
   * @param filename: The filename of the README file.
   * @param problem_collection: The collection of problems for a parent tag
   */
  std::ofstream readme(filename);
  for (std::vector<std::string> prev_tag;
       auto& [tag, problem_list] : problem_collection) {
    unsigned int level = 0;
    for (auto& token : prev_tag) {
      if (level == tag.size() or token != tag[level]) break;
      ++level;
    }
    while (level < tag.size()) {
      auto tag_label = sanitize(tag[level]);
      readme << "\n"
             << std::string(level + 1, '#') << " "
             << "<a id=\"" << tag_label << "\">" << tag[level] << "</a>\n";
      ++level;
    }

    for (auto& [name, path] : problem_list)
      readme << "* [" << name << "](../" << path << ")\n";
    prev_tag = tag;
  }
}

void print_tag_list(TaggedHierarchicalCollection& tag_map) {
  /**
   * Prints the tag list in markdown format.
   * @param tag_map: The tag map.
   */
  for (auto& [parent_tag, tag_collection] : tag_map) {
    auto tag_readme = readme_filename(parent_tag);
    create_readme(tag_readme, tag_collection);
  }
}

int main() {
  fs::current_path("..");
  TaggedHierarchicalCollection tag_map;
  for (const auto& collection : fs::directory_iterator{"Solutions"}) {
    if (!is_directory(collection)) continue;
    for (const auto& problem : fs::directory_iterator{collection})
      if (is_directory(problem)) process_problem(problem, tag_map);
  }

  print_tag_list(tag_map);
  return 0;
}
