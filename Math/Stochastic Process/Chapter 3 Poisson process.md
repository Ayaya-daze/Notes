# Poisson process

连续时间随机过程的想法是从离散时间推广.

考虑一个 DTMC 形式的计数过程

$$
X_n = X_0+Z_1+\cdots+Z_n,\qquad
Z_i=\begin{cases}
1 \quad p\\
0 \quad 1-p
\end{cases}
$$

这是一个经典的计数过程 counting process.

#### counting process

$$
N(0)=0,\qquad N(t)\in \mathbb{N}_0,\qquad N(t)\ \text{non-decreasing and right continuous}
$$

到达时间 arrival time $T_i$ , inter-event time $\tau_i=T_i-T_{i-1}$ , 其中 $T_0=0$ .

可以进一步对时间轴做切分, 比如在单位时间内考虑 $N$ 个小 bin. 若 $tN$ 不是整数, 可以取 $\lfloor tN\rfloor$ :

$$
X_t^N=Z_1^N+\cdots+Z_{\lfloor tN\rfloor}^N
$$

其中

$$
Z_i^N\sim \mathrm{Bernoulli}(p_N)
$$

且令

$$
\mathbb{E}(X_1^N)=Np_N=\lambda,\qquad p_N=\frac{\lambda}{N}
$$

当考虑 $N\to\infty$ 的极限时, 这称为一个 Poisson process.

### Poisson process

先看单点分布

$$
X_t^N \sim \mathrm{Binom}\left(\lfloor tN\rfloor,\frac{\lambda}{N}\right)\to \mathrm{Poisson}(\lambda t)
$$

同样考虑

$$
X_t^N-X_s^N \sim \mathrm{Binom}\left(\lfloor tN\rfloor-\lfloor sN\rfloor,\frac{\lambda}{N}\right)\to \mathrm{Poisson}(\lambda(t-s))\quad t\geq s
$$

并且在两个不相交的时间段上发生的事件是独立的.

#### define

$(N(t),t\geq 0)$ is a Poisson process with rate $\lambda$ if

* $N(t)$ is a counting process ($N(0)=0$)
* $N(t)-N(s)\sim \mathrm{Poisson}(\lambda(t-s))$ for $t\geq s$
* $N(t)$ has independent increments

更多性质:

$$
\mu_N(t)=\mathbb{E}N(t)=\lambda t
$$

若 $s\leq t$ , 则 $N(t)=N(s)+[N(t)-N(s)]$ , 且增量独立, 因此

$$
C_N(s,t)=\mathrm{Cov}(N(s),N(t))=\mathrm{Var}(N(s))=\lambda s=\lambda(s\land t)
$$

joint pmf: 若 $s\leq t$ 且 $i\leq j$ , 则

$$
P(N(s)=i,N(t)=j)=P(N(s)=i)P(N(t)-N(s)=j-i)
$$

即

$$
P(N(s)=i,N(t)=j)=e^{-\lambda t}\frac{(\lambda s)^i}{i!}\frac{(\lambda(t-s))^{j-i}}{(j-i)!}
$$

更一般地, 对 $0=t_0<t_1<\cdots<t_m$ , 有

$$
P(N(t_1)=n_1,\cdots,N(t_m)=n_m)
=\prod_{k=1}^m e^{-\lambda(t_k-t_{k-1})}
\frac{(\lambda(t_k-t_{k-1}))^{n_k-n_{k-1}}}{(n_k-n_{k-1})!}
$$

其中 $0=n_0\leq n_1\leq\cdots\leq n_m$ . 这说明有限维分布完全由独立增量给出.

从单点分布还可以得到 probability generating function:

$$
\mathbb{E}z^{N(t)}=\exp(\lambda t(z-1))
$$

因此 moment generating function 为

$$
\mathbb{E}e^{\theta N(t)}=\exp(\lambda t(e^\theta-1))
$$

这在计算随机和、thinning 和 compound Poisson process 时很方便.

#### small interval characterization

Poisson process 也可以用小时间间隔描述. 当 $h\downarrow 0$ ,

$$
P(N(t+h)-N(t)=1)=\lambda h+o(h)
$$

$$
P(N(t+h)-N(t)\geq 2)=o(h)
$$

因此也有

$$
P(N(t+h)-N(t)=0)=1-\lambda h+o(h)
$$

