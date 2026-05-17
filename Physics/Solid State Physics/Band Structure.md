对于固体来说, 一开始可以近似成一些固定的格点上排列着原子, 而电子被束缚在原子中.
这种情况忽略了电子在原子中的传导, 故下一步的近似是考虑电子可以在原子阵列中传导, 作为初步近似, 我们仍然考虑电子被原子束缚的情形, 但给电子增加跃迁概率

## Tight - Binding Model

![[attachments/tikz/solidstate-tight-binding-chain-v2.png]]

首先考虑单电子情形, 用电子在原子上的占据态来建立 Hilbert 空间, 即我们考虑正交基

$$
\ket{n}\quad \braket{n|m}=\delta_{nm}
$$

当不存在跃迁时, 哈密顿量的构造是简单的

$$
H_0 =E_0 \sum_n \ket{n}\bra{n}
$$

当我们考虑跃迁时, 哈密顿量应该有新的部分, 构造的直觉来自于态的演化

$$
\ket{\psi}\to\ket{\psi}-\frac{i\Delta t}{\hbar}H\ket{\psi}+\mathcal{O}(\Delta t^2)
$$

可以看到, 如果能演化到更多的态, 这来自于 $H$ 的作用, 即应该含有跃迁矩阵元 $\ket{m}\bra{n}$
作为初步的近似, 我们考虑电子在实空间的局域性, 只加入电子在相邻原子之间跃迁的成分

$$
H=E_0\sum_n\ket{n}\bra{n}-t\sum_n\left(\ket{n}\bra{n+1}+\ket{n+1}\bra{n}\right)
$$

我们把厄米性显式写在了里面, 下一步就是解这个方程, 这个方程需要一些边界条件, 在这里采用周期边界条件, 考虑共有 $N$ 个格点, 那么

$$
\ket{N+1}=\ket{1}
$$

考虑求解 $H$ 的本征态, 在占据态基底下展开

$$
\ket{\psi}=\sum_m \psi_m\ket{m}\quad H\ket{\psi}=E\ket{\psi}\quad \psi_m\in \mathbb{C}
$$

得到

$$
E_0\psi_n-t(\psi_{n-1}+\psi_{n+1})=E\psi_n
$$

取 ansatz (这里省略了归一化)

$$
\braket{n|\psi}=\psi_n =\exp(ikna)\quad n=1,\cdots,N
$$

首先讨论波矢的范围, 这个解在 $k\to k+2\pi/a$ 时不变, 其中 $a$ 是原子间距, 这给出 $k$ 有规范冗余, 我们先规定

$$
k\in \left[-\frac{\pi}{a},\frac{\pi}{a}\right)
$$

我们称 $k$ 的允许范围叫 Brillouin zone
同时, 周期性边界条件给出 $\psi_1 =\psi_{N+1}$ , 要求

$$
\exp(ikNa)=1
$$

这给出 $k$ 在 Brillouin zone 一共有 $N$ 个允许值, 并且可以得到平移关系以及能量

$$
\psi_{n\pm1}=e^{\pm ika}\psi_n
$$

$$
E=E_0-2t\cos ka
$$

![[attachments/tikz/solidstate-tight-binding-dispersion-v2.png]]

在这个一维模型中, $k>0$ 和 $k<0$ 分别对应相反方向传播的 Bloch 模式

我们看到: 在我们的模型中
1. 为电子增加了相邻格点的跃迁项, 导致了一些类似于平面波的模式存在, 这些平面波模式是电子的能量本征态, 而不是位置的本征态! 这种邻域的微小扰动导致了非局域的能量本征态
2. 原先的能量本征态是完全简并的, 增加了跃迁项之后破除了这种简并性, 由波矢 $k$ 标记的能量本征态的能量在范围 $[E_0-2t,E_0+2t]$ 里面, 这给出了所谓能带的概念, 我们称这个区间的长度为带宽, 即 $4t$
3. 在长波极限 $k\ll \pi/a$ 下, 可以展开能量, 可以看见除常数外最低阶项是类似于动能的平方项, 这和一个自由粒子的色散关系极为相似, 这表明在长波极限下, 这种电子的行为很像一个自由粒子, 并且具有动力学上的等效质量 (注意这并不是粒子的真实质量)

