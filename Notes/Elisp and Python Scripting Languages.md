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

* additionally the keystroke can also be `(kbd "C-x C-a")` to change a keybind to C-x C-a without escaping the control characters.

To edit a configuration file: we enter the `~/.emacs.d/init.el` and enter any commands that we want to change.

`C-]` closes the debugger in Lisp.

`(quote (1 2 3))` quote is a special form. It is the same as `'(1 2 3)`

`(list 1 (+ 1 1) 3)` displays the list after it evaluates

* `(1 2 3)`

`(reverse (1 2 3))` reverses a list:

* `(3 2 1)`

`(append '(1 2) '(3 4))` appends at the end of a list

* `(1 2 3 4)`

`cadr` the car of the cdr

`(cadr '(1 2 3))` returns `2`

Doing extra `car`/`cdr` on a single symbol will give you an error. The number of a's and d's in `car`/`cdr` can go up 4.

Example Problem:

convert (3 + 2 * 5 > 0 && 7 < 3 / 5) to elisp

`(and (> (+ (* 2 5) 3) 0) (< 7 (/ 3 5)))`

`(and X Y)` logical X and Y. This returns the second element if X is true.

`(or X Y)` logical X or Y. This returns the first true element or nil if neither is true.

`(not X)` logical not X

`(point)` returns the character position of cursor in the buffer

`(mark)` returns the character position of the mark in the buffer

### Example Elisp Code Snippets

```lisp
(defun is-line-number-even ()
    (interactive)
        (setq line (line-number-at-pos))
            (if (= (mod line 2) 0)
                (message "Line %d is even" line)
                (message "Line %d is odd" line))
)
```

For a function to run with `M-x` you need to include `(interactive)`.

```lisp
(defun add-two (a b)
    (interactive "nNumber 1: \nnNumber2: ")
        (message "%d + %d = %d" a b (+ a b))
)
```

The `n` prompts the user for an integer.

`%d` stands for substitute a decimal

`%s` stands for substitute a string

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

## Python Mapping types

`m[k]` where `k` does not need to be integer, accesses the element of a map. `k` is an immutable key.

`d = {}` initiallizes an empty dictionary.

`d = {'a':1, 'b':3, 'z':-3}` initializes the dictionary with different keys and values.

`d['abc'] = 27` sets the value of the dictionary at key `'abc'` to 27

`len(d)` shows how many items are in the dictionary

`d.clear()` removes every item in dictionary

`d = d'` creates the shallowest copy of a dictionary. Simply points `d` to `d'`

`d.copy(d')` creates a shallow copy of the dictionary itself, with each object inside the dictionary `d` as pointers to the elements in `d'`

`d.deepcopy(d')` creates a deep copy of the dictionary `d'`

`d.items()` gives the list of items

`d.keys()` gives the list of keys

`d.values()` gives the list of values

`d.update(d')` modify `d` by taking every value in `d'` and overwriting values of `d` that exist or adding them to `d` if they do not exist

`d.get(k[,v])` gets the value `k` or gives the default value `v` if it is not in the dictionary. if v is ommited in the arguments, it returns `None` if `k` is not found.

`del d[k]` deltes an item from `d`

The dictionary order in Python is the same as insertion order.

`d.popitem()` removes and returns the most recently added key-value pair

## Callable types

Functions are callable objects

```python
    f(a,b,c)
    # f is a callable type

    f = lambda a,b: a+b*b

    # is equivalent to:

    def f(a,b):
        return a+b*b

    g = f
    # g(3,9) is equivalent to f(3,9)
```
