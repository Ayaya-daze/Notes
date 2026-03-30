# Discrete - time Markov chain
考虑事件列 $X_1, \cdots,X_n,X_{n+1}$ 的联合分布, 可以做分解

$$
P(X_1,\cdots,X_{n+1})=P(X_1,\cdots,X_n)P(X_{n+1}\mid X_1,\cdots,X_n)=\cdots
$$

Markov chain 就是对上面的分解做一些假设, 我们称 $i<n$ 的事件 $X_i$ 叫过去, $i> n$ 的事件 $X_i$ 为未来, 事件 $X_n$ 为现在
Markov chain 的假设即: 未来的状态只取决于现在的状态 $X_n$ , 而与过去的状态无关

#### Conditional independence
Markov chain 的假设为

$$
P(X_{n+1}\mid X_1,\cdots,X_n)=P(X_{n+1}\mid X_n)
$$

记为

$$
\left(X_1,\cdots,X_{n-1}\right) -X_n-X_{n+1}
$$

同样有等价刻画

$$
P( X_{n+1},X_1,\cdots,X_{n-1}\mid X_n)=P(X_{n+1}\mid X_n)P(X_1,\cdots,X_{n-1}\mid X_n)
$$

#### 定义 DTMC
事件列 $(X_n)$ 是一个 Markov chain 若满足

$$
P(X_{n+1}\mid X_n,\cdots,X_0)=P(X_{n+1}\mid X_n)\quad \forall n
$$

称 $P(X_{n+1}=j\mid X_n=i)=p_n(i,j)$ 为转移概率 Transition probability
同时, 若 $p_n(i,j)=p(i,j)$ , 则称这个 Markov chain 为时齐的 time - homogeneity / temporally

> [!examples] coupon collector
> $X_n:\text{number of distinct types at time n ( N total)}$ 假设每种抽到的概率相同
>
> $$
P(X_{n+1}=k+1\mid X_n =k)=1-\frac{k}{N}\quad P(X_{n+1}=k\mid X_n=k)=\frac{k}{N}
> $$
>
> 对于其他状态, 概率皆为 0 即: $P(X_{n+1}=j\mid X_n=k)=0\quad j\neq k,k+1$    
>
> ```mermaid
> flowchart LR
> D["..."] --> A["k-1"]
> A -. "1-(k-1)/N" .-> B["k"]
> B -. "1-k/N" .-> C["k+1"]
> C --> E["..."]
>
> %% 节点颜色
> style A fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px
> style B fill:#E8F5E9,stroke:#43A047,stroke-width:2px
> style C fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px
> style D fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px
> style E fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px
>
> ```
>

转移概率的信息可以被矩阵储存, 称为转移概率矩阵
可以定义首达时间

$$
\tau =\inf\{n:X_n=N\}:\Omega\to \mathbb{N}\cup\{+\infty\}
$$

> 对于现实中的抽卡, 具有非均匀的概率, 如何建立 Markov 模型
> 实际上是给状态一个好的定义, 一种定义方式是在状态中显式区分不同概率卡的种类 $[X_{n,k}]_k$ 表为状态向量
> 最极端的划分即为: 将状态定义已获得的卡 (区分每个种类)

> [!examples] Random walk / gambler‘s ruin
> $X_n:\text{wealth of time n}$ 转移概率为
>
> $$
P(X_{n+1}=k+1\mid X_0=i,\cdots ,X_{n}=k)=p\quad P(X_{n+1}=k-1\mid X_0=i,\cdots,X_n=k)=1-p
> $$
>
> 同时有终止条件
>
> $$
\text{Quit if} \,X_n=0 \,\text{or}\, X_n=N
> $$
>
> 称之为吸收态

#### Define sample path
给定  $\omega\in \Omega$ ,  $(n,X_n(\omega))$ 可以形成一条 path , 叫 sample path
所以也可以认为一个随机过程是指这些所有 sample path

传递矩阵有等价刻画: 

$$
\text{Transition matrix}\Leftrightarrow \text{(row) stochastic matrix}\begin{cases}0\leq p(i,j)\leq 1\\ \sum_{j}p(i,j)=1\quad \forall i\end{cases}
$$

> 若 $X_{n+1}$ 不仅依赖于 $X_n$ , 还依赖于 $X_{n-1}$ 是否可以等价地用 Markov chain 刻画
> 同样做法是定义一个好的状态, 可以将两个状态定义为一个新状态 $(X_n,X_{n-1})=S_n$ 则
>
> $$
P(S_{n+1}|S_{n},\cdots,S_0)=P(X_{n+1},X_{n}\mid X_n,X_{n-1},\cdots,X_0)=P(X_{n+1},X_n\mid X_n,X_{n-1})=P(S_{n+1}\mid S_{n})
> $$
>
> 这种做法叫 lifting state space

## Multistep transition
现在不止考虑一步转移, 考虑多步转移 $X_0=i$ , 先看两步

