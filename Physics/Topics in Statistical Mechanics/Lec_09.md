上次提到两个弛豫时间近似

问题在于 $\delta f$ 的 ambiguity

在 relaxation time approximation 中写

$$
\text{collision}=-\frac{\delta f}{\tau},\qquad
\delta f=f-f_{\text{leq}}
$$

但 $f_{\text{leq}}$ 本身由局域的热力学参数决定. 如果改变 $\mu(x),\beta(x),u(x)$ 等参数, 一部分原来放在 $\delta f$ 里的变化就可以被吸收到 $f_{\text{leq}}$ 中. 因此需要额外的条件来固定这个分解.

通常的做法是要求 $\delta f$ 不携带 collision conserved quantities:

$$
\int_p Q\,\delta f=0
$$

这和 relaxation time approximation 的一致性有关. 如果 $Q$ 是真实 collision invariant, 则精确的碰撞项应满足

$$
\int_p Q\,(\text{collision})=0
$$

代入 $-\delta f/\tau$ 后就得到上面的约束. 但是这里有一个细节: 这些守恒量是实空间局域的守恒量, 不是相空间里唯一确定的局域 current.

$$
0=\partial_\mu J^\mu
=\partial_t\int_p f+\partial_x\int_p \dot{x}_{\text{EoM}} f
=\int_p(\text{collision})
$$

但是这个积分里面可以相差一个 $p$ 的全导数

对于单个 particle, 有 Noether Theorem

$$
\frac{\mathrm{d}Q}{\mathrm{d}t}=0
$$

也就是沿着相空间轨道

$$
\partial_t Q+\dot{\xi}^{I}\partial_I Q=0
$$

同时有连续性方程

$$
\partial_t\rho+\partial_I(\dot{\xi}^{I}\rho)=0
$$

这不依赖于运动方程

得到

$$
\partial_t(Q\rho)+\partial_I(\dot{\xi}^{I}Q\rho)=0
$$

这里 $\rho$ 是相空间中的密度. 这个式子看起来像一个相空间连续性方程, 但真正进入 Boltzmann 守恒律的是对动量积分后的量.

对动量积分后, $p$ 方向的全导数不贡献, 因而得到实空间的守恒形式

$$
\partial_t\int_p Q\rho+\partial_i\int_p \dot{x}^{i}Q\rho=0
$$

虽然没有直接的相空间守恒流, 但对动量积分后的量有守恒方程

即没有一个相空间的 current , 只有一个定义在实空间的类似 current 的量

> 可以发现在 locality 一般只在实空间中出现

所以在使用 RTA 时, 约束 $\delta f$ 的对象应该是 collision 真正保持的 $Q$. 对于没有杂质、只靠粒子间碰撞的情形, 通常有粒子数、能量、动量守恒; 但对于杂质导致的 1 - 1 scattering, 动量可以交给背景, 不是电子气自身的 conserved quantity.

因此这种 local equilibrium 中没有 conserved 的 momentum

$$
f_{\text{leq}}=\frac{1}{e^{\beta(H-\mu)}\mp1}
$$

考虑 1 - 1 scattering

$$
(\text{collision})_1
=\int_{p_2}\left(W_{2\to 1}f_2-W_{1\to 2}f_1\right)
$$

这里的 $1,2$ 标记的是同一条能带上的不同动量态. 对杂质散射来说, 背景破坏平移对称性, 所以 $p_1$ 和 $p_2$ 不必相等; 但如果杂质是静态的, 散射仍保持单粒子的能量.

而

$$
\int_{p_1}\epsilon^1_1(\text{above})=0
$$

这是因为碰撞概率

$$
W_{1\to2},W_{2\to 1}\propto \delta(\epsilon_1^1-\epsilon_2^1)
$$

类似地, 粒子数也守恒:

$$
\int_{p_1}(\text{above})=0
$$

但一般没有

$$
\int_{p_1}p_1^i(\text{above})=0
$$

因为杂质或晶格可以吸收动量. 这就是为什么这里的 $f_{\text{leq}}$ 只有 $\beta,\mu$ 这类参数, 而没有流速项 $u^ap_a$.

