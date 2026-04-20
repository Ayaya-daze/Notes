前面只得到了 local equilibrium 

![[Lec_06#^8fed1d]]

$$
\partial_\mu s^\mu =0
$$

一个回答是 entropy 的定义和前面的 entropy 并不相同

$$
S=\int s^0
$$

这是 extensive 的 entropy, 在热力学的图景中, 这对应系统之间没有长程的作用

但最大化 $s^0$ 只会导出 local equilibrium, 最大化 $S$ 才会导出 global equilibrium
另一个观点即为: 最大化这两个量的约束不同

## Understand entropy from micro physics

### Boltzmann's entropy (classical)
一个图景是 BBGKY Hierarchy

考虑整个 ensemble

$$
\xi_{\text{tot}}=(\xi_1^I,\xi_2^I,\cdots,\xi_N^I)
$$

引入 

$$
F(\xi_{\text{tot}},t):\text{prob. for this ensemble to be in state } \xi_{\text{tot}}
$$

则有

$$
\partial_tF
+\sum_{\alpha}\frac{\mathrm{d}x_\alpha}{\mathrm{d} t}\Big|_{\text{EoM}}\partial_{x_\alpha}F
+\sum_{\alpha}\frac{\mathrm{d}p_\alpha}{\mathrm{d}t}\Big|_{\text{EoM}}\partial_{p_{\alpha}}F
=0
$$

在 non - interaction 情形, 粒子的坐标, 动量的导数只依赖自己 $(x_{\alpha},p_{\alpha})$ , 假设概率有形式

$$
F=\prod_{\alpha}F_{1}(\xi_{\alpha},t)
$$

代入上面得到 collision - less Boltzmann Equation 合于

$$
f(\xi,t)=\sum_{\alpha}\int_{\xi_{\alpha}}\delta^d(\xi-\xi_{\alpha})F_1(\xi_{\alpha},t)
$$

当存在 interaction 时, 例如 $V_{\alpha\beta} = V(x_{\alpha}-x_{\beta})$ , 则动量导数也会包含 $\partial_{\alpha} V_{\alpha\beta}$ 这些形式

先考虑前 $s$ 个粒子, 则

$$
F_s(\xi_1,\cdots,\xi_s,t)=\left(\prod_{\alpha=s+1}^N\int_{\xi_\alpha}\right)F
$$

得到 $F_s$ 满足的方程

$$
\begin{aligned}
\frac{\partial F_s}{\partial t}
&+\sum_{\alpha=1}^s\frac{\mathrm{d}x_\alpha}{\mathrm{d}t}\Big|_{\text{EoM}}\partial_{x_\alpha}F_s\\
&+\sum_{\alpha=1}^s \left(
\frac{\mathrm{d}p_{\alpha}}{\mathrm{d}t}\Big|_{\text{EoM}}
+\sum_{\beta=1,\beta\neq \alpha}^s\left(-\frac{\partial V_{\alpha\beta}}{\partial x_{\alpha}}\right)
\right)\partial_{p_{\alpha}}F_s\\
&=\sum_{\alpha=1}^s\int_{\xi_{s+1}} (N-s)\frac{\partial V_{\alpha,s+1}}{\partial x_\alpha}\cdot \partial_{p_{\alpha}}F_{s+1}
\end{aligned}
$$

> 最后把其他粒子的指标换成了同一个指标

即研究 $F_s$ 的演化, 需要知道 $F_{s+1}$ , 对于 Boltzmann Equation, 需要 $F_1$ 

**Truncation assumption**
一种方式是取 $F_2 (\xi_1,\xi_2,t)=F_1(\xi_1,t)F_1(\xi_2,t)$ 且不影响我们感兴趣的观测量

一个问题是: 这种假设在多长时间内成立

> Important to know how this gives B.E. and how long this assumption remains self - consistent

Gerd 1940s 
Last year , proved how long this stays self - consistent (open system, closed system)

> 即对 entropy 的研究即为研究上面的 assumption 到底在多长时间内成立

### Quantum case (some picture)
对于 quantum collision

$$
W\sim |\braket{p_1p_2 |T| p_3p_4}|^2
$$

由于这是一个经典概率, 必须做假设:

**Assumption**
Actually we don't make such observation. But pretending we have done so does not affect observable of interest

例如: 考虑一个粒子在杂质中的散射 $T_1$ , 假设杂质原子旁边还有一个杂质原子 $T_2$

问题即为, 是否应该考虑干涉?

$$
|\braket{p_2|T_1|p_1}|^2 +|\braket{p_2|T_2|p_1}|^2
\quad \text{or}\quad
|\braket{p_2|(T_1+T_2)|p_1}|^2
$$

如果粒子的波包足够小, 或者原子之间足够远时可以用前者, 即 Boltzmann Eq. 的保证, 即

$$
\text{de Broglie} < \text{separation of impurities}
$$

这是不平凡的

## Understand entropy from statistics without physics

### Jaynes' MaxEnt Principle (Brandeis summer school)

一个例子: 扔骰子, 扔出数字的 average 是 3.5
但我们看到了 average 为 4 , nonuniform 的 distribution 的概率应该长成什么样子?
考虑两个情形

![[attachments/tikz/lec07-dice-maxent-contrast.png|620]]

两张图都满足 $\langle i\rangle=4$。左边只是人为塞进一个满足约束的形状；右边则是在 uniform prior 下由单个平均值约束给出的指数倾斜，因而更像 MaxEnt 会选出的分布。

看起来第二个分布更靠谱, 从一种意义上说 , 看起来最 make sense 的分布可能就是 Boltzmann 分布

现在尝试导出它: 考虑分布 $p_i$ , 先考虑 $p_i =1/6$ , 现在扔 $N$ 次骰子 $(N\gg 1)$
观察到第 $i$ 个点的次数是 $n_i$ , 现在只知道计算出的 $\braket{i} = 4$ 

$$
P_{\{p_i\}}(\{n_i\})=\prod_{i}p_i^{n_i} \frac{N!}{\prod_i n_i!}
$$

即

$$
\ln P\simeq \sum_{i} n_i \ln p_i +N\ln N-\sum_i n_i \ln n_i
=-N\sum_i\rho_i \ln(\rho_i/p_i) <0,
\qquad \rho_i =n_i/N
$$

那么最大化 $P$ , 得到 $P=1 \quad p_i =\rho_i$ (law of large numbers)

但上面是自由约束, 现在需要加上 $\braket{i} =4$ 的约束,即 $\sum_{i}\rho_i i=4$

这个过程由 Lagrange multiplier 完成, 得到

$$
\rho_i =p_i \exp(b\cdot i+c)
$$

若 $p_i$ 是 uniform , 则直接得到 Boltzmann 分布

可以看到

$$
\ln P=-N \cdot (\text{relative entropy/K-L divergence} )
$$
即

$$
p:\text{original belief}\quad \rho :\text{update belief}
$$

用更 Bayesian 的观点

$$
P(\rho|\braket{i},p)=\frac{P(\braket{i}|\rho,p)P(\rho|p)}{P(\braket{i}|p)}
$$

若 $i$ 被替换为连续变量 $x$ , relative entropy 给出

$$
\text{relative entropy} = \int \mathrm{d}x \rho(x)\ln(\rho(x)/p(x))
$$

对比

$$
\text{entropy} =- \int \mathrm{d}x \rho(x)\ln \rho(x)
$$

即对于 entropy , 在连续变量情形, 到底什么是 uniform 是 ambiguous 的

Dice tossing model                  | Statistical mechanics
----------------------------------- | ------------------------------------------
N tosses                            | The whole system consists of N small subsystems
average outcome × N                 | Total energy (or other extensive quantities)
outcome of each toss                | Energy of each small subsystem
independent tosses, uniform dist.   | Assumption of equal a priori probability
前者是纯人类脑子中的假设, 但是后者的等概率假设是需要一个物理上的真实的结果的

最后回到, 为什么local entropy 和 global entropy 的 maximize 的结果不同, 从 Bayesian 的结果看, 两者的 $P(\rho|p)$ 是相同的, 但是 $P(\braket{i}|\rho,p)$ 对于两者方式的约束量是不同的, 前者是 local energy , 后者是 global energy. 这也就导致了最后的结果不同