这说明在很短时间内发生一次的概率与长度成正比, 发生两次及以上是更小量. 若一个 counting process 有独立增量, 并且满足这些小区间条件, 则可以推出它是 rate $\lambda$ 的 Poisson process. 这个刻画常用来从 infinitesimal transition rate 出发定义连续时间过程.

#### arrival time

首先

$$
\{T_1>t\}=\{N(t)=0\}
$$

即

$$
P(T_1>t)= e^{-\lambda t}\implies T_1 \sim \mathrm{Exp}(\lambda)
$$

> 独立增量表明后面的到达时间间隔都是独立同分布的指数形式:
>
> $$
> \tau_i=T_i-T_{i-1}\overset{\text{i.i.d.}}{\sim}\mathrm{Exp}(\lambda)
> $$

同样

$$
\{T_k>t\}=\{N(t)\leq k-1\}
$$

即

$$
P(T_k>t)=\sum_{i=0}^{k-1}e^{-\lambda t}\frac{(\lambda t)^i}{i!}
$$

从而 pdf

$$
f_{T_k}(t)=-\frac{\mathrm{d}}{\mathrm{d} t} P(T_k> t)=\lambda e^{-\lambda t}\frac{(\lambda t)^{k-1}}{(k-1)!},\qquad t>0
$$

也就是说

$$
T_k=\tau_1+\cdots+\tau_k\sim \mathrm{Gamma}(k,\lambda)
$$

这里第二个参数采用 rate 记号.

也可以得到 joint pdf of $(T_1,\cdots,T_n)$ , 做法是划分然后用独立增量. 对 $0<t_1<\cdots<t_n$ , 取足够小的 $\epsilon$ ,

$$
P(T_i \in(t_i-\epsilon,t_i]\ \forall i)=e^{-\lambda t_n}(\lambda \epsilon)^n+o(\epsilon^n)
$$

从而 pdf

$$
f_{T_1,\cdots,T_n}(t_1,\cdots,t_n)=\lambda^n e^{-\lambda t_n}\mathbf{1}_{0<t_1<\cdots<t_n}
$$

做微分同胚 $(T_1,\cdots,T_n)\to (\tau_1,\cdots,\tau_n)$ , 其中 $t_k=\tau_1+\cdots+\tau_k$ , Jacobian 为 $1$ , 即可得到

$$
f_{\tau_1,\cdots,\tau_n}(u_1,\cdots,u_n)=\lambda^n e^{-\lambda(u_1+\cdots+u_n)}\mathbf{1}_{u_i>0}
$$

这正好分解成 $n$ 个 $\mathrm{Exp}(\lambda)$ 密度的乘积.

#### conditional arrival times

给定 $N(t)=n$ 时, 这 $n$ 个到达时间在 $[0,t]$ 上的条件分布等价于 $n$ 个 i.i.d. $\mathrm{Unif}(0,t)$ 排序后的 order statistics. 因此

$$
f_{T_1,\cdots,T_n\mid N(t)=n}(t_1,\cdots,t_n)=\frac{n!}{t^n}\mathbf{1}_{0<t_1<\cdots<t_n<t}
$$

这个性质和独立增量是等价地刻画 Poisson process 的方式之一.
更准确地说, 它通常需要和 $N(t)\sim \mathrm{Poisson}(\lambda t)$ 这样的边缘分布条件一起使用, 才能完整刻画 Poisson process.

当然另一种方式是直接按照 conditional probability 计算, 因为我们已经获得了联合分布

$$\{T_1=t_1,\cdots ,T_n=t_n, N(t)=n \}=\{\tau_1=t_1,\cdots,\tau_n=t_{n}-t_{n-1},\tau_{n+1}>t-t_n\}$$

即

$$(\lambda e^{-\lambda t_1})\cdots (\lambda e^{-\lambda(t_{n}-t_{n-1})})e^{-\lambda (t-t_{n})}=\lambda^n e^{-\lambda t}$$

于是

$$f_{T_1,\cdots,T_n\mid N(t)=n}(t_1,\cdots,t_n)=\frac{\lambda^n e^{-\lambda t}}{(\lambda t)^n e^{-\lambda t}/n!}=\frac{n!}{t^n}$$

