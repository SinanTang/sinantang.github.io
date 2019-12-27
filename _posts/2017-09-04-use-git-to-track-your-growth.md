---
title: 用 Git 记录成长轨迹 | 写给小白的工程师入门
date: 04-09-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - programming
  - python
  - newbie
  - git
  - github
---



这是我**面向小白写的 Python 编程教程**的第二篇。拿勺子同学当小白鼠讲过一遍后，就把修改完的讲义发到**⌈影子练习SinanTalk⌋**上来啦。

和勺子上课时，我意识到，不和新手交流的话，离出发点越远的人就越不可能记得自己当初学习笨拙的样子。但事实是：**谁都是那样开始的。**所以就算你要花几天时间才能完成这篇教程的内容，也不要觉得自己太笨太慢，毕竟每天都能进步一点点就已经很可贵了。

如果你认可这篇教程的价值，欢迎分享到朋友圈，分享给更多人！有看不懂的地方也可以留言或者加我的个人微信（LynnTang_）问询。**越多关注，作者就越多动力及时更新呐** 😊



------



### a. Git 是什么？

关于 Git，有这么一个浪漫的说法——“**工程师的时光穿梭机**”。

我以前在公司实习时，老板总会说，"Don't worry. You won't break anything (because we have git!)." 

如此神奇的 Git 其实是一个版本控制（Version Control System, VCS）工具，可以用它来快速有效地管理成千上万个文件（不止是代码）的历史版本与进度。对于编程小白来说，Git 是个全新的概念，完全理解并掌握需要时间加练习，这篇教程就会带你完整走完“安装 - 设置 - 使用 Git”一条龙学习体验。

顺便提一句，“可以熟练使用 Git”是值得写在求职简历上的程序员技能哦！跟着这篇教程走几遍，完成课后作业，就可以让你的简历再添亮点。



### b. 安装并设置 Git 运行环境

- ##### 安装 Git

查看电脑是否已经提前安装了 Git，在 Terminal 中输入：

```Shell
git --version
```

若返回 `git version xx.xx.x ` (xx代表数字) 则说明电脑已经安装 Git，否则就需要跟着下面几步先安装 Git，继续在 Terminal 内输入：

```Shell
brew install git   # 这里假设读者已按第1节教程安装了 Homebrew，否则请返回第1节安装
brew link git
```

- ##### 设置 Git 运行环境

第一步，先设置通用的用户名与邮箱（与你的 GitHub 账号信息相同）:

```shell
git config --global user.name "Sinan Tang"            # 注意引号
git config --global user.email tangsinan92@gmail.com
```

如果没问题的话，输入下面两行检查刚才的设置是否成功：

```Shell
git config user.name
git config user.email
```

若返回了你输过的用户名与邮箱，则说明设置成功。

为什么要设置用户名与邮箱呢？为了今后每次你用 Git 提交改动 (commit) 时都会自动刻上你的个人信息，这个是无法改变的（指不能改变某次改动的作者，而非不能改变 Git 的用户名或邮箱）。



### c. 利用 GitHub 创建永不丢失的个人作品集

- ##### 什么是 GitHub？

上面以非常简短的篇幅介绍完 Git 基本知识后，让我们再来看看 GitHub 与Git 的关系。 

Git 是一个**版本管理工具** (VCS tool)，可以在命令行（command line）使用，可以在许多 IDE 内使用（比如PyCharm），也可以在网站使用——这个网站即为 GitHub，是更加直观的 Git 操作界面（web-based Git）与项目托管网站。从这三种途径进行的操作大多数时候可以相互替代。我一般用命令行来运行 Git 指令——虽然对于新手来说命令行不如网站界面那么直观，但熟悉后会发现命令行比网站方便快捷很多。

> 有时 GitHub 这个名称会让人困惑，因为创建 Git 与 GitHub 网站的公司也叫 GitHub。并且 GitHub 这个名称常用来指代基于 GitHub 的开发者社区——一个工程师们的主流社交网站！

