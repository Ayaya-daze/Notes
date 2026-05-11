上次的结果 [[Lec_09]] 

relaxation time 和 linear response

$$
J^i
=\int_p \frac{p^i}{m}\delta f
=\underbrace{
\tau q\int_p \frac{p^ip^j}{m^2}
\left(-\frac{\partial f_{\text{eq}}}{\partial \varepsilon}\right)
}_{\sigma^{ij}}
\left(E_j-\partial_j\mu/q\right)
\quad \text{linear response}
$$

同时存在一个 exact solution

$$
\mu+q\phi=\text{const.}
$$

问题是: 这是一个 local 还是 global 的 equilibrium
这个回答有不同的角度: 首先这个结果是 $x$ dependent 的, 包含了 local 的性质
另外这个结果也满足 global equilibrium 的解的要求

> 一个例子是干电池, 内部是不是 equilibrium
> 电池的能量可以来源于不同的形式, 满足上面结果的干电池是哪种? 
> 最简单的回答是没电的电池

但是如果一直有 $\phi=\phi(x)$ 这就不一定是一个 global 的性质

> 这也可能是先约定好什么叫 global equilibrium
> 一种好的约定是认为当系统没有 time dependent 的时候系统达到了 global equilibrium
> 如果上面的结果也没有 time dependent, 我们也可以认为这描写了 global equilibrium

回到前面的两个 scale


$$
1/\tau \ll \partial_t ,v\partial_x \quad \text{ballistic}
$$

$$
1/\tau \gg \partial_t ,v\partial_x\quad \text{hydrodynamics}
$$

如果做进一步的细化, 讨论 $\partial_t ,v\partial_x$ 的关系

首先的观察是, 前文的外场得到的 exact solution 在 slow limit $\partial_t \ll v\partial_x$ 对两种情景都是满足的 (和 $\tau$ 无关) , 只要 $\partial_t\approx 0$

但在 fast limit, 就不相同了, 此时 $\partial_x\simeq 0$

$$
\partial_t f+ qE\cdot \partial_p f
=-\frac{\delta f}{\tau}
$$

在 linear response 下, 可以将动量部分做替换 $f\sim f_{\text{eq}}$, 但是为了保留含时贡献, 对时导数只能做 $\delta f$ 的替换 ($f_{\text{eq}}$ 不含时)

这种情况下, 一种解是

$$
\left(\partial_t +\frac{1}{\tau}\right)\delta f
=qE\cdot \frac{p}{m}
\left(-\partial_{\varepsilon}f_{\text{eq}}\right),
\qquad
f_{\text{leq}}\sim f_{\text{eq}}
$$

> 这里需要对 $p$ odd 的部分

这个方程可以解

$$
\delta \tilde{f}
=\frac{
i\omega q A_i \frac{p_i}{m}\partial_{\varepsilon}f_{\text{eq}}
}{
-i\omega +\frac{1}{\tau}
}
$$

在 $\omega , \frac{1}{\tau}$ 的不同关系下, 这给出了不同响应

当 $\omega \gg  1/\tau$ 时, 这与 $A$ 是 same phase 的
当 $\omega \ll 1/\tau$ 时, 这与 $E$ 是同相的

这两个范围给出了不同的图像

![[attachments/tikz/lec10-fast-slow-response.png|620]]

在这种情况, ballistic 给出 $\sigma \propto 1/\omega$, 而 hydrodynamic 给出 $\sigma \propto \tau$

可以发现, 在 $\omega \ll 1/\tau$ 时, 这给出了和 slow limit 相同的解

但是在 fast limit 下, linear response 是一个合理的近似解, 但在 slow limit 下, 这不是一个合理的解 (环境自由度被藏在了里面), 而 $\mu +q\phi=\text{const.}$ 是一个合理的解

$\partial_x\mu -qE$ 总是一直出现吗? (至少在 slow limit 下)

在 global equilibrium 下, 我们有关系 $\mu +q\phi=\text{const.}$
但在电流中, 并不是这样

我们知道

$$
J^0(x,t)=\int_p f,
\qquad
J^i(x,t)
=\int_p
\left.\frac{\mathrm{d}x^i}{\mathrm{d}t}\right|_{\text{EoM}} f
$$

符合 $\partial_\mu J^\mu=0$, 只要 evolution 和 collision 都保持 particle number

> 但是 current 不一定都是这个形式, 粒子数守恒的条件允许添加一项全散度 $\partial_\nu M^{\mu\nu}$
> 上面实际上是粒子流, 而实验中通常使用的是电流
> 首先两者都是一个观测量

