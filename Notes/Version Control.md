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

Plumbing vs Porcelain commands

`Plumbing` commands refer to low level commands of git. Usually, you should not touch these commands unless you are a git expert.

`Porcelain` commands are the high level commands that you may use daily.

One example of a plumbing command is `git show HEAD`

## Navigating .git directory:

`.git/branches` is a directory that is obselete. It is left there for backward compatibility for older repositories. It was abandoned because it was too slow to store branches in a directory.

`.git/config` tells you info needed to access the repository

`git config` command is a better way to edit the `.git/config` because it has safety features.

`git config -l` displays the config file

`.git/description` is also obselete

`.git/HEAD` is a pointer to where current commit is

`.git/hooks` contains shell scripts that act as a sample for what you can put there

* these change how git behaves
* file names are specified by git

`.git/index` is the file that keep track of the changes needed to do in the future. This also keeps a cache for current changes.

`.git/info/exclude` lists files that need to be excluded

`.gitignores` is a working file under git control

* `/dirname` is relative to current directory, not absolute when written in `.gitignore`
* `filename` will ignore any file with the name `filename` in the git repository 

`.git/logs` contains a metahistory

`.git/objects` is where git keeps every change

* this is an object orientated database
* ext2 was originally used for managing entries in `.git/objects`
    * this operation was slow to add/remove entries `O(n^2)`
    * the way they counteracted this was by looking at only first two char of file name. There could only be 256 entries because there are 16 char per hex

under `.git/objects/info`

* there is a commit-graph
* there are packs which lists our packs (when we have files that are too large)

`.git/refs/heads` contains the branches of a git repo

`.git/refs/packsref` stores refereences to packs

### git objects

The simplest object in git is called a `blob`. Each blob is a sequence of bytes

`git hash-object --stdin` computes thhe hash or checksum of standard input

`git hash-object --stdin -w` computes the hash and goes into repository to create an object with that hash. This object is a blob

Say the has is `c5e75...`

the object is contained in `.git/objects/c5/e75...`

`git cat-file -p "hash"` prints out the contents of a blob

`git cat-file -t "hash"` gives the object's type

Both the object's type and content are immutable

The next simplest object is a `tree`. It is similar to a linux directory. It maps names to IDs, type, and mode.

* you can only create a tree for objects that already exist
* trees cannot be changed once it is made

`git catfile -p 'master^{tree}` prints out the table consisting of mode, type, ID, name

`git update-index --add --cacheinfo '1000644m, 98f88..., aenid.txt` adds an entry into a tree

`git write tree` 

The last object is a `commit` object. It specifies a tree, parent of commit, and other details.

### Compression in git repo

* save space and secondary storage
* save time in accessing

Git uses:

* Huffman coding + sender(compressor) tells recipient(decompressor) what popularities are
* Dictionary Compression

`Huffman Coding` communicate symbols as a sequence of bits. This byte can have variable bit width encoding

1. Start from least occuring character and combine them into a subtree.
2. Repeat this and you will get a binary tree that contains the encoding

`Adaptive Huffman Coding` Both sender and recipient has empty binary tree that gets updated as every character is read. This is faster than going through the file once for reading frequencies and then another time for sending.

`git fetch` brings local repository in sync with remote

2 branches:

* master `current working repo`
* origin/master `remote repo`

`git pull` is equivalent to git fetch + git merge

`git remote` shows current remote

`git remote -v` shows URLs used to fetch/push

`git remote show origin` shows more about origin

## Tags

each commit has a confusing name (commit_hash)

* a text file contained in a repository has tags (version, commit_hash) tuple
    * this is not done because someone has to maintain this file, prone to error

`git tag` will show all names that reference to commit

`git tag -a cs35-L -m"demo for class" HEAD^` creates a tag in a local repository

## Branches

`branch` is a lightweight movable pointer to a commit. Branch updates to head when you do a commit on that branch

`git branch` displays the branch in a git repo

`git checkout "branch-name"` changes your current branch to "branch-name"

#### Reasons for a branch:

* maintenence of older version
* developing a new feature (or bug fix)
* forking due to a dispute (rare)

`merge commit` is a commit that has 2 or more parents

* the goal of this is to combine the best features of each branch
* may have collisions during a merge

The angle brackets in a merge message will show collisions. Note that if there are no angle brackets, there could still be errors in the merged code.

`backporting/cherrypicking` picking some features/bug fixes from main branch and copying it into a branch (also called `rebase`)

`git rebase "branch"` moves all changes from currently checked out branch to "branch". This is similar to merging, but the graph will be linear compared to a merge.

Merging tells more about history; Rebasing has simpler histories

`git rebase -i "commit"` lets you interact with editor to edit the commits you want to rebase.

* this command would not make sense if there was no -i option. If you are rebasing/merging from current branch, nothing would change because it is the same branch.

Note: Do not rebase things in remote. Only rebase stuff taht is not pushed. Doing a rebase on remote will confuse other developers.

`git push` put commits from your repo to remote's repo. This is opposite of git fetch

`git blame "file"` displays whos made the change of a line on a file
