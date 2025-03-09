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

## Setup for using GDB

* compilation options
* `set env LC_ALL fr_FR_utf8` is equivalent to `LC_ALL=fr_FR_utf8` in the shell
* `set cwd /usr/local/cs`
* `set disable-randomization off`

### Address Space Layout Randomization (ASLR)

* malloc returns "random" hard to get addresses
* gets in the way of stabilizing failure

`Breakpoints` a spot in machine code

* executable machine instruction
* symbol table
* names, maichine addresses, source code locations
* type information
* local variables
* `gcc -g3` generate debugging info

## System Calls (lower level)

* `read(0, buf, 1000)` reads 1000 bytes from file descriptor 0 and stores it in buf.
* `write(1, buf, 500)` writes 500 bytes from buf into file descriptor.
* `ptrace` is used by debuggers

### Options with GDB

* Remote debugging:
    * embedded device
    * small RAM
    * tiny OS
* Have GDB on remote device that connects with embedded device
    * serial port/internet to connect with


* `set a b` setting config variable
* `dir /a/b/src` look a directory for source code
* `define pp` GDB extension language Guile + Python

## Low Level Performance Improvements

assembly language is unportable and rarely used

In C: we can write `asm("halt");`. 

`__attribute__((...))` is advice to the compiler to run faster

```C
#if !__GNUC__
#define __attribute__(x) /* if compiler is not GNUC then define function attribute to nothing*/
#end if
```

`long x __attribute__((aligned(8)));` makes variable x to be a multiple of 8

`void error(char const *msg) __attribute__((cold));` or `attribute((hot));` tells the compiler that this part of the program is not execute often or it is executed often.

* hot stuff is stored in cache while cold stuff is store in RAM or flash drive.
* this is controversial, some people like to let compiler figure it out or use profiling

`gcc -flto` link time optimization/whole program optimization. `O(n^2)`

### Reliability Improvement

#### Static Checking (Checked at compile time)

You help your compiler:
```C
# define N 1024
static_assert(0 < N && N <1000);        // must be a constant expression, cannot be variable
static_assert(UID_MAX <= INT_MAX);
int uid = getuid();
```

compiler does work:

`gcc -Wcomment` warns you if /* ... /* ... */

`gcc -Wparenthese` a<<b+c needs to be written as a<<(b+c)

`gcc -Waddress` 

```C
    char *p = getusername();
    if (p == "abc") {       // this is pointer comparison, not string comparison
        return 1;
    }
```

`gcc -Wstrict-aliasing` warns you about misue of pointer types. Assigning a long long into a long.

`gcc -Wmaybe_uninitialized` 

```C
    int i;
    int j = getchar();
    if (j < 27) {
        return i;
    }
```

`gcc -Wall` all "normally" useful warning options

`gcc -fanalyzer` look at entire module, cheaper than -flto

You can also help compiler do static checking and gain performance:

```C
[[noreturn]] void exit(init);
if (i < 0) {
    exit();
}
```

```C
int hash(char *, size_t) __attribute__((pure, access(read_only, 1, 2)))
// pure does not change state, but can depend on state
// taken from first argument
// size from second argument
[[reproducible]]
double sqrt(double) __attribute__((const))
// const doesn't change state and is not state dependent
[[unsequenced]]
```

gcc will enforce this when compiling hash. gcc can optimize caller based on this

```C
int my_print(void*, char const *, ...)__attribute__((nonnull(1), format(printf(2,3))));
```

### Runtime Checking

Check for errors yourself:

```C
#include <stdchdint.h>
bool sum (int a, int b, int *r) {
    return ddadd(&r, a, b);
}
```

`gcc -fstanitize=undefined` whenever the behavior is not defined by language, make the program crash reliably

`gcc -fsanitize=address` catches behaviors that lead to invalid addresses

The fsanitize options cannot be done at the same time.

`gcc -fwrapv` for integer arithmetic, overflows

`gcc -fsanitize=thread` puts instrumentation to catch race conditions (when one thread is reading and another is writing into part of code at the same time)

`valgrind diff /dev/null password` runs diff using GDB and checks for mistakes. Valgrind is a GDB subset that looks for bad addresses

* slow
* no need to recompile

#### Runtime Checking Problems

* cost at runtime
* only checks one run
* can miss errors in that run

### Portability Checking:

platforms ahve many attributed(exponential)

* cross-compiling
    * build on x86-64, generates code for arm

### Backups (Disaster Recovery)

* periodically copy everything: restore backup on disaster
* inverse of caching
* you must have a failure model
    * your flashdrive fails
    * your battery fails
    * outside attacker deleting files
    * inside attacker modifies/leaks files
    