>可以计算条件概率
>
>$$P(N(s)=m|N(t)=n)\quad s<t,m\leq n$$
>
>直接的做法是用条件概率展开, 分析中间的独立增量, 上面已经给出了在条件概率下, 独立
>增量是均匀分布的 order statistics, 所以这里就相当于一个二项分布的过程, 按照概率 $s/t$ 给每个独立增量分配位置
>这个结果和发生速率无关

特别地, 对 $0<s<t$ ,

$$
N(s)\mid N(t)=n\sim \mathrm{Binom}\left(n,\frac{s}{t}\right)
$$

更一般地, 若把 $[0,t]$ 划分为不相交的小段 $A_1,\cdots,A_m$ , 长度为 $|A_i|$ , 则给定 $N(t)=n$ 后有 multinomial 分布:

$$
P(N(A_1)=n_1,\cdots,N(A_m)=n_m\mid N(t)=n)
=\frac{n!}{n_1!\cdots n_m!}\prod_{i=1}^m\left(\frac{|A_i|}{t}\right)^{n_i}
$$

这里 $\sum_i n_i=n$ . 这正是 "给定总点数后, 点在区间内均匀撒开" 的离散版本.

#### Markov property and generator

把 $N(t)$ 看成状态空间为 $\mathbb{N}_0$ 的连续时间 Markov chain, 则对 $h\geq 0$ ,

$$
P(N(t+h)=j\mid N(t)=i)=
\begin{cases}
e^{-\lambda h}\dfrac{(\lambda h)^{j-i}}{(j-i)!},\quad j\geq i\\
0,\quad j<i
\end{cases}
$$

即从状态 $i$ 出发只能向上跳, 且跳的次数服从 $\mathrm{Poisson}(\lambda h)$ . 它的生成元 $Q=(q_{ij})$ 为

$$
q_{i,i+1}=\lambda,\qquad q_{i,i}=-\lambda,\qquad q_{ij}=0\quad \text{otherwise}
$$

从生成元看, 过程在每个状态以 rate $\lambda$ 等待, 然后跳到下一个状态. 这和 inter-event time $\tau_i\sim\mathrm{Exp}(\lambda)$ 是同一个事实.

对应的 transition semigroup 为

$$
p_t(i,j)=P(N(t)=j\mid N(0)=i)
=\mathbf{1}_{j\geq i}e^{-\lambda t}\frac{(\lambda t)^{j-i}}{(j-i)!}
$$

它满足 Kolmogorov forward equation

$$
\frac{\mathrm{d}}{\mathrm{d}t}p_t(i,j)
=\lambda p_t(i,j-1)-\lambda p_t(i,j)
$$

这里约定 $p_t(i,j)=0$ if $j<i$ . backward equation 则是

$$
\frac{\mathrm{d}}{\mathrm{d}t}p_t(i,j)
=\lambda p_t(i+1,j)-\lambda p_t(i,j)
$$

#### superposition and thinning

##### superposition
若 $N_i$ 独立, 且 rates 为 $\lambda_i$ , 则 $N=N_1+\cdots+N_n$ 是 rate $\lambda_1+\cdots+\lambda_n$ 的 Poisson process.

验证:
这是一个 counting process, 再考虑 $s<t$ 的计数分布 $N(t)-N(s)= \sum_i N_i(t)-N_i(s)$ , 这是一堆独立分布的和
对于独立增量性质, 考虑 $t_1<t_2<\cdots<t_n$ , $N(t_i)-N(t_{i-1})=\sum_j N_j(t_i)-N_j(t_{i-1})$
都是一些独立分布的和, 且都满足独立增量, 故它们也是相互独立的

##### thinning
对 $N$ , 对事件 $Y_i=j \quad \mathrm{w.p.} \quad p_j$ , 那么 $N_j(t)=\sum_{i=1}^{N(t)}\mathbf{1}_{Y_i=j}$ , 则 $N_j$ 是相互独立的 poisson process with rate $\lambda p_j$

性质的验证也是简单的, 记 $N_i(s+t)-N_i(s)=X_i$ 那么

$$P(X_1=j, X_2=k)=P(N(t+s)-N(s)=j+k,\sum_{i=1}^{j+k}\mathbf{1}_{Y_i=1}=j)=e^{-\lambda t}\frac{(\lambda t)^{j+k}}{(j+k)!}\binom{j+k}{j}p_1^j p_2^k$$

