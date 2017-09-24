---
title: 用 Jekyll 在 GitHub 上搭建你的个人网站
date: 23-09-2017 23:31:06
categories: 
  - A Developer Guide for Newbies - Starting with Python 
tags: 
  - developer
  - jekyll
  - github pages
  - newbie
  - markdown
---



这是我面向小白写的 Python 编程教程的⎡加餐⎦。

.

### 引子

前段时间折腾几次后终于把我的个人博客站点搭建起来啦：SinanTang.github.io 

因为有朋友来问，我就打算写个如何利用 Jekyll 在 GitHub 上搭建静态个人站点的小白教程。

.

先简单科普一下，[Jekyll](https://jekyllrb.com/) 是个简单的**博客形态的静态站点生产工具**，可以通过 Jekyll 来生成可发布的网站／博客。网站需要服务器来对外发布，可以选择在 [GitHub Pages](https://pages.github.com/) 上运行，利用 GitHub 服务器不仅方便追踪历史版本、迭代更新，而且完全**免费**。

> 提供与 Jekyll 类似服务的工具不止一个。我最开始尝试过 Hexo，但中途遇到一些麻烦没解决掉……无意间看到阳志平这篇[《理想的写作环境：Git+Github+Markdown+Jekyll》](http://www.yangzhiping.com/tech/writing-space.html)，就转而投向 Jekyll 的怀抱了。
>
> 这也从侧面说明，对小白来说，一开始选择一门编程语言或工具入门时，最好考虑使用人数（即是否主流）这个因素，越主流网上的学习资源就越多，当你遇到问题时就更有可能搜索到解决方法。

.

至于为什么要搭建一个属于自己的个人网站，除了看起来有点炫酷外，对于有意在创作型领域（写作／摄影／绘画／编程等）发展的小伙伴来说，**个人网站就是最好的个人作品集**——

> “**作品会帮助你与第三方沟通**。尤其是一些你在意，但不理解你的人。比如父母/亲友。在外在动机的人看来，作品是最重要的；但在内在动机的人看来，作品是水到渠成的结果。”
>
> ——阳志平

.

### 开始搭建个人网站

好啦，下面进入正题。

#### 新建一个 GitHub 项目

首先你要有个 GitHub 帐号，同时最好已经熟悉了[《用 Git 记录成长轨迹》](https://sinantang.github.io/a%20developer%20guide%20for%20newbies%20-%20starting%20with%20python/2017/09/04/use-git-to-track-your-growth/)这一节中的常见 Git 操作。

然后新建一个 GitHub repository（具体操作见第2节），将新 repo 命名为 `USER-NAME.github.io`。注意，这个名称的格式是固定的，有一点儿不同就没法用 GitHub 服务器来帮忙发布。`USER-NAME` 是你的用户名，即点击 GitHub 页面右上角个人头像时出现的名字（`Signed in as USER-NAME`）。

.

#### 本地初始化一个  Jekyll 站点

##### 安装 Git 和 Ruby

呼出 Terminal，确认本地已经安装好 Git 和 Ruby:

```shell
# 若未安装 git，请回到第2节进行安装操作
git --version
# 若未安装 ruby 或版本低于 2.1.0, 可以跟着下面的操作来安装 ruby
ruby --version
```

选做：安装 Ruby 2.3.1

```shell
\curl -sSL https://get.rvm.io | bash -s stable
# rvm 是 Ruby 的版本管理工具
rvm install 2.3.1
rvm use 2.3.1
# Terminal自己忙完后，再确认一下是否成功安装 ruby, rvm, gem
ruby --version
rvm --version
gem --version
```

.

##### 安装 bundler

还是在 Terminal 中输入下面指令：

```shell
gem install jekyll bundler
```

.

##### 创建你的本地 Jekyll 站点

继续输入：

```shell
# 把 jekyll 站点建在 Public directory 下
cd ~/Public
jekyll new USER-NAME.github.io
cd USER-NAME.github.io
bundle exec jekyll serve  #1
```

以上几步都完成后，点击 `⌘T` 开一个新 Terminal tab，输入：

```shell
open http://localhost:4000  #2
```

或者也可以直接打开浏览器，输入 `localhost:4000`。

此时你就可以在浏览器上看到网站的初始模样啦。以后每次你做了修改后，想要预览改动时，就可以在  Terminal 中依次输入 #1 #2 这两步（注意要先 `cd` 到目标路径哦）。

![](http://upload-images.jianshu.io/upload_images/4719384-6afd9acaa5e89ea1?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

退出预览模式，在 Terminal 内键盘点击 `⌤C`。

.

##### 初始化本地站点并发布

在 `USER-NAME.github.io` 目录下，在 Terminal 中继续输入：

```Shell
git init
git status
git add . 
git commit -m "initial commit"
# 从最开始创建的新GitHub repo页面，复制项目网址，粘贴到下面网址部分
git remote add origin https://github.com/USER-NAME/USER-NAME.github.io.git 
git push -u origin master
```

在输入以上最后一条指令后，也许会出现 `fatal: unable to access 'https://github.com/USER-NAME/USER-NAME.github.io.git': The requested URL returned error: 403` 这样的错误信息，这是权限的问题，可以尝试输入以下指令来解决：

```shell
git remote set-url origin https://USER-NAME@github.com/USER-NAME/USER-NAME.github.io.git
# 检查刚刚输入的那串url是否在这儿出现了
git remote -v
# 重新 push 一次，此时需要输入你的GitHub账号密码
git push -u origin master
# 确认刚刚提交的改动是否出现在日志里
git log
```

.

##### 阶段性成果

现在你可以去浏览器里输入 `USER-NAME.github.io` 查看自己的刚刚发布的网站啦！此时别人也可以通过你的个性化域名来访问你的个人网站了。

.

.

### 接下来……

经过以上几步后，我们已经有了一个个人网站的雏形，接下来还要换名字、换主题、添加目录等页面……不过最重要的是，应该学会发布内容到网站。

其实发布内容（如文章）到个人网站的操作与之前第2节《用 Git 记录成长轨迹》中重点讲解的 `add-commit-push` **提交改动三部曲**差不多，只不过需要用 Markdown 格式来书写文章。

> Markdown 编辑器强烈推荐简洁轻便的 [Typora](https://typora.io/) 

.

换主题、添加更多页面等琐碎操作教程就不在这篇详述了。有搞不定的地方欢迎读者留言，我可能会根据反馈写新的《搭建个人网站 - 进阶篇》！