---
title: Variable shadowing inside functions in Python
date: 12-09-2017 23:31:06
categories:
  - Python Tips
tags:
  - developer
  - programming
  - python
  - variable shadowing
---



I ran into this confusing Python scoping behaviour when attempting Problem Set 7 of [MIT600 (2008 Fall)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/). 

Specifically, in the following examples, the first function doesn't modify the global variables passed into it, while the second function does modify the global variable.

```python
def swap(s1, s2):
  assert type(s1) == list and type(s2) == list
  tmp = s1[:]
  s1 = s2[:]
  s2 = tmp
  return

s1 = [1]
s2 = [2]

swap(s1, s2)

print(s1, s2)  # output: [1] [2]
```

So why is that? Isn't the fucntion `swap()` supposed to swapped the value in lists `s1` and `s2` ?



```python
def rev(s):
  assert type(s) == list
  for i in range(len(s)//2):
    tmp = s[i]
    s[i] = s[-(i+1)]
    s[-(i+1)] = tmp
    
s = [1, 2, 3, 4]

rev(s)

print(s)   # output: [4, 3, 2, 1]
```

And in the second function, the list `s` got passed into `rev()` and `s` is reversed after running the whole block of codes.



That's the issue of **scoping** in Python. 

In the first function `swap()`, although the parameters `s1` & `s2` share the same name with the two global variables, when you feed the global variable `s1` & `s2` into `swap()`, it's not modifying the global variables. Instead, the assignment statement `s1 = s2[:]` indicates that **it is declaring a new local variable with the same name as `s1`** . The global variables got left aside. That's why when you try to `print(s1, s2)` , the program spits the untouched lists back. 

![](https://preview.ibb.co/fqAMgv/Untitled.png)

{:.image-caption}

*have a look at the [visualisation of this function](https://goo.gl/PGEWRG) and get more intuistive sense of what's happening*



Wait — the second function seems similar but does modify the global varaible `s` fed into the function?

If you really understand why function `swap()` behaves in that way, you would know why `rev()` is doing different thing: because the parameter `s` is not declared locally ( = inside the scope of this function), so it assumes the global `s` and subsequently modifies that. 

![](https://preview.ibb.co/eqOrgv/1.png)

{:.image-caption}

*have a look at the [visualisation of this function](https://goo.gl/RQSSPF) and get more intuistive sense of what's happening*



To describe it in jargon phrase, this kind of behaviour is called **variable shadowing** in programming. 

> In computer programming, **variable shadowing** occurs when a **variable** declared within a certain scope (decision block, method, or inner class) has the same **name** as a **variable** declared in an outer scope. 
>
> — Wikipedia

This can be confusing and have costly side-effects in your code.