可以拆分为独立乘积

另一个更快的验证是用生成函数. 对 superposition,

$$
\mathbb{E}z^{N_1(t)+N_2(t)}
=\exp(\lambda_1t(z-1))\exp(\lambda_2t(z-1))
=\exp((\lambda_1+\lambda_2)t(z-1))
$$

对 thinning, 若保留下来的计数记为 $N_p(t)$ , 则

$$
N_p(t)\mid N(t)=n\sim \mathrm{Binom}(n,p)
$$

于是

$$
\mathbb{E}z^{N_p(t)}
=\mathbb{E}\left[(1-p+pz)^{N(t)}\right]
=\exp(\lambda t p(z-1))
$$

若删除的过程记为 $N_{1-p}(t)$ , 联合生成函数为

$$
\mathbb{E}u^{N_p(t)}v^{N_{1-p}(t)}
=\exp(\lambda t(pu+(1-p)v-1))
=\exp(p\lambda t(u-1))\exp((1-p)\lambda t(v-1))
$$

所以保留和删除两个过程不仅边缘上是 Poisson process, 而且相互独立.

#### compensated Poisson martingale

Poisson process 本身不是 martingale, 因为

$$
\mathbb{E}(N(t)\mid\mathcal{F}_s)=N(s)+\lambda(t-s),\qquad s\leq t
$$

但补偿以后

$$
M(t)=N(t)-\lambda t
$$

是一个 martingale:

$$
\mathbb{E}(M(t)\mid\mathcal{F}_s)=N(s)+\lambda(t-s)-\lambda t=N(s)-\lambda s=M(s)
$$

进一步, 因为 jump size 都是 $1$ , martingale 的 quadratic variation 为

$$
[M](t)=\sum_{0<u\leq t}(\Delta M(u))^2=N(t)
$$

predictable quadratic variation 为

$$
\langle M\rangle(t)=\lambda t
$$

于是

$$
M(t)^2-\lambda t
$$

也是 martingale. 这可以直接从条件方差看出:

$$
\mathrm{Var}(N(t)-N(s)\mid\mathcal{F}_s)=\lambda(t-s)
$$

更一般地, 指数补偿后也可以得到 martingale:

$$
\exp\left(\theta N(t)-\lambda t(e^\theta-1)\right)
$$

其中 $\theta$ 取使期望有限的实数. 这个公式和前面的 mgf 是同一个结构.

### simulate Poisson process
最简单的做法是直接生成时间间隔 $\tau_i \sim \mathrm{Exp}(\lambda)$ , 然后得到 arrival time $T_i$
然后增量都发生在 arrival time

$$
N(s)=\max\{n:T_n \leq s\}
$$

这满足 poisson 的要求

>重要的一点是利用分布的无记忆性

具体算法可以写成:

1. 生成 $\tau_1,\tau_2,\cdots\overset{\text{i.i.d.}}{\sim}\mathrm{Exp}(\lambda)$
2. 令 $T_n=\tau_1+\cdots+\tau_n$
3. 对每个 $t$ , 取 $N(t)=\max\{n:T_n\leq t\}$

如果只需要在固定时间 $t$ 模拟 $N(t)$ , 也可以直接抽

$$
N(t)\sim \mathrm{Poisson}(\lambda t)
$$

但如果需要整条 sample path, 用 arrival times 更自然.

前面只考虑了时齐的 poisson process, 现在考虑 non - homogeneous 版本

### Non - homogeneous poisson process
同样, 这也应该满足 poisson process 的性质. 这里至少要求 $\lambda(t)\geq 0$ 且在有限区间上可积.

1. counting process $N(0)=0$
2. Independent increments
3. $N(t)-N(s)=\mathrm{Poisson}(\int_s^t \lambda(u)\mathrm{d}u)$

若记

$$
\Lambda(t)=\int_0^t\lambda(u)\,\mathrm{d}u
$$

则 $N(t)-N(s)\sim\mathrm{Poisson}(\Lambda(t)-\Lambda(s))$ . 如果 $\Lambda$ 严格递增, 经过 time change 后 $\Lambda(T_i)$ 是 rate $1$ 的齐次 Poisson process 的到达时间.

