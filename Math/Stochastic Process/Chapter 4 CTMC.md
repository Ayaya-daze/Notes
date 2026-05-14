在处理连续 poisson process 时, 使用的技术即为考虑切分时间轴, 考虑每段区间发生概率

$$
p=p_n=\frac{\lambda}{n}
$$

这实际上可以用 DTMC 刻画, 则

$$
P(X_{t+1/n}=j|X_t=i)=
\begin{cases}
p\quad j=i+1\\
1-p\quad j=i\\
0\quad \text{else}
\end{cases}
$$

故有限步长时间发生概率

$$
P(T>t)=\left(1-\frac{\lambda}{n}\right)^{nt}\to e^{-\lambda t}
$$

![[attachments/tikz/random-process-ch4-poisson-ctmc.png]]

即 poisson process 实际上也是一种 CTMC

# Continuous time Markov Chain
这是前面 DTMC 的推广

> 首先考虑离散状态空间版本

首先要做的是定义连续版本的 markov property, 在连续时间上, 考虑采样点 $s_0< \cdots<s_n<s<t$ 有

$$
P(X_t=j|X_s=i,X_{s_0}=i_0,\cdots X_{s_n}=i_n)=P(X_t=j|X_s=i)
$$

> Poisson process 具有 markov property 是因为指数分布是 memoryless 的

则也可以考虑 Time - homogeneity

$$
P(X_{t+s}=j|X_s=i)=P(X_t=j|X_0=i)\quad\forall s,t
$$

这是后面讨论的重点, 同样也有 transition probability

$$
p_t(i,j)=P(X_t=j|X_0=i)
$$

类似地我们有 Chapman - Kolmogorov equation 
对于两步, 考虑采样 $r<s<t$ 

$$
P(X_t =j|X_r=i)=\sum_{k}P(X_t=j|X_s=k)P(X_s=k|X_r=i)
$$

或者矩阵形式

$$
P_{t-r}=P_{t-s}P_{s-r}
$$

#### transition rate
现在考虑无穷小时间 transition, 这是 1 - step transition 的连续版本

$$
(P_t)_{0\leq t\leq h}
$$

在 $h\to 0$ 下, 定义为

$$
q(i,j)=\lim_{h\to 0}\frac{P_h(i,j)}{h}\leftrightarrow P_h(i,j)=q(i,j)\cdot h+o(h)\quad i\neq j
$$

当然

$$
P_h(i,i)=1-\sum_{j\neq i}P_h(i,j)=1-\sum_{j\neq i}q(i,j)\cdot h+o(h)
$$

这里记 

$$
\sum_{j\neq i}q(i,j)=\lambda_i
$$


![[attachments/tikz/random-process-ch4-sample-path.png]]

CTMC 的 sample path 的图像即为, 一开始停留在某个状态一段时间, 然后跳跃到新的状态

例如

考虑 $X_t$ 停留在态 $i$ 的时间为 $T_i$ , 则

$$
T_i\sim\mathrm{Exp}(\lambda_i)
$$

考虑上面的停留时间求解 ODE 即可

现在再来考虑到其他态的概率,即当 $X_t$ 离开态 $i$ 时, $i$ 跳到 $j$ 的概率为 routing matrix

$$
r(i,j)=\frac{q(i,j)}{\lambda_i}
$$

因为对于 $i\neq j$ 

$$
P(X_{t+h}=j|X_t=i)=q(i,j)h+o(h)
$$

这也可以写为

$$
\begin{align}
&=P(X_t \text{ leaves } i \text{ during } (t,t+h]|X_t=i)\cdot P(X_{t+h}=j|X_t \text{ leaves } i \text{ during } (t,t+h],X_t=i)\\
&=(\lambda_i h+o(h))(r(i,j)+o(1))
\end{align}
$$

> 注意 routing matrix 的定义
> 另外线性近似表明 $r$ 不依赖于 $h$

取 $h\to 0$ , 有

$$
q(i,j)=\lambda_i\cdot r(i,j)
$$

这即为 CTMC 的 space - time decomposition

### Space - time structure

$$
\begin{align}
&\text{Time: holding time }T_i\sim\mathrm{Exp}(\lambda_i)\\
&\text{Space: DTMC with transition }r
\end{align}
$$

则 rate 也有 C - K equation 

$$
\frac{\mathrm{d}}{\mathrm{d} t}P_t = \lim_{h\to 0}\frac{P_{t+h}-P_t}{h}=\lim_{h\to 0}\frac{P_h-I}{h}P_t
$$

这得到

$$
P_{t+h}(i,j)=\sum_k P_h(i,k)P_t(k,j)=\sum_{k\neq i}(q(i,k)h+o(h))P_t(k,j) +(1-\lambda_i h+o(h))P_t(i,j)
$$

这样

