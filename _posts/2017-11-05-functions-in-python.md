---
title: 函数、作用域、封装 | 写给小白的工程师入门
date: 05-11-2017 23:31:06
categories:
- A Developer Guide for Newbies - Starting with Python 
tags:
- developer
- programming
- python
- funtions
- encapsulation
---





> "Functions should do one thing. They should do it well. They should do it only."
>
> — Robert C. Martin



### A. 函数定义与基本用法

**函数（function）是一组复合语句，可以接收输入值，执行特定命令，选择性地返回输出结果。**

Python 中函数与数学里的函数相似。比如这个代数函数：

> f(x) = x * 2

等式左边定义了一个函数 `f` ，这个函数需要一个输入值 `x` ——即为**参数**（parameter）。一个函数可以带一个或多个参数，也可以不用参数。

等式右边就是这个函数的具体定义了。这个函数可以把传入的参数乘二，并返回结果。

在代数和 Python 中，呼出（= “调用”、使用）函数的语法都是一样的：

> FUNCTION_NAME\(PARAMETERS_SEPERATED_BY_COMMA)

（在这套教程里，我用约定俗成的「大写字母 + 下划线」来代表应该用真实代码取代的内容；在编程中这样的习惯用法很多。）

比如我们可以传入参数 `4 `到上面的代数方程中，

> f(4)
>
> \>> 8

再比如，`print()` 是一个我们已经很熟悉的 Python 3 内建函数 (built-in function) 了：

```python
>>> print("Whatever you like :p")
Whatever you like :p
```



#### 自定义函数

由程序员来定义一个函数在 Python 中极度常见。比如，上面的代数方程用 Python 自定义函数表达即为：

```python
def f(x):
	return x * 2
```

这几乎是最简形式的函数定义了，由此我们不难推断出 Python 自定义函数的基本规则：

```Python
def FUNCTION_NAME(PARAMETERS_SEPERATED_BY_COMMA):
	FUNCTION_DEFINITION
```

定义函数的关键字为 `def`，函数名称可以随意取，但应该避免 Python 关键字（keywords）；习惯上 Python 函数命名通常为「小写字母 + 下划线」组合，例如 `print_area`, `multiply`, `even_or_odd`.

函数名称后紧跟一对单括号 `()`，如果有参数的话应该放在括号里，多个参数以逗号隔开。不要忘记句末冒号。

```python
# 零参数的函数
>>> def hello():
...		return 'Hello Python!'
...
>>> greeting = hello()
>>> print(greeting)
Hello Python!

# 多个参数的函数
>>> def sum_all(x, y, z):
...		return x + y + z
...
>>> my_sum = sum_all(1,2,3)
>>> print(my_sum)
6
```



所有跟在 `def` 行后面缩进的语句都是该函数的定义。上面 `f(x)` 的函数定义只有一行，且用到了 `return` 关键字。`return` 后跟着的表达式或值即为这个函数会返回的输出值。函数定义可以不包括 `return` 语句，没有 `return` 的函数返回值为 `None`. 比如：

```python
# calling a function with return statement
>>> f(2)
4
>>> result = f(2)
>>> print(result)
4

# create a function without return statement
>>> def no_return(x):
...		x = x * 2
...		print('multiplied by 2:', x)
...
# call a function without return statement
>>> no_return(4)
multiplied by 2: 8
```

注意：很容易忽略的一点是，当你想要保存一个函数的输出值（以便之后使用）时，需要新建一个变量（variable），用这个变量来保存函数的输出结果，比如上面的 `result` 变量。



#### 函数的复用

为什么要创建、调用函数而不是直接写出具体指令呢？

因为有一个现成函数可以大大降低程序员的码字工作量。想实现什么功能第一反应应该是，“是否有现成的 函数／方法／模块 可用？“——而不是**重复造轮子** (reinventing the wheel) 。

> To **reinvent the wheel** is to duplicate a basic method that has already previously been created or optimized by others.
>
> — Wikipedia

当前人已经发明、优化出一种解决问题的方法后，后人若还要自己从零开始新造自己的方法，这就被称为「重复造轮子」。在大部分情况下，应该尽量避免「重复造轮子」。



调用已经写好的函数，就是一种减少「自造轮子」，提高代码**复用性**（reusability）的方式。

例如，我们可以用这节课学到的函数自定义方法和上节课条件控制语句写一个“判断输入值奇偶性”的函数：

```python
def even_odd(x):
	if x % 2 == 0:
      	print('input is even')
    else:
        print('input is odd')
```

接着调用这个函数：

```python
>>> even_odd(2)
input is even
>>> even_odd(3)
input is odd
```

接下来每次需要用到这个功能（functionality）的时候，只要一行代码调用 `even_odd` 函数即可，大大减少了重复的工作量。



#### 嵌套函数

上一节，我们认识了嵌套条件语句（nested conditionals），就是在一个条件语句的 True 分支后又接了一个条件句。在函数定义中，嵌套函数（nested functions）也是允许的。

例如，

```python
def outer():
	print('Outer Funtion!')
	
	def inner():
		print('Inner Function!')
    inner()
```

外层函数（outer function）与内层函数（inner function）的命名也不言自明。

此时调用 `outer` 函数，会是出现什么结果呢？

```python
>>> outer()
Outer Funtion!
Inner Function!
```



#### 内建函数 Built-in functions

如果我们需要用的所有函数都要自己一一写，那写代码效率就太太低了。因此，Python 是有自带内建函数库的（https://docs.python.org/3/library/functions.html）。

比如，刚刚提到的 `print()` 函数。常见的 Python 内建函数还有以下这些：