$$
\begin{align}P(X_1=j,X_2=k\mid X_0=i)&=P(X_2=k\mid X_1=j,X_0=i)P(X_1=j\mid X_0=i)\\&=p(i,j)p(j,k) \end{align}
$$

若 $P(X_0=i)=q(i)$ 则 joint pmf

$$
P(X_0=i,X_1=j,X_2=k)=q(i)p(i,j)p(j,k)
$$

同样两步转移

$$
P(X_2=k\mid X_0=i)=\sum_{j}P(X_2=k,X_1=j\mid X_0=i)=\sum_j p(i,j)p(j,k)=p^2(i,k)
$$

对于一般情况, 有

#### Champan - Kolmogorov equation

$$
\begin{align}P(X_{n+m}=j\mid X_0=i)&=\sum_{k}P(X_m=k,X_{n+m}=j\mid X_0=i)\\&=\sum_{k}P(X_m=k\mid X_0=i)P(X_{m+n}=j\mid X_m=k,X_0=i)\\&=\sum_{k}P(X_m=k\mid X_0=i)P(X_{m+n}=j\mid X_m=k)\end{align}
$$

#### Theorem 
对时齐 Markov chain, 有

$$
P(X_{n+m}=j\mid X_m=i)=(p^n)(i,j)
$$

考察 marginal distribution of $X_n$ 

$$
P(X_n=i)=\sum_{k}P(X_n=i\mid X_0=k)P(X_0=k)=\sum_k q(k)p^n(k,i)=(\mathbf{q}\mathbf{P}^n)_i
$$

即 $q_n=q\cdot p^n=q_{n-1}p$ 

对于非时齐 time - inhomogeneous 的过程, 我们也有
定义 $H_{st}(i,j)\coloneqq P(X_t=j\mid X_s=i)$ , 那么 C - K equation 有形式

$$
r<s<t\quad H_{rt}=H_{rs}\cdot H_{st}
$$

> 这种结构实际上是半群, 称为 Markov 半群

> [!examples] Markov reward process
> visit state $j$ , reward $f(j)$ 在 $k$ 时刻的 reward 也是一个随机变量 $f(X_k)$ 
> 想给每个状态给一个加权函数: total reward $r(i):\text{total reward at state i}$ 的期望
>
> $$
\begin{align}
r(i) &=\mathbb{E}\left[\sum_{k=0}^nf(X_k)\Bigg| X_0=i\right]=\sum_{k=0}^n\mathbb{E}[f(X_k)\mid X_0=i]\\
&=\sum_{k=0}^n \sum_{j}f(j)P(X_k=j\mid X_0=i)\\
&=\sum_{k=0}^n\sum_{j}f(j)p^k(i,j)=\left((1+p+\cdots +p^n)f\right)_i
\end{align}
> $$
>
> 这是一种强化学习的建模, 即给每个状态打分

## Classification of states

#### Define reachable
态 $j$ 是从态 $i$ 可达的 reachable : $i$ communicate with $j$  , $i\mapsto j$ , 若

$$
P(X_n=j\mid X_0=i)>0\quad\exists n
$$

#### Lemma 
可达是传递的: $i\mapsto j\, ,\,j\mapsto k\implies i\mapsto k$ 
这可以由 C - K 方程直接得到

> 做一个符号的简化
>
> $$
P_i(\cdot)\coloneqq P(\cdot\mid X_0=i)
> $$
>
> 同样期望也有形式
>
> $$
\mathbb{E}_i[\cdot]\coloneqq \mathbb{E}[\cdot\mid X_0=i]
> $$
>

#### Define returning time
返回时间 : time of return state $j$ 

$$
T_j=\inf\{n\geq 1:X_n=j\}
$$

同样有 从 $i$ 到 $j$ 的概率和返回概率

$$
\rho_{ij}=P_i(T_j<+\infty)\quad \rho_{jj}=P_{j}(T_j<+\infty)
$$

则有

$$
\{T_j<+\infty\}=\bigcup_{n=1}^{\infty}\{T_j=n\}
$$

于是有可达的等价定义

$$
i\mapsto j \Leftrightarrow \rho_{ij}>0
$$

#### Define stopping time
称 $T$ 是一个 Stopping time, 若 $\{T=n\}$ 被 $X_0 ,\cdots, X_n$ 决定 (或者 $\{T=n\}\in \sigma(X_0,\cdots,X_n)$)

对返回时间有相同的分解

$$
\{T_j=n\}=\{X_1,\cdots,X_{n-1}\neq j,X_n=j\}
$$

这也是一个随机变量 $T_j\colon \Omega \to \mathbb{R}$ 

同样也可以定义 $k$ 次返回时间

$$
T^k_j=\inf\{n>T_j^{k-1}:X_n=j\}
$$

> 这也是一个 stopping time

#### Define Strong Markov Property
将 markov 性质推广到 stopping time 上:
对于一个 stopping time $T$ 