$$
\frac{\mathrm{d}}{\mathrm{d}t}P_t=\lim_{h\to 0}\frac{P_{h+t}-P_t}{h}=-\lambda_i P_t(i,j)+\sum_{k\neq i} q(i,k)P_t(k,j)=(Q\cdot P_t)(i,j)
$$

这里

$$
Q(i,j)=
\begin{cases}
q(i,j) \quad j\neq i\\
-\lambda_i\quad j=i
\end{cases}
$$

对比得到

$$
Q=\lim_{h\to0}\frac{P_h-I}{h}
$$

此即

$$
\dot{P}_t=Q\cdot P_t\quad \text{Kolmogorov backward equation}
$$

一个例子是 poisson process

$$
P_t(i,j)=
\begin{cases}
e^{-\lambda t}\dfrac{(\lambda t)^{j-i}}{(j-i)!}\quad j\geq i\\
0\quad j<i
\end{cases}
$$

现在计算 $Q$ matrix

$$
Q =
\begin{bmatrix}
-\lambda & \lambda & 0 & 0 & 0 & \cdots \\
0 & -\lambda & \lambda & 0 & 0 & \cdots \\
0 & 0 & -\lambda & \lambda & 0 & \cdots \\
0 & 0 & 0 & -\lambda & \lambda & \cdots \\
0 & 0 & 0 & 0 & -\lambda & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$

现在分析这个 matrix 的含义

对角元 $-\lambda$ 为停留率, 而副对角元实际上为

$$
e^{-\lambda t}\frac{(\lambda t)^{j-i-1}}{(j-i-1)!}\lambda
$$

这可以看作 $i+1$ 到 $j$ 的概率

这种拆分是反向传播模式, 将 $h$ 取为起点时间, 另一种方式即为前向传播, 考虑 $h$ 为结尾时间

#### kolmogorov forward equation

$$
P_{t+h}(i,j)
=\sum_k P_t(i,k)P_h(k,j)
=\sum_{k\neq j}P_t(i,k)(q(k,j)h+o(h))+P_t(i,j)(1-\lambda_j h+o(h))
$$

同样矩阵形式

$$
\frac{\mathrm{d}}{\mathrm{d} t}P_t = \lim_{h\to 0}\frac{P_{t+h}-P_t}{h}=\lim_{h\to 0}P_t\frac{P_h-I}{h}=P_t Q
$$

在 poisson 的例子里

$$
\frac{\mathrm{d}}{\mathrm{d} t}p_t(i,j) =p_t(i,j)(-\lambda)+p_t(i,j-1)\lambda
$$

前向传播模式和后向传播模式的区别在于微分的端点, 即认为起点固定或者是终点固定

同样一个例子是考虑 双态系统

![[attachments/tikz/random-process-ch4-two-state.png]]

那么

$$
Q=
\begin{bmatrix}
-\lambda &\lambda\\
\mu &-\mu
\end{bmatrix}
$$

按照后向传播模式

$$
\dot{P}_t=QP_t
$$

这个方程的解是

$$
P_t=e^{tQ}
$$

Codex 补充：令 $a=\lambda+\mu$ . 这个 $Q$ 有两个特征值 $0$ 和 $-a$ , 因此矩阵指数可以写成稳态投影加上衰减项:

$$
e^{tQ}
=\frac{1}{\lambda+\mu}
\begin{bmatrix}
\mu+\lambda e^{-at} & \lambda(1-e^{-at})\\
\mu(1-e^{-at}) & \lambda+\mu e^{-at}
\end{bmatrix}
$$

也可以直接用第一行的方程看出. 设 $u(t)=p_t(1,1)$ , 则

$$
u'(t)=-\lambda u(t)+\mu(1-u(t))=\mu-a u(t)
$$

所以

$$
u(t)=\frac{\mu}{a}+\left(1-\frac{\mu}{a}\right)e^{-at}
$$

同理可以得到其他三个元素, 即上面的矩阵形式.

可以发现, 若 $Q$ 非退化, 当 $t\to \infty$ 时, 我们仍能看到极限行为

$$
p_t(\cdot,1)\to \frac{\mu}{\mu+\lambda}\quad p_t(\cdot,2)\to \frac{\lambda}{\mu +\lambda}
$$

### Limiting behavior
同样是问, 是否有

$$
p_t(i,j)\to \pi(j)\quad \forall i
$$

#### Necessary condition

$$
\pi(j)=\lim_{t\to \infty}P_{t+h}(i,j)=\lim_{t\to\infty}\sum_k P_t(i,k)P_h(k,j)=\sum_k \pi(k)P_h(k,j)
$$

同样, 即为

$$
\pi =\pi \cdot P_h\quad \forall h>0
$$

同样称为 stationary distribution

现在考虑无穷小时间步长

