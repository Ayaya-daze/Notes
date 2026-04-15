# 基本定义

martingale 的概念是源于赌钱, 在赌博时, 往往需要根据已知信息, 对下一步下注进行决策, 对于公平的情况, 我们期望: 对任何决策, 下一步的收益与当前的收益是相同的, 即满足条件

$$
\mathbb{E}(X_{n+1}\mid X_0,\cdots,X_n)=X_n
$$

注意这是随机变量之间的等式, 下面先讨论条件期望

> [!example]
> 对于 branching process, 定义
>
> $$
> M_n=\frac{X_n}{\mu^n}\implies \mathbb{E}(M_{n+1}\mid X_n)=M_n
> $$
>
> 这也是一个 martingale

为了定义 martingale, 需要先定义 条件期望

## conditional expectation

首先条件期望为

$$
P(E\mid A)=\frac{P(E\cap A)}{P(A)}=\frac{\mathbb{E}(\mathbf{1}_{E}\cdot\mathbf{1}_{A})}{P(A)}
$$

从而条件期望

$$
\mathbb{E}(Y\mid A)=\frac{\mathbb{E}(Y\cdot \mathbf{1}_A)}{P(A)}
$$

> [!note]
> 在 pmf 情况下可以这么理解
>
> $$
> \mathbb{E}(Y\mid A)=\sum_{\omega\in A}Y(\omega)\times\frac{P(\omega)}{P(A)}
> $$
>
> 相当于修改了概率测度

看几个特殊例子和性质

- Y & A are independent, 则有

$$
\mathbb{E}(Y\mid A)=\mathbb{E}(Y)
$$

- Y is determined by A

$$
\mathbb{E}(XY\mid A)=c\mathbb{E}(X\mid A)
$$

这里 $Y(\omega)=c \quad \omega\in A$

- Linearity

$$
\mathbb{E}(Y+Z\mid A)=\mathbb{E}(Y\mid A)+\mathbb{E}(Z\mid A)
$$

- Jensen's inequality

$$
\phi\quad \text{convex}\implies \phi(\mathbb{E}(Y\mid A))\leq \mathbb{E}(\phi(Y)\mid A)
$$

同样, 有全概率, 考虑如下

$$
B=\bigcup_i^k A_i\quad A_i\quad\text{disjoint}
$$

则

$$
\mathbb{E}(Y\mid B)=\frac{\sum_i\mathbb{E}(\mathbf{1}_{A_i}Y)}{P(B)}=\sum_i \mathbb{E}(Y\mid A_i)\frac{P(A_i)}{P(B)}
$$

然后考虑

$$
\mathcal{A}=\{A_i\}\quad \implies \mathbb{E}(Y\mid\mathcal{A})=\sum_i\mathbb{E}(Y\mid A_i)\mathbf{1}_{A_i}=\mathbb{E}(Y\mid A_i)\quad \text{on}\, A_i
$$

> 对期望最好的理解是在概率空间 $\Omega$ 中进行计算, 一切等号均理解为 $\Omega$ 上的等号
> 所有上面的意思不过是 $\omega$ 选择出了划分 $\mathcal{A}$ 中的一个子集 $A_i$ , 然后在 $A_i$ 上 point-wise 地定义值, 最后再定义到整个 $\Omega$ 上即可

> 补充: 这里的 $\mathcal{A}$ 更准确地说是一个划分, 真正对应的是它生成的 $\sigma(\mathcal{A})$

注意这是一个随机变量, 即 $\mathbb{E}(Y\mid\mathcal{A}):\Omega \to \mathbb{R}$

则有塔式性质

$$
\mathbb{E}(\mathbb{E}(Y\mid\mathcal{A}))=\mathbb{E}(Y)
$$

> 这是上面的直接结果, 因为
>
> $$
> \mathbb{E}(Y\mid\mathcal{A})=\sum_i\mathbb{E}(Y\mid A_i)\mathbf{1}_{A_i}\implies \mathbb{E}[\mathbb{E}(Y\mid\mathcal{A})]=\sum_i\mathbb{E}(Y\mid A_i)P(A_i)=\mathbb{E}[Y]
> $$

正式的表述是: $Y$ is determined by $\mathcal{A}$ , 则

$$
\mathbb{E}(XY\mid\mathcal{A})=Y\mathbb{E}(X\mid\mathcal{A})\quad Y\text{ is } \sigma(\mathcal{A})\text{ measurable}
$$

