---
title: 能与你聊天的机器人管家 | 对话系统扫盲
date: 01-12-2017 23:31:06
categories: 
- Natural Language Processing
tags: 
- Dialogue System
---



![题图：苹果官网](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRywiaasfgibicHFECmT15QSn6uBpgsibeAib6peFZTVXEtiayahzS3X7LicJ59BzdBGB73egicy4vI3FbB3gg/0?wx_fmt=png){:style="margin:0 auto"}

在近几年人工智能高歌猛进的大趋势下，机器与人的关系日趋复杂微妙。

一方面，机器在**专能**上必然或已经逐步超过人类，比如今年名声大噪的 AlphaGo，还有从工业革命起就已越来越发达的取代了无数纺织女工的工业机器；另一方面，走上另一条岔路的机器人在往越来越“像人”的方向发展——要不为什么会叫“机器**人**”呢。不难想象到，越来越像人的终极目标之一就是**使机器人具备与普通人用人类语言自如交流合作的能力**。

.

这类机器人的雏形就是像现阶段 Siri 这样的智能个人助理。说“雏形”是因为 Siri 还远远达不到能与普通人正常交流的水平。在普通用户中流传最广的 **Siri 讲段子**反而是最没技术含量的功能。那些段子仅仅是提前存储好的问题和答案罢了，与人工智能啊人机对话啊扯不上一丁点关系，主要在为营销宣传做贡献。

![比如，我用「Will you marry me?」反复提问我的 Siri，只能收到这几个随机丢给我的有限固定答复](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRywiaasfgibicHFECmT15QSn6uzj8nSTTrhxkaicl0ZQM2QoicdZnM7TLia1qicOXldawNVJQKZichAhQhsug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1){:style="margin:0 auto"}



虽然 Siri 2011年才刚问世，但智能个人助理背后的核心科技——**自然语言处理（Natural Language Processing）**——却相当"古老"。最早试图进行机器翻译（自然语言处理的一个细分领域）的尝试出现在上世纪 30 年代。在自然语言处理中，一系列应用于智能个人助理的技术组合即为**对话系统（Dialogue System）**。

.

### 建立对话系统究竟难在哪儿

为什么自然语言处理的研究已经如火如荼进行了八十年，但 Siri 还是现在这个鸟样呢？

.

因为理解、处理人类语言对于机器来说实在太难。

首先，Siri 要学会**语音识别**（Speech Recognition）。当你家中某处呼唤“Hey Siri”时，它能迅速忽略背景杂音并拾起你的语音信号，但不会在你跟人打招呼“Hi Sarah”时误以为在跟它对话。

开启后，Siri 接着就要进行下一步，**自然语言理解**（Natural Language Understanding），它得搞清楚你在说什么。“我小学时的美国总统有谁？”——“我”还是“你”？“小学”？“美国总统”？互联网上不存在这个问题的现成答案，Siri 必须拆解出这个问题背后的假设（小学生的通常年龄段，“我”在那个年龄段的年份）和需要的常识性知识（美国总统有谁，分别在哪几年任职）。

接着还需要**识别用户意图**（Intent Recognition）。人类语言可以有无数种形式来表达同一意思，Siri 需要在模糊、多义、多变的人类语言里准确鉴别出真实意图。“我今晚出门需要带伞吗？”——这其实是在问天气。人可以毫不费劲地迅速理解这句话，但对于机器来说，这就绕了不止两个弯。

.

当以上过程出现在人机**对话**中时，难度又翻了几番。

有时 Siri 需要**推断谈话目的**（Goal Inference），主人为什么要跟我讲这个？我若是说“我想看电影”，那 Siri 究竟应该网页搜索最近热门电影，还是定位附近电影院，还是应该问我想看什么类别的电影呢？

有对话就出现了**语境**，一些人类眼中无比自然的信息到了 Siri 这儿，就需要额外建模分析 (Context Modeling)。比如，下面这一串问题，

> “奥巴马是谁？”
>
> “他的妻子是谁？”
>
> “她生日在什么时候？”

这里只提到过一回“奥巴马”，从未提及“米歇尔”，但 Siri 需要推断出第二句话中的“他”指奥巴马，第三句的“她”则指米歇尔。

有时，用户并不会给出一个明确指令或意图，Siri 就得自己琢磨此时该**生成何种反馈**（Response Generation）。当听到“Siri，我很无聊”时，该做出什么反应才合适？很多人类自己也拿不准该如何回应的话题，机器有可能表现得更好吗？

.

### 对话系统的基本架构

现在市场中的智能个人助理应用主要有这几个玩家：

