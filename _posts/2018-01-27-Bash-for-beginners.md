---
title: 写给小白的第一份命令行工具Bash教程
date: 27-01-2018
categories: 
- A Developer Guide for Newbies - Starting with Python
tags: 
- Bash
- vim
---



> 这是一枚属于拖稿很久的「面向小白的 Python 教程」系列的彩蛋。
>

.

作为一个编程小白，你是不是见过其他程序员电脑屏幕上这样花花绿绿的窗口以及一双在键盘上飞快跳跃自带重影的手？

![](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRwzybUvLyuz8bDpu85yPmJMR85ic7q3hJHTL4Obic1R4PC0emsdAUakrg4gicPGn9OcfonbaliaEuE1FA/0?wx_fmt=jpeg)

徘徊半天不好意思开口问对方窗口里的那些命令是什么，暗暗希望自己有一天也能把屏幕搞得如此神秘炫酷？

——你需要一篇优秀程序员必备的命令行工具教程！

.

#### 近看 Bash

关于命令行（command line）工具和终端（terminal）的概念，我们在「Python 教程」的开篇就简单介绍过了：

> 一开始对于 Terminal 这个东西理解困难的读者，可以把它想象成一个壳（shell），在这个壳里，你可以写命令（command），这些命令直接发给电脑，电脑收到特定命令会执行特定行为，比如打开、编辑、删除文档。

