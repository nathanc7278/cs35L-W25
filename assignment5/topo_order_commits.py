#!/usr/bin/env python3
import os
import posixpath
import sys
import zlib



class CommitNode:
    def __init__(self, commit_hash):
        self.commit_hash = commit_hash
        self.parents = set()
        self.children = set()

    def __lt__(self, other):
        return self.commit_hash < other.commit_hash

# ============================================================================
# ======================== Auxiliary Functions ===============================
# ============================================================================


def in_git_directory() -> bool:
    """
    :rtype: bool

    Checks if `topo_order_commits.py` is inside a Git repository.
    """
    for name in os.listdir(os.getcwd()):
        if name == ".git":
            return True
    return False


def get_branch_hash(branch_name: str) -> str:
    """
    :type branch_name: str
    :rtype: str

    Returns the commit hash of the head of a branch.
    """

    if os.path.isdir(branch_name):
        return None
    f = open(branch_name, 'r')
    return f.readline().strip('\n')


def decompress_git_object(commit_hash: str) -> list[str]:
    """
    :type commit_hash: str
    :rtype: list

    Decompresses the contents of a git object and returns a
    list of the decompressed contents.
    """
    with open(commit_hash, 'rb') as file:
        compressed_data = file.read()
        decompressed_data = zlib.decompress(compressed_data)
        decompressed_data = decompressed_data.split(b"\x00", 1)[1]
        decompressed_data = decompressed_data.split(b"\x00", 1)[0]
        return decompressed_data.decode()


# ============================================================================
# =================== Part 1: Discover the .git directory ====================
# ============================================================================

def get_git_directory() -> str:
    """
    :rtype: str
    Returns absolute path of `.git` directory.
    """
    directory = os.getcwd()
    while directory != "/":
        if in_git_directory():
            return f"{directory}"

        os.chdir("..")
        directory = os.getcwd()
    sys.stderr.write("Not inside a Git repository")
    return 1

# ============================================================================
# =================== Part 2: Get the list of local branch names =============
# ============================================================================


def get_branches(path: str) -> list[(str, str)]:
    """
    :type path: str
    :rtype: list[(str, str)]

    Returns a list of tupes of branch names and the commit hash
    of the head of the branch.
    """
    curr_path = os.path.join(".git/refs/heads", path)
    branches = []
    more_branches = []
    if not os.path.isdir(curr_path):
        return []

    for name in os.listdir(curr_path):
        branch_hash = get_branch_hash(posixpath.join(curr_path, name))
        if branch_hash != None:
            branches.append((posixpath.join(path, name), branch_hash))
        else:
            more_branches = get_branches(posixpath.join(path, name))
    return branches + more_branches

# ============================================================================
# =================== Part 3: Build the commit graph =========================
# ============================================================================


def build_commit_graph(branches_list: list[(str, str)]) -> dict[str, CommitNode]:
    """
    :type branches_list: list[(str, str)]
    :rtype: dict[str, CommitNode]

    Iterative builds the commit graph from the list of branches and
    returns a dictionary mapping commit hashes to commit nodes.
    """
    output = {}
    queue = []
    seen = []
    for branch in branches_list:
        queue.append(branch[1])

    while len(queue) != 0:
        if queue[0] not in seen:
            current_node = CommitNode(queue[0])
            output[queue[0]] = current_node
            os.chdir((queue[0])[:2])
            decompressed_data = decompress_git_object((queue[0])[2:])
            decompressed_data = decompressed_data.split("\n\n")[0]
            decompressed_data = decompressed_data.split("\n")
            parents = []
            for line in decompressed_data:
                if "parent" in line:
                    parents.append(line)
            for i in parents:
                hsh = i.split(" ")[1]
                current_node.parents.add(hsh)
                queue.append(hsh)
            seen.append(current_node.commit_hash)
            os.chdir("..")
        queue.pop(0)

    for commit in output.values():
        for parent in commit.parents:
            output[parent].children.add(commit)

    return output

# ============================================================================
# ========= Part 4: Generate a topological ordering of the commits ===========
# ============================================================================


def topo_sort(root_commits: list[CommitNode]) -> list[str]:
    """
    :type root_commits: list[CommitNode]
    :rtype: list[str]

    Generates a topological ordering of the commits in the commit graph.
    The topological ordering is represented as a list of commit hashes. See
    the LA Worksheet for some starter code for Khan's algorithm.
    """
    l = []
    s = []
    indegree = {}
    for commit in root_commits:
        indegree[commit.commit_hash] = len(commit.children)
        if indegree[commit.commit_hash] == 0:
            s.append(commit)


    while len(s) != 0:
        current_node = s.pop(0)
        l.append(current_node.commit_hash)
        for parent in sorted(current_node.parents):
            for commit in root_commits:
                if commit.commit_hash == parent:
                    indegree[commit.commit_hash] -= 1
                    if indegree[commit.commit_hash] == 0:
                        s.append(commit)
                        
    if len(l) < len(root_commits):
        return 1
    else:
        return l

# ============================================================================
# ===================== Part 5: Print the commit hashes ======================
# ============================================================================


def ordered_print(
    commit_nodes: dict[str, CommitNode],
    topo_ordered_commits: list[str],
    head_to_branches: dict[str, list[str]]
):
    """
    :type commit_nodes: dict[str, CommitNode]
    :type topo_ordered_commits: list[str]
    :type head_to_branches: dict[str, list[str]]

    Prints the commit hashes in the the topological order from the last
    step. Also, handles sticky ends and printing the corresponding branch
    names with each commit.
    """


    sticky = False
    for i in range(len(topo_ordered_commits)):
        if sticky:
            sticky = False
            child = ""
            for children in sorted(commit_nodes[topo_ordered_commits[i]].children):
                child += children.commit_hash + " "
            print("=" + child.rstrip())
        branch_print = ""
        for branch in head_to_branches:
            if head_to_branches[branch] == topo_ordered_commits[i]:
                branch_print += (" " + branch)
        print(topo_ordered_commits[i] + branch_print)

        if i + 1 == len(topo_ordered_commits):
            break

        if topo_ordered_commits[i + 1] not in commit_nodes[topo_ordered_commits[i]].parents:
            sticky = True
            parent_print = ""
            for parent in sorted(commit_nodes[topo_ordered_commits[i]].parents):
                parent_print += parent + " "
            print(parent_print.rstrip() + "=\n")








# ============================================================================
# ==================== Topologically Order Commits ===========================
# ============================================================================


def topo_order_commits():
    directory = get_git_directory()
    if directory == 1:
        return 1
    os.chdir(directory)
    branches = get_branches("")         # [(branch, hash)]

    os.chdir("./.git/objects")

    commit_nodes = {}
    commit_nodes = build_commit_graph(branches)   # {hash: CommitNode}


    head_to_branches = {}
    for pair in branches:
        head_to_branches[pair[0]] = pair[1]


    l = topo_sort(list(commit_nodes.values()))
    if l == 1:
        return 1
    else:
        ordered_print(commit_nodes, l, head_to_branches)


# ============================================================================

if __name__ == '__main__':
    topo_order_commits()



'''
Doing the following command:
strace -f pytest | grep 'execve'

gives me no output. So my python program does not inovke any other git commands.
'''