$$
P(X_{T+1}=j|X_{T}=i,T=n,(X_0,\cdots,X_{T-1})\in A)=p(i,j)
$$

> 在一般的情况, 这和 markov 性不同, 但在离散时间, 离散状态, 时间齐次的 markov chain 下, 两者是一样的
> 对于连续时间, 连续状态的情况有些许不同

这种情况可以直接计算

$$
P(X_{T+1}=j,X_{T}=i,T=n,(X_0,\cdots,X_{T-1})\in A)=\sum _{ V_n}P(X_{n+1}=j,X_0=x_0,\cdots,X_n=i )
$$

这里 

$$
V_n=\{(X_0,\cdots,X_n):X_{T}=i,T=n,(X_0,\cdots,X_{T-1})\in A\}
$$

则为

$$
\sum_{V_n}P(X_{0}=x_0,\cdots,X_n=i)\cdot p(i,j)=p(i,j)\cdot P(X_T=i,T=n,(X_0,\cdots,X_{T-1})\in A)
$$

#### Theorem
若 $X$ 为一个 DTMC , $T$ 是一个 stopping time

$$
\{(X_{T+k})_{k\ge0}\mid T=n,X_T=i\}
\stackrel{d}{=}
\{(X_k)_{k\ge0}\mid X_0=i\}
$$

这可以帮我们理解 returning time

$$
\begin{align}P_{j}(T^2_j<+\infty)&=\sum_{n}P(T_j^2<+\infty,T_j=n)\\&=\sum_{n}P(T_j^2<+\infty|T_j=n,X_{n}=j)P(T_j=n,X_n=j)\\&=\sum_{n}P(T_j<+\infty)P(T_j=n)\\&=\rho_{jj}^2\end{align}
$$

这立即得到

$$
P_j(T_j^2<+\infty|T_j<+\infty)=P_j(T_j<+\infty)
$$

同时

$$
P_j(T_j^k<+\infty)=\rho_{jj}^{k}\quad P_{i}(T_j^k<+\infty)=\rho_{ij}\rho_{jj}^{k-1}
$$

利用上面的工具, 可以很好地给不同状态分类
* Transient state: $\rho_{ii}<1$
* Recurrent state: $\rho_{ii}=1$

状态分类可以用另外一种语言, 用计数的语言

$$
N(j)=\sum_{n=1}^{\infty}\mathbf{1}_{\{X_n=j\}}
$$

则 

$$
\mathbb{E}_i[N(j)]=\sum_{n=1}^{\infty}P_i(X_n=j)=\sum_{n=1}^\infty p^n(i,j)=\sum_{k\geq 1}^{\infty}P_i(N(j)\geq k)
$$

而 

$$
P_i(N(j)\geq k)=P_i(T_j^k<+\infty)=\rho_{ij}\rho_{jj}^{k-1}
$$

最后

$$
\mathbb{E}_i[N(j)]=\frac{\rho_{ij}}{1-\rho_{jj}}
$$

从这也可以看出: 在无穷时间内, transient state 只会返回有限次, 但 recurrent state 会返回无穷次

#### Lemma
State $i$ 是一个 recurrent state iff 

$$
\sum_{n=1}^{\infty}p^n(i,i)=+\infty
$$

#### Lemma

$$
\rho_{ij}>0 \quad(i\mapsto j),\quad\rho_{ji}<1\implies i\text{ is transient state}
$$

Proof: 
$\exists n, P_i(X_n=j)>0$ , 于是可定义 $k=\min\{n:P_i(X_n=j)>0\}$ , 那么 $X_1,\cdots,X_{k-1}\neq j$ 

$$
P_{i}(T_i=\infty)\geq p(x_0,x_1)\cdots p(x_{n-1},x_n)P_{j}(T_i=\infty)>0
$$

> 直觉是这个态应该会从 $j$ 处泄漏出去, 所以应该先刻画到 $j$ 态的情况, 给出下界

那么有 $\rho_{ii}<1$ 即为 transient state

#### Lemma
若 $i\mapsto j$ 而 $i$ 是一个 recurrent state, 这导致 $j$ 也是一个 recurrent state 
Proof:
先说明还有 $j\mapsto i$ , 即 $\exists n, P_j(X_n=i)>0$ , 如果不成立, 则 $\rho_{ji}<1$ , 则与上面的命题矛盾

所以

$$
\sum_{n=1}^{\infty}p^n(i,i)=\infty
$$

那么

$$
\begin{align}\sum_{n=1}^\infty p^n(j,j)\geq\sum_n p^{m}(j,i)p^n(i,i)p^k(i,j)=\infty\end{align}
$$

> 注意最后一个求和只对 $n$ 进行

故状态空间的不同 recurrent state 和 transient state 进行了一个划分

#### Define closed
集 $S$ 是 closed 的, 若 $p(i,j)=0 \quad \forall i\in S,\forall j\notin S$

#### Lemma
$S\neq\emptyset$ 且是一个有限且闭合的集, 则存在 $s\in S$ 是 recurrent

