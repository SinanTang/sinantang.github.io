---
title: 写给小白的工程师入门 - 从 Python 开始
date: 31-08-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - programming
  - python
  - newbie
---

这是我**面向小白写的 Python 编程教程**的第一篇。本周三已经抓勺子同学上完了这节课，得到了很多珍贵反馈，于是我把讲义初版又修改了一遍，放到⌈影子练习SinanTalk⌋上来。

原本有想法招募一个 ⌈给小白的工程师入门 - 从Python开始⌋ 的在线学习实验小班，不为赚钱，只是想实践下自己的编程教学思路。但后来和勺子讨论过后，我也同意我的设想太过苛刻——我想找到大概率可以坚持学习 Python 编程一年及以上 ／ 有长期 (指一年以上) 目标 ／ 但无短期急功近利想法 的同行小伙伴们。我明白人群中一定存在着这样的人，可我的个人影响力尚小，也无太多精力可以用在这件“不务正业”的事上。于是，就决定只对勺子同学一对一授课，把每次修改过的讲义发到这儿来，供更多有心的读者参考。



如果你认可这篇教程的价值，欢迎分享到朋友圈，分享给更多人！有看不懂的地方也可以留言或者加我的个人微信（LynnTang_）问询。越多关注，作者就越多动力及时更新呐 😊



## 写给小白的工程师入门 - 从 Python 开始

macOS 版本



### 第1节  基本开发环境设置

#### a. 学会使用基本命令行

- ##### 命令行的基本设置

在键盘上点击 `⌘Space` ，用 Spotlight 呼出 Terminal。

