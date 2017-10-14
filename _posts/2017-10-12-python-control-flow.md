---
title: 条件控制、代码块、错误与异常 | 写给小白的工程师入门
date: 12-10-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - programming
  - python
  - newbie
  - control flow
---

![image credit: pexels](http://upload-images.jianshu.io/upload_images/4719384-71854ed845c4a8ae?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这一节的目标是写出一个能执行条件控制的 Python 短程序！在这个过程中，你会学到如何正确地写出 Python 代码块，如何优雅地写注释，如何冷静地应对错误与异常，以及什么才是专业优美的 Python 代码风格。

.

#### A. 代码块与注释

##### 代码块 Code block

**代码块是一组由代码构成的功能“单元”**。一个代码块可以单独运行。比如一个函数（function）或一个类（class）定义、一个模块（module）都是代码块，例如：

```python
def print_parity(x):
	if x % 2 == 0:
		print(x, "is even")
	else:
		print(x, "is odd")
```

这是一个**函数定义**（function definition），这个函数可以用来查询某个输入数字的奇偶性。这个函数就是一个代码块儿，能单独运行，多行语句共同实现一个功能。

.

##### 行与缩进 Indentation

为了能让编译器或解释器准确地把一堆代码划分到各自独立的代码块中去，不同的编程语言有不同的方法。很多编程语言利用大括号 `{}` 围起一个代码块，还有语言只用分号 `;` 来表示一句语句的结束。Python 很特别，以强制**缩进**（indentation）表示代码块归属。

缩进可以用 tab 键或空格缩进，但同一脚本中**不能混用**（虽然你肉眼看不出到底按了 tab 还是空格，但 Python 解释器看得见……）。习惯上一个缩进单位为4个空格，一般 tab 键会默认4个空格的长度。如果用 PyCharm 这类 IDE 编程，一般不需要特别操心缩进混用或长度问题；但如果用单独的文本编辑器，如 notepad++、TextMate 这些，就得在偏好里勾上类似"replace tabs as spaces"的设置选项，否则特别容易报错。

那什么时候需要缩进呢？简单来说，在 Python 代码里看到冒号 `:` 时就说明这个语句（statement）还没说完，还有下个语句，此时后面的语句若另起一行就必须缩进。比如上面 `print_parity` 这个函数定义里就出现了3个冒号，而每个冒号紧跟着的下一句都缩进了。



由于缩进方式或长度不统一而导致运行错误，会在报错信息里看到 `IndentationError` 的提示。

关于更多运行 Python 可能出现的错误与异常，在本节后半部分会专门细说。

.

##### 空行

专门把空行拎出来，是因为空行也是一枚好程序的一部分。在函数定义（function definition）、类定义（class definition）代码块之间一般空1-3行，具体是1行还是3行主要看代码块之间的逻辑关系。在 PyCharm IDE 中，编辑器会提示如何空行。

.

##### 注释 Comments

注释不仅是为了向所有可能看到你代码的人间接解释你的程序在干嘛，更为了让你自己将来回顾时还能理解自己曾写过的代码。因此，注释的基本原则就是只简洁地解释那些其他程序员可能看不懂或要停下来思考半天才能理解的代码。

.

Python 中注释分两大类：单行注释与多行注释。

**单行注释**以 `#` 开头，如：

```python
# calculate the area of a square
square_side = 2.0
square_area = square_side ** 2
print(square_area)
```

**多行注释**则以三对单引号 `‘’‘` 或三对双引号 `“”“` 将注释内容括起来，如：

```python
def square_area(side):
  	”“”
	returns the area of a square.
    :param side: length of one side of the sqaure
	“”“
	area = side * 2
	return area
```

多行注释多用于像上面例子中函数定义中，用于解释某个函数的目的。

.

细心读者也许会发现在上面的两个注释举例中，尤其是第一个单行注释例子，注释本身显得很多余，因为变量名已经足够清楚准确——这就是好的编程风格（programming style）；与其费时间专门为变量名注释一大堆，不如一开始就起个更清晰易懂的名称。

关于编程风格，我还会在本节末尾多说几句。

.

.

#### B. 流程控制之条件语句

##### 流程控制 Flow control

小学时，一次暑假作业集（那时叫《暑假园地》）上面有道题，我至今依然记得。

题目是一幅漫画，画了“小白”一人在家的画面。勤劳的小白同学需要做：

> 1. 扫地，用时30min
> 2. 烧热水，用时10min
> 3. 洒水，用时10min
> 4. （用热水）热牛奶，用时10min
> 5. 把脏衣服放进洗衣机，洗衣程序需要90min
> 6. 晾衣服，用时20min
> 7. 擦桌子，用时15min
> 8. 给花浇水，用时5min

你需要在完成所有任务的前提下，给小白安排一个用时最短的流程。

我之所以一直记得这道小学题目，是因为在之后的很多场景下，我都联想到过这个简单的流程题。当我刚接触到编程的基础思想时（在中学数学课上学画流程图），一拍脑袋，这不就是小学的任务流程题嘛！

其实从宏观角度来看，**流程控制就是编程的中心议题之一**。为了实现一个或一组功能，一个程序需要完成若干个小任务。有些任务像给花浇水和擦桌子一样无所谓先后，但有些任务之间存在着必须“先洗衣服才能晾衣”这样的先后次序，还有些任务像烧热水一样可以和其他任务“并联”，默默像背景音乐一样运行。这样的流程控制在 Python 中可以依靠很多工具实现，**条件语句**就是其中一种。

.

##### 条件控制

我们已经在上文求奇偶性的函数定义例子中见过条件控制语句（conditional statement）了，再来看一个例子：

```python
def compare(x, y):
	if x < y:
    	print(x, "is less than", y)
	elif x > y:
		print(x, "is greater than", y)
	else:
    	print(x, "and", y, "are equal")
```

这是个比较两个输入值（不一定是数字）的函数。比较两个值（x & y）的结论只可能在这三个中挑一个：`x < y`，`x > y` 或 `x = y`。查询一个数字奇偶性的函数也类似，一个数字只可能在奇数或偶数中挑一个归属，不存在其他可能性。当遇到这样的情景时，就适合用条件控制来表达。

.

从这两个例子中，我们可以抽象出条件控制语句的一般形式：

```python
if condition_1:
	statement_block_1
elif condition_2:
	statement_block_2
else:
	statement_block_3
```

这里出现了三个 Python 关键词：`if／elif／else`，`elif` 是 else if 的缩写，即除了 `if` 以外的条件。当解释器走到这儿时，

- 先查看 `if` 语句的条件（condition\_1）是否满足，如果满足（即为True），便执行 statement_block\_1，并直接跳过后面所有 `elif／else` 语句块；
- 若不满足 condition\_1，再判断 `elif` 语句中的 condition\_2 是否为 True；
- 若 condition\_2 为 True，则执行 statement_block\_2；
- 若 condition\_2 为 False，就执行 `else` 语句下的 statement_block\_3.

三个条件语句分支（branching）并不非得同时存在，比如求奇偶性的例子就只有 `if／else`，`if` 语句块也可单独存在；还可以有三个以上的条件，此时可以多次利用 `elif` 语句块。

注意：每个条件语句（`if／elif／else` statement）后都要加冒号 `:` ，冒号后的语句（或者也可以称为子句 clause）若另起一行则需要缩进；`else` 语句块必须放在末尾。

.

描述再多也不如一张图直观，多个条件控制语句的代码块可以用这个流程图来表示**链式条件** (chained conditionals) ——即一连串彼此平行的条件语句块：

![flowchart](http://csharpcorner.mindcrackerinc.netdna-cdn.com/UploadFile/75a48f/python-if-else-nested-if-elif/Images/NewFiles/4.PNG)

思考时间：上面已经给出了如何比较两个输入值的函数定义，那么如果要比较三个输入值呢 (为简化问题，假设这三个输入值<u>互不相同</u>) ？你会怎样设计这个条件控制代码块的结构？可以先画一画流程图。

.

这个问题可以先倒着思考，比较两个值一共只有三种结果，那比较三个不同的值可能出现几种结果呢？

.

我提供一种典型思路：

```python
def compare(x, y, z):
	if x > y:
		if y > z:
        	print("x > y > z")
        elif z > x:
        	print("z > x > y")
        else:
        	print("x > z > y")
	else:
		if x > z:
			print("y > x > z")
		elif z > y:
			print("z > y > x")
		else:
			print("y > z > x")
```

在这个函数定义中，条件控制语句似乎更复杂了。在第一个 `if` 语句后，又套了一个 `if／elif／else` 语句块；在第一层的 `else` 语句后，也套了个新的  `if／elif／else` 语句块。像这样多层条件语句块，被称为**嵌套条件**（nested conditionals）。这个例子只嵌套了两层条件语句块，但实际上可以多层嵌套。

嵌套条件的流程图可以是这样：

![](https://ittimepass.files.wordpress.com/2016/11/flow-chart-of-nested-if-else.png?w=616)

仔细观察的话，会发现嵌套条件的流程图与链式条件的差别在于：嵌套条件里至少有一个判断为 True 的分支下，会再加一个条件判断菱形。

.

.

#### C. 错误与异常

当你开始学习编程后，最不陌生的反馈应该就是来自计算机的报错信息（error message）。看到报错没什么可紧张的，就算是经验丰富的程序员，也不太可能一次就把一个程序毫无错误地从头写到底。报错信息只是 Python 想要温柔地告诉你哪里出了问题的方式 :)

在看懂报错信息前，我们首先要了解下在 Python 编程中可能会出现什么错误。

第一大类错误是**语法错误**（syntactic errors），新手最易犯，即写出一些 Python 语法不允许的表达式（illegal expressions），比如忘记加冒号、忘记缩进等。出现语法错误的代码不能通过编译。好消息是 Python 语法分析器会帮你找出所有语法错误，并以 `SyntaxError:` 的信息来提示你具体错误在哪里，比如：

```python
>>> print "abc"
File "<stdin>", line 1
  print "a"
		  ^
SyntaxError: Missing parentheses in call to 'print'
```

这条报错信息就非常清楚地告诉我：1. 是语法错误；2. 具体错误是没给 `print` 加括号；3. 出错位置在第一行（向上尖箭头指着检查出错的具体位置，但这个指示不表示错误仅在尖箭头处出现，还可能在附近）。

.

当语法正确时，还可能出现**语义错误**（semantic errors）。语义错误指的是代码的含义出了点问题。

语义分为两大类：

> - 静态语义（static semantics）: 如，这句代码是否有意义；
> - 全语义（full semantics）: 这个程序的目的是什么？会生成什么结果？

静态语义错误也叫**异常**（exception）或**运行时错误**（runtime error），Python 会在运行时帮忙判断一部分静态语义错误，以 Traceback 的形式返回报错信息。这里示范两个静态语义错误：

```python
>>> a + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
  
>>> a = '3'
>>> a + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

这两条 Traceback 指出了异常的类型：分别是 `NameError` 和 `TypeError`；还告诉了出错的位置。

为什么会报异常呢？因为 Python 解释器不能理解代码的含义是什么：第一条，变量 a 没赋值；第二条，字符串与整型不能相加 (相加无意义)。

.

全语义的错误 Python 就无能为力了。因此有时就算你写的程序可以正常运行，也吐出一些似乎正常的结果了，也不代表这个程序就没有任何错误。

为了减少编程中可能产生的错误（bug），降低后期捉虫（debug）的时间，学会一套专业优雅的编程风格绝对是必要的。

.

.

#### D. Develop Good Style 风格指南

说到底，所谓风格就是编程习惯；好的编程风格不仅让你看起来更专业，还能让你的代码更易于维护，编程时心情也更愉悦 :)

在现阶段已经可以依样画瓢遵循的风格指南有：

> 1. 写好注释，让自己一年后也依然能读懂这段代码；
> 2. 取有意义的变量名，让业内人士一眼能看懂这个变量代指的含义；
> 3. 合理空格；
> 4. 不要随意改变变量的类型（type）；
> 5. 测试一个代码块中的所有分支（branch），确保每个分支都有结果（fruitful）。

还有更多更多写出优美代码的 Python 编程准则，在今后的教程中还会不定时地继续插入更多。

.

.

#### 第5节 作业

- 阅读 *Think Python: How to Think Like a Computer Scientist* (2nd Ed) Chapter 5.1-5.7
- 完成 Think Python Chapter 5 课后习题 5.2.1, 5,3,1.


.

#### 第5节 小结

这一节的重点是学会写条件控制代码块。此外，我们初步读懂了各种语法、语义报错信息，还初步建立了对优雅 Python 编程风格的印象。已经可以用 Python 代码来表达更多想法了呢！