我们希望将 collision 用 relaxation time 替换后, 保持 collision 的性质

因此 RTA 不能任意写成 $-\Delta f/\tau$, 而要写成对 $f_{\text{leq}}$ 的偏离, 并且配合

$$
\int_p Q\,\delta f=0
$$

来保持相应的 collision invariant. 对杂质 1 - 1 scattering, $Q$ 至少包括粒子数和能量, 但不包括动量.

上次提到的两个 region [[Lec_08]]

$$
1/\tau \ll \partial_t ,v\partial_x \quad \text{ballistic}
$$

$$
1/\tau \gg \partial_t ,v\partial_x\quad \text{hydrodynamics}
$$

并且在每种情况, 右侧的两个量之间的比较也很重要

继续上次电导率的例子

$$
\sigma^{ij}
=\tau q^2\int_p \partial_{p_i}H \partial_{p_j}H(-\partial_H f_{\text{geq}})
$$

> 对于旋转对称的系统
>
> $$
p_ip_j \propto \frac{p^2}{d} \delta_{ij}
> $$
>

简单的计算得出

$$
\sigma^{ij}
=\frac{nq^2\tau}{m}\delta^{ij}
$$

这样的流会给出能量 $\mathbf{J}\cdot \mathbf{E}$ , 温度会升高, 故不存在一个稳定的状态 $\partial_t =0$ 不成立

Linear response result can be totally different from the actual solution

> 但是实际上的计算中揭示出这个计算和电导率的结果符合很好
> 一个原因是发热是高阶量 $\sim E^2$
> 另一个原因是存在环境的耦合

> 实际上, 我们在 Boltzmann 方程的 set up 中, 并没有考虑环境的自由度
> 但在使用 linear response 中, 需要 coupling with environment 的结果才能得到真实解的结果
> Anton Kapustin (2024) 有过类似的讨论

如果我们仍然要求, 在环境的 coupling 下有

$$
\partial_t f=0
$$

但我们让 local equilibrium 有坐标的依赖, $\mu(x)$

$$
\frac{p}{m}\partial_x f_{\text{leq}}
+qE\cdot \frac{p}{m}\partial_{\epsilon} f_{\text{eq}}
=-\frac{\delta f}{\tau}
$$

得到 (替换 1 阶项的系数为 $f_{\text{eq}}$)

$$
\frac{p}{m}\cdot (\partial_x\mu-qE)
$$

出现了可以 factor out 的部分

> 这是必然的吗?
> 是也不是(

首先看看这是 factor 的含义, 当 $\partial_t =0$ 时, 可以取 Coulomb gauge

$$
\partial_x(\mu+q\phi)
$$

得到电化学势 $\mu +q\phi$ 

在这种情况下得到的电流

$$
J^i=\sigma^{ij}(E_j-\partial_j\mu/q)\quad \text{linear response}
$$

当 $\delta f =0$ 时, 我们有 $\mu+q\phi=\text{const.}$ , 这是一个 exact 的解

一般地

$$
\partial_t f
+{\omega^{-1}}^{IJ}(\partial_J H+\partial_t\gamma_J)\partial_I f
=\text{collision}
$$

若认为 local equilibrium 存在时, 取 $\partial_t =0$ 和 $\text{collision}=0$ 

一般地, 有

$$
{\omega^{-1}}^{IJ}\partial_J H\partial_I f=0
$$

一种解是

$$
f=f(H)
$$

在现在的例子中 

$$
H=\frac{p^2}{2m}+q\phi=\epsilon^1(p)+q\phi
\implies f=f(\epsilon^1+q\phi)
$$

而 local equilibrium 写成

$$
f=\frac{1}{e^{\beta (\epsilon^1-\mu)}\mp 1}
$$

这给出

$$
\mu+q\phi=\text{const.}
$$

> 为什么 local equilibrium 的形式长那样?
> 一个原因是 collision 是 local 的, 在碰撞中不出现 $\phi$ 
> 或者认为 $\phi$ 作为 gauge 进入了 $\mu$ 