```python
# len() returns the length of an object
>>> len('Monty')
5
>>> len('12345')
5

# type() returns the data type of an object
>>> type('Welcome to SinanTalk!')
<class 'str'>
>>> type(98)
<class 'int'>

# str() takes an onject and returns a new object with a string data type
>>> str(100)
'100'

# int() takes an object and returns a new object with an integer data type
>>> int('99')
99

# float() takes an object and returns a new object with a floating point data type
>>> float(88)
88.0

# input() collects information from the user
>>> age = input('How old are you? ')
How old are you? 18
>>> age = int(age)
>>> if age < 28:
...		print('Still young!')
... else:
... 	print('You must have seen a lot!')
...
Still young!
>>>
```





### B. 变量作用域 Scope

是时候了解**变量的作用域**这个重要概念了！

作用域（scope）是变量（variable）的重要特性之一。

> **变量作用域**决定了哪一部分程序可以访问某个特定的变量，即为对一个变量的「访问权限」。
>
> **A variable's scope**: refers to what part of your program has access to the variable.

变量的访问权限是有这个变量的赋值位置决定的。

为什么一开始讲变量的时候没有涉及这个重要概念呢？

因为在没学自定义函数之前，是很难理解变量作用域是怎么回事。



根据作用域，变量可分为两大类：

> 全局变量（global variable）：定义／赋值在函数（或类）之外的变量；
>
> 局部变量（local variable）：定义／赋值在函数（或类）内的变量。

对于一个全局变量而言，在这个程序的任何位置都可以访问它；而局部变量则只能在局部（即某个函数／类的内部）访问，走出了这个函数／类，就不能再访问局部变量了。



打个比方，在你面前站着一面放满书的书柜，你可以看到每本书的书名，但只有选其中一本书翻开，才能看到这本书里提到的人名。

![image credit: pexels](http://upload-images.jianshu.io/upload_images/4719384-bb80edd8103281fa.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这面书柜就是一个程序，每本书都是一个代码块，写在书脊上的书名是全局变量，需要翻开某本书才能看到的人名是局部变量——站在书架前是看不见局部变量的！



我们来看看在具体代码中的全局／局部变量。

```python
>>> x = 1
>>> y = 2
>>> z = 3
>>> print(x, y, z)
1 2 3
```

全局变量可以从程序的任何位置访问，也包括函数内部：

```Python
>>> def print_vals():
...		print(x, y, z)
...
>>> print_vals()
1 2 3
```



如果在函数内部定义了局部变量，则不能在函数外单独访问，否则会抛出 `NameError` 异常：

```Python
>>> def print_new_vals():
...		val = 100
...		print(val)
...
>>> val
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'val' is not defined
```

这种情况下，Python 解释器看不见局部变量 `val` ，有点像选择性失明。



如果在函数内容定义一个与已经存在的全局变量名称相同的局部变量，那么在这个函数外再访问此变量，会返回什么值呢？

```Python
>>> x = 1
>>> def local_val():
... 	x = 100
...
>>> x
```

在 idle 内敲一遍的话会发现，x 返回的值是 1。这个例子更加充分地证明了局部变量和全局变量的作用域差别。



如果想在函数内部改变某个全局变量的话，可以用 `global` 这个关键字来表明这儿访问、修改的是全局变量。

```Python
>>> x = 1
>>> def f():
... 	global x
...		x += 1
...		print(x)
...
>>> f()
2
```



为什么编程语言中的变量普遍需要规定作用域呢？

如果不存在作用域限制的话，一个程序中的任何变量在任何位置都可以访问。那么在一个很长的程序中，如果你在一个函数内部使用了全局变量且不小心改变了这个变量的值或类型，那在接下来的程序中这个变量就可能会拥有不同的特性，引发意想不到的错误。

如果有多个程序员碰过同一个程序，可能并不是每个人都清楚别人命名的变量，没有作用域的访问限制的话，很可能会出错。



变量的作用域不同同时也引出了编程中**封装**（encapsulation）的概念。



### C. 函数的封装

![Encapsulation](https://lh6.googleusercontent.com/-zmf0GwQKR7A/VJgNNFspOOI/AAAAAAAAK7c/y05ZQ_m1psA/w970-h386/Encapsulation%2Bin%2BJava.jpg)



封装是面向对象编程（object-oriented programming）中的重要概念。今天我们只粗浅地介绍一点和函数有关的封装行为。

封装，顾名思义，就像把一些代码封起来装进胶囊或瓶子里去，在胶囊外的代码不能访问胶囊内代码。

> When code is **encapsulated**, it means when it is called, the caller cannot access the code's internal data. 

比如，上面介绍的函数内部的局部变量，就是函数封装行为的体现。

这样做的好处很多。当用户（指所有使用这个程序的人）运行你的代码时，他并不需要知道你的代码里有什么函数，每个函数内部又存在怎样的变量和运算，他只需要知道如何运行即可。另一方面，正常情况下，一个程序会需要反复优化升级，后期你可能会修改一个函数内部的代码，没有封装的话，这个函数外部的代码可能会直接访问内部，一旦修改内部代码，就可能会造成“连锁事故”。

所以说，封装是提高代码可维护性与可移植性的重要前提。



### 第7节  小节

掌握本节的自定义函数与上一节的[条件语句](http://mp.weixin.qq.com/s?__biz=MzI1OTQ1MTYyMw==&mid=2247484143&idx=1&sn=5a9454917f90d244d2f8de44aff2329c&chksm=ea79fd67dd0e7471b5d2a2d1a6990fb749a0b6398048260ff5b5b1be073af7835fb4a28c675f&scene=21#wechat_redirect)，已经能写很多 Python 短程序了呢！