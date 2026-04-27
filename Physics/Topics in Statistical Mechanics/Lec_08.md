
# Relaxation time (approximation)

Boltzmann collision term 是复杂的

* non - linear in $f$ 
* even when it's linear in $f$ : 1 - 1 散射(杂质情形) , 经典极限下, 这也是一个积分微分方程

通常会用一些近似, 如 relaxation time approximation

$$
\text{collision} = -\frac{\delta f}{\tau}
$$

当忽略空间变化时, 有

$$
\partial_t f =-\frac{\delta f}{\tau}\implies \delta f \propto e^{-t/\tau}
$$

### question
What does $\delta f$ mean ?

$$
\delta f=f -f_{\text{leq}}
$$

> 注意 relaxation time approximation 中减去的应该是 local equilibrium, 因为 collision term 消失时应有 $f=f_{\text{leq}}$.

我们总有分解

$$
f=f_{\text{eq}}+\Delta f=f_{\text{leq}}+\delta f
\implies
\Delta f=(f_{\text{leq}}-f_{\text{eq}})+\delta f
$$

其中 local equilibrium 的形式为

$$
f_{\text{leq}}=\frac{1}{e^{\beta(H-\mu-u^{a}p_{a})}\mp1}
$$

在这样的分解下, 改变局域的参数 $\beta ,\mu,\cdots$ , 可以将变化吸收进 $\delta f$ 中. 即 $\delta f$ 和 $f_{\text{leq}}$ 的分解是 ambiguous 的

* $f_{\text{eq}}\quad \text{v.s.} \quad f_{\text{leq}}-f_{\text{eq}}$

首先 $f_{\text{eq}}$ 我们可以等待系统到达平衡态之后来定义, 同样, 对右侧, 我们可以用一些守恒量来约束

$$
\int_{\vec{x}}\int_{\vec{p}} Q(f_{\text{leq}}-f_{\text{eq}})=0
$$

类似地, 我们可以尝试使用

$$
\int_{\vec{p}} Q\delta f=0
$$

实际上, 这是 relaxation time approximation 的要求, collision 需要保持守恒量

$$
\int_p Q\times(\text{collision})=0
$$

想要将 $\delta f,\Delta f$ 视作小量 (这和 relaxation time 无关) 

一般地, 上面这两个要求并不是必然相关的, 通常我们会使用这两个要求

> 注意 $\#$ of ambiguity = $\#$ of independent $Q$ = $\#$ of collision invariants
> 一般不考虑角动量, 除非有 spin

首先 $\tau =\text{const}$ 通常不是很合理, 例如我们可以有

$$
\tau =\tau(|\vec{p}|)
$$

> 例如 absorber 是一个很软的物质, 动量大的粒子就直接穿过去了, 动量小的粒子才会发生相互作用

但是可以认为 $\tau$ 是一个我们关心的物理过程的 typical scale, 这样使用起来是方便的

在研究问题时, 我们常常需要将一些 scale 用来对比

$$
\partial_t\sim \omega,\qquad
v\partial_x \sim vq
\quad
\text{time/spatial variation of our exerted force or measurements}
$$

这些一般是宏观的 scale, 还有一些 scale

$$
1/\tau \quad \text{typical scattering rate}
$$


$$
\frac{H}{\hbar}\quad \text{very large}
$$

### ballistic
ballistic 的图像是, 当施加外场时, 能够看到粒子的各种运动

$$
1/\tau \ll \partial_t ,v\partial_x
$$

即在这种情况下 collision 的发生频率很低

例子是:
相互作用比较弱 (如低温的 phonon) 
Fermi liquid (little room in $p$ space for scattering)
### hydrodynamic
即为相反的情况, 这是一个稠密粒子的情形, 处处很快达到 local equilibrium

$$
1/\tau \gg \partial_t ,v\partial_x
$$

> "hydrodynamics" 有两种含义
> 最初, 这就是指的液体, 像水一样, 如粒子数, 能量, 动量守恒等
> generally, study local conserved quantities
> 如: 导体中的电子在杂质中的散射, 此时没有动量守恒

当然, $\partial_t$ 和 $v\partial_x$ 的 ratio 也是重要的, 因为在 local equilibrium 时我们仍需要比较两者

#### Simplest example: non - interaction electrons in conductor

Boltzmann eq.

$$
\partial_t f +\frac{\partial H}{\partial p}\partial_x f +qE \partial_p f=-\frac{\delta f}{\tau}
$$

Suppose $\Delta f$ is driven by $E$
此时的图像: 当施加一个disturb 时, 电子会很快达到 local equilibrium , 但会很慢地到达 global equilibrium

> 为什么到达 global equilibrium 会慢得多?
> 因为不同区域之间需要时间交换守恒量, 这是一个输运过程

> 我们实际上有如下 hierarchy:

![[attachments/tikz/lec08-kinetic-hydro-hierarchy.png|620]]

> 但是实际上, hydrodynamics 并不需要粒子的概念。

我们将 $\Delta f$ 和 $E$  视作同阶量

若 $E=\text{const}$ , 且 system stays uniform and stable, 即认为 $\partial_t ,\partial_x=0$ 

$$
qE \partial_p f_{\text{geq}} =-\frac{\delta f}{\tau}
$$

而 global equilibrium 是能量的函数, 我们可以解出

$$
\delta f= \tau q E \partial_p H(-\partial_H f_\text{geq})
$$

则电流

$$
J^i=q\int_p \frac{\mathrm{d}x^i}{\mathrm{d}t}\Big|_{\text{EoM}}f
=\tau q^2\int_p \partial_{p_i}H \partial_{p_j}H(-\partial_H f_{\text{geq}}) E_j
$$

即得到了电导

$$
\sigma^{ij}
=\tau q^2\int_p \partial_{p_i}H \partial_{p_j}H(-\partial_H f_{\text{geq}})
$$

> 注意我们将 $f$ 替换为 $\delta f$, 也包含了一些近似

但是这个电导的结果需要小心理解: 上面的稳态解隐含了能量可以被某个外界 bath 带走, 或者说 relaxation time approximation 固定了一个背景的 $f_{\text{geq}}$。如果是封闭电子系统, 持续电场会不断加热, 不应有严格的稳态解; 这表明前面保留到一阶的处理只是线性响应/Drude 近似, 不是完整的非平衡稳态。