借助上面的色散关系 $E=E(k)$ 我们可以去理解一些物质的行为

### 金属与半导体
施工中

## 近自由电子
紧束缚模型是格点上的原子对电子的吸引极为强烈的情形, 我们再考虑另一个极限, 原子对电子的作用极为微小, 我们可以用一个局域的场 $V(x)$ 来模拟电子感受到的原子的作用, 这个情况就像一个电子运动在周期性势场中

$$
H=\frac{p^2}{2m}+V(x)\quad V(x+a)=V(x)
$$

![[attachments/tikz/solidstate-nearly-free-electron-potential.png]]

同样我们也取周期性边界条件, 即考虑一个长度为 $L$ 的圆环 $\mathbb{S}^1$ 上的电子, 这要求 $L/a=N\in \mathbb{Z}$
我们的出发点仍然是去寻找本征态的主要成分, 由于在远离原子时, 原子势极弱, 我们可以先用自由粒子平面波基做 ansatz, 当没有势场时, 粒子的本征态是动量态

$$
\psi_k(x)=\braket{x|k}=\frac{1}{\sqrt{L}}e^{ikx}
$$

满足正交归一关系

$$
\braket{k|k'}=\frac{1}{L}\int\mathrm{d}x e^{i(k'-k)x}=\delta_{k,k'}
$$

对应的能量为

$$
E_0(k)=\frac{\hbar^2k^2}{2m}
$$

现在我们来尝试理解, 当存在原子势场时, 电子的本征态的变化

### Perturbation Theory
为了使用微扰论, 我们要先看本征态是否是简并的, 当然我们知道 $E_0(k)=E_0(-k)$ , 但这并不意味着我们必须使用简并微扰论, 因为非简并微扰论爆掉是因为如果微扰的矩阵元非零, 分母会爆掉, 这里不妨检查一下微扰矩阵元

首先对周期性势场做 Fourier 分解

$$
V(x)=\sum_{n\in \mathbb{Z}}V_n e^{2\pi inx/a}\quad V_n =V^*_{-n}
$$

那么

$$
\braket{k|V|k'}=\frac{1}{L}\int \mathrm{d}x \sum_{n\in \mathbb{Z}}V_n e^{i(k'-k+2\pi n/a)x}=\sum_{n\in \mathbb{Z}}V_n\delta_{k'-k+2\pi n/a,0}
$$

当且仅当

$$
k=k'+\frac{2\pi n}{a}\quad n\in \mathbb{Z}
$$

时, 矩阵元才非零, 而对于 $k'=-k$ 这给出

$$
k=\frac{n\pi}{a}
$$

即在 Brillouin zone 边缘, 而在远离 Brillouin 区边缘时, 我们可以放心使用非简并微扰论

此时即 $|k|\ll \pi/a$ , 非简并微扰论给出

$$
E(k)=\frac{\hbar^2k^2}{2m}+ \braket{k|V|k}+\sum_{k'\neq k}\frac{|\braket{k|V|k'}|^2}{E_0(k)-E_0(k')}+\cdots
$$

上面已计算出 $\braket{k|V|k}=V_0$ 为能量的整体平移, 并且二阶修正只对 $\ket{k'}=\ket{k+2n\pi/a}$ 有贡献, 当 $|k|\ll \pi/a$ 时, 这些修正很小, 即在小动量的情形, 粒子仍然表现得像一个自由粒子, 并且对应的 de Broglie 波长远大于原子间距

$$
\frac{2\pi}{|k|}\gg a
$$

电子就像感受不到原子之间的间隙一样

当然, 这个结果也适用于 $\pi n/a \ll k\ll \pi(n+1)/a$ 的情形, 只要我们远离 $\pi n/a$ 的位置, 一切都是安全的, 但是正是这些失效的地方, 带给我们更多的物理, 在这种情况必须使用简并微扰论

在 Brillouin zone 边缘时, 非简并微扰论失效, 例如 $k=\pi/a$ 时, 非简并微扰的结果直接炸掉, 这迫使我们使用简并微扰论

简并微扰论使用的原因是这种情况, 微扰使得简并态混合了, 所以一个新的微扰态应该是简并态的线性组合

$$
\alpha\ket{k}+\beta\ket{k'}
$$

然后我们求解本征方程

$$
\begin{pmatrix}
\langle k|H|k\rangle & \langle k|H|k^{\prime}\rangle\\
\langle k^{\prime}|H|k\rangle & \langle k^{\prime}|H|k^{\prime}\rangle
\end{pmatrix}
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
=E
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
$$

代入之前的计算

$$
\begin{pmatrix}
E_0(k)+V_0 & V_n\\
V_n^\star & E_0(k^{\prime})+V_0
\end{pmatrix}
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
=E
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
$$

这里 $k=-k'=n\pi/a$ 求解本征值得到

$$
E=\frac{\hbar^2}{2m}\frac{n^2\pi^2}{a^2}+V_0 \pm|V_n|
$$

我们看到, 在 Brillouin zone 的边缘, 存在一个大小为 $2|V_n|$ 的带隙

为了理解在这里发生了什么, 我们也可以用一个具体的势进行计算

$$
V(x)=2V_1 \cos \left(\frac{2\pi x}{a}\right)
$$

当 $k=\pm \pi/a$ 时, 出现本征态的混合, 计算特征向量得到

$$
(\alpha,\beta)=(1,-1)\quad (\alpha,\beta)=(1,1)
$$

对应的波函数

$$
\begin{aligned}
\psi_+(x)&=\langle x|\left(|k\rangle+|-k\rangle\right)\sim\cos\left(\frac{\pi x}{a}\right)\\
\psi_-(x)&=\langle x|\left(|k\rangle-|-k\rangle\right)\sim\sin\left(\frac{\pi x}{a}\right)
\end{aligned}
$$

而电子密度正比于 $|\psi|^2$ , 可以看到一种本征态电子更倾向于集中在原子处, 另一种情况更倾向于集中在原子之间. 对这里写成正值的势 $V_1>0$ , $\psi_+$ 的能量高于 $\psi_-$ ; 若把离子势写成吸引势, 上下顺序会随 $V_1$ 的符号交换.

![[attachments/tikz/solidstate-zone-edge-standing-waves.png]]

同样, 我们可以考察靠近带边的区域

$$
k=\frac{n\pi}{a}+\delta
$$

从势能矩阵上可以看到, 微扰只会混合波矢相差 $2n\pi/a$ 的简并态, 但此时, 这两个混合态几乎是简并的

$$
E(k)=\frac{\hbar^2}{2m}\left(\frac{n\pi}{a}+\delta\right)^2\quad\mathrm{and}\quad E(k^{\prime})=\frac{\hbar^2}{2m}\left(\frac{n\pi}{a}-\delta\right)^2
$$

所以我们仍然考虑简并版本, 求解相同的本征方程, 得到

$$
\left(\frac{\hbar^2}{2m}\left(\frac{n^2\pi^2}{a^2}+\delta^2\right)+V_0-E\right)^2-\left(\frac{\hbar^2}{2m}\frac{2n\pi\delta}{a}\right)^2-|V_n|^2=0
$$

以及能量

$$
E_\pm=\frac{\hbar^2}{2m}\left(\frac{n^2\pi^2}{a^2}+\delta^2\right)+V_0\pm\sqrt{|V_n|^2+\left(\frac{\hbar^2}{2m}\frac{2n\pi\delta}{a}\right)^2}
$$

我们对小 $\delta$ 的情形感兴趣, 不过, 作为 sanity check , 我们先考虑大 $\delta$ 的情形, 检查是否与非简并微扰相容, 实际上会得到

$$
E_\pm=E_0(n\pi/a\pm\delta)+V_0\pm\frac{|V_n|^2}{E_0(n\pi/a+\delta)-E_0(n\pi/a-\delta)}
$$

这与二阶微扰论的结果一致

同时我们考虑小 $\delta$ 展开, 给出

$$
E_\pm\approx\frac{\hbar^2}{2m}\frac{n^2\pi^2}{a^2}+V_0\pm|V_n|+\frac{\hbar^2}{2m}\left(1\pm\frac{1}{|V_n|}\frac{n^2\hbar^2\pi^2}{ma^2}\right)\delta^2
$$

在带边附近, 每一支能量都长得像一个二次曲线; 但允许能量在上下两支之间留下带隙, 所以能带之间不是连续连起来的.

![[attachments/tikz/solidstate-nearly-free-band-extended.png]]

### Band structure

现在总结一下我们观察到的能谱 $E(k)$ 的现象, 最开始我们从带底的平方形式, 被扭曲到了其他形式

1. 对小动量 $k\ll \pi/a$ , 能谱的结构没有改变
2. 能谱由于势的存在, 被分为了很多离散的带, 这些带的端点是 $n\pi/a\quad n\in\mathbb{Z}$ , 并且带隙的大小为 $2|V_n|$ , $V_n$ 是势能的 Fourier 模式
3. 在靠近带底端时, 能谱是平方形式的, 且 $\mathrm{d}E/\mathrm{d}k\to 0$

这里要区分两个对象: 动量空间中由 $-\pi/a,\pi/a$ 等边界切出的区间称为 Brillouin zone ; 能量轴上的允许区间称为 energy band . 在 extended-zone scheme 中, 常把第一、第二、第三能带分别画在第一、第二、第三 Brillouin 区附近; 在 reduced-zone scheme 中, 这些能带都会折回第一 Brillouin 区.

注意到在第一 Brillouin zone 时, 自由电子模型和紧束缚模型给出了相同的能谱, 不同的地方在于紧束缚模型只有有限个态, 都处于第一 Brillouin zone 内, 而自由电子模型有连续的态取值, 也有第一 Brillouin zone 以外的态

### Floquet matrix
带隙是一个很重要的概念, 在后面我们会看到很多材料的性质都是因为带隙的存在

这里我们会用另一种方法来展示带隙的存在, 而不借助微扰论, 我们同样考虑一个周期势 $V(x)$
我们尝试直接求解 Schrodinger 方程

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+V(x)\psi(x)=E\psi(x)
$$

这个方程是二阶的, 因此有两个线性无关的通解 $\psi_1(x),\psi_2(x)$ , 并且周期性要求, 这两者的平移也是这个方程的解, 而两组通解之间的关系是一个线性变换

$$
\begin{pmatrix}\psi_1(x+a)\\\psi_2(x+a)\end{pmatrix}=F(E)\begin{pmatrix}\psi_1(x)\\\psi_2(x)\end{pmatrix}
$$

这里 $F(E)$ 是一个 $2\times 2$ 矩阵, 由能量 $E$ 决定, 这被称为 Floquet matrix
我们有以下性质

#### Claim

$$
\det F=1
$$

证明:

对这个关系微分得到

$$
\begin{pmatrix}\psi_1^{\prime}(x+a)\\\psi_2^{\prime}(x+a)\end{pmatrix}=F(E)\begin{pmatrix}\psi_1^{\prime}(x)\\\psi_2^{\prime}(x)\end{pmatrix}
$$

我们借助 Wronskian determinant

$$
W(x)=\begin{pmatrix}\psi_1(x)&\psi_1^{\prime}(x)\\\psi_2(x)&\psi_2^{\prime}(x)\end{pmatrix}
$$

即有

$$
W(x+a)=F(E)W(x)
$$

借助 Schrodinger 方程, 能够证明 $(\det W(x))'=0$ , 即 $\det W(x)=\mathrm{const.}$ , 从而取 determinant 得到

$$
\det F(E)=1
$$

#### Claim

$$
\mathrm{Tr} F\in \mathbb{R}
$$

证明:

选取 $\psi_1,\psi_2$ 为实函数, 则 $F$ 的矩阵元都是实数, 从而 trace 也是实数

为了理解解的结构, 我们考虑 $F(E)$ 的特征值, 设为 $\lambda_+,\lambda_-$ , 则上面的性质给出 $\lambda_++\lambda_-\in\mathbb{R}$ 和 $\lambda_+\lambda_-=1$ , 特征方程为

$$
\lambda^2-\mathrm{Tr} F(E)\cdot\lambda+1=0
$$

然后讨论这个方程根的性质

当 $(\mathrm{Tr}F)^2<4$ 时, 这给出了两个复根

$$
\lambda_+=e^{ika}\quad \lambda_-=e^{-ika}
$$

考虑 $(\alpha_{\pm},\beta_{\pm})$ 是特征向量, 则线性组合 $\psi_\pm=\alpha_\pm\psi_1+\beta_\pm\psi_2$ 给出了

$$
\psi_\pm(x+a)=e^{\pm ika}\psi_\pm(x)
$$

这些态是在整个晶格中的态

当 $(\mathrm{Tr}F)^2>4$ 时, 给出两个实根

$$
\lambda_+=e^{\mu a}\quad \lambda_-=e^{-\mu a}
$$

同样按照特征向量重组态

$$
\psi_\pm(x+a)=e^{\pm \mu a}\psi_\pm(x)
$$

表明这些态是不合法的, 因为它们的波函数会在 $+\infty$ 或者 $-\infty$ 处发散; 这些能量就是能谱中的 gap 出现的地方

最后对 $(\mathrm{Tr}F)^2=4$ 时, 给出两个简并的根: $\pm1$ , 这对应带边的不连续
例如 $\lambda=+1$ , 则此时 $F$ 的标准型有两种形式

$$
PF(E)P^{-1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\quad\mathrm{~or~}\quad PF(E)P^{-1}=\begin{pmatrix}1&0\\1&1\end{pmatrix}
$$

前一种给出了两个允许的解, 而后一种只给出了一个允许的解, 另一个会爆炸

### 一维 Bloch Theorem
在上面的两个例子中, 我们都用波矢 $k$ 标记一个态, 但是问题是: 为什么要这么做, 这里 $k$ 到底是什么意思?

首先我们知道, 对于自由粒子, 我们可以用动量 $p$ 标记态, 这是因为 $[p,H]=0$ , 故动量本征态自动是能量本征态, 我们知道这实际上是哈密顿的连续平移对称性
而在晶格的情形, 这种平移的连续对称性消失了, 但我们为什么还能用 $k$ 标记能量本征态?
虽然我们没有连续的平移对称性, 但在晶格情形, 我们仍然有离散的平移对称性

$$
x\to x+a
$$

这足以表示我们能够用一种离散的"动量"来标记能量本征态, 这个结果即为 Bloch Theorem

#### 平移算子
为了证明这个结果, 我们先引入一些工具, 考虑平移算子 $T_l$

$$
T_l\psi(x)=\psi(x+l)
$$

并且这是一个幺正算子

$$
\braket{\phi|T_l|\psi}=\int\mathrm{d}x \phi^*(x)T_l\psi(x)=\int\mathrm{d}x \phi^*(x)\psi(x+a)=\int\mathrm{d}x \phi^*(x-a)\psi(x)=\int\mathrm{d}x (T_{-l}\phi(x))^*\psi(x)
$$

即

$$
\braket{\phi|T_l\psi}=\braket{T_l^\dagger\phi|\psi}=\braket{T_{-l}\phi|\psi}\implies T_l^{\dagger}=T_{-l}
$$

则

$$
T_{l}^\dagger T_{l}=T_{-l}T_l=1
$$

注意, 平移算子实际上形成了一个 Abelian group

$$
T_{l_1}T_{l_2}=T_{l_1+l_2}\quad [T_{l_1},T_{l_2}]=0
$$

> 交换性是一维特有的

借助动量算符, 我们可以表示平移算子

$$
T_l=\exp(l\mathrm{d}/\mathrm{d}x)=\exp(ilp/\hbar)
$$

于是一个系统是 $l$ 平移不变的, 若哈密顿与平移算子交换

$$
[T_l,H]=0
$$

> 在无穷小平移下, 展开平移算子, 就可以得到哈密顿与动量对易

但即使系统在离散平移对称性下, 仍然有与之对易的平移算子

这种情况, 虽然不能对 $p$ 和 $H$ 同时对角化, 但是我们可以对 $T_a$ 和 $H$ 做同时对角化, 即能量本征态可以被 $T_a$ 的本征值标记, 但 $T_a$ 是一个幺正算符, 他的本征值是复数 $e^{i\theta}$ , 同时, 如果考虑群结构

$$
e^{i\theta}=e^{ika}
$$

这样与 $T_{na}$ 的本征值相容, 在 $k$ 标记的本征态下, 我们有

$$
T_a\psi(x)=\psi(x+a)=e^{ika}\psi(x)
$$

并且由于本征值是相位, 具有选取规范, 我们一般取

$$
k\in\left[-\frac{\pi}{a},\frac{\pi}{a}\right)
$$

我们发现这就是第一 Brillouin zone 的结果

当平移对称性的间距任意小时, 让 $a\to0$ , 我们就得到了一般的连续 $k$ 版本

这个结果直接给出如下定理

一维 Bloch Theorem

在周期势 $V(x)=V(x+a)$ 下, 存在能量本征态基底

$$
\psi_k(x)=e^{ikx}u_k(x)
$$

这里 $u_k(x)=u_k(x+a)$ 是周期函数, 而 $k$ 落在 Brillouin zone 内

证明:

只需要选取 $\psi_k(x)$ 作为 $T_a$ 的本征态, 则

$$
\psi_k(x+a)=e^{ika}\psi_k(x)\implies u_k(x+a)=e^{-ik(x+a)}\psi_{k}(x+a)=e^{-ikx}\psi_k(x)=u_k(x)
$$

这告诉我们, 周期势的存在并不会极大地改变能量本征态, 实际上, 只是将平面波用 $u_k(x)$ 替换了, 这被称为 Bloch 函数, 并且波矢被限制在了 Brillouin zone 以内

最后, 对于紧束缚模型, 讨论是相同的, 只是平移算子变为了

$$
T_{a}\ket{n}=\ket{n+1}
$$

![[attachments/tikz/solidstate-zone-schemes.png]]

**晶格动量**

在上面, 我们使用的动量 $\hbar k$ 严格来说并不是物理上的动量, 可以看到, 它只是平移算符的生成元, 我们称它为晶格的动量

在现在的情况, 晶格动量是一个守恒量, 但这只是在 $\mathrm{mod} \,2\pi/a$  的意义下, 严格来说晶格的动量可以增加, 只要增加量是 $2\pi/a$ 的整数倍
Roughly speaking, 可以认为是晶格吸收了多余的动量

这实际上让我们回来重新看能谱的结构, 在第一 Brillouin 区以外的区域实际上应该被看作具有相同的晶格动量, 真正的能谱图实际上是把这些结构全部画在 $k\in[-\pi/a,\pi/a)$ 的范围内, 这得到了一个能量的多值函数

上面展示了两种画能谱图, 第一种为 extended-zone scheme, 第二种为 reduced-zone scheme, 或者说 Brillouin 区实际上在一个环上

### 哈密顿的真实结构
待施工

接下来我们讨论一下一般的晶格情形, 这会比一维的原子链复杂一些
### Bravais Lattices

晶格的最简单一种情况是 Bravais lattice, 也就是由 primitive lattice vectors 生成的周期阵列. 如二维情形可以写成

$$
\Lambda =\{\mathbf{r}=n_1 \mathbf{a}_1+n_2 \mathbf{a}_2: n_1,n_2\in \mathbb{Z}\}
$$

同样可以推广到 3 维

$$
\Lambda =\{\mathbf{r}=n_1 \mathbf{a}_1+n_2 \mathbf{a}_2+n_3\mathbf{a}_3: n_1,n_2,n_3\in \mathbb{Z}\}
$$

这种阵列具有的性质是所有点都是等价的, 这就是晶格的含义

我们称构成阵列的矢量 $\mathbf{a}_i$ 为 primitive lattice vector , 这不是唯一的, 我们可以取不同的线性组合, 只要他们给出同一个阵列

同样, 一个 primitive unit cell 是晶格空间区域的一个重复单元, 它通过 lattice vector 进行复制, 并填满整个空间, 同样, 这也不是唯一的
并且不难发现, 每个 unit cell 里面都包含一个 lattice point, 同样 unit cell 的体积是定值

$$
V=|\mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a}_3)|
$$

这是因为 $V=1/n$ , 这里 $n$ 是晶格点的数密度

注意到一个 unit cell 不一定具有晶格体系的所有对称性, 你可以把他的形状弄的很奇怪, 让他丢失旋转对称性

![[attachments/tikz/solidstate-wigner-seitz-cell.png]]

对任意晶格, 我们有一个 canonical choice of primitive unit cell , 能够保留晶格体系的大部分对称性, 即 Wigner - Seitz cell $\Gamma$
构造是这样的: 选择一个格点作为原点, 取 Wigner - Seitz cell 的区域为离选中格点最近的区域, 即

$$
\Gamma=\{\mathbf{x}:|\mathbf{x}|<|\mathbf{x}-\mathbf{r}|:\forall \mathbf{r}\in \Lambda, \mathbf{r}\neq 0\}
$$

一种理解 Wigner - Seitz cell 的方式是画出选中格点到周围其他格点的连线的垂直平分线(面), 则 Wigner Seitz cell 的区域即为这些垂直平分线(面)共同约束的区域

#### 2维 Bravais lattices 的例子

待施工

#### 3维 Bravais lattices 的例子

待施工

### Reciprocal Lattice
给定一个 Bravais Lattice $\Lambda$ , 我们能构造一个对偶的阵列 $\Lambda^*$

$$
\Lambda^*=\{\mathbf{k}=\sum_i n_i\mathbf{b}_i:n_i\in \mathbb{Z}\}
$$

新的矢量满足如下关系

$$
\mathbf{a}_i\cdot\mathbf{b}_j=2\pi \delta_{ij}
$$

在 3 维情形, 可以上面的关系可以显式求解

$$
\mathbf{b}_k =\frac{2\pi}{V}\frac{1}{2}\epsilon_{ijk}\mathbf{a}_i\times \mathbf{a}_j
$$

当然也可以写出逆变换

$$
\mathbf{a}_k=\frac{2\pi}{V^*}\frac{1}{2}\epsilon_{ijk}\mathbf{b}_i\times \mathbf{b}_j
$$

这里 $V^* =|\mathbf{b}_i\cdot(\mathbf{b}_j\times \mathbf{b}_k)|=(2\pi)^3/V$

上面的关系实际上也可以等价写为

$$
e^{i\mathbf{k}\cdot \mathbf{r}}=1\quad \forall \mathbf{r}\in \Lambda,\mathbf{k}\in \Lambda^*
$$

#### 一些例子

待施工

#### Fourier Transform
根据 reciprocal lattice 矢量的量纲: 长度的倒数, reciprocal lattice 实际上并不存在于实空间中, 而应该存在于 Fourier 空间, 即动量空间, 我们下面会看到这一点

首先考虑一个实空间中的周期函数 $f(\mathbf{x})$ , 对格点具有周期性, 那么就可以只在 Wigner Seitz cell 内部进行积分

$$
\begin{align}
\tilde{f}(\mathbf{k})=\int \mathrm{d}^3x e^{-i\mathbf{k}\cdot \mathbf{x}} f(\mathbf{x})
&=\sum_{\mathbf{r}\in \Lambda}\int_{\Gamma} \mathrm{d}^3x\,e^{-i\mathbf{k}\cdot(\mathbf{x}+\mathbf{r})}f(\mathbf{x}+\mathbf{r}) \\
& = \sum_{\mathbf{r}\in \Lambda}e^{-i\mathbf{k}\cdot\mathbf{r}}\int_{\Gamma}\mathrm{d}^3x e^{-i\mathbf{k}\cdot\mathbf{x}}f(\mathbf{x})
\end{align}
$$

我们看到, 在 $\mathbb{R}^3$ 上的积分通过晶格的对称性转化成了在 Wigner Seitz cell $\Gamma$ 中的积分, 最后只是出现一个因子

$$
\Delta(\mathbf{k})=\sum_{\mathbf{r}\in \Lambda}e^{-i\mathbf{k}\cdot \mathbf{r}}
$$

这个因子的性质很特殊

#### Property 1
$$
\Delta(\mathbf{k})=0\quad \text{unless}\quad \mathbf{k}\in\Lambda^*
$$

考虑晶格平移, 我们有

$$
\Delta(\mathbf{k})=\sum_{\mathbf{r}\in\Lambda}e^{-i\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}_0)}=\Delta(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{r}_0}\implies \Delta(\mathbf{k})(1-e^{i\mathbf{k}\cdot\mathbf{r}_0})=0
$$

由于 $\mathbf{r}_0$ 是任取的晶格上的点, 故 $\Delta(\mathbf{k})=0$ 除非有 $e^{i\mathbf{k}\cdot \mathbf{r}_0}=1$ 对任意 $\mathbf{r}_0\in \Lambda$
那么这就要求 $\mathbf{k}\in\Lambda^*$

#### Property 2

$$
\Delta(\mathbf{k})=V^*\sum_{\mathbf{q}\in \Lambda^*}\delta(\mathbf{k}-\mathbf{q})
$$

现在要求 $\mathbf{k}\in \Lambda^*$ , 则我们可以用 reciprocal lattice 展开 $\mathbf{k}=\sum k_i\mathbf{b}_i$ 和 $\mathbf{r}=\sum n_i\mathbf{a}_i$ 直接计算得到

$$
\Delta(\mathbf{k})=(\sum_{n_1=-\infty}^{\infty}e^{-2\pi ik_1n_1})(\sum_{n_2=-\infty}^{\infty}e^{-2\pi ik_2n_2})(\sum_{n_3=-\infty}^{\infty}e^{-2\pi ik_3n_3})
$$
而

$$
\sum_{n=-\infty}^{\infty}e^{-2\pi ikn}=\sum_{n=-\infty}^{\infty}\delta(k-n)
$$

那么实际上 $\Delta(\mathbf{k})$ 里面有一堆 delta 函数, 并且都在 $\Lambda^*$ 的格点上取值, 我们有

$$
\sum_{\mathbf{r}\in\Lambda}e^{-i\mathbf{k}\cdot \mathbf{r}}=A\sum_{\mathbf{q}\in \Lambda^*}\delta(\mathbf{k}-\mathbf{q})
$$

现在需要得到系数, 做法是考虑对一个 $\Lambda^*$ cell 积分, 由于内部只包含一个 lattice point, 右侧得到 $A$ , 现在考察左侧的积分

$$
\int\mathrm{d}^d k\sum_{\mathbf{r}\in \Lambda}e^{-i\mathbf{k}\cdot \mathbf{r}}
$$

将 $\mathbf{k}$ 参数化为 $\mathbf{k}=\sum_{i}x_i \mathbf{b}_i\quad x_i\in[0,1]$ ,那么 $\mathrm{d}^d k=|\det(\mathbf{b}_1,\cdots,\mathbf{b}_n)|\mathrm{d}^dx=V^*\mathrm{d}^dx$

$$
\int V^*\mathrm{d}^dx \sum_{n_i}e^{-2\pi i\sum_ix_in_i}
$$

注意到

$$
\int_0^1 \mathrm{d}x e^{-2\pi inx}=\delta_{n,0}
$$

那么积分为

$$
\sum_{n_i} V^* \prod\delta_{n_i,0}=V^*
$$

故给出

$$
A=V^*
$$

同样, 我们也给傅立叶变换的另一部分赋予含义

$$
\tilde{f}(\mathbf{k})=\Delta(\mathbf{k})S(\mathbf{k})\quad S(\mathbf{k})=\int_{\Gamma} \mathrm{d}^3x e^{-i\mathbf{k}\cdot\mathbf{x}}f(\mathbf{x})
$$

称 $S(\mathbf{k})$ 为结构因子, 并且可以看到 $\tilde{f}$ 只在 reciprocal lattice point 上不消失, 我们也可以做逆变换

$$
f(\mathbf{x})=\int\frac{\mathrm{d}^3k}{(2\pi)^3}e^{i\mathbf{k}\cdot \mathbf{x}}\tilde{f}(\mathbf{k})=\frac{V^*}{(2\pi)^3}\sum_{\mathbf{q}\in\Lambda^*}e^{i\mathbf{q}\cdot \mathbf{x}}S(\mathbf{q})
$$

这表明周期函数都是 reciprocal lattice 上的平面波的组合

### Brillouin Zone
我们把 reciprocal lattice 的 Wigner-Seitz cell 称为 Brillouin zone

待施工