> 一开始对于 Terminal 这个东西理解困难的读者，可以把它想象成一个壳（shell），在这个壳里，你可以写命令（command），这些命令直接发给电脑，电脑收到特定命令会执行特定行为，比如打开或编辑某个文档。
>
> ——那为什么不直接去双击那个文档的图标来打开呢？
>
> 因为用命令行（command-line）快很多！编辑一个文本或许看不出效率的差异，但要想编辑一百个文本的话，一个个地去用鼠标双击打开再编辑保存关闭……是很累的。但使用命令行的话，不管是一个还是一百个，所用时间和需要的操作都差不多。工程师是很懒的人，能逃掉重复步骤的地方就想方设法地要逃掉。
>
> 最后，Terminal 只是承载了这个壳（命令行工具）的 APP 的名字。你还可以像我一样下载其他类似的 APP，比如程序员爱用的 [iTerm](https://www.iterm2.com/), 功能更加强大。



愿意通过提高 Terminal 的外观来提高工作效率和愉悦程度的人，应该选择给 Terminal  换个皮肤：

> 我用的是这个：◦ [Spacegray](https://github.com/wtanna/Spacegray-OSX-Terminal-Theme)



再换个字体。其实字体很重要，除审美和健康需求外，好的字体还可以提高工程师的工作效率。

选择字体的基本原则是“等宽”。等宽字体（如 Courier New）对中文友好，可以轻易辨识出“全角／半角”字符。

除此之外，是否能清楚区分易混淆的字符也是选择字体的重要因素。

> **常见易混淆字符：**
>
> 数字0  vs  字母O
>
> 数字1  vs  大写字母I  vs 小写字母l  vs  运算符|
>
> 数字9  vs  字母q
>
> 分号;  vs  冒号:
>
> ……

我用的是 Courier New。

.

顺便把字号设置得大一点，具体多大视自己电脑屏幕尺寸而定——顺便提一句，有研究表明，电脑屏幕越大，人的效率就越高。所以，一块儿大屏幕还是很值得投资的。

设置 Terminal 的**字体字号**可以在 `Preferences > Profiles > spacegray > Text > Font` 中找到。

.

- ##### 查看是否已经安装 Python，以及 Python 版本（mac／ Linux 已内置 Python2.7，windows 需下载）

在命令行输入：

```shell
python --version
```

若返回了类似于 "Python 2.7.10" 的信息，则已有 Python 2.7.

> Python 2.7 与 Python 3.6 是最重要的两个 Python 版本。Python 3.6 更新，但 Python 2.7 也依然常见。
>
> 两个版本的差别不是特别大，Python 2.7 的网络学习资料更多，但直接从 Python 3.6 开始后面就不用再适应不同版本之间的差别了（当然，以后还有会 Python 4，5……）。



- ##### 安装最新版 Python 3.6

两种方法，第一种直接从命令行安装（看起来更像工程师），依次复制粘贴以下5行代码到 Terminal（一个字母或空格都不能错）：

```shell
xcode-select --install     #安装 XCode Command Line Tool
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"   #安装 Homebrew
curl -O https://raw.githubusercontent.com/donnemartin/dev-setup/master/.bash_profile
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
brew install python3       #用 Homebrew 来安装最新版 python
```

`#` 及后面的内容为备注（同一行内），不需要粘贴入 Termimal（写了也会被忽略）。

小白肯定看不懂大部分指令的含义，不过此时不需要深究，先把目的达到再说，以后会慢慢明白的。



第二种安装方法即传统安装，去 [Python 官网下载页](https://www.python.org/downloads/mac-osx/)，下载需要的版本。接下来跟着指示一步步走即可，参考[安装文档](https://docs.python.org/3/using/mac.html)。



- ##### 在命令行以交互模式写 Python 代码

直接在 Terminal 中输入：

```shell
python
```

这样一般使用了默认的 Python 2.7 版本，如果想用 Python 3.6，可以这样：

```
python3.6
```

当看到光标出现在 `>>>` 之后，就可以输入你的第一行 Python 代码啦！

```python
print "Hello World"   #python 2.7
print("Hello World")  #python 3.6
```

`#` 及后面的内容为备注（同一行内），会被 Python 编译器直接忽略。

看到返回了 `Hello World` 即为成功！



#### b. 工程师的编辑器

- ##### 使用命令行和文本编辑器来运行 Python 脚本

有时我们需要运行多行的代码时，直接在 Terminal 中一行一行地输入会很不方便，这时选择用文本编辑器来写代码、用命令行工具运行写了代码的文本（称为**脚本 script**），就会方便很多！

工程师爱用的编辑器很多，Atom, SublimeText, vi/vim ……我们不参与任何编辑器之间比较的争论，就以 Atom 为例来看一下如何从命令行运行 Python 脚本。



- ##### 安装 Atom

在 Terminal 中输入以下两行代码：

```shell
brew tap caskroom/cask     #安装 brew cask
brew cask install atom     #下载 atom
```

或者也可以按传统方式安装，去 [Atom 官网](https://atom.io/) 下载，打开后拖到 `Applications` 目录去。



- ##### 体验 Atom

有了 Atom 后，可以通过 Spotlight 打开一个 Atom 空白文档，打上我们之前已经见过的第一行 Python 代码：

```python
print "Hello World"   #python 2.7
print("Hello World")  #python 3.6
```

点击 `⌘S` 保存脚本，可以取名为 `test.py`（注意 Python 脚本的扩展名为 `.py`）。保存为 Python 脚本后可以看到代码变彩色了（这就是文本编辑器提供的 syntax highlighting 功能），变得更易辨识。



- ##### 用命令行运行 Python 脚本

接下来回到 Terminal，如果还停留在之前 Python 编译器的页面，可以点击 `⌘T` 打开一个新的空白页（new tab），接下来输入：

```shell
python Path-To-Your-Script/test.py   #使用 python 编译器打开刚写好的脚本；将‘Path-To-Your-Script’替换成你刚写的脚本的路径
```

（不知道一个文件保存在哪儿了的话，可以去到那个文件所在的文件夹，`⌘C` 复制该文件，再 `⌘V` 粘贴到 Terminal，就能看到该文件的路径了。）

此时若在 Terminal 里看到 `Hello World` 就说明操作成功啦！



#### c. 认识 IDE：安装使用PyCharm

Integrated Development Environment (**IDE**)，中文为**集成开发环境**，可以理解成集合了以上我们使用的文本编辑器、命令行工具与文件管理的开发软件。与单纯使用文本编辑器或命令行相比，IDE 更“有条理”，辅助工具更多，也更好上手编程。

让我们用通过一个主流的 Python IDE - PyCharm 来体验下 IDE 吧。

在 Terminal 里输入：

```shell
brew cask install pycharm-ce  # -ce 表示免费的 community 版本
```

等安装结束之后，可以尝试直接在 Spotlight 呼出 PyCharm。

当然也可以按传统安装软件的方式，去 [PyCharm 下载页面](https://www.jetbrains.com/pycharm/download/#section=mac)，下载 Community 免费版本，再拖到  `Applications` 目录去……



- ##### 体验 PyCharm

接下来打开 PyCharm，需要设置一下，基本都可以按默认设置点到最后。PyCharm 的主窗口出现后，左侧已经初始化了一个名叫 untitled 的 project，可以右键点击该名称 New > Python File 换个名字（比如 MyFirstPythonProject）。

右键点击该 project 的名称，选择 `New > Python File`，在这个 project 目录名下新建一个 Python File，再取个名 test.py（注意：因为已经选择了新建 Python File，所以在这儿不需要加 .py 的扩展名）。

现在，在空白的 test.py 编辑区打下我们已经很熟悉的第一行 Python 代码：

```python
print "Hello World"   #python 2.7
print("Hello World")  #python 3.6
```

PyCharm 会自动保存所有改动，所以不需要再手动敲保存键。

你可能已经注意到 PyCharm 自动把输入的代码变成了彩色——其实 PyCharm 还会帮你自动缩进、自动补全固定表达、自动检查语法错误……就像智能输入法！虽然特别便捷，但对于新手来说，弊端很明显：你本来很可能会犯错的地方都被提前预防了，这其实是在躲避你应掌握的编程知识。如果突然切换到普通文本编辑器或者命令行甚至手写代码时，新手才会发现，原来没了“智能输入法”的辅助，自己连基本语法也不能100%写对。。



来看一下运行结果：点击 `⌃⌥R`  会看到一个小窗口跳出来，让你选择要运行哪个文件（此时只有 test 可以选择），选中 test 后，就会在 PyCharm 窗口下方看到运行结果啦！



.

#### 第1节 - 作业：

- 熟练本节的知识点和操作；
- 熟练 Terminal / Mac 的基本快捷操作，最好打印下来贴起来，每天都背几行；
- 思考：三种不同的 Python 编程方式有什么区别与优势呢？



#### 第1节 - 小结：

我们了解了基本的命令行操作，安装了一些工程师的必备工具;

我们还尝试了三种不同的 Python 编程方式：命令行的交互模式，用文本编辑器与命令行配合，还有在 IDE 中编程；

虽然小白肯定会对很多细节半知不解，但慢慢来，以后都会掌握的。

