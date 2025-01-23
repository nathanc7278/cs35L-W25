# Elisp and Python Scripting Languages

`Elisp`, which stands for Emacs Lisp is an extension language of Emacs.

## Basic Lisp: 

`C-j` to evaluate a line.

### Atomic values

* numbers - self evaluating
* strings - self evaluating
* symbols - `'expression`, non-self evaluating

`(setq variable value)`, sets a variable to a value. This is a `special form`. It is not a function.

`conses` are a pair of elements. Conses can be used to create lists.

`(cons expr expr)` to create a cons.

To make a list you can do:

`(cons 'A(cons 'B(cons 'C nil)))`

The following are function calls:

`(car expr)` accesses the first element

`(cdr expr)` accesses the second element

`eval program` executes the program in lisp


This is a special form, `(defun f (a b c) ("code involving a b c"))`

`M-:` to evaluate Lisp in minibuffer

`(global-set-key "keystroke" 'command)` changes a keystroke to a certain command.

`C-]` closes the debugger in Lisp.

## Python:

Every value in Python is an object. Every Python object has three things:

1. identitiy (address) - use `id()` to access identity. This is immutable.
2. type - use `type()` to access type. This is immutable.
3. value - this can change if the object is mutable

Lists are `mutable` or changeable, while tuples are `immutable`.

Objects may also have:

* attributes
* methods

Using the expression `a is b` compares the ids of the two objects while using `a == b` compares the two values.

Python builtin types:

* `None` - nullptr
* numbers - int, float, ...
* sequences - string, tuples, lists, ...

### Sequence Operations:

The following operations make a copy of a sequence:

* `s[i]` accesses the index of a sequence. `-1` index accesses the last index of s.
* `s[i;j]` accesses the range of indices from `i` to `j` not including `j`.
* `s[i:]` accesses from `i` to the end of sequence.
* `s[:j]` accesses from beginning to `j` of the sequence.
* `s[:]` the whole sequence

Example:

X = s[], if you change X, s[] will also change.

Y = s[:], if you change Y, s[] will not change.

`len(s)` returns the length of a sequence

`min(s)` returns minimum

`max(s)` returns maximum

`list(s)` turns any sequence into a list

Mutable Sequences:

`s[i] = v` changes the val at `s[i]` to `v`

`s[i:j] = s1` changes the range from i to j with values in s1

`del s[i]` returns an empty sequence

### List Operations:

`s.append(v)` appends `v` to the end of a list. This operation is `O(1) amortized`. When n = space alloced, append asks for more memory so the list copies itself to memory that has 2x the current memory.