> [!note]
> 对于 sigma 代数
> [[测度, 实分析基础 - 测度]]
> 集合 $X$ 上的 $\sigma$ - 代数是指 $X$ 的一族子集 $\mathcal{F}\subset P(X)$ 合于以下条件
> 1. $\emptyset\in \mathcal{F}$
> 2. 若 $E\in \mathcal{F}$ , 则 $X\setminus E\in\mathcal{F}$
> 3. 若可数个 $E_i\in \mathcal{F}$ , 则 $\bigcup_{i=1}^{\infty}E_i \in \mathcal{F}$

如果做更精细的划分

$$
A_i=\bigcup_j A_{ij}\implies \tilde{\mathcal{A}}=\{A_{ij}\}
$$

先来看特殊情况

$$
\mathbb{E}(Y\mid\tilde{\mathcal{A}})\quad \text{is determined by }\mathcal{A}
$$

由于 $\mathbb{E}(Y\mid A_{ij})=c_i$ 那么

$$
\mathbb{E}(Y\mid\tilde{\mathcal{A}})=\mathbb{E}(Y\mid\mathcal{A})
$$

这本质上是源于 $\sigma(\mathcal{A})\subset \sigma(\tilde{\mathcal{A}})$ , 即即使 $\tilde{\mathcal{A}}$ 的划分更精细, 但它在 $\mathcal{A}$ 的每个大块上仍是常数, 则随机变量取值是相同的

一个例子是

$$
\mathbb{E}(\mathbb{E}(Z\mid X,Y)\mid X)=\mathbb{E}(Z\mid X)
$$

这是实质上是来源于

$$
\mathbb{E}(\mathbb{E}(Y\mid\tilde{\mathcal{A}})\mid\mathcal{A})=\mathbb{E}(Y\mid\mathcal{A})
$$

因为在大块上是常数, 则在小块上本身就是常数

具体地

$$
\begin{aligned}
\mathbb{E}\left[\sum_{ij}\mathbb{E}(Y\mid A_{ij})\mathbf{1}_{A_{ij}}\Bigm|\mathcal{A}\right]
&=\sum_{k}\frac{\sum_{ij}\mathbb{E}(\mathbb{E}(Y\mid A_{ij})\mathbf{1}_{A_{ij}}\cdot\mathbf{1}_{A_k})}{P(A_k)}\mathbf{1}_{A_k}\\
&=\sum_k \frac{\sum_j\mathbb{E}(Y\mid A_{kj})P(A_{kj})}{P(A_k)}\mathbf{1}_{A_k}\\
&=\sum_k\mathbb{E}(Y\mid A_k)\frac{\sum_jP(A_{kj})}{P(A_k)}\mathbf{1}_{A_k}
\end{aligned}
$$

注意 $A_{ij}\cap A_i=A_{ij}$ , 最后一步至少要求分割是测度意义上无交的

另外也有

$$
\mathbb{E}(\mathbb{E}(Y\mid\mathcal{A})\mid\tilde{\mathcal{A}})=\mathbb{E}(Y\mid\mathcal{A})
$$

#### Definition
称 $M_n$ 是一个 Martingale , w.r.t. $X_n$ 若

1. $\mathbb{E}|M_n|<+\infty\quad\forall n$
2. $M_n$ 由 $X_0,\cdots,X_n,M_0$ 确定, 记为 $M_n\in \mathcal{F}_n$
3. $\mathbb{E}(M_{n+1}-M_n\mid X_0=x_0,\cdots ,X_n=x_n,M_0=m_0)=0\quad \forall n,x_0,\cdots,x_n,m_0$

另一种写法是

$$
\mathbb{E}(M_{n+1}\mid\mathcal{F}_n)=M_{n}
$$

> [!note]
> 实际上这和 markov 过程没啥关系, 这描述的只是期望, 而且并不是无记忆性的依赖

例子 Random walk

$$
S_n=S_0+X_1+\cdots+X_n
$$

且

$$
\mathbb{E}X_i=\mu\quad M_n=S_n-n\mu
$$

则 $M_n$ 是 martingale , 验证即可

$$
\mathbb{E}(M_{n+1}-M_n\mid\mathcal{F}_n)=\mathbb{E}(X_{n+1}-\mu\mid\mathcal{F}_n)=0
$$

如果再考虑方差

$$
\mathbb{E}X_i=0\quad \mathrm{Var}X_i=\sigma^2\quad M_n=S_n^2-n\sigma^2
$$

