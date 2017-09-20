---
title: 数据类型、运算符、变量 | 写给小白的工程师入门
date: 17-09-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - programming
  - python
  - newbie
---



从这一节开始，我们将进入正式的 Python 学习。绝大多数网上编程教程都直接从这一节的内容开始，我之所以选择在前面铺垫那么久，一是遵循人脑的自然学习规律——在猛扎进细节中前先建立对大画面的认知理解；二是作为走过这条自学路的人，我会希望当初的自己也得到过这样的指点。

在具体内容前，重复两条很多人都说过的**学习编程最好的方式**：

> 1. 跟着教程或源码敲代码，出错了可以立即得到反馈，甚至应该故意实验一些可能出错的指令，可以获得最佳编程学习效果。学习时故意出些错总比未来在一堆代码里无意中埋下 bug 好久解决不掉要好得多。
> 2. 关键概念**记英文原版**。中文只是翻译参考。

------



### 程序是什么

在上一节《工程师的脑子和普通人不一样》中，我曾把程序员比做写菜谱的人，计算机只是个规规矩矩炒菜的，一个程序就像一份菜谱，算法其实就是那份菜谱里描述做菜的步骤……还可以再学一个更专业抽象的说法：程序即为执行一次计算的一系列指令。

> **Program**: <u>a sequence of instructions</u> that specifies how to perform a computation.

这里的指令指的是什么呢？

用任一程序语言写的任一程序，都完全可以只由以下五种指令组成：

- 输入 input
- 输出 output
- 数学计算 math
- 条件控制 conditional execution
- 重复 repetition 

**只要掌握这五类指令，就可以写出任何程序**——其实很好理解，虽然菜的品类无数，但并不存在煎炸烤炒炖煮拌不能搞定的菜。

.

.

### 值与类型

##### **Value** 值 

**值**即为在编程中所用**数据的基本单位**。主要包括两大类：**数字 (number)** 与**字符串 (string)**。

数字进一步可以分为3种类型（还有一类复数，但很少用到，此处不提）：

> - **整型** (integer)，即整数，如 4, 7, 101
> - **浮点型** (floating point)，即带小数点的数字，如 2.5, 5.0, 3.14
> - **布尔值** (boolean)，说是数字其实更像逻辑数据类型，只包括 **True/False** 两个值（书写固定，开头大写）；但可以和其他数字一起进行数学运算，此时 True = 1, False = 0.



**字符串**是一串由引号（单引号或双引号皆可，但同一对引号需统一单双）围起的字符，如 `"xiaobai"`, `"666"`, `"小  白"` 。注意，a. 当数字加上引号时就成字符串了，不再具备数字值的特性了（比如可以进行数学运算）；b. 引号内可加空格可加标点，都可以构成字符串的一部分。

.

##### **Type** 类型 

**类型是值的分类** (理解成值的属性也行)。我们在上面已经看到 Python 几大基本类型的一部分了：整型、浮点型、布尔值与字符串。想要知道某个值或变量（下面会讲到）的类型，可以用内置 `type()` 函数来问 Python:

```python
>>> type(666)
<class 'int'>
>>> type("666")
<class 'str'>
>>> type(3.1415926)
<class 'float'>
>>> type(True)
<class 'bool'>
```

在后面几节我们还会接着学习列表 (list)、元组 (tuple)、字典 (dictionary)、集合 (set) 等更多类型。

.

.

### 运算符

Python 中的运算符 (operator) 主要用在数学运算上，和通用的算术运算符号大体相同。被运算符连接的值可称为运算数 (operand)。

在这儿通过交互模式来看一下用法：

```python
>>> 3 + 5
8
>>> 3.0 + 5     #当一个运算数为浮点时，结果也会变成浮点
8.0
>>> 1.0 + True  #还记得刚刚说的布尔值的数值吗
2.0
>>> 9 - 2
7
>>> 2.5 * 5     #乘积
12.5
>>> 2**3        #指数运算
8
>>> 3 / 5       #除法
0.6
>>> 3 // 5      #除法，只计整数部分
0
>>> 3 % 5       #3除以5所剩余数
3
```

.

除了用在数字上，有两个运算符还可以用在**字符串**上：`+`, `*`. 猜一猜加号和乘号会在字符串上产生什么效果呢？

```python
>>> 'Sinan' + 'Talk'
'SinanTalk'
>>> 'Hello' * 3
'HelloHelloHello'
```

通过 `+` 将多个字符串顺序连接起来的操作被称为**字串串接** (string concatenation)，非常常用；通过 `*` 把一个字符串复制多次的操作倒没什么专用说法 (可以称为 string multiplication)，用的不多，不过需要注意字符串只能与整型相乘，字符串之间不能相乘。

像这样，一个运算符可以同时用于一个以上数据类型 (type) 的现象被称为**重载** (overloading)。比如， `+` 可以同时用在数字和字符串上。并不是所有编程语言都支持运算符的重载。除了运算符，之后我们还会接触到函数重载 (function overloading)。

.

至于有多个运算符同时存在时该遵从什么运算顺序的问题，和数学计算相同。不确定的时候就用括号明确优先级即可。

.

.

### 变量