> 有点像聚点原理

对 $i\in S$ , $\sum_{j\in S}p^n(i,j)=1$ , 从而

$$
\sum_{j\in S}\frac{\rho_{ij}}{1-\rho_{jj}}=\sum_{j\in S}\mathbb{E}_i[N(j)]=\sum_{n}\sum_{j\in S}p^n(i,j)=\infty
$$

即 $\exists s$ 合于 $\rho_{ss}=1$

#### Define irreducible
集 $S$ 是不可约 irreducible 的, 若 

$$
i\mapsto j\quad\forall i,j\in S
$$

将两个集的性质合并在一起, 这样的集中所有的态都是 recurrent state

#### Theorem
非空集 $S$ 是不可约的有限闭集, 则所有态都是 recurrent state

#### Theorem decomposition of DTMC
对 DTMC, 若状态空间 $S$ 有限, 则

$$
S=T\sqcup R_1\sqcup R_2\sqcup\cdots\sqcup R_k
$$

这里 $T$ 是 transient state , $R_i$ 是不可约的闭集, 包含 recurrent state

Proof:

> 几乎是数数问题

先定义

$$
T=\{i:\exists j, i\mapsto j, j\not\mapsto i\}
$$

然后找 $S\setminus T$ 剩下什么, 然后是归纳法: 若非空, 则存在 $i\in S\setminus T$ , 考察 $C_i=\{j:i\mapsto j\}$ , 这其中的态都能到 $i$ 
再看这是否是一个闭集, 传递性: $i\mapsto j\mapsto l$ , 这导致 $i\mapsto l\implies l\in C_i$ 
再考察是否可约, 同样以 $i$ 态作为中介 $j\mapsto i\mapsto l$ 对任意 $j,l\in C_i$ 然后再考察 $S-T-C_i$ 直到最后得到空集为止
由于 $S$ 有限, 迭代算法会终止, 完成证明

上面的内容都在问 

$$
P_i(T_i<+\infty)\overset{?}{=} 1
$$

对有限状态, 这可以决定这是否是 recurrent 或者 transient

但对于无穷状态, 这一点就截然不同, 状态可能越跑越远, 因为状态数是无穷的. 即使给出了肯定的答复, 也需要问: 到底需要多少时间才能回到
即需要考察 

$$
\mathbb{E}_i[T_i]\overset{?}{<}+\infty
$$

若是, 称为 positive recurrent, 反之为 null recurrent

## Steady state / Limit Behavior

这实际上在问

$$
p^n(i,j)\overset{?}{\to} \pi(j)\quad \text{as} \quad n\to\infty,\forall i
$$

分布会不会收敛到一个与初值无关的分布
即问

$$
X_0\sim q\quad X_n\sim q_n\quad q_n(j)=\sum q(i)p^n(i,j)\to\pi(j)
$$

> 一个例子, 考虑 transition matrix
>
> $$
\begin{bmatrix}1-a & a \\b&1-b\end{bmatrix}
> $$
>
> $q_n(0) = (1-a) q_{n-1}(0) + b q_{n-1}(1)=(1-a-b)q_{n-1}(0)+b$ , 然后这个稳态分布的条件是 $|1-a-b|<1$
> 并且对于不同的参数, 这给出了不同的收敛性, 需要讨论的即为什么情况下会收敛


一种情况是 $a=b=0$ , 此时

$$
p=\begin{bmatrix}1&0\\0&1\end{bmatrix}\implies p^n=\begin{bmatrix}1&0\\0&1\end{bmatrix}
$$

此时给出了一个初值依赖的极限分布, 不是我们想要的稳态

当 $a=b=1$ 时, 即为另一个极端, 此时不存在稳态

下面讨论如果存在稳态, transition matrix 应该有什么性质

#### Necessary condition

$$
\underset{n\to \infty}{\lim} p^n(i,j)=\underset{n\to\infty}{\lim}\sum_{k}p^{n-1}(i,k)p(k,j)
$$

若存在一个初值无关的稳态 $\pi(j)$ , 那么 (现在是 DTMC , 极限和求和可交换)

$$
\pi(j)=\sum_{k}\pi(k)p(k,j)\implies \pi=\pi P
$$

这可以给出平稳分布更方便的表述

#### Define steady distribution
称 $\pi$ 是一个平稳分布, 若 

$$
\pi=\pi P\Leftrightarrow \pi(I-P)=0
$$

> 可以看到, 若在某点达到了平稳分布, 那么往后就一直是平稳分布
> 另外这个解并不一定存在, 我们要求的是非负解

例如一个对称的分布, 每个状态等权, 此时, 列求和也为 1

$$
\sum_{i}p(i,j)=\sum_{j}p(i,j)=1
$$

那么此时一个容易猜到的平稳分布是均匀分布

#### Detailed balance condition
细致平衡即为

$$
\pi(i)p(i,j)=\pi(j)p(j,i)\quad\forall i,j
$$