小区间刻画对应为

$$
P(N(t+h)-N(t)=1)=\lambda(t)h+o(h)
$$

以及

$$
P(N(t+h)-N(t)\geq 2)=o(h)
$$

这时不再有 stationary increments, 因为增量分布不仅取决于区间长度, 还取决于区间所在的位置.


>poisson regression
>更一般地考虑带参强度
>$$\log \lambda(t,x)=\beta_{t,0}+\beta_{t,1}^T\mathrm{x}$$
>
>然后考虑对这种强度进行 regression

### Poisson approximation
考虑

$$
\sum_{i=1}^n \mathrm{Bern}(\lambda(t_i)\cdot \varepsilon)
\simeq \mathrm{Poi}\left(\sum_{i=1}^n \lambda (t_i)\varepsilon\right)
\simeq \mathrm{Poi}\left(\int_s^t \lambda(u)\mathrm{d}u\right)
$$

这里的直觉是: 很多小概率、近似独立的事件相加会趋近 Poisson 分布. 若每个小 bin 的概率是 $p_i$ , 且 $\max_i p_i\to 0$ , $\sum_i p_i\to \mu$ , 则

$$
\sum_i \mathrm{Bern}(p_i)\Rightarrow \mathrm{Poisson}(\mu)
$$

#### arrival time

$$
\{T_1>t\}=\{N(t)=0\},\qquad N(t)\sim \mathrm{Poisson}\left(\int_0^t \lambda(u)\mathrm{d}u\right)
$$

则

$$
P(T_1>t)=\exp\left(-\int_0^t\lambda(u)\mathrm{d}u\right),
\qquad f_{T_1}(t)=\lambda(t)\exp(-\mu(t))
$$

这里

$$
\mu(t)=\int_0^t\lambda(u)\mathrm{d}u
$$

#### Inter - event time
事件之间发生的等待时间不是独立的, 因为现在强度是含时的

$$
P(\tau_2>t\mid \tau_1=s)
=P\left(\mathrm{Poi}\left(\int_s^{s+t}\lambda(u)\mathrm{d}u\right)=0\right)
=\exp\left(-\int_s^{s+t}\lambda(u)\mathrm{d}u\right)
$$

$\tau_1,\tau_2$ dependent , non - identical

给定 $N(t)=n$ 时, unordered arrival times 不再是 uniform, 而是具有密度

$$
f(u)=\frac{\lambda(u)}{\Lambda(t)},\qquad 0<u<t
$$

因此 ordered arrival times 的条件 joint density 为

$$
f_{T_1,\cdots,T_n\mid N(t)=n}(t_1,\cdots,t_n)
=n!\prod_{i=1}^n\frac{\lambda(t_i)}{\Lambda(t)}
\mathbf{1}_{0<t_1<\cdots<t_n<t}
$$

### Compound poisson process
实际上, poisson 过程的事件发生应该对背后的系统有影响

考虑每个事件的影响 $Y_i$ , 先考虑 i.i.d.

$$
S(t)=Y_1+Y_2+\cdots +Y_{N(t)}
$$

那么

$$
\mathbb{E}(S(t)\mid N(t)=n)=\mathbb{E}(Y_1+\cdots +Y_n)=n \mathbb{E}Y
$$

那么

$$
\mathbb{E}(S(t))=\mathbb{E}N(t)\cdot \mathbb{E}Y=\lambda t \mathbb{E}Y
$$

二阶矩也是相同的

$$
\mathbb{E}[S^2(t)\mid N(t)=n]
=\mathbb{E}(Y_1+\cdots+Y_n)^2
=(n\mathbb{E}Y)^2+n \mathrm{Var}Y
$$

从而

$$
\mathbb{E}S^2(t)=\mathbb{E}N^2(t)(\mathbb{E}Y)^2+\mathbb{E}N(t)\cdot \mathrm{Var}Y
$$

最后计算 variance

$$
\mathrm{Var}(S(t))=\mathrm{Var}(N(t))(\mathbb{E}Y)^2+\mathbb{E} N(t)\mathrm{Var}Y=\lambda t \mathbb{E}(Y^2)
$$

前一步对一般的 counting process 都是适用的; 最后一步使用了 Poisson process 的 $\mathbb{E}N(t)=\mathrm{Var}(N(t))=\lambda t$ .