则

$$
\begin{aligned}
M_{n+1}-M_n
&=(S_n+X_{n+1})^2-S_n^2-\sigma^2\\
&=2S_nX_{n+1}+X_{n+1}^2-\sigma^2
\end{aligned}
$$

所以

$$
\begin{aligned}
\mathbb{E}(M_{n+1}-M_n\mid\mathcal{F}_n)
&=2S_n\mathbb{E}(X_{n+1}\mid\mathcal{F}_n)+\mathbb{E}(X_{n+1}^2-\sigma^2\mid\mathcal{F}_n)\\
&=2S_n\mathbb{E}X_{n+1}+\mathbb{E}X_{n+1}^2-\sigma^2\\
&=0
\end{aligned}
$$

这也是 martingale

对于指数

$$
\phi(\theta)=\mathbb{E}e^{\theta X_i}<+\infty
$$

$$
M_n=\frac{e^{\theta S_n}}{\phi(\theta)^n}
$$

则这也是 martingale

补充一下过程:

$$
\begin{aligned}
\mathbb{E}(M_{n+1}\mid\mathcal{F}_n)
&=\mathbb{E}\left(\frac{e^{\theta S_{n+1}}}{\phi(\theta)^{n+1}}\Bigm|\mathcal{F}_n\right)\\
&=\frac{e^{\theta S_n}}{\phi(\theta)^{n+1}}\mathbb{E}(e^{\theta X_{n+1}}\mid\mathcal{F}_n)\\
&=\frac{e^{\theta S_n}}{\phi(\theta)^{n+1}}\phi(\theta)\\
&=\frac{e^{\theta S_n}}{\phi(\theta)^n}=M_n
\end{aligned}
$$

##### Doob martingale

考虑随机变量 $Z,X_1,\cdots,X_n$ , 定义

$$
M_n=\mathbb{E}(Z\mid X_1,\cdots,X_n)
$$

则

$$
\mathbb{E}(M_{n+1}\mid X_1,\cdots,X_n)=\mathbb{E}(\mathbb{E}(Z\mid X_1,\cdots,X_{n+1})\mid X_1,\cdots,X_n)=M_n
$$

Martingale 可以推广为 supermartingale, 和 submartingale , 做法是修改等号为不等号

即

- supermartingale $\mathbb{E}(M_{n+1}\mid\mathcal{F}_n)\leq M_n$
- submartingale $\mathbb{E}(M_{n+1}\mid\mathcal{F}_n)\geq M_n$

现在用这些结果来

$W_n$ 是第 $n$ 轮的 wealth , $H_n$ 是由前面轮 $W_0,X_1,\cdots ,X_{n-1}$ 决定的策略, 即 predictable, 则

$$
W_n=W_0+\sum_k H_k (M_k-M_{k-1})
$$

也是一个 martingale

一种策略是每轮都按照 $2$ 的幂次下注, 这样只要赢一次, 就会把收入拉到 $1$

#### Theorem
$H_n$ is predictable, $0\leq H_n\leq c_n$ , $M_n$ is a (super)martingale
then $W_n$ is a (super)martingale

proof:

$$
\mathbb{E}(W_{n+1}-W_n\mid\mathcal{F}_{n})=\mathbb{E}(H_{n+1}(M_{n+1}-M_n)\mid\mathcal{F}_n)=H_{n+1}\mathbb{E}(M_{n+1}-M_n\mid\mathcal{F}_{n})
$$

故 $W_n$ 和 $M_n$ 做差具有相同的符号, 并且 $W_n$ 由 $\mathcal{F}_n$ 决定

> 可以看到符号和 $H_n$ 的符号有关, 如果 $H_n$ 可以为负, 即允许做空, 则性质就反过来了

#### Stopping time
回顾之前 stopping time 的定义

$$
\{T=n\}\in\mathcal{F}_n
$$

继续前面的下注策略, 另一种策略是每次下注一块钱
我们需要有一个时间停止, 这个时间就是一个 stopping time, 即

$$
H_n=\begin{cases}1 \quad \text{if }n\leq T \\ 0\quad \text{if } n\geq T+1\end{cases}
$$

则

$$
\{T\leq n-1\}=\bigcup_{k=1}^{n-1}\{T=k\}\in \mathcal{F}_{n-1}
$$

则

$$
W_n=W_0 +\sum_{k=1}^{n\land T}(M_k-M_{k-1})\quad a\land b=\min\{a,b\}
$$

