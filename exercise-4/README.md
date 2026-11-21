# The Pragmatic Programmer Exercise 4

## Problem:

We want to implement a mini-language to control a simple
turtle-graphics system. The language consists of single-letter
commands, some followed by a single number. For example, the
following input would draw a rectangle:

```python
P 2 # select pen 2
D # pen down
W 2 # draw west 2cm
N 1 # then north 1
E 2 # then east 2
S 1 # then back south
U # pen up`
```

Implement the code that parses this language. It should be
designed so that it is simple to add new commands.

## Notes:

- 4 versions, v3 is an AI reference
- v4, was written completely by hand
- Compare v3 (AI) and v4 (written by me) and you will notice the differences, It's not a copy

- I wanted to try out different ideas with each version, not sprint to the finish