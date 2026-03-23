继续上节课

![[Lec_03#^b055b4]]

![[Lec_03#^bb0d22]]

这就是 "canonical" 坐标的定义

先提了一下 symplectic 2 - form 的抽象定义: 非退化, 闭的反对称 2 - form

即 $\omega$ 本身没有任何局部的与坐标无关的物理信息; 它在不同坐标中的分量只是同一局域结构的不同写法

并且在所取的正则坐标下, action 一定有形式

$$S=\int_{\text{path}}P_{\alpha}\mathrm{d}Q^{\alpha}-H(P,Q,t)\mathrm{d}t$$

> 当然也可能差一些 gauge, 不一定能一眼看出来


### The Second Very Important Property of $\omega_{IJ}$

Time Evolution $\text{v.s.}$ Coordinate Reparametrization

第一种讨论 $\omega$ 的 time evolution 的想法是看作 $\xi$ 和 $t$ 的函数

$$\begin{align}\frac{\mathrm{d}\omega_{IJ}}{\mathrm{d}t}(\xi,t)&=\partial_t\omega_{IJ}(\xi,t)+\frac{\mathrm{d}\xi^K}{\mathrm{d}t}\partial_K\omega_{IJ}(\xi,t)\\&= \frac{\omega_{IJ}(\xi(t+\delta t),t+\delta t)-\omega_{IJ}(\xi,t)}{\delta t}\end{align}$$

但是 time evolution 是否有其他观点? 

An infinitesimal change of variable 

$$\tilde{\xi}^{I}(\xi,t)=\xi^I(t+\delta t)= \xi^I +\delta t\frac{\mathrm{d}\xi^I}{\mathrm{d} t}(\xi,t)$$

即把 $\xi$ 随时间的变化本身看作一种 change of variable , 现在看 $\omega$ 如何变换

首先算 Jacobian (算到一阶)

$$\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}=\delta_{\tilde{I}}^I-\delta t\,\partial_{\tilde{I}}\frac{\mathrm{d}\xi^I}{\mathrm{d} t}$$

$$\begin{align}\frac{\tilde{\omega}_{IJ}(\tilde{\xi},t)-\omega_{IJ}(\xi,t)}{\delta t}&=-\omega_{KJ}(\xi,t)\partial_I\frac{\mathrm{d}\xi^K}{\mathrm{d} t}-\omega_{IK}(\xi,t)\partial_J\frac{\mathrm{d}\xi^K}{\mathrm{d} t}\\&=\frac{\mathrm{d}\xi^K}{\mathrm{d}t}\partial_I\omega_{KJ}-\frac{\mathrm{d}\xi^K}{\mathrm{d}t}\partial_J\omega_{KI}-\partial_I(\omega_{KJ}\frac{\mathrm{d}\xi^K}{\mathrm{d}t})-\partial_J(\omega_{IK}\frac{\mathrm{d}\xi^K}{\mathrm{d}t})\end{align}$$

这里同样只算到一阶

现在检验两者是否相同, 将两者做差

$$\partial_t\omega_{IJ}+\frac{\mathrm{d}\xi^K}{\mathrm{d}t}(\partial_K\omega_{IJ}+\partial_J\omega_{KI}+\partial_I\omega_{JK})+\partial_I(\omega_{KJ}\frac{\mathrm{d}\xi^K}{\mathrm{d}t})+\partial_J(\omega_{IK}\frac{\mathrm{d}\xi^K}{\mathrm{d}t})$$

即

$$3\partial_{[K}\omega_{IJ]}\frac{\mathrm{d}\xi^K}{\mathrm{d}t}+\partial_t\omega_{IJ}-2\partial_{[I}(\omega_{J]K}\frac{\mathrm{d}\xi^K}{\mathrm{d}t})$$

出现了一个 $\mathrm{d}$ , 这很好, 剩下的东西: 如果 EoM 是满足的, 有关系

$$\partial_t\omega_{IJ}-2\partial_{[I}\kappa_{J]}=0\quad \kappa_{J}=\partial_JH+\partial_t\gamma_J$$

只要符合 EoM , 剩下的两项其实就是相等的

回忆运动方程 

![[Lec_03#^d87288]]

> 所以应该弄清楚到底在说什么
> 另外上面的计算在 Darboux 定理的时候也会用到

继续讨论: 如果一开始就使用了 canonical coordinate, 则 $\omega_{IJ}$ 的分量就是常数矩阵

$$\frac{\mathrm{d}\omega_{IJ}}{\mathrm{d}t}=0$$

这说明由时间演化定义的那个坐标变换在 EoM 下保持 $\omega$, 这就是

> Time evolution is a canonical transformation
> 这个东西其实就是 Lie 导数的观点


### Liouville Volume, Liouville Theorem, Collisionless Boltzmann Eq.

在坐标变换下, 一个好的 volume 是不依赖坐标的

$$|\det \tilde{\omega}|=|\det\omega|\left|\det\frac{\partial\xi^I}{\partial\tilde{\xi}^{\tilde{I}}}\right|^2$$

原先的 volume 是 $\mathrm{d}^{2n}\xi\quad \mathrm{d}^{2n}\tilde{\xi}$  相差一个 Jacobian , 所以这迫使我们构造一个坐标无关的 volume

$$\mathrm{d}^{2n}\xi \sqrt{|\det \omega(\xi)|}=\mathrm{d}^{2n}\tilde{\xi}\sqrt{|\det \tilde{\omega}(\tilde{\xi})|}$$

这就是一个 coordinate - independent volume measure 即 Liouville measure

可以看见, 对于 canonical coordinate

$$\text{Liouville measure} = \mathrm{d}^nQ\mathrm{d}^nP$$

前面定义的 number of particle per phase space volume , 需要换一个定义

$$\mathrm{d}^{2n}\xi \,\rho(\xi,t)=\mathrm{d}^{2n}\xi\sqrt{|\det\omega(\xi)|} \,f(\xi,t)$$

这样 $f(\xi,t)$ 也应该是 coordinate - independent 的, 这是一个良好定义的 density

$$\tilde{f}(\tilde{\xi},t)=f(\xi,t)$$

这立即导出 Liouville Theorem: 首先由于

$$\omega_{IJ}(\xi(t+\delta t),t+\delta t)\overset{\text{EoM}}{=} \tilde{\omega}_{IJ}(\tilde{\xi}(t),t)$$

则可以考虑 Time evolution under EoM

$$\xi^I=\xi^I(t;\xi_0,t_0)\quad \text{view as coordinate transformation}$$

这样就有

$$\mathrm{d}^{2n}\xi\sqrt{|\det\omega(\xi,t)|}=\mathrm{d}^{2n}\xi_0\sqrt{|\det\tilde{\omega}(\tilde{\xi}=\xi_0,t)|}$$

在 EoM 下, 右边就是

$$\mathrm{d}^{2n}\xi_0\sqrt{|\det \omega(\xi_0,t_0)|}$$

这就是 Liouville Theorem

> 两个等号都来自把时间演化视为坐标变换的观点: 第一个等号用的是 Liouville measure 在坐标变换下的不变性, 第二个等号用的是该坐标变换在 EoM 下保持 symplectic form

进一步就有: 沿着 EoM 生成的轨道

$$f(\xi(t;\xi_0,t_0),t)=f(\xi_0,t_0)$$

在 EoM 下, 对时间求导就有

$$\partial_t f+\frac{\mathrm{d}\xi^I}{\mathrm{d}t}\Big|_{\text{EoM}}\partial_If=0$$

这就是 Collisionless Boltzmann Eq.

回到 Lecture 1 的另一个方程

![[Lec_01#^883183]]

在 canonical 坐标下, 两者几乎相同, 但是必须澄清 $f$ 和 $\rho$ 不是同一个东西
在后续对 collision 的讨论中, 应该使用 $f$ ; 这才是坐标无关、也更物理的量

Q: 一般情况反而是 $\rho$ 更有物理意义

A: 后续一般是用 $f$ 来构建理论, 但对观测量的联系需要回到 $\rho$ 上去

接着可以讨论: Total action of an ensemble of non-interacting particles

对每个粒子 $\alpha$ , 则

$$S_{\text{total}}=\sum_{\alpha} S_{\alpha}[\xi_{\alpha}]$$

但是求和并不方便, 可以考虑在 phase space 积分, 用每个粒子的初值条件来 label 每个粒子

$$S_{\text{total}}=\int\mathrm{d}^{2n}\xi_{0}\rho(\xi_0,t_0)S[\xi(t;t_0,\xi_0)]$$

> 现在这个东西还是废话(

### Noether's Theorem

现在做一个更一般的 Noether's Theorem

$$S=\int_{\text{path}}[\gamma_I\mathrm{d}\xi^I-H\mathrm{d}t]$$

做变分之后

$$\delta S = \int_{\text{path}}[\delta\xi^I\omega_{IJ}(\xi,t)\mathrm{d}\xi^J-\delta\xi^I(\partial_IH(\xi,t)+\partial_t\gamma_I(\xi,t))\mathrm{d}t+\mathrm{d}(\gamma_I\delta\xi^I)]$$

回忆原先的证明过程, 需要 find $\mathrm{d}\xi^I$ 合于 $\delta S= \text{boundary term for any } \delta \xi^I$

反过来, 找 $\delta\xi^I$ 合于 $\delta S= \text{boundary term for any } \mathrm{d}\xi^I$

> 这个东西就和对称性有关系: 找特殊的变分 $\delta\xi^I$ , 对任意的运动过程, 仍然保持运动方程
> 某种意义上这也许就是对称性

首先考虑, 若变分里面只有全微分

$$\delta S = \int_{\text{path}}\mathrm{d}(\gamma_I\delta \xi^I)$$

那么 

$$\delta\xi^I\omega_{IJ}=0$$

若存在非平凡的 $\delta\xi^I$ , 则必有 $\det\omega=0$

那么 $\delta\xi^I$ 就应该是 unphysical 的自由度

如果考虑 $\omega$ 非退化, 那就只有

$$\delta S=\int_{\text{path}}\epsilon\,\mathrm{d}Q(\xi,t)+\mathrm{d}(\gamma_I\delta\xi^I)$$

$Q(\xi,t)$ 就是 Noether charge

但是这两个全微分的意义不同, 后者是 gauge dependent 的, 但是前者就不一定是 gauge dependent 的