![](http://upload-images.jianshu.io/upload_images/4719384-f5d5d5e924526997){:style="margin:0 auto"}

虽然名称图标长短处各有不同，但它们背后的基本架构大同小异。

当开启任务时，先要识别人类语音，有时还需要核实个人音色来解密。输入的语音信号转化成文字，再理解这个文字内容。接下来到了对话管理环节，需要决定该做出什么回应，调用相关的任务。接着把这个回应转化为人类语言，最后把内容合成为语音，输出给用户。

![](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRywiaasfgibicHFECmT15QSn6uOu3mU1SHevOwNXFFXqsAB0rUSSvE3D04545vagaKDLNckth0bHYDicg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1){:style="margin:0 auto"}

观察一下，这个架构设计其实模拟了人类社交谈话时的过程分解。其中，**对话管理**（Dialogue Manager）就扮演了 **Siri 大脑**的角色。

![](http://upload-images.jianshu.io/upload_images/4719384-97ca2bda6bb86fec){:style="margin:0 auto"}

.

### 对话管理

作为对话系统的大脑，对话管理模块既负责处理输入信息，还负责决定接下来该采取什么行动，并输出信息给任务管理器与语言生成/语音合成模块。

对话管理存在多种架构，比如：（中文译名仅供参考）

> 有限状态（Finite State）
>
> 基于框架 (Frame-based)
>
> 信息状态 (Information State, Markov Decision Process)
>
> 经典 AI 设计 (Classic AI Planning)
>
> 分布式/神经网络 (Distributional / neural network)

.

这里只简单介绍前两种常见对话管理实现方式。

.

#### 有限状态对话管理

想象当你网上订机票时，需要做出哪些决定呢？

大致是以下几个关键信息吧：

> 出发城市；
>
> 目的地；
>
> 何时起飞/到达；
>
> 单程 or 往返。

当使用**有限状态对话管理**系统来预订机票时，系统与你之间的对话简化之后是这样的：

![蓝框内代表系统提问，Yes/No 为用户答复](https://mmbiz.qpic.cn/mmbiz_png/ETsNbcnZdRywiaasfgibicHFECmT15QSn6uFDKN4FCgVqmUzW6dhVocHKpQoXozjqwVH0mSicPB1JibjjIBmK4eEUnA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1){:style="margin:0 auto"}



这个系统确实非常清晰有逻辑，开发难度也不高，一切尽在电脑的掌控中。

但其缺陷也很明显。因为**对话主动权**（dialogue initiative）完全由系统控制，系统只接受特定的答复，非常机械生硬。只能适应于极其有限且简单的专门应用。这个例子也许会唤起你对带声音 ATM 的记忆；除此之外，创建用户名与密码的场景也应用了有限状态机。

.

#### 基于框架的对话管理

在人与人之间的对话中，对话主动权会在说话方中交替传递。除了特殊关系和情景，并不会有一方一直提问、主导对话走向，还不允许对方给出不同回应或转移话题。为了让人机对话更自然灵活，就需要双方均有使用对话主动权的机会（mixed initiative）。实现共享对话主动权的最简对话管理模型，即为**基于框架的对话管理**。

此处的框架可以理解为，在某个特定领域下涉及到的信息都可以在某个框架里确定。

看个例子，还是刚才预订机票的情景，可以先设计好这样一个框架：

> <u>Flight Frame</u>:
>
> ​	ORIGIN:
>
> ​		CITY:
>
> ​		DATE:
>
> ​		TIME:
>
> ​	DESTINATION:
>
> ​		CITY:
>
> ​	AIRLINE:

在所有空格都被填满前，用户可以直接提供信息，“我想订下个月 5 号从伦敦飞纽约的单程机票”；对话系统也可以提问，“早上的航班可以吗？”

当这个框架被必要信息填满后，就可以查询相关数据库，验证无误后就能下单出票。

这个对话管理系统的背后理论涉及**框架语义学**（frame semantics）、**隐马尔可夫模型**（HMM）与**机器学习**，在这儿就不展开讲了，有兴趣的读者可自行查阅相关资料。

基于框架的对话管理系统已经非常“古老”，最早在 1977 年就有人提出。不仅古老还十分长寿；直到今天，大多数现代商业对话机器人（比如智能客服）都**依然在使用这个对话管理系统**。

.

### 小结

本文非常简单地扫盲了 Siri 类智能个人助理背后的对话系统原理。

限于篇幅与作者知识水平，讲了讲一部分机器人必然会越来越像人、最终达到能与人交流合作的未来趋势，从语言学和自然语言处理角度讲了讲机器要理解、处理人类语言需要克服的几大困难，最后写了写对话系统的基本架构，以及对话系统的大脑——对话管理。

对话系统科技以及其中各个小模块目前大都处于快速发展期，仍有很大发展潜能，我认为这是非常适合自然语言处理或人工智能从业者学习进入的领域。欢迎从业者们留言交流 :）

.

既然有一部分专能机器人的工作效率早已超过人类，还有一部分机器人在拼命向人类靠齐。那，未来会是什么样呢？

也许会是这样吧：

![图片来自《纽约客》杂志封面](http://upload-images.jianshu.io/upload_images/4719384-a1d0fbe575ec4f97?imageMogr2/auto-orient/strip%7CimageView2/2/w/700){:style="margin:0 auto"}

（但我不觉得这会在自己有生之年发生 :P

.

**References:**

*Speech and Language Processing. Daniel Jurafsky & James H. Martin.*

*Keynote: Conversational AI in Amazon Alexa - Ashwin Ram | Udacity Intersect 2017.* 

*CS224S Spoken Language Processing, Lecture 10.*

