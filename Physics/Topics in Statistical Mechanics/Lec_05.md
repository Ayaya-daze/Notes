> [!note] Last time: [[Lec_04]]
> 问满足任意 $\mathrm{d}\xi^I$ , 使得作用量相差边界项的 $\delta \xi^I$

考虑了连续对称性之后

![[Lec_04#^989e17]]

关于 $Q$ 讨论什么?

1. What is coordinate dependence of $Q(\xi,t)$ ? 
2. 和前面的项的关系是什么?

即

![[Lec_04#^e66895]]

就有

$$
\epsilon\mathrm{d}Q(\xi,t)=\delta\xi^I \omega_{IJ}(\xi,t)\mathrm{d}\xi^J-\delta\xi^I(\partial_IH(\xi,t)+\partial_t\gamma_I(\xi,t))\mathrm{d}t
$$

这样就可以得到 $Q$ 对 $\xi,t$ 的导数

$$
\begin{align}
&\epsilon\partial_J Q(\xi,t)=\delta\xi^I\omega_{IJ}(\xi,t)\\
&\epsilon\partial_tQ(\xi,t)=-\delta\xi^I(\partial_IH(\xi,t)+\partial_t\gamma_I(\xi,t))
\end{align}
$$

应该做什么? 

* Propose a $Q(\xi,t)$ 
* $\delta\xi^I=-\epsilon (\omega^{-1})^{IJ}(\xi,t)\partial_J Q(\xi,t)$ 

Check

$$
\partial_t Q(\xi,t) \overset{?}{=} (\partial_I H+\partial_t \gamma_I)(\omega^{-1})^{IJ}\partial_J Q
$$

If yes, then $\delta\xi^I$ is a continuous symmetry transformation

一种理解是 Poisson bracket

$$
\partial_t Q=\{H,Q\}\quad \mathrm{If} \,\partial_t\gamma_I =0
$$

另一种理解是运动方程

$$
\partial_t Q+\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\partial_I Q=0\implies \frac{\mathrm{d}Q(\xi,t)}{\mathrm{d}t}\Big|_{\text{EoM}}=0
$$
^d9464c

是一个守恒量, 即 Noether charge

> [!note]
> 当然
>
> $$
\delta\xi^I=-\epsilon (\omega^{-1})^{IJ}(\xi,t)\partial_J Q(\xi,t)
> $$
>
> 也是一个 Poisson bracket, 这在当前不依赖于 canonical language 的情况下更明显

### Another route for Noether charge

Let

$$
\delta\xi^I=\epsilon(t)\eta^I(\xi,t)
$$

使得当且仅当 $\epsilon$ 是一个常数时, $\delta S$ 是一个全微分

> 如果对任意 $\epsilon(t)$ 都成立, 则这就是前面的 unphysical 自由度

这表明

$$
\delta S=\int_{\text{path}} Q(\xi,t)\mathrm{d}\epsilon+\mathrm{d}(\cdots)
$$

> [!note]
> 这和上面的写法相差一个负号, 但这不重要

在 Equation of Motion 时, 要求

$$
\frac{\delta S}{\delta \epsilon}=0
$$

因为 $\epsilon$ 是变分的一部分, 在 EoM 下应该为 0 , 这给出

$$
\mathrm{d}Q\Big|_{\text{EoM}}=0
$$

然后就可以计算出 $Q$ 

####  Elementary examples

 Usual action of canonical $(x^i,p_i)$

$$
Q_{a}=P_{a}
$$

Check: 

$$
\delta x^i=-\epsilon \delta_j^i \delta^j_a
$$

即

$$
\partial_{x^i}H\overset{?}{=}0
$$

同样, 能量守恒
当

$$
\partial_t\gamma_I=0\quad Q=H
$$

check:

$$
\partial_t Q\overset{?}{=}(\omega^{-1})^{IJ}\partial_IH\partial_JQ=0
$$

S.H.O in polar coordinate of phase space

$$
S=\int -\frac{\rho^2}{2}(\mathrm{d}\theta+\omega \mathrm{d}t)
$$

Let 

$$
Q=\frac{\rho^2}{2}\implies \delta\theta\text{ shift}
$$

这里不能写成 $Q=\rho$ ; 否则得到的是 $\delta\theta=\epsilon/\rho$ , 并不是一个均匀的 shift

这是 trivial 的结果: particle number

> The setup is particle-number conserving
> 这个意义来自于量子化后的结果, 连续对称性为相位的 shift


### Ensemble

$$
\sum_{\alpha}\mapsto \int\mathrm{d}^{2n}\xi_0 \rho(\xi_0,t_0)=\int\mathrm{d}^{2n}\xi\rho(\xi,t)
$$

那么考虑所有 粒子的 charge

$$
\sum_{\alpha} Q_{\alpha}\mapsto\int\mathrm{d}^{2n}\xi\rho(\xi,t)Q(\xi,t)
$$

$$
\rho(\xi,t)Q(\xi,t)\quad \text{Some Noether charge density ?}
$$

从之前的演化方程

$$
\partial_t Q+\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\partial_I Q=0
$$

和

$$
\partial_t\rho +\partial_I(\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\rho)=0
$$

得到

$$
\partial_t(\rho Q)+\partial_{I}(\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\rho Q)=0
$$

此即 phase space conserved charge current

> 但一般没人用, 这是因为没有描述相互作用

## particle interacting with each other

先考虑一些简单的情形 $(x^i,p_i)$

从 collisionless Boltzmann equation [[Lec_01]]

$$
\partial_t f+\frac{\mathrm{d}x^i}{\mathrm{d}t}\partial_{x^i}f+\frac{\mathrm{d}p_i}{\mathrm{d}t}\partial_{p_i}f=0
$$

如果存在相互作用, 一个可能的 correction 为 $\mathrm{d}p_i/\mathrm{d}t$ 中应该存在新的且非常复杂的力

> [!note]
> Boltzmann's point of view:
> > Not directly take into account the new forces
>
> $$
\text{details} \mapsto \text{probability}
> $$
>
> 即不具体地考虑各个粒子之间的相互作用, 而是将它抽象为概率性的东西

![[attachments/tikz/lec05-collision-probability.png|420]]

引入: impact parameter (瞄准距离)

![[attachments/tikz/lec05-impact-parameter.png|360]]

方程右侧的 $0$ 变为 

$$
\text{rate of creation of particle at }\xi \, -\, \text{rate of annihilation}
$$

rate of creation ? Let

$$
\xi_1=\xi\quad \xi_2
$$

先考虑 1 in 1 out:

$$
\int _2C_{2\to 1}-\int_2 C_{1\to2}
$$

进一步 2 in 2 out

$$
\int_{234}C_{34\to 12}-\int_{234}C_{12\to 34}
$$

> 即只追踪方程描述的那个粒子的状态

#### Desired properties for $C$
##### Locality
即

$$
C_{2\to 1}\propto \delta^d(\mathbf{x}_2-\mathbf{x}_1)\text{ or } \partial^{(?)}\delta^d(\mathbf{x}_2-\mathbf{x}_1)
$$

> 在这里就出现一些对 coordinate transformation 的限制了, 至少为了简单(
> 所以我们并不能随便取 canonical coordinate

##### conserved charge still conserved in interactions ?
eg: $C_{\emptyset \to 1}$ 这种东西可以破坏粒子数守恒
eg: 能量守恒在 $C_{1\to 2}$ 中保持, 例如取 $C_{1\to2}(\text{elastic})\propto \delta(H(\xi,t)-H(\xi_2,t))$

> 这里的 $H$ 是在粒子距离很远处定义的
> 当然还有一些 gauge 选择的问题

eg: 动量守恒 , 例如 $C_{12\to 34}$

##### $f$ dependence
在讨论之前, 先把 Liouville volume 无量纲化

$$
\frac{\mathrm{d}^{2n}\xi\sqrt{\det\omega(\xi,t)}}{(2\pi\hbar)^n}
$$

相应的 $f$ 也是无量纲的

$$
C_{1\to 2}\propto f(\xi_1,t), (1\pm f(\xi_2,t))
$$

对于 Fermion: $1-f(\xi_2,t)$  from Pauli exclusion, 特别地, 此时有 $f\in [0,1]$
对于 Boson: $1+f(\xi_2,t)$ 
对于 Classical: $1$ 

> [!note]
> 可以用 Boson 的散射振幅来理解, 在相对于经典粒子的情形的意义上
> 若某个过程对应的单粒子概率幅为 $a$ , 则当末态已经有 $n$ 个同种 Boson 时, 再产生一个 Boson 的概率幅会增强为 $\sqrt{n+1}\,a$ , 即
>
> $$
\langle n+1\mid n\rangle=\sqrt{n+1}\,a
> $$
>
> 因而对应到这里就会出现 final-state factor $1+f$ . 相关背景可参见 [[Week 3#^boson1]]

> [!note]
> 虽然前面发展了一套任意坐标的理论, 但是由于 interaction 的存在
> 坐标平权已经被破坏了: 例如 locality 只体现在实空间中