先看看如果存在多的项 $M^{\mu\nu}$ , 这应该是什么

一个想法是考虑多极矩, 按照一般的电流密度的定义, 可以加入极化电流, 这样 $M^{\mu\nu}$ 可以理解为极化密度

但是这个结果如何进入上面的定义?

考虑单粒子 action

$$
S=\int \left[p_i\dot{x}^i+qA_\mu(x,t)\dot{x}^\mu-H\right]\mathrm{d}t,
\qquad
\dot{x}^\mu=(1,\dot{x}^i)
$$

若还带有多极矩, 应该在 action 里面加入什么项? 首先应该有一部分能量, 可以用极化密度和电磁场构造

$$
S_{\text{int}}
=\int \mathrm{d}t
\left[
qA_\mu(x,t)\dot{x}^\mu
+\frac{1}{2}\mu^{\mu\nu}F_{\mu\nu}(x,t)
\right]
$$

其中 $\mu^{\mu\nu}=-\mu^{\nu\mu}$, 且

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu
$$

同时从 Noether thm 得到的 Noether current 也不能探测出全导数项, 之前提到过, 这需要考虑和场的耦合, 按照电流的结果

$$
J^\mu(x',t')=\frac{\delta S_{\text{int}}}{\delta A_\mu(x',t')}
$$

对多极矩项做变分. 利用 $\mu^{\mu\nu}$ 反对称性,

$$
\frac{1}{2}\mu^{\mu\nu}\delta F_{\mu\nu}
=\mu^{\mu\nu}\partial_\mu\delta A_\nu
$$

这里对外场的泛函导数为

$$
\frac{\delta A_\mu(x(t),t)}{\delta A_\nu(x',t')}
=\delta_\mu^\nu\delta^d(x(t)-x')\delta(t-t')
$$

以及

$$
\frac{\delta F_{\rho\sigma}(x(t),t)}{\delta A_\nu(x',t')}
=
\left(
\delta_\sigma^\nu\partial_\rho
-\delta_\rho^\nu\partial_\sigma
\right)
\left[
\delta^d(x(t)-x')\delta(t-t')
\right]
$$

其中 $\partial_\mu$ 作用在粒子位置的时空坐标 $(x(t),t)$ 上. 代入作用量得到

$$
\frac{\delta S_{\text{int}}}{\delta A_\nu(x',t')}
=\int \mathrm{d}t
\left[
q\dot{x}^\nu\delta^d(x(t)-x')\delta(t-t')
+\mu^{\mu\nu}\partial_\mu
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right]
$$

现在对 $t$ 积分. 对第一项直接令 $t=t'$. 对第二项, 空间导数可用

