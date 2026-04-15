Review: 用概率性的语言描述粒子的碰撞

![[Lec_05#^36b009]]

例如 1 - 1

$$
\int_{p_2} W_{2\to 1}f_2(1\pm f_1) - W_{1\to 2}f_1(1\pm f_2)
$$

2 - 2

$$
\int_{p_2,p_3,p_4} W_{34\to 12}f_3f_4 (1\pm f_1)(1\pm f_2) - W_{12\to 34} f_1 f_2 (1\pm f_3)(1\pm f_4)
$$

一些典型的结果

$$
W_{2\to 1} = (2\pi\hbar)\delta(H_2-H_1)\times |\braket{p_1|T|p_2}|^2
$$

$$
W_{34\to 12} = (2\pi\hbar)^{d+1}\delta(H_3+H_4-H_1-H_2)\delta^d(p_3+p_4-p_1-p_2)\times \frac{|\braket{p_1p_2|T|p_3p_4}|^2}{2!}
$$

> 这是一种概率性的语言, 所以应该清楚, 越接近量子, 上面的结果应该用概率幅来描述。
> 1 - 1 散射一般没有动量守恒, 例如对于固定晶格上的散射。
> $2!$ 来自于 3, 4 粒子的交换效应。

一个观察是在这种语言下, $x,p$ 的地位已经不再等同。

### conservation currents

当不存在相互作用时, 考虑 Noether charge $Q(x,p)$

对单粒子, 有守恒方程

$$
\partial_t(\rho(x,p)Q(x,p))+\partial_{\xi^I}\left(\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\rho Q\right)=0
$$

并且 $x,p$ 是 canonical 的, 有 $\rho = f$

但当存在相互作用时,

$$
\partial_t(fQ)+\partial_I\left(\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}fQ\right)=\text{collision}\times Q(x,p)\neq 0
$$

例: 1 - 1 scattering

$$
\int_{p_2}\left[W_{2\to 1} f_2 (1\pm f_1)-W_{1\to 2}f_1 (1\pm f_2)\right]Q_1\neq 0
$$

一般不为 0, 但可以问怎样才能让这个式子为 0。由于积分内部是一个反对称项, 一个想法是对 1 也做积分, 但是 $Q_1$ 破坏了反对称; 如果过程中 $Q$ 是守恒的, 也可以将它移出积分。

例如 $Q_1 = Q_2$, $Q_1 = 1$ 或者 $Q_1 = H$

对于 2 - 2

$$
\int_{p_2,p_3,p_4}\left[W_{34\to 12}f_3f_4 (1\pm f_1)(1\pm f_2) - W_{12\to 34} f_1 f_2 (1\pm f_3)(1\pm f_4)\right]Q_1
$$

同样的做法, 这里可以取

$$
Q_1+Q_2 = Q_3 + Q_4 \implies Q_1\to \frac{Q_1+Q_2-Q_3-Q_4}{4}
$$

即: 若 $Q_1$ 保持 $W$ 内部的 delta 函数的对称性时, 有

$$
\partial_t\left(\int_p fQ\right)+\partial_i\left(\int_p \frac{\mathrm{d}x^i}{\mathrm{d}t}\Big|_{\text{EoM}}fQ\right)=0
$$

> 注意这里积掉了动量的 divergence, 因为这是一个边界项。

即

$$
\partial_t J_Q^0(x,t)+\partial_i J_Q^i(x,t)=0
$$

即这是一个 real space 的守恒流, 即

$$
\partial_\mu J_Q^\mu = 0
$$

但是问题是这个定义并不唯一, 考虑

$$
J_Q^\mu \to J_Q^\mu + \partial_\nu M_Q^{\mu\nu},
\qquad
M_Q^{\mu\nu} = -M_Q^{\nu\mu}
$$

因为 $\partial_\mu\partial_\nu M_Q^{\mu\nu} = 0$

一种想法是做了某种积分, 利用边界条件使 total current 在积分之后不变。
但是重要的想法是:

> current density is not defined only by $\partial_\mu J_Q^\mu = 0$; we also need to couple it to an external gauge field.

以后会讨论这一点

## Boltzmann H - theorem

忽略碰撞的细节, 从概率的角度描述它们。若从量子角度看, 这相当于在每次碰撞后都 "made an observation"; 但微观散射本身仍是 reversible 的, 因此应该存在某种 "increase of entropy" 来刻画这种描述。

如何看到这一点: 如果找到某个

$$
\partial_\mu S^\mu \geq 0
$$

则积分之后, 就可能找到一个单增的函数

assume (根据前面的守恒方程)

$$
S^0=\int_p h(f),
\qquad
S^i=\int_p \frac{\mathrm{d}x^i}{\mathrm{d}t}\Big|_{\text{EoM}}h(f)
$$

> 这个应该是关于 $f$ 的函数, 并且应该是空间的函数, 所以选择积掉动量。

$$
\partial_\mu S^\mu = \int_p h'(f)\times (\text{LHS of Boltzmann eq.}) = \int_p h'(f)\times(\text{collisions})
$$

首先, 当不存在 collisions 时, 这是自洽的 $\partial_\mu S^\mu = 0$

先看 2 - 2 collision

$$
\int_{p_1,p_2,p_3,p_4}\left[W_{34\to 12}f_3f_4 (1\pm f_1)(1\pm f_2) - W_{12\to 34} f_1 f_2 (1\pm f_3)(1\pm f_4)\right]h'(f_1)
$$

$W$ 在 $1\leftrightarrow 2$ 与 $3\leftrightarrow 4$ 下对称, 而能量和动量守恒由 delta function 保证。

首先代换

$$
h'(f_1)\to \frac{h'(f_1)+h'(f_2)-h'(f_3)-h'(f_4)}{4}
$$

**Bad news**: 若 $W$ 没有更多的约束, 则不能找到这样的 $h$ (Maxwell demon)

The condition we want for $W$ is

$$
W_{34\to 12} = W_{12\to 34}
$$

这对应时间反演意义下的微观可逆性, 也就是 detailed balance。

若如此, 令

$$
r = \frac{f_1f_2(1\pm f_3)(1\pm f_4)}{f_3 f_4 (1\pm f_1)(1\pm f_2)}
$$

$$
h'=\ln\frac{1\pm f}{f}
$$

就能满足前面的要求。此时记共同的 transition rate 为 $W$。

$$
\int_{p_1,p_2,p_3,p_4} W f_3 f_4 (1\pm f_1)(1\pm f_2)(1-r)\frac{-\ln r}{4}\geq 0
$$

则

$$
\boxed{h = -f\ln f\pm (1\pm f)\ln(1\pm f)}
$$

Non-linear in $f$

Boltzmann 假设了粒子的每次碰撞都做了观测, 但实际上并没有发生。实际上在大多数尺度下, 这是可以容许的。

那经典力学中少了什么?
一个想法是: 经典描述中忽略了不同碰撞之间的关联, 在这里反而考虑到了多对多的碰撞过程, 而经典力学都几乎认为这些碰撞都是独立的。问题是到底需要多长时间, 这种对关联性的影响才会体现在最终的预言中。

When does

$$
\partial_\mu S^\mu = 0
$$

如 $r = 1 \implies \log r = 0$, 即

$$
h'(f_1)+h'(f_2)=h'(f_3)+h'(f_4)
$$

这是某种守恒量, 故 $h'$ 是某个 Noether charge 的 linear combination

$$
\frac{1\pm f}{f} = \exp\left(\sum_{\alpha}\lambda_{\alpha}Q_{\alpha}\right)
\implies
f = \frac{1}{\exp\left(\sum_{\alpha}\lambda_{\alpha}Q_{\alpha}\right)\mp 1}
$$

这是 local equilibrium, $\lambda_{\alpha}=\lambda_{\alpha}(x,t)$

问题是: 为什么 $\lambda$ 可以是 local 的, 以及 local equilibrium 时, 为什么 $\lambda$ 还可以继续演化?
