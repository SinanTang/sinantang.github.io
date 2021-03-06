---
title: 自然语言处理的前世今生与未来展望
date: 12-07-2020
categories:
- Natural Language Processing
tags:
- NLP
---

##### ——基于 Kathleen McKeown 教授的 ACL2020 Keynote 演讲

.

自然语言处理（Natural Language Processing）或计算机语言学（Computational Linguistics）虽仍算是年轻学科，但也已发展了几十年。这篇短文总结了这个学科的发展路径和研究者对其未来的预测展望。



#### 1980s - Interdisciplinary focus 聚焦跨学科

八十年代时，认知学科（语言学、哲学、心理学）在早期自然语言处理中占有中心地位。这些认知学科的理论在引领自然语言处理的发展。当时的主流研究方法主要是定性分析例子，比如通过 minimal pairs 来探究自然语言的句法语义形成规律。

乘上当时计算机的发展（摩尔定律），早期机器学习模型的雏型开始出现。

ACL会议当时只有200人参加。



#### 1990s - Moving to large scale data analysis 开启大量数据分析的序幕

语料库出现了。人们开始收集标注自然语料，建立多种语料库，并利于语料库来进行语言现象分析。此时语言数据的收集过程非常严谨细致，如何科学地清洗标注语料是风靡一时的热门研究。这种严谨的数据处理态度与后来真正大数据时代几乎“来者不拒”的数据收集手段形成鲜明对比。

举个例子，有了语料库，语言学家才有了定量分析词语搭配频率的途径。想知道一个动词最常跟哪个介词搭配，不再需要查由字典学家编写的字典，也不需要去做大规模语言学人类学田野调查，只需要在语料库里进行简单的搜索操作即可。



#### 1990-2000 Transformation: Statistical NLP 统计自然语言处理

统计学以统计学指标（statistical metrics，e.g. mutual information）开始带领了一场自然语言处理领域的变革。这个年代见证了自然语言处理的重心从认知理论和定性分析到大数据与机器学习的转移。

更成熟的传统机器学习算法也在此时出现，其中包括一直到现在还很常用的SVM算法。

此时NLP从业者也开始引入检验指标来评估不同模型的效能。

因为以上这些系统性变革，符号模型与统计模型之间的关系日趋紧张、对立。对此流传最广的可能是Fred Jeline在同时代的名言「Every time I fire a linguist, the performance of the speech recognizer goes up」了。

语言学与机器学习之间的紧张关系可以说是一直延续至今。



#### 2000 至今 - Deep Learning 深度学习的时代

这回是深度学习技术引领了自然语言处理领域的迄今为止影响最大的突破。

神经网络和深度学习模型的出现纷纷打破各项NLP任务的最好成绩——注意，并不是一项两项任务的最佳成绩被超越，而是几乎所有NLP任务的最佳成绩现在都被深度学习模型占据。

由于这些模型实在太好用了，加之计算机算力的大幅进步和云计算平台的出现，机器学习的浪潮愈加热烈，再次炒热了人工智能的概念。现在ACL会议每年收到的论文中，机器学习主题的数量总遥遥领先。



#### 未来展望

关于目前深度学习的局限性，McKeown 教授此次采访的NLP专家的观点如下：

* 无法做到对语言生成应用的高阶控制；
* 过拟合：文本中不真实的关联被深度学习模型捕捉；
* 无法学习因果性和推论；
* 无法解释模型输出结果，无法修正结果；
* 没有更新知识图谱的简单方法;
* ……

那有什么新研究方法也许能够解决这些问题吗？

* 将符号表征（symbolic representations）融合到深度学习算法；



McKeown 教授对业内研究者的期望则已总结在下面这页演讲幻灯片里了：

![keynote finalwords](../../../../../assets/images/acl-keynote.png){:style="margin:0 auto"}