光有值还不够用，我们还需要**变量** (variable)。**变量自身不能单独存在**。变量用来存储、命名值，是其代表的一个值的名字。当我们给变量赋值时，会用到**赋值语句** (assignment statement)：

```python
# 赋值语句用'='进行赋值，此处'='与算术中相等的概念不同，含义上更像'<-'右指箭头
a = 5
b = 2.0
c = 'Python'
d = True
# 这个赋值语句能更清楚看到赋值'='并非算术中的等号，而是'<-'右指箭头，将'='右边的值赋给'='左边的变量
a = a + 5
print(a)  # 输出结果：10
```

关于 Python 中**变量与值的关系**，我没见过比 David Goodger 讲得更好的了，此处就借用下他的[例子和插图](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#python-has-names)吧。

**Python 中的变量就像是其绑定的值的姓名标签**。如，当给变量 a 赋值 1 时，`a = 1`，1 这个整数就绑了 a 的标签， 并且 1 会在内存里占一个位置：



![](http://python.net/~goodger/projects/pycon/2007/idiomatic/a1tag.png){:style="margin:0 auto"}

当你重新给 a 赋新值 2 时，`a = 2`，就等于把这个标签移到 2 身上了，2 此时也会在内存里占一个位置：

![](http://python.net/~goodger/projects/pycon/2007/idiomatic/a2tag.png){:style="margin:0 auto"} ![](http://python.net/~goodger/projects/pycon/2007/idiomatic/1.png){:style="margin:0 auto"}

此时你无法再通过 a 来找到 1 了。如果 1 没有绑定任何其他标签（变量）的话，那 1 就不会再在内存里占位置了。

如果你创建一个新变量 b，并用 a 来给 b 赋值，其实等同于在 2 身上绑了两个姓名标签，通过 a 或 b 都可以找到 2:



![](http://python.net/~goodger/projects/pycon/2007/idiomatic/ab2tag.png){:style="margin:0 auto"}





> 并不是所有编程语言里的变量都是值的“姓名标签”。

.

##### 变量的命名

Python 变量命名的规则不复杂，可以是：

> 1. 字母组合，如 a, foo, val, counter
> 2. 字母与数字组合，如 dict1, list2
> 3. 可以加下划线，如 is_even, max_val2
> 4. 但不能以数字开头
> 5. 习惯性以小写字母命名
> 6. 不可以用 Python 保留字／关键字 (keywords) 来命名变量

**Python 保留字／关键字**都有哪些呢？可以在交互模式下输入：

```python
# to see the Python keyword list
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

当你在文本编辑器或 IDE 中编程时，Python 保留字会自动呈现不同的颜色，所以一开始也不用背保留字列表。每个保留字都非常常用，之后很快会在实践中熟悉。

.

虽然变量命名并不复杂，但这不仅关系到 style，还关系到代码的易读性，因此最好起个**易懂易记易区分并符合逻辑**的名字，比如，我给字符串 `"SinanTalk"` 起名的话，明显 `blog_name` 比 `foo` 要合理得多。

.

.

### 表达式与语句

**Python 表达式 (expression) 是值、变量与运算符的组合**。一个值或变量本身也可以构成一个表达式。

> **Expressions**: a combination of values, variables and operators.

刚开始接触 Python 编程的新手可能都遇到过这个困惑，为什么有些代码可以在交互式编程 (interactive programming) 模式下直接返回结果，但脚本式编程 (script programming) 时就不会返回结果呢？这其实是 Python 表达式在解释器 (interpreter) 中的不同行为。当你在解释器的提示符 (prompt) ——就是尖箭头 `>>>` ——处输入一个表达式时，解释器会在回车后求得表达式的值并返回，如：

```python
>>> 1
1
>>> 5 + 2
7
>>> a = 3.14
>>> a
3.14
>>> a + 10
13.14
```

在脚本模式下运行，虽然解释器也会对表达式求值 (evaluate)，但并不会返回结果。

在上面几个简单例子中，唯一没有即时返回结果的就是 `a = 3.14`，因为这并非表达式，而是一个 Python 语句。

.

**Python 语句 (statement) 是一组有效力的代码块**。

> **Statement**: a unit of code that has an effect.

目前为止我们已经遇到过的语句有：

- 赋值语句 (assignment statement)：创建新变量并赋予一个值。
- 输出语句 (print statement)：输出一个值。

解释器不会对语句求值，而是直接执行 (executes) 一个指令。

今后我们还会接触更多 Python 语句。

.

.

### 第4节 作业

- 阅读 *Think Python (2nd edition)*  第1&2章，并完成文后练习。 

  *Think Python: How to Think Like a Computer Scientist* 是小白学习 Python 的最佳入门书（不是我评价的，而是很多大佬推荐），第2版面向 Python3。英文原版并不难懂。

.

### 第4节 小结

我们在这一节进入 Python 编程知识的正题，先介绍了一些基本的编程概念：值与类型、运算符、变量、表达式与语句。虽然已经能写简单的赋值语句和输出语句，进行数学运算了，但还不会用 Python 来表达更复杂的程序逻辑，下节课我们将开始学习条件控制和更多编程基础概念。