这是上面对称分布的条件的加强版, 两侧对 $i$ 求和得到

$$
\sum_{i}\pi(i)p(i,j)=\sum_{i}\pi(j)p(j,i)=\pi(j)\implies \sum_{i}p(j,i)=1
$$

> 更一般这也叫可逆性, 进一步深入的话也可以在其上建立 Hilbert space
> Codex 补充：相对于平稳分布 $\pi$ 看, detailed balance 等价于转移算子在 $L^2(\pi)$ 里是自伴的, 所以很多谱性质会更清楚.
> 但这里不再深入

这是一个更强的条件, 从 detailed balance 也可以直接解出 steady distribution (若存在的话)
这给出了一个平稳分布的充分不必要条件

一个例子 

$$
\begin{bmatrix}0.5&0.5&0\\0.3 & 0.1& 0.6\\0.2 &0.4& 0.4\end{bmatrix}
$$

满足双随机性, 存在平稳分布, 但并不是细致平衡的

Codex 补充：这个转移矩阵对应的拓扑如下.

![[attachments/tikz/random-process-ch1-topology.png]]

在这个 markov chain 中, 存在一个 cycle $1\to2\to3\to1$
但是逆向的 cycle 是不对称的, 这导致该过程并不是 detailed balance


一般的, 对于一个长度为 $n$ 的 cycle , 满足

$$
\prod_{k}p(x_{k-1},x_k)=\prod_{k}p(x_k,x_{k-1})
$$

这叫做 Kolmogorov - cycle condition : 对有限不可约链, 若上式对**所有** cycle 成立 $\Leftrightarrow$ 存在一个平稳分布 $\pi$ 满足 detailed balance

> [!note]
> 定理的证明: 待写

回到对极限行为研究的主线: 

首先对 transient state 的分析, 由于 transient 的性质, 可以猜测

$$
p^{n}(i,j)\to 0\quad \text{j transient}
$$

可以给出一个 scratch

$$
\mathbb{E}_i[N(j)]=\sum_{n=1}^{\infty}p^n(i,j)=\frac{\rho_{ij}}{1-\rho_{jj}}<\infty
$$

则余项是趋于 0 的, 故 transient state 的极限行为非常简单, 只需要分析 recurrent state 即可

容易看出, 若起点是一个 transient state , 它会到达所有可达到 recurrent class 上, 可以想象极限分布应该是这些 recurrent class 中的平稳分布的线性组合, 而权重由通向各个 recurrent class 的概率给出,  这都是可以接受的平稳分布

> Limit of $p^n(i,j)$ is non - unique , it depends on $X_0$
> 原因在于存在 transient state 的 chain 不是 irreducible 的

所以需要做的就是先做单个 recurrent class 

> 当然, 并不说明一个 recurrent class 中就一定收敛到极限分布, 对最开始的双态, 若跃迁概率都为 $1$ , 虽然有平稳分布 $\pi=(1/2,1/2)$ , 但 $p^n(i,j)$ 并不收敛
> 这种情况的原因在于, 系统处于某一个态只能处于某些特定时刻, 某种特殊的周期性会导致他不会收敛到平稳分布

#### Define period
态 $j$ 的周期是指

$$
d_j \coloneqq \gcd\{n: p^n(j,j)>0\}=\gcd I_j
$$

这并不说在周期上一定会回来, 只是说可能会回来

同样, 称一个态 $i$ 是 aperiodic 的, 若 $d_i =1$

#### Lemma 可达传递周期
若 $i\mapsto j,j\mapsto i$ , 那么 $d_i=d_j$ 
proof:

$$
i\mapsto j\implies \exists k,m\quad p^k(i,j)>0, p^m(j,i)>0
$$

不妨取 $d_i\leq d_j$ , 而 $p^{k+m}(j,j)>0$ , 那么 $\forall l\in I_i\quad p^{k+m+l}(j,j)>0$
这导出 $k+m\in I_j$ , $k+m+l\in I_j$ , $\forall l \in I_i$ 

这表明任意 $l$ 都是是 $d_j$ 的正整数倍数 $d_i \geq d_j$ 这导出 $d_i=d_j$ 

则若一个态有连接到自己的环, 那么他的周期一定是 1 , 即

#### Claim 反周期充分大时间内可返回
若 $d_i =1$ , 则存在 $n_0$ , 对任意 $n>n_0$ , 有 $p^{n}(i,i)>0$ 

这是因为 $I_i$ 对加法封闭, 并且 $\gcd I_i=1$ , 则对于 $a,b\in I_i$ 存在 $m,n\in \mathbb{Z}$ 合于

$$
an+bm =1
$$

模 $a$ 得到

$$
bm \equiv 1 \quad \mathrm{mod }a
$$
在商群里做加法闭包得到

