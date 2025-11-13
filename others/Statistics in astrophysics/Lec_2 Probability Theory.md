  quiz: 回顾两种三段论

>Laplace

统计是什么

通常统计被解读为: "不可靠" , 充满偏差, 数据处理的各种技巧, 各种随意的测试和规则, 没有统一的工具

希望的统计: 
* 一个唯一的, 透明的, 符合逻辑的框架, 将假设和数据变成一个诚实的结论
* 唯一的, 一致的规则, 带有常规性
* 能用在极端的情况下
* 能大量用在真实世界的问题上

从常识出发搭建理论
正式的逻辑语言: 表示真与假的代数

> Bool 代数
> 二元值: true  , false
> 逻辑操作: 与 $\cdot$ , 或 $+$ , 非  $\overline{}$ 
> 真值表 & Venn 图
> Bool 代数相关恒等式
> 

分析: $A\implies B$ 的 bool 代数等式 $A=AB$ , 从真值表上:
* 一个真命题 implies 所有其他真命题
* 一个假命题 implies 所有命题
* 当 $A$ 真或 $B$ 假时: 强 syllogism
* 当 $A$ 假或 $B$ 真时: nothing

此时仅仅使用 bool 代数已经不能满足需求了, 需要一种能够表达合情合理的推断的语言
这种语言需要满足:
1. 可能性需要用实数表示 (连续, 全序, 满足一些 bool 代数)
2. 定性地与常识相符
3. 自洽(一致性)
	1. 不同的推理给出相同的结果
	2. 能够使用所有已知的信息
	3. 对相同的了解的东西应该有相同的可能性

记号: 
条件性的合情合理的程度: 在知道 $B$ 为真时, $A$ 为真的合情程度为 $$\mathcal{P}(A\mid B)$$在知道 $C$ 和 $D$ 都为真时, $A$ 或 $B$ 为真的合情程度为 $$\mathcal{P}(A+B\mid CD)$$

一些考虑
* 不尝试去定义 $$\mathcal{P}(A\mid BC)$$ 若 $B,C$ 之间是矛盾的
* 单调性, 已知 $I$ 时, 若 $A$ 比 $B$ 更合情 $$\mathcal{P}(A\mid I)> \mathcal{P}(B\mid I)$$
* 连续性: 若 $\mathcal{P}(A\mid I)$ 变化了一点点

逻辑积
表达 $\mathcal{P}(AB\mid I)$ , 需要下面的项 $$\mathcal{P}(A\mid I)\quad \mathcal{P}(B\mid I)\quad \mathcal{P}(A\mid BI)\quad \mathcal{P}(B\mid AI)$$

>为什么不出现 $\mathcal{P}(A\mid I)$ 之类的项?
>这和一致性矛盾, 这项忽略了 $I$ 的信息

只有一种做法不违背前面的要求
$$\mathcal{P}(AB\mid I)=F[\mathcal{P}(A\mid I),\mathcal{P}(B\mid AI)]=F[\mathcal{P}(B\mid I),\mathcal{P}(A\mid BI)]$$
>为什么不出现 $$G[\mathcal{P}(A\mid I),\mathcal{P}(B\mid I)]$$这忽略了 $A$ 和 $B$ 的关系

>为什么不出现 $$G[\mathcal{P}(B\mid AI),\mathcal{P}(A\mid BI)]$$这不能给出任何信息, $A$ 和 $B$ 都是未知的

>为什么不加入更多项?
>带来的信息是冗余的

