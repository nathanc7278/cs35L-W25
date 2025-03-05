# Debugging (Low Level)

* Try to avoid it
* Inefficient way to find bugs
* It can take > 50% of your time in badly ran projects
* You must be proactive
    * review code before it goes in
    * prevent bugs from arriving
* Design program to resist bugs
* Debugger can change how your program behaves

## Static Checking

* using a compiler to look at your source code
* `gcc -Wall`
* `git blame` or `git diff`

## Dynamic Checking

* run the program and look for unexpected behavior
* `gcc --sanitize=undefined`

## Test Cases (Test Driven Development)

`TDD` write test cases before source code

You can also use a better platform

`C, C++` to `Python, Rust`

`JS` to `TypeScript`

## Defensive Programming:

* write your program assuming your program is wrong
* dynamic checking (little programming work)
* assertions (often optional)
    * `gcc -DNDEBUG` turns off assertions to get more efficient program

```C++
#include <assert.h>

assert(0 <= i && i <= n);
    // if this is not true, the program errors out
```

* exception handling

```C++
try {
    buggycode_maybe();
} catch (exception E) {
    handle_bug();
}
```

* traces and logs (print statements)
* checkpoint/restart
    * `checkpoint();` saves the program state into a file or db
    * `restart();` restores program state
* barricades
    * you have core part of program that is simple and fast (clean)
    * there is the messy/suspicious part that handles stuff from outside world. This only feeds clean data to the core part of program
    * The barricade is where messy code is filtered out
* interpreters (JS interpreter in browsers)
    * refuses to execute bad code
* virtual machines
    * gets help from hardware to pretend you have a CPU to refuse bad code

### How to debug:

* don't debug at random
    * don't guess what the bug is
* systematic exploration of exponential space of possible error

`error` mistake in programmer's head

`fault` latent problem in your software

`failure` observed bad behavior in a program

1. Stabilize the failure (Heisenbugs) make the bug reproduceable
2. Locate fault that caused the failure (debugger is used here). Debugger can be thought of as a program history explorer.
3. Fix the bug

### GDB commands

`p "any expression"` prints the expression

`r "args"` runs the program

`start` does the setup and runs until it reaches the main function. Creates a breakpoint at main.

`attach "process id"` starts debugging a process that is running

`detach` detaches from a process

`b "location"` sets a breakpoint at any location

`c` continues to the next breakpoint

`info break` displays breakpoints

`info registers` displays registers

`fin` put a temporary breakpoint at end of function and then continues

`step` or `s` execute until the source code line changes (step in)

`stepi` executes 1 machine code instruction

`next` or `n` execute through the line or a function (step over)

`rc` reveerse continue. This can be expensive; enabled only if you invoke GDB appropiately

`watch "expression"` watches the value of an expression, and will stop when it changes. This can be slow. Worse case it will single step through each line of code. This can run in  full speed on most modern computers when there are less or equal to 4 variables that are watched at once.

`catchpoints` are breakpoints for try/except

`checkpoint` creates a checkpoint

`restart` start from last checkpoint

`bt` backtrace shows the stack frams for function calls. This tells you planned future of executions. 

```
src: main --> f --> g ---> h
gdb bt: h, f, main

// when h is done, some code in f will be ran, and then some code in main will be ran
```
