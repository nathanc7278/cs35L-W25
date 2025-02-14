# Version Control

* keeps a history of what a project used to be
* history contains a useful subset of content, not everything

### Purposes

* contains a backup
* answers "why is this here?":
    * look at related code (changed at same time)
    * look at commit message
    * look at bug reports
    * software archaeology (look at records of code changes)
* to-do list
* can contain possible lines of development: for example
    * c++ package
    * browser extension
* can contain urgent vs longterm tasks

## Git

* object database repository
    * persistent objects that live in secondary storage
    * atomic updates to collections of objects. This makes sure that an operation is completely executed or not executed at all. No half updates to a repository.
* index (cache) records the plans for the future
    * creating commits
    * manage merges
    * cache data

### Getting Started

`git init` starts a project from scratch

from an existing repository:

`git clone https://git.sv.gnu.org/git/diffutils.git` this clones everything including history of this repo

`git clone diffutils diff-tmp` you can clone locally as well

Cloning locally is much faster. Most of the repo is alreading in the local environment. So cloning it will create hard links to existing files.

files in `.git/objects` are read only and do not ever change.

`git add "filename"` saves changes to plans for the future

`git commit` will prompt for a message

* the first line is the message, it should be 50 characters or less
* the second line should be left blank
* extra details can come after the empty line

`HEAD` is the most recent commit

`index` is the plan for next commit

`working files` is what your compiler sees

All of these type of files can be different at the same time.

`git diff` shows the changes made from working files and index

`git diff HEAD` compares HEAD and working files

`git diff --cached` compares index and HEAD

`git log` shows the complete history of all your commits

`git log --summary` gives slightly more information

`git log --pretty=fuller` gives more information on the git log

`git log -S "pattern"` searches for the specific commit a pattern was introduced

`git log --pretty=format:" identifiers"` will show git log with specific identifiers:

* `%H` commit hash
* `%h` abbreviated commit hash
* `%T` Tree hash
* `%t` Abbreviated tree hash
* `%P` Parent hashes
* `%p` Abbreviated parent hashes
* `%an` Author name
* `%ae` Author email
* `%ar` Author date, relative
* `%cn` Committer name
* `%ce` Committer email
* `%cd` Committer date
* `%cr` Committer date, relative
* `%s` Subject

`git log --graph` shows an ascii graph of the commit history

Git commits can be represented as a directed graph:

```mermaid
    graph RL
        37@{shape: circle} --...--> 3@{shape: circle} --> 2@{shape: circle} --> 1@{shape: circle}
        HEAD ---> 37
        style 1 fill:#290
        style 2 fill:#290
        style 3 fill:#290
        style 37 fill:#290
        style HEAD fill:#237
```

`cryptographically "secure" checksum` different ways to combine digits of a sequence to generate a unique ID without collisions.

Git uses `SHA-1` or secure hash algorithm 1. 

`git log commitID` will include all commits up to and including the commit in the log

`git log commitID1..commitID2` will show commits in a range

Instead of commitID you can use HEAD

* `C^` is equivalent to C's parent
* `C^^` is equivalent to C's parent's parent
* `C~3` is equivalent to `C^^^`
* `C^2` is C's second parent

`git diff HEAD^..HEAD` and `git diff HEAD^!` show change of previous commit and current version

history is immutable in Git. Commits cannot be changed once they are made

`git status` shows the current status of changes

`git grep "P"` matches all patterns in the current version

`git ls-files` shows all files that are in version controls

`.gitignore` file contains a list of file name patterns for Git to ignore. We do not want to put these type of files into version control.

Creating a directed graph between two commits. The graph should include commit ID, author, and committer if it is different from author

```
git log --graph --pretty=format:"%H:%an:%cn" \
c03bee6e9f5c05259f5f501e1f47cd8adb63af38 2a7d63a2453e2c30353342a2c9385fa22a846987 \
| awk -F':' '{if ($2 == $3) print $1, $2; else print $0}' | tr ':' ' '
```

`git push` to send commits from local repository to github

`git pull` to take changes from github and put them into local repo

`git merge "branch"` this merges the changes from the branch with the branch you are currently located.

`git checkout "branch or commit"` this detaches HEAD and puts the cursor at the commit or branch

`git checkout -b "branch name" "location"` creates a new branch and puts the cursor at location