若取 $W_0=M_0=0$ 即

$$
W_n=M_{n\land T}\quad \text{is a martingale}
$$

这件事也可以用 DTMC 的语言来描述

![[attachments/tikz/random-process-ch2-stopped-chain.png]]

这里可以把它想成“到达 $1$ 之后就停止”的 stopped chain, 因此 $1$ 是吸收态

上面的意思是对一个 martingale, 加上一个 stopping time , 仍然是 martingale

补充上面条件的一般证明:

记

$$
N_n=M_{n\land T}
$$

先说明 $N_n\in \mathcal{F}_n$ . 因为

$$
N_n=M_n\mathbf{1}_{\{T\ge n\}}+\sum_{k=0}^{n-1}M_k\mathbf{1}_{\{T=k\}}
$$

其中 $\{T\ge n\}\in\mathcal{F}_n$ , $\{T=k\}\in\mathcal{F}_k\subset \mathcal{F}_n$ , 所以整体对 $\mathcal{F}_n$ 可测

再看增量

$$
N_{n+1}-N_n=M_{(n+1)\land T}-M_{n\land T}=\mathbf{1}_{\{T\ge n+1\}}(M_{n+1}-M_n)
$$

于是

$$
\mathbb{E}(N_{n+1}-N_n\mid\mathcal{F}_n)=\mathbf{1}_{\{T\ge n+1\}}\mathbb{E}(M_{n+1}-M_n\mid\mathcal{F}_n)=0
$$

故

$$
\mathbb{E}(N_{n+1}\mid\mathcal{F}_n)=N_n
$$

这就证明了 $M_{n\land T}$ 仍然是 martingale

下一个问题是 $\mathbb{E}M_T$ 和 $\mathbb{E}M_0$ 的关系

考虑

$$
T=\min\{n\geq 0, M_n\in\{0,N\}\}
$$

则

$$
\mathbb{E}_kM_T =\mathbb{E}_kM_0=k
$$

或者

$$
T=\min\{n\geq 0, M_n=0\}
$$

则

$$
\mathbb{E}M_T=0\neq \mathbb{E}M_0
$$

### Optional stopping theorem
under certain conditions

$$
\mathbb{E}M_T=\mathbb{E}M_0
$$

在上面的反例中 $\mathbb{E}T=\infty$

并且 $R = \max_n M_{n\land T}$ , 有

$$
\{R\geq N\}=\{T_N<T_0\}
$$

其中

$$
T_N=\inf\{n\ge 0:M_n=N\},\qquad T_0=\inf\{n\ge 0:M_n=0\}
$$

对于简单对称随机游走, 若从 $k$ 出发, 则

$$
P_k(R\geq N)=P_k(T_N<T_0)=\frac{k}{N}
$$

则

$$
\mathbb{E}R=\sum_{N=1}^{\infty}P(R\ge N)=\infty
$$

具体的定理是

* $T$ is bounded , $P(T\leq k)=1$
* $|M_{n\land T}|\leq k$ bounded

证明是

$$
\mathbb{E}M_{n\land T}=\mathbb{E}M_{0\land T}=\mathbb{E}M_0
$$

故取 $n\geq k$ , 即

$$
\mathbb{E}M_T=\mathbb{E}M_0
$$

$$
\mathbb{E}M_{n\land T}=\mathbb{E}M_T \mathbf{1}_{T<n}+\mathbb{E}M_n \mathbf{1}_{T\geq n}
$$

对 $\mathbb{E}M_T$ 做相同的拆分, 在 $T<n$ 时两者相同, 但是 $T$ 有界

则 $|M_{n\land T}|<k \implies |M_T|<k$

则在测度意义下

$$
|\mathbb{E}M_{n\land T}-\mathbb{E}M_T|\leq 2k\quad P(T>n)\to0
$$

> 我们总是假设 $T<+\infty$

或者用另一个常见条件
* Bounded increments

$$
\mathbb{E}(|M_{n+1}-M_n|\mid\mathcal{F}_n)\leq k
$$

这需要使用 DCT

都会有

$$
\mathbb{E}M_T=\mathbb{E}M_0
$$

> 充要条件

