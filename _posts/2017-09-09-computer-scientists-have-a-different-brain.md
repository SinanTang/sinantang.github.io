---
title: 计算机科学家的脑子和普通人不一样 - 学习全新的思考方式
date: 09-09-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - programming
  - python
  - newbie
  - problem solving
---

这是我**面向小白写的 Python 编程教程**的第三篇。拿勺子同学当小白鼠讲过一遍后，就把修改完的讲义发到**⌈影子练习SinanTalk⌋**上来啦。

如果你认可这篇教程的价值，欢迎分享到朋友圈，分享给更多人！有看不懂的地方也可以留言或者加我的个人微信（LynnTang_）问询。**越多关注，作者就越多动力及时更新呐** 😊



------

最近在读 *Sapiens: A Brief History of Humankind* (《人类简史》)，作者赫拉利说，**书写系统的出现逐渐改变了人类思考问题的方式。**大脑最擅长的**自由联想**与**整体性思维**（free association and holistic thought）在科学符号系统发明后开始逐步让位于**局部思维**与**官僚主义**（compartmentalisation and bureaucracy，此处官僚主义指用大量文件、流程来管理生活以及国家的方式）。

![relativity](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRyXy5VicaSibGuwU1YyvqVRkViaCDBgYnibnAwAcLbBHjfs9r99qd2LMboCjmovy37ictcUv4ibsl4tkEKA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

{:.image-caption}

*插图来自《人类简史》*



正常人看到以上相对论的应用公式时都会瑟瑟发抖一秒并想要立刻逃开，如果你也有这种直觉，那说明——你是正常人类……但现代生活要求每个成年人都要懂得算术和一些科学知识——更别说还有你我这群试图写代码指挥电脑做事的不正常人类呢！学习另一套非自然语言（编程语言）的过程，的确是**改造大脑**的浩大工程。



![Everyone-should-know-how-to-program-a-computer-steve-jobs-840x560-e1467195471876](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRyXy5VicaSibGuwU1YyvqVRkVZ2GVsGXI0sTGXIKVf9oVvE8Xn6gQFZlT2knV4g1t0DtlEExIoCCkgQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

{:.image-caption}

*Steve Jobs 的这句名言流传颇广。但我不完全同意他的观点：乔布斯这句话假设了人类在学习编程前并不会思考。但我认为，只是人类的天然思考方式与编程要求的思考方式不同，仅此而已。*



所以，当你学了一门编程语言的语法和语义却不确定该如何使用，或者看代码示例似懂非懂但亲自实现一个功能就卡壳时，你要知道，这只是大脑还没被成功改造的信号。

这就是为什么在写完前两篇设置基础开发环境的教程后，我选择先写学习编程的目的和意义——先了解想要把大脑改造成什么样，再动手去改造——这样更符合人类大脑的天然学习习惯。

 

### a.  计算与算法

什么是计算 (computation)？

在讲什么是计算之前，我们先来看看另一个相关问题：什么是**知识** (knowledge)？

我们可以通过分类来认识知识。知识可以分成：**陈述性知识**（declarative knowledge）与**过程性知识**（imperative knowledge）。

> **陈述性知识**：事实性陈述；比如，地球是圆的。
>
> **过程性知识**：告诉你该如何进行推断的描述性知识；比如，如果你去海边望向远处，就会发现海天交接处的海平面并非一条直线，而是略带弧度，由此我们可以推断地球是圆的。

陈述性知识不会告诉你如何证明、推断出一个结论；而过程性知识就像**菜谱**一样，按123步骤走，你就能得出设定的结果。

毫无疑问，计算 (computation) 属于第二类过程性知识。你大可以把计算想象成实用的菜谱：**软件工程师是发明菜谱的人，电脑只是个炒菜的……**



另一个计算机科学家常挂在嘴边的抽象术语，**算法** (algorithm)，只要借助计算这个我们刚学的概念，其实并不难理解。很多人对算法打怵，很可能是把它想象成了上面那个相对论的应用公式了吧……当然，很多复杂的算法确实和高数紧密相关，但算法并不一定非要扯上高数。

简单地说，算法即为描述**具体如何执行一次计算**的方法。计算通过算法实现。或者说，算法就是计算的“套路”。

> Algorithm - how to perform a computation.

具体来说，算法包含了**指令**（instructions），**控制流程**（flow of control），**结束条件**（termination condition）。

举个例子，我们都坐在马桶上读过洗发水的成分表和使用说明书吧？其中很短的几行“如何使用”就是**洗发的算法**：

> 1. 打湿头发；
> 2. 倒适量洗发水到手掌；
> 3. 把洗发水抹在头发上；
> 4. 按摩头皮，打出泡沫；
> 5. 用清水冲洗头发；
> 6. 若有需要，重复步骤 2 - 5。
>

这个算法的指令即为以上6步；控制流程可以理解为步骤之间的顺序，比如，步骤5肯定在步骤3之后，但步骤2可能会出现在步骤6之后；至于结束条件，严格来说这里并未给出——并没有一句指令明确告诉用户：“走到这步洗发就结束了”。



### b.  学编程学的是什么？

对于初学者来说，一开始新鲜语法（syntax）和计算机概念学习可能会占用大部分时间，但那些只是在学习 WHAT，任何肯下功夫的正常人都能学会；更重要的是，当你有了一堆“积木”后，该如何 (HOW) 把它们拼插成一座好用又好看的代码城堡（还记得 WHAT-HOW-WHY 思维框架吗？）。

不怕再多强调一句，在编程领域，掌握 **HOW 比 WHAT 要重要得多**！因为，编程的本质就在于**解决问题**（problem solving），只不过程序员通过编程语言借助计算机来解决问题（computational problem solving）。具备能与计算机“沟通”问题，借助计算机力量来执行解决方案的能力，就是我们常听到的“计算思维（computational thinking）”。

这么讲还是有些抽象，下面我来举个简单的数学例子，来近距离观察下计算思维的一个具体实现形式。

> 我想知道一个任意正实数 x 的平方根。只给你一张纸一支笔，你能给出一个可执行的解决方案吗？

.

。。。1分钟思考时间。。。

.

这里给出一个求平方根的经典“菜谱”：

> 1. 先给出一个猜测 y；
> 2. 如果 y*y 和 x 之间的差距足够小，那就可以说 y 是 x 的近似平方根，并结束计算；
> 3. 否则，给出一个新的猜测 y2，使 y2 = ( y + x/y )/2，即 y 与 x/y 的平均数；
> 4. 用这个 y2 替代 y，回到第2步。
>

相传，这个求平方根的算法是古希腊数学家希罗首先提出的。

先不去管该如何用 Python 实现以上算法，但这个解决方案给出了一个非常重要的算法思路：**先猜测，再验证** (Guess and Check)。实际上，简单计算器就在用类似的算法思路求平方根（但不是这个具体的算法）。



![computer-office-calculator-pen-163119](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRyXy5VicaSibGuwU1YyvqVRkVUbBXCjXKic6F1K5jSeHQULEaA0zTQ1x3opZJaiaRuWkLLlyaFA9RN72g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

{:.image-caption}

*image credit: PEXELS*

某种程度来看，计算器和我们的个人电脑很相似。

只不过计算器只能运行特定程序，而且只接受特定输入（input）——我们称这类计算机为**固定程序计算机**（fixed-program computers）。最初的计算机都属于这类。比如，二战期间图灵设计的破密计算机，尽管体积非常庞大，但这台机器只能做唯一一件事，那就是破译德军的恩尼格玛（enigma code）。



![](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRyXy5VicaSibGuwU1YyvqVRkVd3rjnHJGiagib0KLySFChibOHcj3zO0ggWhVPialicKyJrqsy8247oUCOgA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

{:.image-caption}

*The Bombe machine (Image Source: http://www.cryptomuseum.com)*



而现代的个人电脑就强大太多了，可以用来算数，还可以运行各种各样的程序。这是因为，现代计算机不仅可以像计算器一样读取数据，还可以直接读取程序。这类计算机即为**存储程序计算机**（stored-program computers），或称为“**通用计算机**”。



### c.  像计算机科学家一样思考 Think like a computer scientist

> ⌈好了，我知道计算思维很重要了，可是，“解决问题的能力”指的到底是什么？⌋

所有问题的解决过程都可以归纳总结成以下3个步骤：

> 1. 提出问题 to formulate problems；
> 2. 思考解决方案，越多越好 to think creatively about solutions；
> 3. 清晰准确地把最佳解决方案表达出来 to express a solution clearly and accurately。

上面求平方根的题目就是一个解决问题的实例。

计算机科学家一方面像自然科学家，观察现象、提出假设、进行测试；又像数学家，使用形式语言科学符号提出问题与解决方案；还像工程师，设计方案、组装方案、评估效果。

![think like a computer scientist](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRyXy5VicaSibGuwU1YyvqVRkVQuWJhlOKxbynHzHJaW61aKeAjd6Sj244gh82A4YCibjTzsrc2wqPu8A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)



显然，"能够解决问题"并非一项计算机领域所独有的技能。但是，通过学习编程可以大大提高一个人解决问题的能力，不止由于可以求助计算机来解决一些问题，更因为通过解决无数问题而训练出的如何解决问题的逻辑思维方式会深深地刻在大脑皮层——这不就是所谓“改造大脑”吗？



再举个常见的数学例子——如何用多种方法又好又快地证明质数也是程序员技术面试的常见题。

> 给出任意一个大于1的自然数 x，如何确定 x 是否是质数？给出一个可执行的算法。

.

。。。思考1分钟。。。

.

其中最直观最简单的一个算法或许就是“挨个试试能不能整除所有比 x 更小的正自然数”了吧。

质数的定义，“除1和它本身以外，不再有其他因数”。因此，除1和 x 以外，如果找到一个可以整除 x 的自然数，就能证明 x 不是质数，反之则为质数——那就从2开始到 (x - 1) 为止，用 x 去挨个除所有自然数呗（在 CS 里，这种“挨个测试”的方法被称为**遍历** traversal）。

如果用笔去计算的话，当 s 大于2位数时，恐怕就没人想去动笔了……但计算机不一样，不管你喂给它多大的 x，只要承受得住就会任劳任怨地算下去，最终还你一个答案。

> 这句话不全对，计算机并不会完全接受所有程序。在 Python 程序中，有时你可能会不小心陷入无限循环中去；如果是递归方程，在递归深度超过1000左右时 Python 编译器就会报错并停止运行（“RuntimeError: maximum recursion depth exceeded” :)

.

### 第3节 - 作业

- 仿照平方根的计算步骤，为遍历证明质数的算法写一个可执行步骤。
- 思考是否能改进上一题的算法，找到更优解（更优指完成计算所需的总步骤更少，少于从 2 到 (x - 1) 共 (x - 2) 步），试着完整地写出来。
- 你在麦当劳里点过麦乐鸡块吗？麦乐鸡块只有三种规格：6块／9块／20块每盒。如果有位消费者来到柜台前对点餐员说，我想要 xx 块麦乐鸡，你是否能快速告诉点餐员这个要求是否合理？合理即为可以用现有三种规格的麦乐鸡块的组合满足要求，比如，6块、15块、26块都是合理的，但10块就不合理。整理自己的思路，试着完整地写出验证步骤。（麦乐鸡问题 (McNuggets Problem) 是丢番图方程 (Diophantine equation) 的一个变形，有兴趣的可以去搜索更多相关资料）



### 第3节 - 小结

这一节我们从代码细节中暂时抽身，站在高处审视了一下计算机科学家这个物种——计算机科学家是数学家、自然科学家与工程师的结合体，对于计算机科学家来说，最重要的是技能是解决问题的能力。我们还通过几个例子体验了计算思维与算法，接下来我们就会开始学习怎样用 Python 实现这些算法。