$$
\partial_{x^i}\delta^d(x(t)-x')=-\partial_{x'^i}\delta^d(x(t)-x')
$$

时导数项要对 $t$ 分部积分:

$$
\int \mathrm{d}t\,\mu^{0\nu}\partial_t
\left[
\delta^d(x(t)-x')\delta(t-t')
\right]
=
-\left.
\frac{\mathrm{d}}{\mathrm{d}t}
\left[
\mu^{0\nu}\delta^d(x(t)-x')
\right]\right|_{t=t'}
$$

所以完整地有

$$
J^\nu(x',t')
=q\dot{x}^\nu(t')\delta^d(x(t')-x')
-\frac{\mathrm{d}}{\mathrm{d}t'}
\left[
\mu^{0\nu}(t')\delta^d(x(t')-x')
\right]
-\partial_{x'^i}
\left[
\mu^{i\nu}(t')\delta^d(x(t')-x')
\right]
$$

现在把两个分量用带撇的观测点定义重写.

先对 $A_0(x',t')$ 求泛函导数:

$$
J^0(x',t')
=\frac{\delta S_{\text{int}}}{\delta A_0(x',t')}
$$

这一项里面需要用到

$$
\frac{\delta A_\nu(x(t),t)}{\delta A_0(x',t')}
=\delta_\nu^0\delta^d(x(t)-x')\delta(t-t')
$$

以及

$$
\frac{\delta \partial_\mu A_\nu(x(t),t)}{\delta A_0(x',t')}
=\delta_\nu^0\partial_\mu
\left[
\delta^d(x(t)-x')\delta(t-t')
\right].
$$

所以

$$
\begin{aligned}
J^0(x',t')
&=\int \mathrm{d}t
\left[
q\dot{x}^0(t)\delta^d(x(t)-x')\delta(t-t')
+\mu^{\mu 0}(t)\partial_\mu
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right] \\
&=\int \mathrm{d}t
\left[
q\delta^d(x(t)-x')\delta(t-t')
+\mu^{i0}(t)\partial_{x^i(t)}
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right].
\end{aligned}
$$

这里 $\mu^{00}=0$. 再用

$$
\partial_{x^i(t)}\delta^d(x(t)-x')
=-\partial_{x'^i}\delta^d(x(t)-x')
$$

得到

$$
J^0(x',t')
=q\delta^d(x(t')-x')
-\partial_{x'^i}
\left[
\mu^{i0}(t')\delta^d(x(t')-x')
\right].
$$

再对 $A_i(x',t')$ 求泛函导数:

$$
J^i(x',t')
=\frac{\delta S_{\text{int}}}{\delta A_i(x',t')}
$$

此时

$$
\frac{\delta A_\nu(x(t),t)}{\delta A_i(x',t')}
=\delta_\nu^i\delta^d(x(t)-x')\delta(t-t')
$$

以及

$$
\frac{\delta \partial_\mu A_\nu(x(t),t)}{\delta A_i(x',t')}
=\delta_\nu^i\partial_\mu
\left[
\delta^d(x(t)-x')\delta(t-t')
\right].
$$

代入后

$$
\begin{aligned}
J^i(x',t')
&=\int \mathrm{d}t
\left[
q\dot{x}^i(t)\delta^d(x(t)-x')\delta(t-t')
+\mu^{\mu i}(t)\partial_\mu
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right] \\
&=\int \mathrm{d}t
\left[
q\dot{x}^i(t)\delta^d(x(t)-x')\delta(t-t')
+\mu^{0i}(t)\partial_t
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right. \\
&\qquad\qquad\left.
+\mu^{ji}(t)\partial_{x^j(t)}
\left(
\delta^d(x(t)-x')\delta(t-t')
\right)
\right].
\end{aligned}
$$

空间导数项仍然换成对 $x'$ 的导数. 时间导数项对 $t$ 分部积分:

$$
\int \mathrm{d}t\,\mu^{0i}(t)\partial_t
\left[
\delta^d(x(t)-x')\delta(t-t')
\right]
=-\left.
\frac{\mathrm{d}}{\mathrm{d}t}
\left[
\mu^{0i}(t)\delta^d(x(t)-x')
\right]\right|_{t=t'}.
$$

于是

$$
\begin{aligned}
J^i(x',t')
&=q\dot{x}^i(t')\delta^d(x(t')-x')
-\frac{\mathrm{d}}{\mathrm{d}t'}
\left[
\mu^{0i}(t')\delta^d(x(t')-x')
\right] \\
&\qquad
-\partial_{x'^j}
\left[
\mu^{ji}(t')\delta^d(x(t')-x')
\right].
\end{aligned}
$$

对于多粒子情形, 按照相空间权重

$$
\int_{p,x}f(t,x,p)
$$

做积分, 这个积分消掉了 $\delta^d(x-x')$. 定义

$$
M^{\mu\nu}(x,t)
=\int_p \mu^{\mu\nu}(x,p) f(t,x,p)
$$

就得到

$$
J^\mu(x,t)
=J_{\text{conv}}^\mu(x,t)-\partial_\nu M^{\nu\mu}(x,t)
=J_{\text{conv}}^\mu(x,t)+\partial_\nu M^{\mu\nu}(x,t).
$$

这正是 Noether thm 中少写的全导数项; 由于 $M^{\mu\nu}$ 反对称, 它不会改变 $\partial_\mu J^\mu=0$.

一个例子是考虑 global equilibrium 的电荷系统, 即使 $\mu,\phi$ 都不随时间变化

局部仍然可以有电流

$$
\partial_j M^{ij}(\mu)
$$

![[attachments/imagegen/lec10-local-magnetization-current.png|620]]

即使是在 $\phi =0$ 的情况, 这个电流也可能存在. 这种情况 $\partial_i\mu$ 存在, 但 $E_i$ 消失

但对这个局部电流积分之后, 我们总得到总电流为 0:

$$
\int \mathrm{d}^d x\,\partial_j M^{ij}
=\int_{\partial V}\mathrm{d}S_j\,M^{ij}
=0
$$

> 当然也可以问是否存在只和电场有关但和 $\mu$ 无关的电流?
> 这就是 Berry curvature