$$
\{bm,2bm,3bm,\cdots,abm\}\overset{\mod a\text{ 后}}{=} \mathbb{Z}/a\mathbb{Z}
$$
即 $b$ 乘一些正整数跑满了 模 $a$  的整个周期, 取充分大的 $n$ 就有 

$$
b I = \{na+1,na+2,\cdots ,na+a-1\}\quad\text{存在一个}\, I\subset\mathbb{Z}_{\geq 0}
$$

对足够大的 $N = an+r$ , 有 $bk = n_0a+r$ 从而

$$
N=bk+a(n-n_0)
$$
于是取 $n_0=\underset{r\in \mathbb{Z}/a\mathbb{Z}}{\max} n_0(r)$  和 $n>n_0$ 即完成证明, 这个证明只能用于 $I$ 中有两个数的情况

> 这个证明有点像用理想生成整个整数, 
>
> $$
\braket{I} = \gcd(I)\mathbb{Z}\quad I \text{ 是理想}
> $$
>
> 但是不一样的是这里只能用正整数去生成, 所以只能保证能铺满大正数

对于一般情况, 也许可以放到更抽象的情形完成证明: 理想的例子中告诉我们对于 $a_1,a_2,\cdots,a_n\in I$  合于 $\gcd (a_1,\cdots,a_n)=1$, 我们自然有满射 $\phi$

$$
\mathbb{Z}^n\to \mathbb{Z}\quad (n_i)\to\sum_i n_i a_i
$$

所以这个定理实际上在说, 左侧限制到正坐标, 右侧限制到一个大正数后, 依旧有满射 
那么存在 $u\in \mathbb{Z}^n$ 合于 $\phi(u) = 1$  , 但是不能保证坐标都是正的, 所以做一个 shift 保证正坐标

$$
u\to u+ M(1,\cdots,1)\quad \phi(u+M(1,\cdots,1))=1+M(a_1+\cdots+a_n)=1+MA
$$

于是可以得到

$$
\phi(u) = 1\quad \mod A
$$

这把问题放回到了二元版本 $\gcd(\phi(u),A)=1$ 存在充分大正数 $n_0$ 使得 $n>n_0$ 

$$
n=l_1 \phi(u)+l_2 A\in I_i
$$

最后一个属于来自 $I_i$ 对加法封闭

> Codex 补充：这里用到的是数值半群的结论. 若 $A\subset \mathbb{N}$ 非空且对加法封闭, 并且 $\gcd(A)=1$ , 则存在 $n_0$ 使得所有 $n\ge n_0$ 都属于 $A$ . 也就是说, 这样的加法半群会包含所有充分大的正整数. 二元情形就是 Frobenius coin problem 的经典结论, 一般情形可视作它在数值半群中的推广.

后面要做的基本是证明这个定理:
#### Theorem 收敛定理
若 $X_n$ 是不可约 $(I)$ , 非周期 $(A)$ , 存在平稳分布 $\pi$  $(S)$ 的, 则 $p^n(i,j)\to \pi(j)\quad\forall i$


## Returns of a fixed state
$i$ 是 recurrent 的, 且 $\mathbb{E}_i[T_i]<\infty$  , 强大数定律表明

> 因为在强 markov 性质下, 它们是独立同分布的


$$
\frac{T_i^k}{k} \xrightarrow{\text{a.s.}} \mathbb{E}_i[T_i]
$$

> [!note]
> 那么看访问频率
>
> $$
N_{n}(i)=\sum_{l=1}^n \mathbf{1}_{X_l=i}
> $$
>
> 则
>
> $$
\frac{n}{N_n(i)}\xrightarrow{\text{a.s.}}\mathbb{E}_i[T_i]
> $$
>
> 下面这个结果由夹逼给出
>
> $$
T_i^{N_n(i)}\leq n < T_i^{N_n(i)+1}
> $$

所以我们有如下定理

#### Theorem 访问频率
$X_n$ 是 irreducible $(I)$ , 所有态都是 recurrent $(R)$ , 那么

$$
\frac{N_n(i)}{n}\xrightarrow{\text{a.s.}} \frac{1}{\mathbb{E}_i[T_i]}
$$

> 上面这个结构要求常返态, 然后如果所有 $i$ 都满足这个关系, 那要求不可约
> 这样我们几乎找到了平稳分布

现在回到收敛定理

先从一些特例看: 

若 $X_0\sim \pi$ , 那么

$$
\mathbb{E}_{\pi}[N_n(i)]=n\times \pi(i)
$$

若 $\pi_i>0$ , 那么 

$$
\mathbb{E}_{\pi}[N(i)]=\infty
$$

这表明 $i$ 也是一个 recurrent state, 即

#### Lemma
$(S)$ , $\pi(i)>0$ , 则 $i$ 是 recurrent state

那上面的例子代入, 有

$$
\mathbb{E}_{\pi}[\frac{N_n(i)}{n}]=\pi(i)
$$

> 注意这两个收敛的行为不同, 一个是几乎处处收敛, 一个是 1 - 范数收敛

#### Theorem

