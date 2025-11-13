开这门课的目的:
* 原理: 数据是怎么转化成知识的
* 做假设: 对你做了什么和对什么不知道诚实
* 处理天文数据: 通常是不完备且充满噪声的
* 解决问题的技能: 对日常生活和科研学习
* 批判性思维和交流: 可读的图像, 清晰的解释, 结论

技能和能力:
* 将问题转换为统计模型
* 量化和理解不确定性
* 选择合适的方法拟合数据和目标
* 写代码和分析数据和产生清晰的可视化
* 得到可信的结论

教学方法:
* 问题驱动: 从一个现实世界的问题出发
* 可信的推理: 运用常识和清晰的逻辑
* Research-connected: 运用实际的统计研究方法
* iterative 学习: 思考, 分析和 refine
* 动手练习

Grading:
* 课堂参与 10%
* 每周练习 40%
* 大作业 50% 
* bonus(英文写作) 5%

参考书: 见ppt

Lec1: Introduction

***The true logic of this world is the calculus of probability***

为什么要在天文上使用统计?

Why statistics?

从我们认知的世界中获得一些数据, 我们可以建立一套理论, 但这不够, 建立一套理论之后可以来做一些预言
这是科学研究的基本方法: 从理论到预言的过程中使用的是逻辑的推导, 这里面几乎没有不确定性, 但从获得的数据中建立理论的过程更多是一种归纳的逻辑, 这不是完全可靠的.

演绎的逻辑: 最基础的逻辑: (Strong) syllogism (三段论), 例如 $$A\implies B$$若 $A$ 是真的, 则 $B$ 也是真的 & 若 $B$ 是假的, 则 $A$ 也是假的
这是完全的严密逻辑

>例子: 所有人都会死
>苏格拉底是人 $\implies$ 苏格拉底会死

给出一个起因, 可以在严密的逻辑下推导出不同的结论

合情合理的推理: 弱 syllogism , 即 $$A\implies B$$若 $B$ 是真的, 则 $A$ 是真的便更可信 & etc.

>例子: 下完雨地上会湿
>地面是湿的 $\implies$ 很有可能下过雨

这个推导不是严密的, 但是仍是有用的

从一个现象, 可以得出不同原因的可能性

小例子: 见ppt
我们不能每时都能辨别一个三段论是强的还是弱的

逻辑推导和合情推理最本质的区别在哪?  

*completeness of information*

为什么在天文上使用统计: 因为我们获得的信息不完备

>**两种推理**
>
>Deductive: 完备
>	关注: 有效性
>	典型的问题: What follows if this theory is true?
>	
>Plausible: 不完备的信息
>	关注: 证据的强度
>	典型问题: Which theory best explains these data?

定量化合情推理: Statistics
从不完备的信息中推断出量化的结论

对于天文数据, 是否完备? 
典型的天文数据: 见ppt
特征:
* 噪声: 通常是仪器的限制
* 有限的样本量: 不能重启宇宙, 有限的观测时间
* 不完备性: detection limits and masked regions
* contaminations: foregrounds and artifacts

统计能提供什么
* 合情推理: 量化不确定性
* 数据驱动的观点: 从噪声中提取信息
* 模型的有效性: 用观测测试假设
* 证据选择: clarifying trade-offs

>[!Summary] 
>为什么天文需要统计?
>	1. 12

***123***


什么是概率  -- "Formal language of plausibility"

概率的历史

>Jakob Bernoulli (1713)
> "Principle of Insufficient Reason" : 如果有 $N$ 个事件且没有任何信息, 则每个事件的概率都是 $1/N$

>Thomas Bayes (1763)
>解决了用新的信息更新概率的问题: Bayes' Theorem

>Carl Friedrich Gauss (1795)
>建立最小二乘法, 推导误差的 Gauss 分布, 并公式化表达了中心极限定理

>Pierre-Simon Laplace (1820)
>重新发现了 Bayes' Theorem 并应用于 Celestial Mechanics 和统计学

>The Frequentists (1850's)
>拒绝了 Laplace 的成果并尝试去掉概率定义中的主观性, 用频率的角度解释

>The Bayesians (1920's)
>回到 Bayes 和 Laplace 的更直觉的想法
>很大归功于电子计算机的发展

Frequentist v.s. Bayesian

Laplace 的工作: 推测土星的质量 -- 土星的质量为什么有概率?这里的概率代表是什么?
* 对 Bayesians 来说, 概率代表了一种信任程度 degree-of-belief : 对土星质量的把握程度
* 对 Frequentists 来说: 概率是一种对发生没有主观性的事件的长期观测的频率 long-run relative frequency, 概率应该被看作一种处理随机事件的工具

对于仅用较少的数据推断土星质量的问题, 如何在频率学派的观点下表述?
认为观测数据会有随机的噪声, 实际上前面概率应该解释为带有这种随机噪声的东西

这两种观点的结果是相同的, 但频率学派处理这个问题的复杂性会远远加大, 需要处理不同样本不同的噪声
但对于频率学派, 如何预测不会再次发生的事件? 

>随机性意味着什么

概率反映的是对一个事件了解的程度, 了解的越少, 就越随机 -- Bayes 学派的解读

>例子: 加减乘除
>如果让加减乘除给没有学过的人去做, 就会给出不同的结果, 形成一个分布, 这个结果就表现得像一个随机数的分布

对 Bayes 学派来说, 概率代表了 degree-of-belief 
不确定性来源于不完备的信息和噪声, 基于新的信息可以更新我们的知识

***We cannot 'prove' a theory true*** , 因为它总有可能在明天的某个测试中失效

>[!Summary]
>* Bayesian : 由先验知识给出的 degree-of-belief 
>* Fre : 在重复下给出的 lo
>* 随机性: 通常是我们无知的, 不可预测的

统计和天文的关系 "An art as well as a science"

统计最开始由行星力学建立
现代天文学与统计学: 见ppt
现状与挑战

例子: 精确宇宙学

>[!Summary]
>统计与天文的联系


