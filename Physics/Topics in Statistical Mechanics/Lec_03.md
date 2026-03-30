
> [!note] Last time: [[Lec_02]]
> 希望作用量中总只出现一阶项, 并考虑了一般相空间中的坐标.

我们考虑 $2n$ 维相空间上的任意坐标

$$
\xi^I\quad\text{e.g.}\quad\xi^{I}=(x^i,p_i)
$$

**Q:** 为什么要写成 1st-order 的形式?  
**A:** 1st-order 的计算比较方便, 例如离散方法中的插值更容易实现, 数值上也更稳定. 这是最直观的理由.

**Q:** 我们既然允许不依赖任何坐标系, 为什么不能允许任意阶导数出现?  
**A:** 这里想传达的是: 到底哪些东西可以任意, 哪些必须做出一个选择.

一般的作用量

$$
S=\int_{\text{path}}\left[{\large\gamma}_{I}(\xi,t)\mathrm{d}\xi^I-H(\xi,t)\mathrm{d}t\right]
$$

考虑 Berry Connection

$$
{\large\gamma}_I\mathrm{d}\xi^I
=
p_i\mathrm{d}x^i
+qA_i(\mathbf{x},t)\mathrm{d}x^i
+\underbrace{\hbar a^i(\mathbf{p})\mathrm{d}p_i}_{\text{Berry connection}}
$$

### Gauge of the Action
这个作用量里面哪些是物理的, 哪些是非物理的? 非物理的部分对应规范的选取. 若考虑

$$
S\to S+\chi\Big|_{\text{endpoints}}
$$

也就是说, 两个 action 只差一个 boundary term, 因而给出相同的物理. 这就是 action 中的 gauge. 为了看到这一点, 考虑变换

$$
\begin{align}&{\large\gamma}_I(\xi,t)\to{\large\gamma}_I(\xi,t)+\partial_I\chi(\xi,t)\\& H(\xi,t)\to H(\xi,t)-\partial_t\chi(\xi,t)\end{align}
$$
^de958e

则给出相同的 action.

**例：电磁场**

做规范变换

$$
A_i(\mathbf{x},t)\to A_i(\mathbf{x},t)+\partial_i\varphi(\mathbf{x},t),\qquad A_0(\mathbf{x},t)\to A_0(\mathbf{x},t)-\partial_t\varphi(\mathbf{x},t)
$$

这正对应上面

$$
\gamma_I\to\gamma_I+\partial_I\chi,\qquad H\to H-\partial_t\chi
$$

的结构. 同样, Berry connection 也有 gauge.

一般地, 若

$$
p_i\mathrm{d}x^i\mapsto -x^i\mathrm{d}p_i
$$
则取

$$
\chi=-p_ix^i
$$

> 接下来要讨论的就是 Simple Harmonic Oscillator 和 Symmetry 与 Noether theorem

### Change of coordinate
既然这个理论不依赖于具体坐标, 现在就来试着改变坐标系. 考虑

$$
\xi^I=\xi^I(\tilde{\xi}^{\tilde{I}},t)
$$

![[attachments/tikz/lec03-coordinate-transform.png]]

那么

$$
\mathrm{d}\xi^I=\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}\mathrm{d}\tilde{\xi}^{\tilde{I}}+\frac{\partial\xi^I}{\partial t}\mathrm{d}t
$$

如果要求作用量描述相同的物理, 我们需要新的 $\gamma$.

$$
\tilde{{\large\gamma}}_{\tilde{I}}(\tilde{\xi}^{\tilde{I}},t)={\large\gamma}_I(\xi(\tilde{\xi},t),t)\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}
$$

同样, Hamiltonian 也跟着变换.

$$
\tilde{H}(\tilde{\xi},t)=H(\xi(\tilde{\xi},t),t)-\partial_t\xi^I{\large\gamma}_I(\xi(\tilde{\xi},t),t)
$$

**关于上下标**

$$
\mathrm{d}\xi^I=\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}\mathrm{d}\tilde{\xi}^{\tilde{I}}+\frac{\partial\xi^I}{\partial t}\mathrm{d}t
$$

