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
N(0)=0,\qquad N(t)\in \mathbb{N},\qquad N(t)\ \text{non-decreasing and right continuous}
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

#### small interval characterization

Poisson process 也可以用小时间间隔描述. 当 $h\downarrow 0$ ,

$$
P(N(t+h)-N(t)=1)=\lambda h+o(h)
$$

$$
P(N(t+h)-N(t)\geq 2)=o(h)
$$

这说明在很短时间内发生一次的概率与长度成正比, 发生两次及以上是更小量.

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

#### superposition and thinning

两个常用构造:

* superposition: 若 $N_1,N_2$ 独立, 且 rates 分别为 $\lambda_1,\lambda_2$ , 则 $N_1+N_2$ 是 rate $\lambda_1+\lambda_2$ 的 Poisson process.
* thinning: 若对 rate $\lambda$ 的 Poisson process 中每个 arrival 独立保留, 保留概率为 $p$ , 则保留下来的过程是 rate $p\lambda$ 的 Poisson process; 删除的过程是 rate $(1-p)\lambda$ 的 Poisson process, 且二者独立.

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