$$
(I) , (S) \implies \pi(i)=\frac{1}{\mathbb{E}_iT_i}
$$

> 这用到了控制收敛定理 DCT , 即用一个可积函数去控制一列几乎处处收敛的随机变量, 从而交换极限和期望.
> Codex 补充：DCT 的表述是: 若 $Y_n\to Y$ a.s. 且存在可积随机变量 $Z$ 使得 $|Y_n|\le Z$ 对所有 $n$ 成立, 则 $\mathbb{E}[Y_n]\to \mathbb{E}[Y]$ . 这里在平稳初值 $X_0\sim\pi$ 下取 $Y_n=N_n(i)/n$ , 由前面的访问频率定理知 $Y_n\to 1/\mathbb{E}_i[T_i]$ a.s. , 又因为 $0\le Y_n\le 1$ , 可以取 $Z\equiv 1$ . 另一方面 $\mathbb{E}_\pi[Y_n]=\pi(i)$ , 所以 DCT 给出 $\pi(i)=1/\mathbb{E}_i[T_i]$ .


这表明一个 irreducible 的 Markov 过程, 他的平稳分布是唯一的

## One - cycle analysis

对于一个 Markov 过程, 可以把它每段回到初态的过程上单独分析, 这种方法叫 "one - cycle" analysis

Example: 

$$
\sum_{n=0}^{T_{i}-1}\mathbf{1}_{X_n=j}=\sum_{n=0}^{\infty}\mathbf{1}_{X_n=j, n< T_i}
$$

即在一个 访问 $i$ 的 cycle 里面 访问态 $j$ 的次数, 首先可以看的是期望

$$
\mu_i(j)=\sum_{n=0}^{\infty}P_i(X_n=j, n<T_i)
$$

实际上这在某种程度上定义了平稳分布 (缺少归一化), 

$$
\mu_i P=\mu_i
$$

> [!note]
> 直接看计算
>
> $$
\sum_{k}\mu_i(k)P_{kj}
> $$
>
> 意思是先统计 cycle 内有多少次经过 $k$ , 然后再一步走到 $j$ , 实际上就是 cycle 内有多少次到 $j$ 即
>
> $$
\begin{align}
\mathbb{E}_i[\sum_{n=0}^{T_i-1}\mathbf{1}_{X_{n+1}=j}]&=\sum_{k}\sum_{n=0}^{\infty}P_i(X_n=k ,n<T_i,X_{n+1}=j)\\
&=\sum_k\sum_{n=0}^{\infty}P_i(X_n=k,n<T_i)p_{kj}\\
&=\sum_k \mu_i(k)p_{kj}
\end{align}
> $$
>
> 后者来自于 markov 性, 而且有
>
> $$
\sum_{n=0}^{T_i -1}\mathbf{1}_{X_n=j}=\sum_{n=0}^{T_i-1}\mathbf{1}_{X_{n+1}=j}
> $$
>
> 因为求和边缘一定是 $i$ , 所以中间求和是相同的, 而对于 $i=j$ 的情况, 头尾补偿了


归一化系数实际上就为:

$$
\sum_{j}\mu_i(j)\sim\sum_j \sum_{n=0}^{T_{i}-1}\mathbf{1}_{X_n=j}=T_i
$$

$\sim$ 两边恰好相差一个期望, 于是我们得到如下结果

#### Theorem 

$$
(I), (R)\implies \frac{\mu_i(j)}{\mathbb{E}_i T_i} \quad\text{is stationary} \quad , \quad 0<\mu_{i}(j)<+\infty
$$

当然这里要求 $\mathbb{E}_i T_i <\infty$ , 即对任意正常返态 $i$ 
即 $\pi$ 存在

> [!Example] Markov Reward Process reward $f(i)$ on state $i$ 
>
> 现在只考虑一个 cycle 内的 reward: reward in one - cycle
>
> $$
Y_i =\sum_{n=0}^{T_i-1}f(X_n)\quad Y_k =\sum_{n=T_{i}^{k-1}}^{T_i^k -1} f(X_n)
> $$
>
> 那么
>
> $$
\frac{1}{k}\sum_{l=0}^k Y_l\xrightarrow{\text{a.s.}} \mathbb{E}_i Y_i=\sum_{j}\mu_i(j)f(j)
> $$
>
> 那么平均 reward
>
> $$
\frac{1}{n}\sum_{m=1}^n f(X_m)\approx \frac{k}{n}\frac{1}{k}\sum_{l=1}^{k}Y_l\to\frac{1}{\mathbb{E}_i T_i}\sum_j\mu_i(j)f(j)
> $$


#### Theorem Ergodic theorem
若 $(I),(S), \mathbb{E}_\pi[f]<\infty$ , 那么

$$
\frac{1}{n}\sum_{i=1}^n f(X_i)\to \mathbb{E}_\pi[f]=\sum_{i}\pi(i)f(i)
$$

若取 $f(X)=\mathbf{1}_{X=j}$ , 有