上下指标都配对消掉了, 对 $\gamma$ 也是一样. 好处在于可以快速看出最终结果的指标结构.

什么时候需要这样的坐标变换?

SHO 是一个例子.

先做一个无量纲化, 取

$$
x'=\sqrt{m\omega}\,x,\qquad p'=\frac{p}{\sqrt{m\omega}}
$$

$$
p\mathrm{d}x-\omega(\frac{p^2}{2m\omega}+\frac{m\omega}{2}x^2)\mathrm{d}t=p'\mathrm{d}x'-\frac{\omega}{2}(p'^2+x'^2)\mathrm{d}t
$$

这迫使我们想到采用相空间的极坐标

$$
-\rho^2\sin^2\theta \mathrm{d}\theta+\rho\sin\theta\cos\theta \mathrm{d}\rho-\frac{\omega}{2}\rho^2\mathrm{d}t
$$

现在还很丑, 需要找一个 $\chi$ 把表达式化简.

$$
-\frac{\rho^2}{2}\mathrm{d}\theta-\frac{\omega}{2}\rho^2\mathrm{d}t+\mathrm{d}(\frac{\rho^2}{2}\cos\theta\sin\theta)
$$

作用量中不显含 $\theta$, 这在运动方程中给出了极大的便利

$$
\begin{align}&\frac{\delta S}{\delta \theta}\propto \mathrm{d}\rho=0\\& \frac{\delta S}{\delta \rho}=0\implies \frac{\mathrm{d}\theta}{\mathrm{d}t}=-\omega \end{align}
$$

这跟 action-angle coordinates 很像.

> 对于 polar coordinates, 也会采用 $\rho e^{i\theta}$ 的形式, 这使我们想到 QM 的 operator $a,a^{\dagger}$.
> 这种 semi-classical 的描述在没有 QM 时用得较多.
> 后面会讲 (?)

要求 EoM

$$
\frac{\delta S}{\delta{\xi^I}}=0\implies \partial_I{\large\gamma}_J\mathrm{d}\xi^J-(\mathrm{d}\xi^J\partial_J{\large\gamma}_I+\mathrm{d}t\partial_t{\large\gamma}_I)-\partial_IH\mathrm{d}t=0
$$

即

$$
(\partial_I{\large\gamma}_J-\partial_J{\large\gamma}_I)\mathrm{d}\xi^J=(\partial_I H+\partial_t{\large\gamma}_I)\mathrm{d}t
$$

这两部分在 $\chi$ 的 gauge 变换下都保持不变:

$$
{\large\gamma}_I(\xi,t)\to{\large\gamma}_I(\xi,t)+\partial_I\chi(\xi,t),\qquad
H(\xi,t)\to H(\xi,t)-\partial_t\chi(\xi,t)
$$

这两部分看起来就像磁场和电场的结构.

于是定义记号

$$
\omega_{IJ}\coloneqq 2\partial_{[I}{\large\gamma}_{J]}=\partial_I{\large\gamma}_J-\partial_J{\large\gamma}_I
$$

> $[\cdots]$ 的意思是 antisymmetrize, 上面这个东西叫 symplectic 2-form.
> 2 的意思是有两个指标, form 的意思是它是反对称的.

在一般的形式 $\xi^I=(x^i,p_i)$

$$
\gamma=p_i\,\mathrm{d}x^i,\qquad \gamma_{x^i}=p_i,\qquad \gamma_{p_i}=0
$$

这里 $\gamma_I$ 只有一个相空间指标 $I$. 写成 $\gamma_{x^i},\gamma_{p_i}$ 时, $x^i,p_i$ 只是坐标标签, 不是在 $\gamma$ 上再额外附加一个需要升降的 $i$ 型指标.

$$
\omega_{IJ}
=
\left(
\begin{array}{c@{\;\middle|\;}c}
\omega_{x^i,\;x^j}=0 & \omega_{x^i,\;p_j}=-\delta_i^{\ j} \\[4pt]
\omega_{p_i,\;x^j}=\delta_j^{\ i} & \omega_{p_i,\;p_j}=0
\end{array}
\right)
$$

