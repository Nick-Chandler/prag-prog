# The Pragmatic Programmer Exercise 6

## Problem

Design a BNF grammar to parse a time specification. All of the
following examples should be accepted:

```
4pm, 7:38pm, 23:42, 3:16, 3:16am
```

## Notes

- I will admit I did not about grammars (let alone BNF grammars) before this exercise so this was a good learning opportunity
- I was a bit proud that my grammar was able to handle a time in the format of 
```
04:37am
```
- Claude's version (vibe/time.bnf) could not

- This was not explicitly listed as a requirement but I felt it should've been handled (this is a common way to write out the time, no?)
- Score one for humanity :)