$$
\frac{1}{n}\sum_{i=1}^n \mathbf{1}_{X_i=j}\to \pi(j)\quad \frac{1}{n}\sum_{k=1}^n p^k(i,j)\to \pi(j)
$$


> [!note]
> 这里并没有使用到 aperiodic

是否存在唯一的 steady / limit distribution? 
$I$ , $A$ , $S$ , 下面说明这也是充分条件

考虑 markov chian 的两个初值给出的过程 $(B_n,G_n)$
共同相遇时间

$$
T=\min\{n\geq0 ,B_n =G_n\}
$$

#### Theorem 
$(A),(S),(I)$ 则 

$$
p^n(i,j)\to\pi(j)\quad\forall i
$$

Proof:

一种 coupling 的做法, 考虑, 上面的两个过程在相遇之后就同频了, 即 在 $n\geq T$ 之后

$$
B_n=G_n
$$

即在到达时候后的概率相同, 即

$$
\begin{align}
P(B_n=i, n\geq T)& =P(G_n=i,n\geq T)\\
&=\sum_{m=1}^n\sum_{j\in S} P(T=m,B_m=j,B_n=i)
\end{align}
$$

用全概率展开

$$
|P(B_n=i)-P(G_n=i)|\leq P(B_n=i,T>n)+P(G_n=i,T>n)\leq 2P(T>n)
$$
最后取 $B_0=i$ 且 $G_0$ 服从平稳分布, 得到 1 - 范数意义的收敛

## Hitting time / exit time

考虑一个双状态的 markov 过程, 但每个状态连出去一个自连接的状态, 则 hitting time

$$
T=\min\{n\geq 0, X_n\in\{C,D\}\}
$$

分析 $T<+\infty?$ 回答是肯定的, 但最终停留在哪个状态? termination state

考察 

$$
h(i)=P_i(X_T=D)
$$

边界条件 

$$
h(C)=0,h(D)=1
$$

继续做 first - step analysis:

$$
h(A)=0.75h(A)+0.2 h(B)+0
$$

$$
h(B)=0.25h(A)+0.5h(B)+0.25
$$

写成矩阵

Codex 补充：若记未知向量为 $\mathbf{h}=(h(A),h(B))^\top$ , 则线性方程可以写成

$$
\begin{bmatrix}
0.25 & -0.2\\
-0.25 & 0.5
\end{bmatrix}
\begin{bmatrix}
h(A)\\
h(B)
\end{bmatrix}
=
\begin{bmatrix}
0\\
0.25
\end{bmatrix}
$$

解得 $h(A)=\frac{2}{9},\; h(B)=\frac{5}{9}$ .


同样, 还可以计算期望时间 $\mathbb{E}T$ , 想法是相同的, 定义一个函数直接给出期望时间, 然后做 1 - step analysis

另一个例子是 抛硬币 
第一次看到 $HH$ 的期望时间估计, 或者 $HT$ 等, 方法是一样的

## General framework

考虑有限状态空间 $S$ , 子集 $F$ , 定义 hitting time

$$
V_F=\min\{n\geq 0, X_n\in F\}
$$

则 $A,B\subset S$ 无交, 即 $S =A\sqcup B \sqcup C$ 
并且 $h(a)=1,\forall a\in A$ , $h(b)=0, \forall b\in B$ 以及 $h(c)=\sum_{j}p(c,j)h(j),\forall c\in C$ 

就有一般形式的 first - step analysis

#### Theorem
若 $P_c(V_A \land V_B <\infty)=1$ 则 $h(c)=P_c(V_A<V_B)$

证明的思路是对上式取期望
使用有界收敛定理

对于 hitting time 有类似的结果

$g(a)=0,\forall a\in A$ 和 $g(c)=1 +\sum_j p(c,j)g(j),\forall c\in C$ 

#### Theorem
若 $P_c(V_A<+\infty)=1,\forall c$ , 则 $g(c)=\mathbb{E}_c(V_A)$ 


继续讨论 random walk/ gambler‘s ruin
设定 $X_0=k$ , 定义 $T$ 为 hitting time

定义

$$
h(k)=P(X_T=N)
$$

做相同的 first step analysis

$$
h(k)=ph(k+1)+qh(k-1)
$$

然后解线性方程组, 这个稀疏矩阵是可以直接解的

在这里可以将 $N$ 延拓

再求解 $\mathbb{E}T$ , 方法是相同的

此时讨论返回时间



#### Theorem
$X$ 是不可约的 markov 过程, 下面的几点等价: $(TFAE)$

存在一个 positive recurrent state

存在一个 stationary distribution

all states are positive recurrent


#### Theorem
$(I)$ 则 all states are positive recurrent / null recurrent / transient

若 $(S)$ , 则 all states are positive recurrent

若进一步有 $(A)$ , 则

$$
p^n(i,j)\to\pi(j)=\frac{1}{\mathbb{E}_jT_j}
$$