> 而 Terminal 只是承载了这个壳（命令行工具）的 APP 的名字。你还可以像我一样下载其他类似的 APP，比如很多程序员都爱用的 iTerm (https://www.iterm2.com)，功能更加强大。

当时我只说了这个可以写命令的 APP 的名字，为了不让小白产生混淆，没提主流命令行工具的本名 — Bash。Bash 的维基百科定义是，

> Bash is a **Unix shell** and **command language** written by Brian Fox [...] as a free software replacement for the Bourne shell.
>
> — Wikipedia

实际上 Bash 这个名称就是 *Bourne-again shell* 的首字母缩略词，而 Bourne shell 从维基的定义中可以看出是 Bash 的前身，即另一个（有点过时的）命令行工具。

Bash 是 Unix (Linux + macOS) 操作系统（operating system）的默认命令行工具。也就是说，只要你手边的计算机是苹果电脑或 Linux 系统电脑，那打开 Terminal 后就自动进入了 Bash 的环境。

> WIndows 10 用户现在有了从微软官方下载安装正经 Linux 双系统的选项！如果你短期内不打算换到 Unix 操作系统的电脑，又想提前感受更加敏捷流畅的开发体验，不妨试试这条途径。
>
> 我把相关官网链接放在文末了。

.

现在，可以点击 `⌘Space`  用 Spotlight 呼出 Terminal / iTerm 了。

.

#### Bash 入门

在 Terminal 窗口中，我们跟计算机直接交流的（编程）语言就是 Bash。

Bash 指令有点像 Python 函数（functions）。

> 一个 Bash 指令 = 关键词（keyword）[+ 一个空格 + 某个/些参数（parameter）]；
>
> 最后不要忘了点击 `enter` 键才能看到运行结果。

先来试一个非常简单直观的 Bash 指令：

```bash
$ echo Hello World!
```

（代码框内 `$` 符号后面的才是 Bash 代码，下同）

你看到什么回应了吗？

——这个名叫 `echo` 的指令是不是和我们熟悉的 Python `print()` 语句差不多？

Bash 有些指令或许看起来复杂，但实质上和这行 `echo` 语句的语法本质是差不多的。

.

#### 相对路径与绝对路径

前文提到了**操作系统**（operating system）这个词，那操作系统到底指的是什么呢？

某种程度上，我们可以把操作系统看作一台电脑里目录（directories，即文件夹 folders 的另一称呼）与文件（files）的组合。任何一个目录或文件都自带一个路径（path），表示其在操作系统中的地址——就像可以通过网址找到对应的网站一样。当你在使用 Bash 时，你总是在某个有特定路径的目录下；想知道目前所在的目录或路径可以输入这个 Bash 指令：

```bash
$ pwd
```

`pwd` 是 present working directory 的缩写；working directory 是指你（在 Terminal 里）目前所在的操作目录。比如，我现在的路径和操作目录就可以在下面输出结果中看到：

```Bash
$ pwd
/Users/sinansmac
```

（路径表示方式是不是和网址很像 :）

所有目录以“**树**（tree）”的结构呈现。“树”在计算机科学中是个重要概念，是一种数据结构，以后我们还会反复遇到。

为什么说电脑里所有目录构成“树”呢？看看下面的目录结构解剖图就懂了：

![](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRwzybUvLyuz8bDpu85yPmJMLks8JLmxulBamRUbUcR04vcINShoJt117Nics5mtXxcymHXN2gllygA/0?wx_fmt=gif)

在这棵倒立的树的每个分支处都是一个目录，树根有一个唯一的根目录（root），从根目录可以延伸出无数子目录，每个子目录的路径都可以非常清晰地从这棵树上看到。比如，english 子目录的路径就是 `/Users/carol/english` ；`/` 表示 root。

.

知道了路径表示目录或文件在操作系统中地址，就可以不点开 Finder/文件管理器 这类图形界面，在 Terminal 中直接访问目标文件夹或文件。

在 Unix 操作系统中有两种描述路径的方式：绝对路径（absolute path）与相对路径（relative path）。

绝对路径即为**从根目录出发**的的路径，比如前文的例子 `/Users/carol/english` 。

相对路径则是相对于目前所在目录位置的路径。举个例子，如果我目前在 carol 这个目录里，想去访问 english 子目录，那相对路径只需从 carol 出发，表示为 `english` 即可。

.

#### Navigating in Bash

知道怎么写路径了，就可以用 `cd` 这个 Bash 指令关键词访问相应路径。比如，

```bash
$ pwd
/Users/carol
$ cd english
$ pwd
/Users/carol/english
$ cd /
$ pwd
/
$ cd ~
$ pwd
/Users/carol
$ cd physics
$ cd ..
$ pwd
/Users/carol
```

> `cd` 为 change directory (更换目录) 的缩写。

> `/` 为 root directory 的表示方式，前文提到了。

> `~` 为 home directory 的表示方式，这个半角波浪符号的英文名是 tilde。

> `..` 表示退回到上一级目录，所以这里又回到 carol 了。

.

频繁与 `cd` 交替使用的一个指令是 `ls`，可以列出当前目录下所有子目录与文档（这样你才知道能够 `cd` 到哪个目录去）：

```bash
$ pwd
/Users/carol
$ ls
physics
english
$ cd physics
$ ls
proj.txt 
foobar
```

> `ls` 为 list directories 缩写。

.

此外还可以创建一个新目录（即创建新文件夹），用 `mkdir` 关键词，加上新目录名字这个参数。如，

```bash
$ pwd
/Users/carol
$ ls
physics
english
$ mkdir programming
$ ls
physics
english
programming
```

> `mkdir` 为 make directory 的缩写。

创建了新目录后可以用 `ls` 查看是否创建成功。思维方式依然强烈依赖图形界面的同学，可以打开相对应的文件夹，你会看到一个新的文件夹静静地躺在那儿。

.

删除一个目录用 `rmdir dir-name`：

```Bash
$ pwd
/Users/carol
$ ls
physics
english
programming
$ rmdir programming
$ ls
physics
english
```

> `rmdir` 是 remove directory 的缩写。

.

#### 用 Bash 取代 Finder / 资源管理器

我现在已经记不太清如何在 Windows 电脑上新建文档或搜索文件夹内内容了，因为我有 Bash :p

下面让我来介绍下如何用 Bash 相关小工具更快更优雅地完成所有你在 Finder / 资源管理器内能够进行与无法进行的常用操作。

.

##### 新建、删除文档

在合适的目录下输入：

```Bash
$ touch sinan-talk.txt
```

看一眼 Finder，或接着输入 `ls` 指令，是不是能看到一个名为“sinan-talk”的 txt 空白文档？用 `touch` 指令新建任意文档就是这么简单。

删除一个文档可以：

```bash
$ rm sinan-talk.txt
```

> `rm` 即为 remove 缩写。

`rm` 还可以用来重命名文档，使用方法如下：

```bash
$ rm old-name.txt new-name.txt
```

> `rm` 删除掉的文档或文件夹不会出现在垃圾桶中，小白请慎用。

.

##### 预览文档内容

找一个内容的文档，在其目录下输入：

```bash
$ less sinan-talk.md
```

> `.md` 是 Markdown 格式文档的扩展名。

此时你会看到 Terminal 窗口变成了 sinan-talk.md 这个文档内容的预览窗口。这个功能是 `less` 实现的。

退出预览点击 `q` 。

除了文字文档外，还有很多文件类型都能直接在 Terminal 预览，比如音频文件（但需要多走一步安装其他类似 `less` 的小工具）。

.

#####  查看文档内容，合并文档

查看文档内容除了用 `less` 指令外，还常用到 `cat`。`cat` 不会跳到预览界面，而会把文档内容直接返回。比如，

```bash
$ cat sinan-talk.md
### 玩转命令行工具 Bash — 马上让你看起来像个资深程序员！
...
```

除此之外，`cat` 还可以用来做简单拼接文档的工作。比如，

```bash
$ cat f1.txt
Programming is the most fun
$ cat f2.txt
when you can have your clothes on.
$ cat f1.txt f2.txt > newfile.txt
$ cat newfile.txt
Programming is the most fun
when you can have your clothes on.
```

> `cat` 本身是 concatenate（串联）的缩写，即“首尾相连接在一起”。

这里涉及到 `>` 这个符号。虽然是半角大于号，但在 Bash 脚本中常可以把 `>` 看作用于指向的箭头。`cat f1.txt f2.txt > newfile.txt` 里 `>` 很形象地指向了一个保存拼接内容的文档名称。

这里的 `newfile.txt` 既可以是先前不存在的文档（电脑会即时创建这个新文档）；也可以是已经存在的文档（但此步操作会覆盖掉文档中原有内容）。

.

##### 查看文档大小、长度、字数

这个需求也非常常见。用 `wc` 这个小工具即可快速查看各种大小参数。

> `wc` 是 wordcount 缩写。
>
> `wc [-options] [file]`  这个指令可以配不同的选项（options, 也称 flags）。通过明确不同的选项，可以分别查看文档的字数、行数、字节数。具体如下：
>
> `-c` 字节数
>
> `-l` 行数
>
> `-w` 字数

例如：

```bash
$ wc -l blog-post-80.txt
	366 blog-post-80.txt
$ wc -w blog-post-80.txt
	1772 blog-post-80.txt
$ wc -c blog-post-80.txt
	18857 blog-post-80.txt
```

.

##### 不想浏览长文档的全部内容

在程序员的日常中常常需要处理很大的文档（成千上万行内容或更多），这种时候没有正常人会直接打开这个文档（因为太慢，或有些编辑器不支持，或太占用电脑的 working memory），也不便于在命令行直接浏览。此时有个只浏览前 N 行的小指令就非常方便了。

这种情况下我们可以使用 `head` 指令。

```bash
$ wc -l long-file.txt
234124
$ head -10 long-file.txt
Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, 
and the universe trying to build bigger and better idiots. 
So far, the universe is winning.
...
```

`head` 紧跟的数字选项是你想查看的前 N 行内容。前 10 行即为 `head -10`.

配上上面刚学到的 `>` ，`head` 还可以非常方便地选中文档前 N 行内容并单独保存到另一个新文档中。

```Bash
$ head -10 long-file.txt > short-file.txt
```

这样就不用在文档之间跳来跳去地反复“复制粘贴”啦。

.

##### 用文本编辑器打开文档

这个指令就很简单啦！如果我想用 Atom 或 SublimeText 这两个主流文本编辑器打开一个文档以便进一步编辑，可以这样：

```bash
$ atom sinan-talk.md
$ subl sinan-talk.md
```

此时会跳出相应的应用界面。

如果想一次性打开此目录下所有文档，可以用 `.` 表示： 

```bash
$ atom .
```

（以上操作的前提是你已经下载安装了 Atom 或 SublimeText，否则请看第一篇）

.

##### 其他可以一秒上手的 Bash 小技巧

- Tab Complete

各种指令、目录名、文档名手动敲来敲去会让人很快失去耐心。当你写 Bash 指令写到一半时，可以单击 Tab 键，Terminal 会尝试自动补全你的指令。

比如，你输入 `ec`， 再点击 Tab，会被补全为 `echo`。

Tab 还可以用来补全目录名称与文档名称，但前提是你已经输入了一半的名称在当前目录下无歧义，否则 Terminal 没法帮你精准地偷懒。

- 快捷键跳到语句首末

Terminal 内不能用鼠标改变光标位置，因此改变光标输入位置对于新手来说会是件可能会把人逼疯的事。但你只要记住以下四个快捷键组合就可以相对迅速地在指令中跳来跳去修改内容。

> `esc + b` -  跳到前一个词
>
> `esc + f` -  跳到后一个词
>
> `ctrl + a` -  跳到开头
>
> `ctrl + e` -  跳到末尾

还有更多“高级”指令可以做到更多，比如交换光标前两个单词的位置等等。在这儿就先不详述了。

- 重复输入旧指令

单击键盘上的 🔼 键。可多次点击回溯旧指令。

在 Python console 中也适用。

- 查看 Bash 指令历史记录

```bash
$ history
```

.

#### 让 vim 承包文档编辑任务

早在 Python 第一节，我就已经简单介绍过“工程师的文本编辑器 (text editor)”了，但当时我们着重介绍的 Atom 和 SublimeText 依然存在图形界面。今天我们要学着使用一款丢掉外壳，直接从 Terminal 进入文本编辑模式的编辑神器——**vim**。

vim 功能十分强大，如果你能熟练运用，这绝对是大大提高你工作效率（和炫酷程度）的程序员工具。但 vim 和 Bash 本身一样，对从没接触过的人来说，理解起来需要一定时间，学习曲线一开始会有点陡峭。这也是为什么当你在谷歌上搜索“vim tutorial”时会瞬间跳出无数结果……

想知道如何用 vim，可以直接在 Terminal 内输入：

```bash
$ vimtutor
```

这是个完整的 vim 教程，带详细说明和练习，有空可以慢慢敲完。

如果你更习惯更加直观的练习教程，可以试试这个网站（http://www.openvim.com）。

我是那种走一遍教程也记不全的人，所以喜欢下载、手写一些 cheatsheets 帮助记忆。你也可以试试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRwzybUvLyuz8bDpu85yPmJMrdTd9Z2eJgSicjZPxqbxEJXjTgotAcL6PVhUoyescvBd3bGAFZ7rg8w/0?wx_fmt=jpeg)

（苹果电脑一般自带 vim，Linux 可能要自装）

.

#### 小结

认真跟下来这篇 Bash 教程的小伙伴想必会忍不住赞美一下这个强大又炫酷的开发工具了吧。

总结一下各类程序员开发工具的精神就是：偷懒，炫酷，偷更多懒。

Bash 一开始学习曲线会相对陡峭，但说到底还是能否下决定搞熟练的问题。练习直到形成肌肉记忆，是条踏实的捷径。毕竟，长远看来 Bash 会为你的开发生涯节约无穷无尽的时间，让你把那些时间留下给思考更重要的问题。

**Work smarter, not harder!**

.

#### 资源区:

Win10 安装 Linux 双系统，官网指引：

https://docs.microsoft.com/en-us/windows/wsl/install-win10

友好的 vim 教程：http://www.openvim.com

万能的 Bash (shell) 指令查询网站：https://explainshell.com