这里矩阵的行列顺序固定为 $(x^i,p_i)$.

其中
$$
\omega_{p_i,\;x^j}
=
\partial_{p_i}\gamma_{x^j}-\partial_{x^j}\gamma_{p_i}
=
\partial_{p_i}p_j
=
\delta_j^{\ i},
$$
所以左下角块必须写成 $\delta_j^{\ i}$.

将上式除以 $\mathrm{d}t$, 得到

$$
\omega_{IJ}\frac{\mathrm{d}\xi^J}{\mathrm{d}t}=\partial_I H+\partial_t{\large\gamma}_I
$$

因此

$$
\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}=(\omega^{-1})^{IJ}(\partial_J H+\partial_t{\large\gamma}_J)
$$
^d87288

看逆矩阵

$$
(\omega^{-1})^{IJ}
=
\left(
\begin{array}{c@{\;\middle|\;}c}
(\omega^{-1})^{x^i,\;x^j}=0
&
(\omega^{-1})^{x^i,\;p_j}=\delta^i_{\ j}=\{x^i,p_j\}
\\[4pt]
(\omega^{-1})^{p_i,\;x^j}=-\delta_i^{\ j}=\{p_i,x^j\}
&
(\omega^{-1})^{p_i,\;p_j}=0
\end{array}
\right)
$$

Poisson bracket 自动出现了. 这无非是在一种特殊坐标系下, 取 2-form 逆的分量.

> [!Summary]
> 到这里我们做了什么?
> 1. 我们从一般的 action 出发, 讨论它的 gauge invariance, 并计算了 EoM.
> 2. 将方程整理为在 $\chi$ 的 gauge 变换下不变的形式. 这是 EoM 中真正物理的部分, 并从中定义了 symplectic 2-form.
> 3. 从中写出最一般的 EoM, 在 usual case 中计算逆, 发现 Poisson bracket 自动出现. 这表明这个矩阵的逆更为重要, 它不依赖于具体坐标.
>
> 所以现在需要去找这个矩阵有哪些不依赖于坐标的性质.

### Check Coordinate Transformation Properties

$$
\tilde{\omega}_{\tilde{I}\tilde{J}}=\omega_{IJ}\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}\frac{\partial\xi^J}{\partial\tilde{\xi}^{\tilde{J}}}
$$

需要检查这与 $\tilde{\omega}$ 的定义相容.

> 这是一个作业

Abstractly, a symplectic 2-form:
* is antisymmetric:
	$$\omega_{IJ}=-\omega_{JI}$$
* transforms as
	$$\tilde{\omega}_{\tilde{I}\tilde{J}}=\omega_{IJ}\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}\frac{\partial\xi^J}{\partial\tilde{\xi}^{\tilde{J}}}$$
* is non-degenerate, i.e. $\det\omega\neq 0$. (When it is degenerate, it means some directions in phase space are unphysical, i.e. gauge degrees of freedom.)
  (这是指相空间中有些维度对应 gauge.)
* is closed: $\partial_{[K}\omega_{IJ]} = 0$. (这是一个 local 性质.)


### The First Very Important Property of $\omega_{IJ}$

 $\omega_{IJ}$ has no intrinsic local information. ^b055b4

#### Darboux theorem
Locally in phase space, one can always find a coordinate system such that

$$
\omega_{IJ}
=
\left(
\begin{array}{c@{\;\middle|\;}c}
\omega_{x^i,\;x^j}=0 & \omega_{x^i,\;p_j}=-\delta_i^{\ j} \\[4pt]
\omega_{p_i,\;x^j}=\delta_j^{\ i} & \omega_{p_i,\;p_j}=0
\end{array}
\right)
$$

^bb0d22

这就是 "canonical" 的定义.

不同的坐标在局部没有本质区别, 但它们有时没有明确的物理意义, 所以很多时候我们不会采用这种方便的坐标.

> 证明留作作业