GitHub 值得聊的趣闻轶事太多，这里就不占用过多字数，先把正事搞定！



- ##### 为什么要提交代码到 GitHub？

在讲具体操作前，来简单介绍下积极利用 GitHub 的好处。

有些IT公司招聘工程师时，会要应聘者的 GitHub 账号，目的是查看应聘者在 GitHub 上的真实**贡献值** (contribution activity) 和参与项目。如果你不是很清楚那是什么的话，可以参考下面我之前实习参与公司项目不到五个月的贡献值截图：





![](https://mmbiz.qpic.cn/mmbiz_jpg/ETsNbcnZdRy65bygnBWDlQwCz9Eq0PSvKhqvjbps17HQCofyY2bA0s1JRWGxicwdumuA4iakNHAYCL5yas33WQNQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

中间像日历一样的灰网格区域即为我提交代码的贡献值记录，深浅不一的小绿块儿代表了代码提交次数——越深提交越多。因此，当别人看到你的 GitHub 个人主页时，就能一目了然看到从你加入 GitHub 之后**每天**的贡献值。

正因为 GitHub 上的贡献值记录很难造假，所以对于工程师来说，GitHub 才是最真实的**个人简历**（不过听说国内有些程序员为了求职会去 GitHub 提交假项目……sigh）。



☺︎ **以下操作建立在读者已申请好一个 GitHub 账号的假设上——还没账号的请先去 https://github.com 申请哦!**

- ##### 创建 Git repository，克隆项目到本地

在上一节已经初步学会使用 PyCharm 的基础上，我们来看看如何在 PyCharm 中编程，并通过 Terminal 把代码改动提交到 Git 上。

安装了 PyCharm 后，会在电脑上自动生成一个文件夹叫 PycharmProjects，在 Finder 里找到它，在 Terminal 中打开。

> 要想在 Terminal 内打开某个文件夹，除了第1节提到过的“复制该文件夹 - 粘贴到 Terminal 内 `cd` 指令之后”之外，还可以：
>
> 1. **设置快捷键**：去往 `System Preferences > Keyboard > Shortcuts > Services > Files and Folders`，找到一个选项叫“New Terminal at Folder”，**启用**它并把后面的**快捷键**改成更顺手的键盘组合，比如我改成了 `⌃⌥⌘T` (T for Terminal)。每次只要选中一个文件夹，再按 `⌃⌥⌘T` 就可以很快在 Terminal 内打开啦！
> 2. **右键点击**：当你启用了“New Terminal at Folder”后，可以右键点击一个文件夹，点击跳出菜单的最后一行“New Terminal at Folder”
>
> 直接用快捷键呼出 Terminal 的方法最快捷（= 最像工程师），推荐！

然后在 Terminal 中输入：

```shell
git init     # init = initialise 初始化
```

这一步会在 PycharmProjects 内创建一个你看不到的文件夹 `.git` ，里面包含了所有你在本地使用 Git 的所需文件。

接下来，打开 GitHub 官网，登陆你的账户，在首页右下方有个窗口叫“Your repositories” (你的项目，有人翻译成“库”，但我觉得不如“项目”易于理解)，右边有个绿色按钮“New repository”，点开，在设置页面给这个项目取个名（Repository name），选择“Public”，选中"Initialize this repository with a README"，最后点击“Create repository”。这样你就拥有了自己的第一个 GitHub 项目！

在新建项目的主页，找到页面右端一个写着“Clone or download”的绿色按钮，点开，复制其中自动生成的 https 地址。

现在回到刚才的 Terminal 中（依然在 PycharmProjects 的位置），输入：

```shell
git clone https://github.com/SinanTang/xxxxx.git   # 网址部分替换成你刚刚复制的地址，注意不要把这里的网址范例贴上
```

接下来等待 Terminal 内进度条完成的时间里，你可以去 PycharmProjects 文件夹中看一眼，应该会发现刚刚在 GitHub 新建的项目，已在这里出现了同名“克隆”文件夹——这个文件夹与 GitHub 上的 Repository 是一模一样的，你在本地修改文件夹内内容，**提交后**，就会自动同步到 GitHub 相关 Repo (repo = repository, 这是个极其常用的缩写) 上。

> 创建并本地化一个 GitHub repo 的方法不止这一个，但实践下来，我认为这是最有利于小白上手的方法。



- ##### 用 IDE (PyCharm) 与命令行提交改动到 GitHub

现在用 Spotlight 呼出 PyCharm，出现的应该还是上一次随便玩玩的 project，点击上方任务栏  `File > New Project… > Pure Python` ，在 `Location` 一栏选中刚刚新建的项目名字，选择 Interpreter (即 Python 2.7 或 Python 3.6)，最后点击 `Create`. 

顺利的话，此时窗口左侧已经变成新项目的名称了。按第1节里写过的新建 Python 脚本的方法，现在在此目录下新建一个 `test.py`，在空白脚本里写下这句我们现在已经非常熟悉了的：

```python
print("Hello World")   # Python 3.6
```

在 PyCharm 内敲击 `⌘9`，下方会跳出 `Version Control` 框，在 `Local Changes` 这儿你能一眼看到自己改动／添加／删除了哪些文件。你还可以点第二个 `Log` 标签，猜猜这儿是用来展示什么的？答案一会儿揭晓。



现在回到 Terminal 内，**确认已位于新项目的位置**（需要`cd`到该项目），输入：

```Shell
git status    # 查看目前的 git 状态
```

可能需要输入 GitHub 邮箱与密码。

接着会返回一堆信息，看看刚刚添加的 test.py 是不是也在其中呢？我们现在就来提交它。接着输入：

```Shell
git add -A                  # 把所有改动都添加到“暂存区”
git commit -a -m "initial commit"  # 提交所有暂存的改动，引号内填写此次提交的解释说明
git push origin master       # 将改动推送到服务器
git log                      # 查看提交历史，如果成功会在这里看到
git status                   # 再次查看 git 状态，当所有改动都已推送到云端后，这里会出现“nothing to commit, working tree clean”的信息
```

第三步 `git push`  在第一次提交改动时或许会返回信息需要你单独设置些参数， 但以后一般情况下只需输入 `git push` 即可。



为了加深小白对 **add / commit / push** 提交改动三步曲的理解，我找到了下图——

![](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRy65bygnBWDlQwCz9Eq0PSvfAWgLibHfxHbpeEmSkWp2scKGa03QdfYEHju5cbXPib2oia2jaoMfS7pA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1){:style="margin:0 auto"}

{:.image-caption}

*ref：http://rogerdudler.github.io/git-guide/index.zh.html*



现在回到 PyCharm 内，看下方 `Local Changes` 区是不是变成空白了？再点右边的 `Log` 标签，和刚刚不太一样了吧？是不是出现了一个名为"initial commit"的新“节点”，进度树向上生长了一节？

再回到 GitHub 网站，你的新项目应该已经和本地改动同步了，你可以在这个 Repo 的 commits 页面看到你刚刚在 Terminal 进行的操作。

.

### 第2节 - 作业

- 拓展阅读：Pro Git book by Scott Chacon and Ben Straub (https://git-scm.com/book/en/v2) (推荐阅读英文书，不过页面也有中译本可选)
- 从 GitHub 体验官升级为真正用户：去 GitHub 主页，点击上方 Explore，在 Trending 里翻翻最近的流行项目与牛人。
- 有个 [GitHub 项目](http://resume.github.io/)专门帮工程师一键生成 GitHub 个人简历，你也可以去玩玩 (http://resume.github.io/)。虽然现在还没有东西可以展示，但将来总会有的嘛！




### 第2节 - 小结

这节课我们简单了解了一种主流版本管理工具 Git 与工程师的社交网站 GitHub，创建了第一个 GitHub 项目，并使用 IDE 与命令行第一次提交了代码改动！一切都才刚刚开始。

