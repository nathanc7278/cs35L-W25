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

`git log 

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
