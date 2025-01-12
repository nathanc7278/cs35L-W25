# Emacs Command Sheet

## Basic Commands

| Command | Description |
| --- | --- |
| emacs | opens emacs in gui mode |
| emacs -nw | opens emacs in terminal mode |
| C-x C-c | exit |
| C-u `n` `command` | repeats the `command`, `n` times |
| M-x shell RET | opens the shell |
| C-g | quits the current command |
| C-x C-f | open file |
| C-x d | opens directory |
| C-x C-s | saves the file |
| C-x C-b | lists the buffers (for files that were opened recently) |
| C-x b `filename` | switches buffer to `filename` |
| C-x s | saves buffers |
| C-h c `char` | displays brief info about `char` |
| C-h k `char` | displays info about `char` |
| C-h f `function` | displays info about `function` |
| C-h a `name` | opens command Apropos: lists the commands containing `name` that can be invoked with M-x |
| C-h i | info manuals |

## Navigational Commands

| Command | Description |
| --- | --- |
| C-v | next page |
| C-M-v | scroll bottom window |
| M-v | previous page |
| C-l | redisplay the screen around the cursor |
| C-p | previous line |
| C-n | next line |
| C-b | back one character |
| C-f | forward one character |
| M-b | back one word |
| M-f | forward one word |
| C-a | start of the line |
| C-e | end of the line |
| M-a | start of the sentence |
| M-e | end of the sentence |
| M-< | start of the file |
| M-> | end of the file |
| C-s | search from cursor, repeated C-s will go to next occurance. Backspace will go to previous |
| C-r | reverse search from cursor |
| C-M-s | regex search from cursor |

## Window Management

| Command | Description |
| --- | --- |
| C-x `n` | changes the current number of windows on the screen to `n` |

## Text Editing

| Command | Description |
| --- | --- |
| C-d | delete next character |
| M-backspace | kill previous word |
| M-d | kill next word |
| C-k | kill from cursor to end of line|
| M-k | kill to the end of sentence |
| C-space C-w | highlights region to kill |
| C-space M-w | highlights region to copy |
| C-y (M-y) | yank text, clicking M-y will cycle back previously killed/copied text |
| C-x u | undo |
| C-/ | undo |
| C-_ | undo |
| C-x 8 RET | insert unicode characters |

## Extending Command Set

`C-x` command extend

`M-x` named command extend

| M-x commands | Description |
| --- | --- |
| replace-string | replaces string after cursor |
| recover-file | recovers auto-saved file |
| fundamental-mode | goes to fundamental mode |
| text-mode | goes to text-mode |
| auto-fill-mode | toggles auto-filled mode |
| make-frame | makes frame |
| delete-frame | deletes frame |

### Text edit mode

| Command | Description |
| --- | --- |
| C-u `n` C-u f | set fill lines to `n` characters (70 is default) |
| M-q | refills inside a paragraph |
