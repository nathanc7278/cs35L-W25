# Little Languages and Scripting

`little language` - small, specialized, to do one thing very well

* domain specific language `DSL` is specialized

`kitchen sink language` one language to rule them all

* `C#`, `java`, `C`, `C++`, `Python`

## The language of POSIX/Linux File Names (Littlest Language)

A file name is a string of bytes, except with some rules:

* `/` is special (directroy seperator)
* `\0` is special (ends file name)

A file name is a sequence of file name components

* each component is a nonempty byte sequence. None of these bytes can be `/` or `\0`

If a file name starts with `/` it's absolute: you start at the root directory to interpret it; otherwise it's relative and you start at the working directory.

`""` empty string is not a valid file name

`////` is another name for `/` becauuse two or more slashes are treated like a single slash.

`../` is a relative file name; the trailing slash means: "this file must be a directory".

## Globbing patterns for the Shell (a Larger Little Language)

`*` match zero or more characters in a file name component. Does not match `.` at the beginning of a file name.

`?` match exactly one character in a file component. Does not match `.` at the beginning of a file name.

`[xyz]` match exactly one character in a file name component that is in the brackets. Brackets do not nest in the normal way.

`[ab[:digit:]cd]` is equivalent to `[ab01234567890cd]`

`[^a-z] caret sign inside bracket is a compliment to whatever is in the brackets. Here it means everything but lowercase ascii characters.

`[]abc]`, `]` at the start of the globbing pattern for an ordinary closing bracket.

`[abc-]`, `-` at the end of the globbing pattern for an ordinary hyphen character.

`[ab?*]`, the question mark and asterist symbols are not special characters within brackets

1. A directory is a tree. A file name specifies a path through that tree. Starts at either root or current directory. File name is a `little program` telling you where to go next. The program counter points to the next file name component the state of the program is: which directory(file) are you at?

2. A globbing pattern is a more complicated program because the instructions contain special characters like `*.?`. Following the instructions are harder. The state of the program is a set of directories, not just a single directory.

3. Regular Expressions (use "grep" command). There are two or more such languages!

* Fixed string `grep -F`
* Ordinary `grep` - basic regular expressions `BREs`
* Extended `grep -E` - extended regular expressions `EREs`

### EREs:

`x` (any ordinary character) matches itself

`.` matches any single character

`PQ` (`P`,`Q` any patterns) matches any instance of `P` then matches any instance of `Q`

`P*` (`P` any pattern) matches 0 or more instances of `P`

`P+` (`P` any pattern) matches 1 or more instances of `P`

`(P)` matches whatever `P` matches to

`(PQ)*` matches 0 or more instances of `PQ`

`P?` matches 0 or 1 instance of `P`

`P{n}` matches `n` instances of `P`

`P{n, k}` matches `n` to `k` instances of `P`

`P{n,}` matches `n` or more instances of `P`

`P|Q` matches any matched pattern of `P` or `Q`

`)` matches itself

`]` matches itself

`[expression]` matches `expression` the same way globbing does

`\x` matches `x` when `x` is a special character

`^P` matches only the start of the line

`P$` matches only at the end of the line

`?=P` positive lookahead, matches if the pattern `P` occurs ahead in the line.

`?!P` negative lookahead, matches if the pattern `P` does not occur ahead in the line.

`?<=P` positive lookbehind, matches if the pattern `P` occurs behind in the line.

`?<!P` negative lookbehind, matches if the pattern `P` does not occur ahead in the line.

**Distributive Law:** `P(Q|R) == (PQ|PR)`

### BREs are like EREs, except:

* `?+{|()}` lose special meaning; they are ordinary. You can escape the characters as substitutes: `\{`, `\}`, `\(`, `\)` are substitutes for `{}()`
* `\2` matches the same string that the 2nd paranthesis matches

#### Regular Expression(R.E) is a little program:

program counter - cursor in R.E.

data - cursor pointing into the input

## The Shell Language:

There are two uses:

1. interactively
2. shell scripts - as if you typed them by hand
    * it has to be executable
    * has to start with a line `#!/bin/sh`

`#!` is special to the OS

`/bin/sh` specifies which `shell` to use

Each instance of a shell is a a seperate process with its own data, input/output, working directory, etc. 

### Shell Syntax

#### Tokens:

`xyzzy` - any word, delimited by non-word characters

#### Special Characters:

`white space` seperates words

`\x` escapes a special character

`xyz xy` string contents (cannot include `'` has a string content)

`$abcdef` variable expansion, just dereferences what is in a variable name

#### Reserved Words:

`{}`

```
get_name() {
   echo "john"
}
```

```
for ((i=0; i<$1; i++)); do
   'command'
done
```

```
while [condition]; do
   'commands'
done
```

```
if [[ condition ]]; then
   'commands'
elif [[ condition ]]; then
   'commands'
else
   'commands'
fi
```
if statements enter the block if the condition is an exit code of 0.

```
case 'i' in
   'condition')
      'command';;
   'condition')
      'command';;
   *)
      'command;;
esac
```

`exit n` quit the script and return an exit code of `n`

#### Variables have String Values

`a='b c d'` declares a variable `a` with contents in the string

`$?` most recent exit status

`$#` number of arguments

`$*` expands the arguments `$1, $2, $3...`. less safe than `$@`. Use with double quotes to handle arguments with white spaces.

`$@` expands the arguments `$1, $2, $3...`. Use with double quotes to handle arguments with white spaces.

`$n` gets argument `n`

`$0` name of the command

`$x` value of the variable `x`

`${x-'default'}` get's `x`'s value unless not initialized. If not initialized then get's `'default'`

`${x+ifset}` get's `x`'s value if `ifset` == true, nothing otherwise

`${x=default}` sets `x` to `default` if unset

`sum=$((5+3))` arithmetic expansion is done with double parenthesis.

`$(seq n k)` outputs the amount of elements in the sequence from `n` to `k`

`-eq` used in conditional statements for `equal to`

`-ne` used in conditional statements for `not equal`

`-gt` used in conditional statemetns for `greater than`

`-ge` used in conditional statemetns for `greater than or equal to`

`-lt` used in conditional statemetns for `less than`

`-le` used in conditional statemetns for `less than or equal to`

