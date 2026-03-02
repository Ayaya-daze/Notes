### Office Hour
Thu 13:00 - 14:00
考核: 作业 60% , 两次随堂小测 40% (期中, 期末附近) 

> 小测说是(
> 内容: 接近作业

### Contents
Boltzmann 方程为主, 以及 hydrodynamics . 关于 classical 及 semi - classical 的情况
Transport Experiments , 关心一些理论框架和真实物理的联系

### Flavor
$$\text{Study} \to\text{Research(theoretical)}$$
- 好的 Physical picture : set up, numbers, order of magnitude
- Systematic / General language

## Invitation
In thermodynamics $$\delta Q\leq T\mathrm{d}S\quad\text{In general}$$
为什么是 $\leq$ , 一种角度为
$$\delta Q=T\mathrm{d}S_{\text{in}}+T\mathrm{d}S_{\text{prod}}$$
在系统过程中还会产生熵, 并且 $\mathrm{d}S_{\text{prod}}\geq 0$ , 这些熵产生的例子: friction , free expansion

Jarzynski 写下了一个一般情况的等式, 首先来看一个不等式:
若一个过程的自由能变化和功进行比较
$$\Delta F\leq W\quad \text{process kept at fixed temperature}$$
> Intuition 是功可以全部浪费掉, $\Delta F$ 是被系统的状态决定的, 当然可以做一些复杂的过程把中间做的功全部浪费掉
> 当然也可以从最初的不等式得到
> $$\mathrm{d}F=\mathrm{d}E-T\mathrm{d}S-S\mathrm{d}T=\delta Q+\delta W-T\mathrm{d}S-S\mathrm{d}T\leq \delta W$$

这里 $W$ 是一个宏观热力学量, microscopically means $\overline{W}\quad \text{averaged over possible microscopie process}$ 

所以从微观的视角来写
$$\Delta F\leq \overline{W}$$
那么这个等式来自于哪里
##### Jarzynski‘s Equation (very easy?)
考虑热平衡的系统, 但考虑一个任意过程
$$\exp\left({-\frac{\Delta F}{T}}\right)=\overline{\exp\left(-\frac{W}{T}\right)}$$

问题: 
* 末态不是热平衡, 如何定义 $\Delta F$ ?
* $T$ 是什么意思, process or final
* Does it implies $\Delta F\leq W$ ?
* Relation to patition function ratio (derivation)
* How about distribution before averaging ?
* $\overline{x} \quad\mathrm{v.s.} \quad\overline{e^{-x}}$  behave differently
* Usual thermodynamical 是可加的
* 为什么不直接用指数描述热力学

一个想法是代数去检验它, 但是可以估计指数上的数量级:
$$T\sim\text{energy of one particle}$$
但是 typical $W\propto \Delta F\sim NT$ , 这个量太小了
这是一个 90 年代才写出的结果, 相信 100 年前也有人得到, 但它们应该并不会当回事, 只有当指数上的数量级接近时, 这个等式才有意义, 即 few body system. 即现代物理可以接触的尺度

如果并不局限于少体系统, 之前的不等式和这个等式的区别在哪?
差别在统计了所有可能的微观概率: 某些 $W$ 很大的微观过程贡献在平均值内部, 如果只考虑热力学极限, 比如只统计在经典过程周围的过程, 就给出了原先的不等式, 只有统计了其他极小概率的过程才能补回这个差距

理论推导可以得到一个完全严谨正确的结果, 但是对它的评价可以不同, 在一百年前这个结果并没有什么用, 但到现代我们有 nano physics了, 这个结果就有意义了.

具体推导后面再来.

##  Classical Mechanics with a Little Formality (some semi - classical)
回顾一下经典力学的框架

考虑相空间 $(x,p)$ , 一些粒子在相空间里面有一些线

>这些线能不能相交?
>一般的情况不会相交, 不然就不是决定性的了, 当然有摩擦力的时候可能会出现 attractor

考虑这些粒子在相空间的演化 (no interaction for now)

让 $\rho(\mathbf{x},\mathbf{p},t)$ 为时间 $t$ 时刻, $\mathbf{x},\mathbf{p}$ 在 $\mathrm{d}^d\mathbf{x}\mathrm{d}^d\mathbf{p}$ 处的粒子的密度, $\rho$ 的方程
$$\partial_t\rho+\partial_{\mathbf{x}}\cdot(\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}\rho)+\partial_{\mathbf{p}}\cdot(\frac{\mathrm{d}\mathbf{p}}{\mathrm{d}t}\rho)=0$$
或者是
$$\partial_t\rho+\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}\cdot\partial_{\mathbf{x}}\rho+\frac{\mathrm{d}\mathbf{p}}{\mathrm{d}t}\cdot\partial_{\mathbf{p}}\rho=0$$
哪条是对的? 
第一条总是对的, 第二条在 Hamiltonian evolution 下是对的, 做差就可以验证
$$\Delta =\rho(\partial_{\mathbf{x}}\cdot\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}+\partial_{\mathbf{p}}\cdot\frac{\mathrm{d}\mathbf{p}}{\mathrm{d}t})$$

为什么第一条总是对的? 第一条有点像 current , 比如考虑均匀的 $\rho$ 但速度有区别, 可以想像粒子密度还是会变化, 因为进出速度不一样, 那么在不是 Hamiltonian evolution 时: 有摩擦力的情况, 第二条方程就不对了

也可以给一个有限时长的图像
notation: $\mathbf{x}(t;\mathbf{x}_0,\mathbf{p}_0,t_0),\mathbf{p}(t;\mathbf{x}_0,\mathbf{p}_0,t_0)$ , 前面是 initial condition
by definition, 可以直接得到
$$\mathrm{d}^d\mathbf{x}\mathrm{d}^d\mathbf{p}\rho(\mathbf{x},\mathbf{p},t)=\mathrm{d}^d\mathbf{x}_0\mathrm{d}^d\mathbf{p}_0\rho(\mathbf{x}_0,\mathbf{p}_0,t_0)$$
在 Hamiltonian evolution 情况, 看原先的第二条方程, 可以得到有限时间版本
$$\rho(\mathbf{x},\mathbf{p},t)=\rho(\mathbf{x}_0,\mathbf{p}_0,t_0)$$
这是因为此时有 Liouvelle theorem, 体积元是不变的
可以看到, 两个版本的差别就在于 Jacobian 
$$|\det\frac{\partial(x,p)}{\partial(x_0,p_0)}|=|\det(1+\cdots\mathrm{d}t)|=1+\mathrm{Tr}(\cdots)$$
>这个看起来像 poisson bracket

现在考虑过渡到 infinitesimal time version $t=t_0 +\mathrm{d}t$ 就得到第一个方程

Boltzmann Eq. 通常呈现为 
$$\partial_t f+\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}\partial_{\mathbf{x}}f+\frac{\mathrm{d}\mathbf{p}}{\mathrm{d} t}\partial_{\mathbf{p}}f=\text{collision}$$
为什么通常写成第二种形式? 在这里 $f$ 的含义也不太一样

