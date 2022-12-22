class FileSystem(object):
    """
    Design and implement a simple in-memory file system abstraction with directories and files.
    You'll only implement mkdir;

    mkdir /foo => ok
    mkdir /foo/bar => ok
    mkdir /foo/bar/baz => ok
    mkdir /bar => ok
    mkdir /foo/bar => error (/foo/bar already exists)
    mkdir /baz/foo => error (no /baz directory found)
    mkdir /foo/baz/bar => error (no /foo/baz directory found)
    """

    class Directory:

        def __init__(self, name):
            self.name = name
            self.sub_dirs = {}

    def __init__(self, structure: dict or Directory = None):
        self.structure = structure if structure else {}

    # String approach, implemented at the interview:
    def mkdir(self, path):
        path_list = path.split("/")[1:]
        curr_dir = self.structure
        if len(path_list) == 1:
            if path_list[0] in curr_dir:
                return "Error: Directory already exists!"
            else:
                self.structure[path_list[0]] = {}
        for i, f_name in enumerate(path_list):
            if i == 0:
                if f_name not in curr_dir:
                    return f"Error: No directory '{f_name}' found!"
            else:
                if f_name not in curr_dir and i != len(path_list) - 1:
                    return f"Error: No directory '{f_name}' found!"
            if i != len(path_list) - 1:
                curr_dir = curr_dir[f_name]
            elif len(path_list) != 1:
                if f_name in curr_dir:
                    return "Error: Directory already exists!"
                else:
                    curr_dir[f_name] = {}
        return "OK"

    # Graph approach:
    def mkdir_graph_approach(self, path):

        def _mkdir(_parent_dir, _path_list):
            current_dir_name = _path_list.pop(0)
            if _path_list:
                current_dir = _parent_dir.sub_dirs.get(current_dir_name, None)
                if not current_dir:
                    return f"Error: No directory '{current_dir_name}' found!"
                else:
                    return _mkdir(current_dir, _path_list)
            elif _parent_dir.sub_dirs.get(current_dir_name, None):
                return "Error: Directory already exists!"
            else:
                _parent_dir.sub_dirs[current_dir_name] = self.Directory(current_dir_name)
                return "OK"

        path_list = path.split("/")[1:]
        parent_dir = self.structure
        return _mkdir(parent_dir, path_list)


def are_there_bad_words(sentence, bad_words_list):
    """
    Question: An engineer wants to improve their word choice by removing usages of words like “basically” or “like”
    from the things they write. Write a plugin for something like Grammarly that will detect when a given text uses
    certain, prohibited words.
    Any usage of the word should alert the engineer (don’t need to worry about misspellings).
    """

    found_bad_words_list = []
    is_found = False
    for bad_word in bad_words_list:
        if bad_word.upper() in sentence.upper():
            found_bad_words_list.append(bad_word) if bad_word not in found_bad_words_list else None
            is_found = True
    if is_found:
        return f"The sentence has the following bad words: {str(found_bad_words_list)[1:-1]}. Consider correcting"
    else:
        return f"The sentence has no bad words. Good job!"


def test_manual_links(text):
    """
    Check all links in the markdown text resolve to a heading on the page.
    """

    import re
    link_format = r"\[.*\]\(.*\)"
    links_list = re.findall(link_format, text)
    bad_links = []
    for link in links_list:
        stripped_link_format = r"\]\(.*\)"
        [stripped_link] = re.findall(stripped_link_format, link)
        link_only = stripped_link[2:-1]
        if link_only[0] == "#":
            link_text = link_only[1:]
            link_words = link_text.split("-")
            link_re_string = f"#+.{'.'.join(link_words)}"
            bad_links.append(link_only) if not re.findall(link_re_string, text.lower()) else None
        #  TODO: this can be updated with if scenarios for other types of headings/anchors, other than #
        else:
            bad_links.append(link_only)
    if bad_links:
        return f"Warning, no heading found for: {', '.join(bad_links)}"
    else:
        return "Everything looks cool"