同样可以补偿成 martingale:

$$
S(t)-\lambda t\,\mathbb{E}Y
$$

是 martingale, 这里默认 $Y_i$ 与 $N(t)$ 独立且一阶矩存在.

compound Poisson process 的分布通常不用直接写 pmf, 而是用 transform 描述. 若 $Y_1$ 的 mgf 存在, 则

$$
\mathbb{E}e^{\theta S(t)}
=\mathbb{E}\left[(\mathbb{E}e^{\theta Y_1})^{N(t)}\right]
=\exp\left(\lambda t(\mathbb{E}e^{\theta Y_1}-1)\right)
$$

同样, characteristic function 为

$$
\mathbb{E}e^{iuS(t)}
=\exp\left(\lambda t(\mathbb{E}e^{iuY_1}-1)\right)
$$

从独立增量看, $S(t)-S(s)$ 只由 $(s,t]$ 内的 arrivals 和 jump sizes 决定, 因而 compound Poisson process 仍有 independent increments. 若 $Y_i\geq 0$ , 它也是一个 non-decreasing process; 若 $Y_i$ 可正可负, 它就是一个带有限活动 jumps 的纯跳过程.

对 $\tau_i$ 的分布的无记忆性的推广, 即为 renewal process

### Renewal process
即等待时间满足

1. $\tau_1,\tau_2,\cdots\overset{\text{i.i.d.}}{\sim} F$  且 $F(0)=0$
2. $T_n=\tau_1+\tau_2+\cdots +\tau_n$
3. $N(t)=\max\{n: T_n\leq t\}$

当 $F$ 是指数分布时, 回到 poisson process

和 Poisson process 不同, 一般 renewal process 的 increments 不独立, 也通常不是 Markov process. 原因是未来的等待时间分布会依赖当前时刻在一个 renewal interval 中已经等待了多久, 即所谓 age 或 residual lifetime.

#### renewal rate
考虑平均发生次数, 则满足

$$
\frac{N(t)}{t}\quad \lim_{t\to \infty}\frac{N(t)}{t}=\frac{1}{\mathbb{E}\tau_1}
$$

这个结果一样来自 SLLN

$$
\frac{T_n}{n}=\frac{\tau_1+\cdots+\tau_n}{n}\overset{\mathrm{a.s.}}{\to} \mathbb{E}\tau
$$

从而

$$
T_{N(t)}\leq t<T_{N(t)+1}
$$

同样夹逼得到结果:

$$
\frac{T_{N(t)}}{N(t)}\leq \frac{t}{N(t)}<\frac{T_{N(t)+1}}{N(t)}
$$

左右两边都趋向 $\mathbb{E}\tau_1$ , 因而 $N(t)/t\to 1/\mathbb{E}\tau_1$ .

#### renewal reward process
和前面的想法几乎相同, 在每个事件发生时, 都有 reward $r_i$ , pair $(r_i,\tau_i)$ 是 i.i.d. 的

$$
R(t)=r_1+\cdots+r_{N(t)}
$$

同样有 reward rate, 看长期的收益率

$$
\frac{R(t)}{t}
$$

则也有

$$
\frac{R(t)}{t}\overset{\mathrm{a.s.}}{\to} \frac{\mathbb{E}r_1}{\mathbb{E}\tau_1}
$$

同样是使用 SLLN

$$
\frac{R(t)}{t}=\frac{N(t)}{t}\frac{1}{N(t)}\sum_{i=1}^{N(t)}r_i
$$

这里要求 $\mathbb{E}|r_1|<\infty$ 和 $\mathbb{E}\tau_1<\infty$ . 若 $r_i$ 和 $\tau_i$ 不独立也没关系, 只要 pair $(r_i,\tau_i)$ 是 i.i.d. 即可.


>前面的 renewal rate 可以看作一个特殊的 reward rate

另一个例子是 alternating renewal process

考虑每次发生事件会改变系统的状态, 如: 可用/不可用

那么

$$
\tau_i=s_i+u_i\quad r_i=s_i
$$

从而

$$
\frac{R(t)}{t}\to \frac{\mathbb{E}s_i}{\mathbb{E}(s_i+u_i)}=\frac{\mu_F}{\mu_F+\mu_G}
$$

还有一些排队系统的建模