$$
0=\lim_{h\to 0}\frac{\pi P_h-\pi}{h}=\pi Q
$$

Conversely, 若 

$$
\pi Q=0
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t}(\pi P_t)=\pi \frac{\mathrm{d}}{\mathrm{d}t}P_t =\pi QP_t=0
$$

即 $\pi$ 是一个 stationary distribution

#### detailed balance

$$
\begin{align}
&\pi(i)q(i,j)=\pi(j)q(j,i)\\
\implies\quad
&\sum_{j\neq i}\pi(j)q(j,i)=\pi(i)\sum_{j\neq i}q(i,j)=\pi(i)(-q(i,i))\\
\implies\quad
&(\pi Q)(i)=0
\end{align}
$$

> 同样这不是 necessary 的, 考虑相同的环流解, 则不存在 detailed balance

同样的一些例子

birth - death process

$$
\begin{align}
&\text{Birth}\quad q(n,n+1)=\lambda_n \\ 
&\text{Death} \quad q(n,n-1)=\mu_n
\end{align}
$$

![[attachments/tikz/random-process-ch4-birth-death.png]]


计算平稳分布, 利用 detailed balance

$$
\begin{align}
&\pi(0)\lambda_0= \pi(1)\mu_1 \\
& \pi(1)(\lambda_1+\mu_1)=\pi(0)\lambda_0+\pi(2)\mu_2 \implies \pi(1)\lambda_1=\pi(2)\mu_2 \\
&\cdots \\
&\pi(k)\lambda_k =\pi(k+1)\mu_{k+1}
\end{align}
$$

最后

$$
\pi(k+1)=\frac{\lambda_k}{\mu_{k+1}}\pi(k)=\cdots=\frac{\lambda_k\cdots\lambda_0}{\mu_{k+1}\cdots\mu_1}\pi(0)
$$

归一化

$$
1=\sum_k\frac{\lambda_{k-1}\cdots\lambda_0}{\mu_k\cdots \mu_1}\pi(0)=S\pi(0)
$$

若 $S<+\infty$ , 存在平稳分布 $\pi(0)=1/S$

### Irreducible
同样定义

$$
\forall i,j\in S\quad\exists \text{ finite } t \quad \mathrm{s.t.}\quad P(X_t=j|X_0=i)>0
$$

按照 C - K 方程, 这表明可以找到一条状态 path 从 $i$ 到 $j$ , 即

$$
\exists i=k_0,k_1,\cdots,k_{m-1},k_m=j\quad q(k_{l},k_{l+1})>0\quad P_h(k_l,k_{l+1})=q(k_l,k_{l+1})h+o(h)
$$

那么

$$
P_{mh}(i,j)\geq \prod_l P_h(k_l,k_{l+1})>0
$$

并且

$$
P_{mh+t}(i,j)\geq P_{mh}(i,j)P_t(j,j)>0
$$

不过问题是在这里没有周期的概念, 不过上面的结果表明, 如果 chain 是不可约的, 自动有类似周期的条件

### Theorem
CTMC $X_t$ , irreducible $(I)$ , $\exists$ stationary $(S)$ , 则

$$
\lim_{t\to\infty}P_t(i,j)=\pi(j)
$$

证明和前面是相同的. 固定一个足够小的 $h>0$ , 看 sampled chain $(X_{nh})_{n\geq 0}$ . 对 CTMC 来说 $P_h(i,i)>0$ , 所以这个 sampled chain 没有离散时间中的周期障碍；并且 $\pi P_h=\pi$ .

考虑 $nh\leq t <(n+1)h$ , 则

$$
P_t(i,j)\geq P_{nh}(i,j)P_{t-nh}(j,j)\geq P_{nh}(i,j)\exp(-\lambda_jh)
$$

因此先令 $t\to \infty$ , 也就是 $n\to\infty$ , 得到

$$
\liminf_{t\to\infty}P_t(i,j)\geq \pi(j)e^{-\lambda_jh}
$$

再令 $h\downarrow 0$ , 得到

$$
\liminf_{t\to\infty}P_t(i,j)\geq \pi(j)
$$

取 $A\subseteq S-\{j\}$  且是 finite 的

$$
P_t(i,j)\leq 1-\sum_{k\in A}P_t(i,k)
$$

从而

$$
\limsup_{t\to\infty}P_t(i,j)\leq 1-\sum_{k\in A}\pi(k)
$$

最后取一列有限集合 $A\uparrow S-\{j\}$ , 右侧单调收敛到

$$
1-\sum_{k\neq j}\pi(k)=\pi(j)
$$

于是

$$
\limsup_{t\to\infty}P_t(i,j)\leq \pi(j)\leq \liminf_{t\to\infty}P_t(i,j)
$$

所以极限存在且等于 $\pi(j)$ .