> 补充: 若在第二个条件 $|M_{n\land T}|\le k$ 下, 可以更直接地写
>
> $$
> M_{n\land T}\to M_T\quad \text{a.s.}
> $$
>
> 且被常数 $k$ 支配, 所以由 DCT
>
> $$
> \mathbb{E}M_T=\lim_{n\to\infty}\mathbb{E}M_{n\land T}=\mathbb{E}M_0
> $$
>
> 如果再假设 increments 有界并且 $\mathbb{E}T<\infty$ , 也可以把
>
> $$
> M_{n\land T}=M_0+\sum_{j=0}^{n-1}(M_{j+1}-M_j)\mathbf{1}_{\{T\ge j+1\}}
> $$
>
> 展开后用 DCT 或绝对可和来证明同样的结论

#### Wald equation

$$
S_n=X_1+\cdots+X_n\quad \mathbb{E}|X_n|<+\infty\quad \mathbb{E}X_n=\mu
$$

则 $\mathbb{E}S_n=n\mu$

$T$ is a stopping time, $\mathbb{E}T<+\infty$ , 则

$$
\mathbb{E}S_T =\mu\mathbb{E}T
$$

证明是构造一个 martingale 用停时定理

$$
M_n=S_n-n\mu
$$

则若有

$$
\mathbb{E}M_T=\mathbb{E}M_0
$$

即完成证明

并且直接计算

$$
\mathbb{E}(M_{n+1}\mid\mathcal{F}_n)=\mathbb{E}(S_n+X_{n+1}-(n+1)\mu\mid\mathcal{F}_n)=S_n-n\mu=M_n
$$

同时

$$
M_{n+1}-M_n=X_{n+1}-\mu
$$

因此在前面的 OST 条件满足时, 就得到

$$
\mathbb{E}(S_T-\mu T)=\mathbb{E}M_T=\mathbb{E}M_0=0
$$

从而

$$
\mathbb{E}S_T=\mu \mathbb{E}T
$$

例子:

$$
S_{n}=S_0+X_1+\cdots X_n\quad T=\min \{n\geq0: X_n\in\{a,b\},X_n\notin (a,b)\}
$$

则 $S_{n\land T}\in [a,b]$ bounded

$$
X_n =\begin{cases}1 \\-1\end{cases}
$$

* $p=1/2$

$S_n$ is a martingale, 有 $\mathbb{E}_iS_T =\mathbb{E}_iS_0=i$ 则有

$$
\begin{align}aP_i(S_T=a)+bP_i(S_T=b)=i \\ P_i(S_T=a)+P_i(S_T=b)=1\end{align}
$$

即可求解出退出分布

解得

$$
P_i(S_T=b)=\frac{i-a}{b-a},\qquad P_i(S_T=a)=\frac{b-i}{b-a}
$$

* $p\neq 1/2$

则 $M_n=(q/p)^{S_n}$ is a martingale, $M_{n\land T}$ is bounded

OST $\mathbb{E}_iM_T=\mathbb{E}_iM_0=(q/p)^i$

从而计算出退出分布

即

$$
\left(\frac{q}{p}\right)^aP_i(S_T=a)+\left(\frac{q}{p}\right)^bP_i(S_T=b)=\left(\frac{q}{p}\right)^i
$$

联立

$$
P_i(S_T=a)+P_i(S_T=b)=1
$$

可得

$$
P_i(S_T=b)=\frac{1-(q/p)^{\,i-a}}{1-(q/p)^{\,b-a}},\qquad
P_i(S_T=a)=\frac{(q/p)^{\,i-a}-(q/p)^{\,b-a}}{1-(q/p)^{\,b-a}}
$$

类似的方法可以计算出 stopping time

类似的 $T=\min\{n\geq 0, X_n=0\}$

* $0<p < 1/2$  $S_n -n(p-q)$ is a martingale

若取区间退出时间的版本, 对 $p=\frac12$ 还可以用

$$
S_n^2-n
$$

也是 martingale, 从而

$$
\mathbb{E}_i(S_T^2-T)=i^2
$$

再代入上面的退出分布可以得到

$$
\mathbb{E}_iT=(i-a)(b-i)
$$

First step analysis

$$
f(i,n)=\sum_j p(i,j)f(j,n+1)
$$

则 $M_n =f(X_n,n)$ is a martingale

验证是

$$
\mathbb{E}(f(X_{n+1},n+1)\mid X_n=i)=\sum_j p(i,j)f(j,n+1)=f(i,n)
$$

因此

$$
\mathbb{E}(f(X_{n+1},n+1)\mid\mathcal{F}_n)=f(X_n,n)
$$