更多记号 $$x= \mathcal{P}(A\mid I)\quad y = \mathcal{P}(B\mid AI)\quad z=\mathcal{P}(C\mid ABI)$$ 而 $$\mathcal{P}(AB\mid I)=F(x,y)$$有两种方式$$\mathcal{P}(ABC\mid I)=F[\mathcal{P}(AB\mid I),\mathcal{P}(C\mid ABI)]=F[F(x,y),z]$$和$$\mathcal{P}(ABC\mid I)=F[\mathcal{P}(A\mid I),\mathcal{P}(BC\mid AI)]=F[x,F(y,z)]$$即$$F[F(x,y),z]=F[x,F(y,z)]$$若加入单调性的要求, 可以证明只有一种解(jayne's book)$$w[F(x,y)]=w(x)w(y)$$定义$$q(A\mid I)=w[\mathcal{P}(A\mid I)]$$从而有 $$q(AB\mid I)=q(B\mid AI)q(A\mid I)=q(A\mid BI)q(B\mid I)$$对确定的情况: 
* 若 $A$ 是确定的 ($I\implies A$) , 有  $$q(AB\mid I)=q(B\mid I)\quad q(A\mid BI)=q(A\mid I)$$从而有 $$q(B\mid I)=q(A\mid I)q(B\mid I)$$即$$\implies \quad q(A\mid I)=1$$

对不可能的情况
* 若 $A$ 是假的 ($I\implies \overline{A}$) 可以得到 $$q(A\mid I)=0$$

Negation mapping
考虑补 $$q(\overline{A}\mid I)=S[q(A\mid I)]$$有边界条件 $$S(0)=1\quad S(1)=0$$对任意命题 $A,B$ 有 $$q(AB\mid I)=q(A\mid I)q(B\mid AI)\quad q(A\overline{B}\mid I)=q(A\mid I)q(\overline{B}\mid AI)$$可以得到 $$q(AB\mid I)=q(A\mid I)S[q(\overline{B}\mid AI)]=q(A\mid I)S[\frac{q(A\overline{B}\mid I)}{q(A\mid I)}]$$利用交换律可以得到 $$q(A\mid I)S[\frac{q(A\overline{B}\mid I)}{q(A\mid I)}=q(B\mid I)S[\frac{q(B\overline{A}\mid I)}{q(B\mid I)}$$考虑一些情况
* $\overline{B}\implies A$ , 有 $$A\overline{B}=\overline{B}\quad B\overline{A}=\overline{A}$$
* 可以得到 $$xS[\frac{S(y)}{x}]=yS[\frac{S(x)}{y}]$$
* 在 $y=1$ 时, $S[S(x)]=x$ , 此时有唯一解 $$S(x)=(1-x^m)^{1/m} \quad $$
容易验证上面的解对任意 $A,B$ 也成立, 则是充分必要的

从而有加法规则 $$q^m(A\mid I)$$


从而可以定义概率 $$P(x)=q^m(x)\in[0,1]$$满足连续单调增
并且有积规则和加法规则$$P(AB\mid I)=P(A\mid I)P(B\mid AI)=P(B\mid I)P(A\mid BI)$$和$$P(A\mid I)+P(\overline{A}\mid I)=1$$
再看特例:
若 $I=(A\implies B)$ , 则 $$P(AB\mid I)=P(A\mid I)\quad P(A\overline{B}\mid I)=0$$加入乘法规则 $$P(B\mid AI)=\frac{P(AB\mid I)}{P(A\mid I)}=1\quad P(A\mid \overline{B}I)=\frac{P(A\overline{B}\mid I)}{P(\overline{B}\mid I)}=0$$此即强 syllogism

同样, 有 $P(B\mid I)\leq 1$ , 代回乘法规则
$$\begin{array}{l}P(A\mid BI)\geq P(A\mid I)

 &\implies P(\overline{A}\mid BI)\leq P(\overline{A}\mid I)\\ &\implies P(B\mid \overline{A}I)\leq P(B\mid I)\end{array}$$
此即弱 syllogism

>若 $P(B\mid AI)>P(B\mid I)$ , 有 $P(A\mid BI)>P(A\mid I)$ , 可以解读为新的 syllogism (更弱版本):
若 $A$ 是真的, 则 $B$ 更有可能
$B$ 是真的
$\implies$ $A$ 更有可能

定量的应用:

推广加法规则: 
$$P(A+B\mid I)=1-P(\overline{A}\cdot\overline{B}\mid I)=1-P(\overline{A}\mid I)P(\overline{B}\mid \overline{A}I)=1-=\dots=P(A\mid I)+P(B\mid I)-P(AB\mid I)$$可以继续对多个命题继续推广

假设各个命题是互斥的, 则加法规则会变简单

若这些命题是完备的, 则有


给概率赋值

....


>无差别原理
>考虑完备的, 无交的事件 $\{A_{i}\}$ , 有 $$\sum_{i=1}^nP(A_{i}\mid I)=1$$
>前提 $I$ 为无法区别任意一个命题, 则可以交换任意命题的指标, 这给出 $$P(A_{i}\mid I)=\frac{1}{n}$$

统计推断:
* 目标: 给定背景信息 $I$ , 在样本集 $D$ 中 , 更新假说 $H$ , $P(H\mid DI)$
* Bayes' theorem $$P(H\mid ID)=\frac{P(D\mid HI)P(H\mid I)}{P(D\mid I)}$$
	* $P(H\mid DI)$ : 后验概率, 在样本 $D$ 中 $H$
	* $P(D\mid HI)$ : 似然, 在假说 $H$ 下和 $D$ 的相容性
	* $P(H\mid I)$ : 先验概率: 在获得样本 $D$ 前, $H$ 的可能性
	* $P(D\mid I)$ : 证据

Normalization
对任意命题 $B$ : 




推广: 对互斥和完备的所有假说模型 $\{H_{i}\}_{i=1}^N$ , 有 $$P(D\mid I)=\sum_{i=1}^NP(D\mid H_{i}I)P(H_{i}\mid I)$$

>例子: Monty Hall Game
.....


边缘化 marginalization 