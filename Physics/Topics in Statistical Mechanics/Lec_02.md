
>Last time
>![[Lec_01#^2a2161]]

##### Motivation
一般的 Boltzmann 方程

$$
\partial_t f+\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}\partial_{\mathbf{x}}f+\frac{\mathrm{d}\mathbf{p}}{\mathrm{d} t}\partial_{\mathbf{p}}f=0
$$

要求系统在 Hamiltonian 演化下才成立；比如，在耗散系统中该方程就不成立。我们想找出这两种情况之间的联系。

对于处在磁场中的粒子，其 Hamiltonian 为

$$
H=\frac{\left(\mathbf{P}-q\mathbf{A}(\mathbf{x})\right)^2}{2m}
$$

它是否还满足原先的正则方程？

$$
\begin{align}
\dot{x}^i &= \partial_{P_i} H
= \frac{P_i - q A_i(\mathbf{x})}{m} \\
\dot{P}_i &= -\partial_{x^i} H
= \frac{q (P_j - q A_j(\mathbf{x}))}{m}\,\partial_{x^i} A_j(\mathbf{x})
\end{align}
$$

这里还没有看到 $\mathbf{B}$ 的痕迹，而且 $\mathbf{p}$ 也不是粒子的机械动量。
进一步修改

$$
p_i=P_i-qA_i(\mathbf{x})
$$

得到

$$
\frac{\mathrm{d}x^i}{\mathrm{d}t}=\frac{p_i}{m}\quad
\frac{\mathrm{d}p_i}{\mathrm{d}t}
=\frac{q}{m}p_j\partial_{x^i}A_j-q\partial_{x^j}A_i\frac{\mathrm{d}x^j}{\mathrm{d}t}
=q\frac{\mathrm{d}x^j}{\mathrm{d}t}B_{ij}
$$

描述粒子时，不能直接使用机械动量；但是为了得到熟知的方程，必须引入新的坐标，并从正则方程中导出结果，这就是正则变量。

>这里面还有 gauge transform 存在, 这表明
>$A_i$ 应该不是 physical 的；但两个动量相差一个 non-physical 的量，所以至少有一个也不是 physical 的
>即 canonical momentum

为了保持 mechanical momentum 在 gauge transform 下不变，也即保持 Hamiltonian 不变，要求 canonical momentum 协变：

$$
P_i\to P_i+q \partial_{x^i}\phi(\mathbf{x})
$$

* canonical 动量: 符合 canonical equation, gauge non-inv., not physically well defined
* mechanical 动量: intuitive, observable, gauge inv.

>为什么存在磁场后，momentum 就不再是 canonical 的了？
>换言之，如何确定在新的系统中，momentum 是否是 canonical 坐标？
>canonical 的标准是什么

一个观察是：在相空间中，$(x,P)$ 是一组 canonical 坐标，我们可以按等 $x,P$ 线对相空间分 bin。
但代价是：按等 $x,p$ 线分 bin 时，相空间会被扭曲；不管我们选哪组坐标分 bin，都会导致另一组坐标扭曲。

![[attachments/tikz/lec02-bin-transform.png]]

>insight from GR
>>No coordinate makes you feel totally happy
>一种妥协是: **需要发展一种不依赖于坐标卡选择的理论**

* 磁场就是一个例子。当存在 Berry phase 的影响时（如 Hall 输运），事情会变得更复杂。
* 更一般地，当我们有很好的理由使用某种曲线坐标时（例如弯曲空间中的粒子，或者 GR 中），问题也会以类似方式出现。

**Before we develop such a language, we first present the known examples in a form that makes generalization easy**

选择作用量的语言: 
当不存在磁场时

$$
S=\int_{\text{path}}\left[p_i\mathrm{d}x^i-H(\mathbf{p},\mathbf{x},t)\mathrm{d}t\right]
$$

而不是通常写成的形式（当 $H=p^2/2m +V$ 时）：

$$
S=\int_{\text{path}}\left[\frac{1}{2}m(\frac{\mathrm{d}x^i}{\mathrm{d}t})^2-V(\mathbf{x})\right]\mathrm{d}t
$$

>联系两种形式的方式是 Legendre 变换
>因为当 Lagrangian 的形式改变时，并不会改变第一种形式。
>为什么选择第一种形式？这种表述总是把微分写成 1-形式。

推导运动方程的方式是

$$
\begin{align}&\frac{\delta S}{\delta p_{i}}=0\implies \mathrm{d}x^i-\partial_{p_i}H\mathrm{d}t=0\\&\frac{\delta S}{\delta x^i}=0\implies -\mathrm{d}p_i-\partial_{x^i}H\mathrm{d}t=0\end{align}
$$

>>观察到 Hamiltonian 形式总是暴露 canonical 变量

当有磁场的情形

$$
S=\int_{\text{path}}\left[p_i\mathrm{d}x^i+qA_i(\mathbf{x})\mathrm{d}x^i-H(\mathbf{p},\mathbf{x},t)\mathrm{d}t\right]
$$

为了回到原先的形式，这驱使我们定义

$$
P_i=p_i+qA_i
$$

推导运动方程的过程是相同的（物理并不取决于我们使用的坐标）。
我们也可以强行使用原先的坐标，不同的是

$$
\frac{\delta S}{\delta x^i}=0\implies-\mathrm{d}p_i+q\partial_{x^i}A_j\mathrm{d}x^j-q\partial_{x^j}A_i\mathrm{d}x^j-\partial_{x^i}H\mathrm{d}t-\partial_{t}A_i\mathrm{dt}=0
$$

若改写

$$
\tilde{H}=H-qA_0,
$$

则上式中会出现

$$
q(\partial_tA_i-\partial_i A_0)
$$

可以看出，上面的结果就是电磁场中电荷的运动方程。
上面的方程是 gauge 不变的。

>问题：这些运动方程是 gauge inv. 的，但 $S$ 中的 $A_i$ 是依赖 gauge 的。
>能看出 $S$ 也是 gauge inv. 的吗？

做一个 gauge transform 检测：

$$
A_i\to A_i+\partial_{x^i}\phi\quad A_0\to A_0+\partial_t\phi
$$

$$
\Delta S =\int_{\text{path}} q\partial_{x^i}\phi \mathrm{d}x^i+q\partial_t\phi\mathrm{d}t=q\phi\Big|_{\text{path}}=0\quad \text{当固定边界条件时}
$$

>Comment: 第一种形式甚至可以看出不确定性原理；在固定边界条件时，只能固定某一个坐标 (?)

>Note: In these derivations, $x^i$ 总是上指标，$p_i,A_i$ 总是下指标；收缩时总是上下指标收缩。
>在发展一种不需要坐标选取的理论时，我们需要注意指标上下的形式；它们应该用不同的语言来翻译。
> * 我们希望对相空间用任意坐标
> * 我们总希望是一阶微分的

我们考虑 $2n$ 维相空间上的任意坐标

$$
\xi^I\quad\text{e.g.}\quad\xi^{I}=(x^i,p_i)
$$

^0fc686

一般的作用量为

$$
S=\int_{\text{path}}\left[{\large\gamma}_{I}(\xi,t)\mathrm{d}\xi^I-H(\xi,t)\mathrm{d}t\right]
$$

^fa85b4

在原先的表述中：
当没有磁场时

$$
{\large\gamma}_{x^i}=p_i\quad {\large\gamma}_{p_i}=0
$$

当有磁场时

$$
{\large\gamma}_{x^i}=p_i+qA_i\quad {\large\gamma}_{p_i}=0
$$

Semi-classical particle with both magnetic field and Berry phase: ^47a412

$$
{\large\gamma}_I\mathrm{d}\xi^I
=
p_i\mathrm{d}x^i
+qA_i(\mathbf{x},t)\mathrm{d}x^i
+\underbrace{\hbar a^i(\mathbf{p})\mathrm{d}p_i}_{\text{Berry connection}}
$$

^c24196

>这应该是一个量子理论, 但是被做了半经典近似, 使之能用经典物理描述

>下节课的内容预告:
>* The coordinate transform in this formalism $\longrightarrow$ some invariant quantities
>* Gauge invariance
>* Equation of Motion $\longrightarrow$ symplectic form, Poisson bracket
>* What is a canonical coordinate?
>* Liouville theorem

##### Note (Codex 生成): 为什么固定边界条件时只能固定一半?
先说最直观的版本:

对一阶作用量 ^3c6d64

$$
S=\int_{t_i}^{t_f}(p\dot{x}-H(x,p))\mathrm{d}t
$$

^804334

变分后得到的是 Hamilton 方程

$$
\dot{x}=\partial_pH,\qquad \dot{p}=-\partial_xH
$$

它们都是一阶微分方程.  
一阶方程的意思是: 只需要给一组初始数据, 轨道就被决定了.  
所以边界上不能把 $(x,p)$ 全都当成彼此独立、任意指定的数据；那样通常会过约束。

更准确地说:
* 可以固定一组共轭变量, 例如固定两端的 $x(t_i),x(t_f)$
* 然后由驻值条件选出满足这两个端点的经典轨道
* 一旦轨道确定, 边界上的 $p(t_i),p(t_f)$ 也就随之确定, 它们不再是额外独立输入的数据

![[attachments/tikz/lec02-endpoint-path.png]]

从变分也能直接看出来. 对上式做变分:

$$
\delta S=\int_{t_i}^{t_f}\left[(\dot{x}-\partial_pH)\delta p+(-\dot{p}-\partial_xH)\delta x\right]\mathrm{d}t+\left[p\,\delta x\right]_{t_i}^{t_f}
$$

这里最关键的是最后的边界项

$$
\left[p\,\delta x\right]_{t_i}^{t_f}
$$

它说明:
* 体内变分给出运动方程
* 边界上自然冒出来的是 $p\,\delta x$
* 因而最自然的边界条件是 $\delta x(t_i)=\delta x(t_f)=0$, 也就是固定两端的 $x$

这并不是说永远只能固定 $x$.  
如果你改写作用量的边界项, 也可以改成固定 $p$.  
真正的结论是:

**对一阶作用量, 边界上只能自然固定一组共轭变量, 而不能把 $(x,p)$ 同时当成独立的边界数据任意固定**

离散化以后这一点会更明显, 因为边界项会直接从求和里跳出来. 取

$$
S_d=\sum_{n=0}^{N-1}\left[p_n(x_{n+1}-x_n)-H(x_n,p_n)\Delta t\right]
$$

则内部点的变分给出离散版 Hamilton 方程:

$$
x_{n+1}-x_n=\partial_pH\,\Delta t,\qquad p_n-p_{n-1}=-\partial_xH\,\Delta t
$$

而边界上只剩

$$
\delta S_d\supset p_{N-1}\delta x_N-p_0\delta x_0
$$

所以离散求和时一眼就能看出:
* 中间点负责给出运动方程
* 头尾只留下 $\delta x_0,\delta x_N$
* 因而最自然的是固定两端的 $x$, 而不是同时再独立固定两端的 $p$

>这和不确定关系不是同一件事, 但它们有共同的根源: $x,p$ 是一对 canonical conjugate variables
