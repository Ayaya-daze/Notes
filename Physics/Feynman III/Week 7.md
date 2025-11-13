## $\alpha$ 衰变
这是量子隧穿的直接应用

>  $^{238}U \to ^{234}Th +\alpha\quad \tau\sim 45\text{亿年}$
>   应该对半衰期怎么这么大没有疑问了, 实际上再大的半衰期我们都能测(
>   实验上发现, 去看这些相同质量核素(相差两个单位带电量)发生 $\alpha$ 衰变出射的 $\alpha$ 粒子的能量, 与寿命的对数存在线性关系
>   比如 $^{238}U$ 能量为 $4.6\mathrm{MeV}$ , $^{228}U$ 能量为 $7\mathrm{MeV}$ , 他们的能量相近, 但寿命相差好几个数量级


>第二件事情是把 $^{238}U$ 放进一个盒子里, 把相同速度 $\alpha$ 粒子打进衰变得到的 $^{234}Th$ 的盒子中
>你会发现怎么打都打不进去, 即
> 这是一个不可逆的指数效应

>每当你发现不可逆的指数效应时, 你都可以猜这里面有量子隧穿在起作用

Gamov : 这可以用量子隧穿来解释:
在很远的地方, 核力是不重要的, 由库仑势主导, 在离原子核很近的地方, 核力产生了一个很深的势井
这就是 口袋模型, 就像把粒子关在盒子里面一样
假设 $\alpha$ 粒子的能量为 $E$ , 在盒子里就像一个自由粒子一样, 于是在遇到势垒时, 概率幅会像指数一样漏出来

>这件事是难以理解的, 原子核内极其混乱, 各种粒子混在一起, $\alpha$ 粒子怎么会像自由粒子一样?
>现在有更好的模型来理解: 液滴模型
>各种粒子混在一起像液滴一样颤抖, 会有不同的模式, 质子和中子可以结成对在液滴里面抖动, 如果动能大于 $0$ , 就有一个非零的概率出来
>如果从这个角度出发, 计算势能曲线, 可以发现: 这个势能和前面的势差不多
>***简单的模型是重要的***

于是可以用上次课的 WKB 近似来估算隧穿率 $$|\psi^{(WKB)}|^2\sim \mathrm{e}^{-2g/\hbar}$$其中 $$g=\int_{r_0}^{r_1} \mathrm{d}r\sqrt{2m(V(r)-E)}$$动能 $E$ 可以从实验中测的, 积分范围在经典禁戒区内

>这个模型如果对的话, 核力应该在一个很小的范围内
>可以想想在数量级下 $r_0$ 是核的半径, $r_1$ 是某个轨道半径, 于是 $r_0\ll r_1$ 

积分下限可以取 $0$ , 积分结果为 $$g\propto \frac{1}{\sqrt{E}}$$
>值得注意, 这里所有的量都是确定的
>Check: 请验证在这里取下限为 $0$ 是合理的

即衰变率 $$\Gamma \propto \frac{c}{\sqrt{E}}$$
> 这里 $\sqrt{E}$ 与两件事有关: 第一件事是积分内是根号, 第二件事是积分区域是库仑势
> 这告诉你: 在原子核外相互作用被库仑势主导
> 这也是很糟糕的结果: 这个结果和核力的具体形式无关
> 如果势能是其他曲线的话, 同样可以做这个计算估计

>并没有去解方程, 我们也可以得到系统的某些特征

# Chapter 8 Hamiltonian

不会去像书上一样重复无聊的数学, 在这里只对重要的东西评论一下:

>态 / 态矢 (state / state vector) $\mid \psi \rangle\in\mathcal{H}$ 
>这确实是矢量, 称他们的空间为 Hilbert 空间
>>这是从数学家那里借来的, 意思是某种完备的赋范线性空间
>至于收敛性, 我们认为这不重要(

实际上态应该是一种等价类, 意思是 $$\mid \psi\rangle\sim\mathrm{e}^{i\delta}\mid \psi\rangle$$如果将态归一化到 $1$ , 即 $$\langle \psi\mid \psi\rangle=1 $$即实际上态之间相差任意一个非 $0$ 的复数, 我们都认为是同一个态
即态实际上是 Hilbert 空间中的射线

>算符 (operator) : 线性变换 $A$
>实际上是对态的变换

其他都是线性代数, 唯一不同的是会用到无穷维线性空间中的结果, 比如 $$[\hat{x},\hat{p}]=i\hbar$$不对易并不神奇, 神奇的是这个对易子正比于单位

>这在有限维线性空间不可能成立

剩下的内容是无聊的, 不讲了
继续推广一下之前量子电路的记号
说有一个态 $\mid \psi\rangle$ 可以看作一个带左侧插口的器件, 同样, 左矢就可以理解为一个带右插口的器件
算符 $A$ 就是带双边插口的器件
规则是: 去拼接这些器件, 任何一个封闭好的没有多余插口的器件都是一个复数
比如 $$\langle\chi \mid A\mid \psi\rangle$$实际上这种写法是糟糕的, 如果 $A$ 不是线性变换, 这样写的时候其实暗含了结合律, 结果和你插的顺序没关系

>比如时间反演在这里就是糟糕的


比如 $$A\mid \psi\rangle$$带左插口, 这是一个右矢 $$\mid \chi\rangle \langle \psi\mid$$
带双侧插口, 是一个算符

这件事可以推广到张量 tensor

>张量 tensor
>实际上张量就是一个带很多插口的器件: 
>左边有 $p$ 个插口, 右边有 $q$ 个插口, 称这种张量为 $(p,q)-$ 型张量
>即一个 $(p,q)-$ 型的张量 $T$ 就是线性变换 $$T\colon (\mid\psi_1\rangle,\cdots,\mid\psi_1\rangle,\langle \chi_1\mid,\cdots,\langle \chi_p\mid)\mapsto z\in\mathbb{C}$$
>说人话一点是一个 $p$ 维对偶线性空间和 $q$ 维线性空间的积上的线性映射

>这可以得到一个操作: 张量积 tensor product
>可以把两个右矢放在一起组成一个 $(2,0)$ 型张量
>你可以对此做很多解释: 
>把两个左矢映到复数的线性变换, 把一个左矢映到右矢的线性变换 ...

>张量积是重要的
>把两个单粒子态的波函数加在一起 $$e^{ip_1x}+e^{ip_2x}$$
>即 $$\mid p_1\rangle+\mid p_2 \rangle$$
>这仍然是单粒子态!
>如何构造多粒子态, 正确的做法是张量积 $$\mid p_1\rangle \otimes\mid p_2\rangle,\mid p_1\rangle\mid p_2\rangle,\mid p_1 ,p_2\rangle$$后面两种是偷懒写法

>这可以用来描述量子纠缠:
>$$\begin{align}\mid \psi_1\rangle \in\mathrm{Span}\{\mid +_1\rangle,\mid-_1\rangle\}\\ \mid \psi_2\rangle \in\mathrm{Span}\{\mid +_2\rangle,\mid-_2\rangle\}\end{align}$$这样的张量积 $\mid +_1\rangle \mid -_2\rangle$ 称为可分的态 factoried state
>但是存在这样的态, 你如何做线性变换都不能变成一个可分的态, 这样的态叫纠缠态 entangled state
>比如 $$\mid +_1\rangle \mid -_2\rangle +\mid -_1\rangle \mid +_2\rangle$$
>重要的是
> ***一个态是不是纠缠态取决于你怎么取态空间的基***
>张量积空间的基实际上很简单, 就是上面的积做张量积
>在不同的基下, 纠缠态和可分态完全可以倒过来


## Schrodinger 方程

核心的观察时间演化同样可以视为对态的操作

你知道一个态 $\mid \psi(t_1)\rangle$ 是一个动力学状态, 在经过一段时间之后会变成另一个态 $\mid \psi(t_2)\rangle$ 
这样可以定义一个变换 (我们假设这是线性变换) -- 时间演化算符 $$\mathcal{U}(t_2,t_1)$$

>这个世界的代数可以不是线性代数, 但它偏偏就是线性代数
>时间演化算符是不是线性的完全由实验确定

>在一些情况我们可以写出时间演化算符, 比如存在经典极限的系统
>实际上路径积分就是在算时间演化

如果是 Feynman 的话, 下一步就是真的去做路径积分. 在这里采用另一种方式:
将 路径积分 变成 微分方程
这件事在物理里很常见, 如果你不会算一个积分, 就试着将它变成微分方程
即先考虑小段时间间隔, 取 $$t_2=t_1+\Delta t\quad \Delta t\text{极小}$$则 $$\mid \psi(t_1+\Delta t)\rangle =\mathcal{U}(t_1+\Delta t,t_1)\mid \psi(t_1)\rangle$$于是你可以对这个算符做展开 $$\mathcal{U}(t_2,t_1)\simeq \mathcal{U}(t_1,t_1)-\frac{i}{\hbar}H(t_1)\Delta t=\mathbf{1}-\frac{i}{\hbar}H(t_1)\Delta t$$
> 实际上这就是哈密顿量的定义!
> 前面的符号来自于我们的选择: 需要它具有能量的量纲, 需要它和前面的自由粒子相容...

那么去掉时间的标记 $$i\hbar\frac{\mid\psi(t+\Delta t)\rangle-\mid \psi(t)\rangle}{\Delta t}=H(t)\mid \psi(t)\rangle$$
取极限得到 $$i\hbar\frac{\partial }{\partial t}\mid \psi(t)\rangle=H(t)\mid \psi(t)\rangle$$
这就是 Schrodinger 方程

>上面的所做的全部就只是在定义哈密顿量:
>你不知道时间演化算符你就不知道哈密顿量! 所做的全部都是形式上的东西
>给一个系统, 如果你不给我哈密顿量, 那我什么也干不了, 也不能告诉你他在时间上的演化


>Remark
>1. $H$ 是时间演化的生成元 generator
>2. $\langle \psi\mid H\mid \psi\rangle$ 具有能量的含义
>3. 一般情形下 $H$ 是含时的, 显含时间的哈密顿量某种意义上是开放系统, 这导致能量不守恒


>需要区别什么叫显含时间
> $H$ 实际上有两种东西: 动力学变量 和 参数
> 比如谐振子的哈密顿量 $$H=\frac{p^2(t)}{2m}+\frac{1}{2}\omega^2x^2(t)$$
> 动力学变量是 $p,x$ , 而参数 $m,\omega$ 也可能含时
> 所谓显含时间是参数含时, 而不是动力学变量含时


## 再谈幺正性 unitarity -- 时间演化的幺正性

之间讲过幺正性意味着概率守恒, 实际上是考虑动力学状态 $$\langle \psi(t_2)\mid \psi(t_2)\rangle=\langle \psi(t_1)\mid \psi(t_1)\rangle$$
这个内积和你在什么时候做没有关系, 即 $$\langle \psi(t_1)\mid \mathcal{U}^\dagger(t_2,t_1)\mathcal{U}(t_2,t_1)\mid\psi(t_1)\rangle=\langle\psi(t_1)\mid \psi(t_1)\rangle$$一种选择是 $$\mathcal{U}^\dagger\mathcal{U}=\mathbf{1}$$
这就是幺正性的定义, 并且这可以立刻得到: 哈密顿量是 Hermite 的

>你可以想象 Hermite 是某种实数的推广, Unitarity 是某种指数的推广
>>Lie 群和 Lie 代数


上面这种描述在相对论里面是糟糕的, 如果你考虑 $\mid \psi(t_1)\rangle$ 这样的东西的话, 一个 Lorentz 变换会把时间和空间扭在一起, 之前用等时面来定义态的说法就相当糟糕了

## 解 Schrodinger 方程
单态系统: $\mid \psi(t)\rangle$ 
哈密顿 $H$ 就是一个实数
考虑不含时的话 $$i\hbar\frac{\partial }{\partial t}\mid \psi(t)\rangle=H\mid\psi(t)\rangle$$将 $H$ 替换为 $E$  , 解为 $$\mid \psi(t)\rangle =\mathrm{e}^{-i E/\hbar}\mid\psi(0)\rangle$$这就是定态, 现在我们用哈密顿量来定义能量了

双态系统:
一个具体的例子是氨分子 $NH_3$ 
一个重要的观察是 $N$ 和 $H$ 不在同一个平面上, 可以想象 氨分子有两种构型: 氮原子既可以在上面也可以在下面
并且他们都是稳定的 : 在上面 $\mid \uparrow\rangle$ , 在下面 $\mid \downarrow\rangle$

> 什么叫稳定的?
> 实际上就是势能极小: 按住 $H$ 去移动 $N$ , 你会发现有两个势能极小点

下面要做的事情是猜哈密顿量

>这是粒子物理中常做的事, 最大化利用对称性确定哈密顿量 , 剩下的都当作实验测量参数

认为这两个态是完备正交归一的, 则哈密顿在这个态的表象下是一个 $2\times 2$ 的矩阵
可以发现: 系统是对称的, 即对这两个态是对称, 故哈密顿的两个对角元是相同的
并且用量子隧穿的直觉: 哈密顿量的非对角元不为 $0$ ,存在某种隧穿现象, 用 $A$ 表示, 为隧穿幅
即这两个态都不是哈密顿的本征态
$$H=\begin{pmatrix} E &-A \\-A & E\end{pmatrix}$$
>应该问为什么这里的矩阵元都是全实数的, 这里面应该有哈密顿的某种性质

>同样, 对角元也不应该解释为上下两个态的能量: 他们不是哈密顿的本征态, 不应该有确定的能量


# Chapter 9 氨微波激射器

简单介绍今天想讲什么:
这节课其实讲的就是激光的原型 MASER 
上次课已经写出了氨分子在上态和下态表象下的哈密顿, 如果有一个非零的能量将两个态耦合在一起, 后果是这两个能级会发生分裂
MASER 干的就是利用这个能级差, 来制造一种工作来这两个能级差波段的激光器
但这里用的是电偶极矩, 氨分子有非零的电偶极矩, 如果将氨分子放在有梯度的电场里, 则和 Stern - Gelach 实验中相同, 氨分子会因为电偶极矩的取向不同而分裂
所以要做的就是设置一个有梯度的电场 $\varepsilon$ , 把能量较高的氨分子束引入到盒子里, 然后再加一个含时的电场 $\varepsilon(t)$ , 让电场振荡, 可以想象这里会发生共振, 高能量的氨分子会把能量给电场, 合理地调节氨分子束的速度, 不断地加入氨分子, 就可以不断地给盒子里的电磁驻波加入能量
当然, 这只是理想条件, 总之有一个不为 $0$ 的效率构造一个 MASER
但是今天的课与这个背景关系不大, 反而想借这个机会介绍一些观念和技术

>* 能级耦合 $\implies$ 能级分裂 $\implies$ Schrodinger 的猫(对称性自发破缺)
>* 尺度分隔 separation of scale $\implies$ 量级估计
能做尺度分隔的近似是我们能做物理的终极原因: 你做一个小滑块的实验怎么能忽略滑块内复杂的电子运动? 可以想象这些运动都发生在很短的时间内. 另外, 对于那些我们不知道的量, 实际上可以将它们参数化为未知数由实验确定

从数量级估计讲起

## 自然单位制
$$c=\hbar=k=1$$
>这些量都是很重要的量, 所以把他们都取为 1 , 相反 $m$ 是一个非常不自然的量, 其定义你会追溯到历史上一些奇怪的原因

自然单位制的后果是: 
$$\begin{align}1\mathrm{s} =10^8 \mathrm{m} \\ 1\mu m= (1eV)^{-1} \\1 K = 10^{-4}eV \\ 1g =10^{23}GeV\end{align}$$
并且不同的量纲塌在一起: $$\begin{align} &[E]=1 \\ &[\text{质量}]=[\text{温度}]=1 \\ &[\text{长度}]=[\text{时间}] =-1 \end{align}$$

电磁相互作用的强度由电荷来控制, 一般用精细结构常数控制 $$e^2\sim\alpha\simeq \frac{1}{137}$$
>所以你开平方之后发现电荷也是一个小于 $1$ 的量, 所以是一个弱的作用, 不同担心有强耦合之类的

牛顿引力: $$G_N\simeq (10^{19}GeV)^{-2}$$

>即牛顿引力常数是一个带量纲的量: 某种意义上电磁相互作用和引力本质上是不同的相互作用
>并且是一个比较弱的作用, 告诉你在氢原子束缚态的时候不用考虑引力的贡献

>重新估计屋子里可见光的光子数: 即来自于日光灯的光子数
>日光灯的功率, 时间 - 来自于屋子的尺寸除光速, 可见光的波长 $$100W \times\frac{10 m}{c}\times \frac{1}{1eV}=\frac{100\times 10^{19}eV}{10^8 m}\times \frac{10 m}{eV}$$

>估算宇宙中的所有光子 --  CMB 估计:
>CMB 的温度是 $2.7 K$ 于是知道数密度, 而宇宙的体积可以估计
>$$T^3R^3\sim (2.7K\times 10Gpc)^3\sim 10^{84}$$


## 尺度分隔
氨分子的红外光谱, 发现有两个明显的吸收峰 $930cm^{-1}\quad960cm^{-1}$

>这个吸收峰是怎么来的?
>实际上是这来源于氨分子的振动的第一激发态能级, 简单来说氨分子的势能像一个双势井
>而在一个基态实际上就像一个谐振子态, 然后就有不同的能级
>为什么是双峰? 实际上就来自于能级分裂: 
>第一激发态到基态的能级在 $950cm^{-1}$ 
>从第一激发态的能级向基态的两个能级跃迁时, 就有两个吸收峰
>实际上这里暗含了第一激发态的裂距比基态的裂距更大, 而裂距由隧穿幅控制, 即哈密顿的非对角元
>这是自洽的: 有更大的能量说明有更大的概率隧穿

之前双态系统的哈密顿 $$H=\begin{pmatrix} E &-A \\-A & E\end{pmatrix}$$
这里已经取了基础态: 我们总假设基础态时正交完备归一的
非对角元刻画了上态到下态的隧穿

>札记中所说的 $E$不为 $0$ 实际上已经取了势能最低点作为能量零点

随便取一个状态, 展开到基础态上 $$\mid \psi\rangle =C_{\uparrow}\mid\uparrow\rangle +C_{\downarrow}\mid\downarrow\rangle$$

于是 $$i\hbar\begin{pmatrix}\overset{\cdot}{C_{\uparrow} }\\ \overset{\cdot}{C_\downarrow{}}\end{pmatrix}=\begin{pmatrix}E & -A \\ -A & E\end{pmatrix}\begin{pmatrix}C_{\uparrow}\\C_{\downarrow}\end{pmatrix}$$

>正确的解法是对角化, 但是实际上你可以直接相加相减
>你在解二元方程组的时候从来不会对角化(

$$C_{\pm}=\frac{1}{\sqrt{2}}(C_{\uparrow}\pm C_{\downarrow})$$在新的基下的哈密顿 $$\begin{pmatrix}E-A & \\ & E+A\end{pmatrix}$$

这是哈密顿的本征态, 直接解是容易的
可以验证, 新的基础态也是正交归一完备的

>结果是出现两个能级, 一个能量更低, 一个能量更高
>实际上就是化学键: 相同能量的轨道做一次线性组合, 能量更低的是成键, 能量更高的是反键

解 Schrodinger 方程可以告诉我们系统对时间的演化: 可以问:
在 $t=0$ , 系统处于下态, 而在 $t$ 时刻, 系统处于上态的概率是多少
方便的做法是全部计算都在定态进行: 因为定态的时间演化全部来自于相因子
$$\begin{align}&t=0 \quad \mid \psi(0)\rangle =\mid \downarrow\rangle =\frac{1}{\sqrt{2}}(\mid +\rangle -\mid -\rangle)\\&t\quad \mid \psi(t)\rangle =\frac{1}{\sqrt{2}}(e^{iAt/\hbar}\mid +\rangle-e^{-iAt/\hbar}\mid -\rangle)\times e^{-iEt/\hbar}\\& \langle \uparrow\mid\psi(t)\rangle= \frac{1}{2}(e^{iAt/\hbar}-e^{iAt/\hbar})\times e^{-iEt/\hbar}\end{align}$$
即概率为 $$P_{\downarrow \to\uparrow}(t)=|\langle \uparrow\mid\psi(t)\rangle |^2 =\sin^2(\frac{A}{\hbar}t)$$
现在逐渐增加问题的复杂性: 加一个静电场 $\vec{\varepsilon}$ , 则有能量 $\Delta E=-\vec{\mu}\cdot\vec{\varepsilon}$ $$\Delta H =\begin{pmatrix}\mu\varepsilon & \\ & -\mu\varepsilon\end{pmatrix}$$
下面的问题是解完整的哈密顿量 $$H=\begin{pmatrix}E+\mu\varepsilon & -A \\ -A & E-\mu\varepsilon\end{pmatrix}$$做法是相同的: 解法是用指数解设解 $$\begin{cases}C_{\uparrow}=a e^{-i\lambda t/\hbar} \\C_{\downarrow}=be^{-i\lambda t/\hbar}\end{cases}$$
实际上就是在做 fourier 变换, 解出定态的能量 $$\lambda_{\pm}=E \pm\sqrt{A^2+\mu^2\varepsilon^2}$$
可以做出两个能量的图像, 当外电场增加时, 能级的距离就越来越大
> 一个观察是: 当外电场越来越大时, 能级的耦合变得不重要
> 所以在这个意义上, 才能做出能级耦合图: 不用考虑基态和第一激发态能不能耦合
> 他们对角元的差值很大: 基态和第一激发态能级差为 $960cm^{-1}$ , 而基态或激发态的能级差为 $1cm^{-1},30cm^{-1}$ 都相当小

>这件事能解释 Schrodinger 的猫:
>对双态系统: 总有概率从一个状态跑到另一个状态: 这件事情在经典上怎么不发生?
>粉笔放在桌子上总是倒向一个方向, 问题是: 它总是倒向一个方向, 为什么不能倒向某些态的线性叠加态?
>这里存在某种退相干
>如果把上面的双态系统取一种宏观极限, 会发生两件事情 $$H=\begin{pmatrix} E &-A \\-A & E\end{pmatrix}$$
>1. $A$ 会趋于 $0$ : 隧穿概率是指数小的
>2. 宏观系统是一个开放系统, 总存在环境的干扰, 开放系统的意思是对角元存在一些涨落 $\Delta H_i(t)$
>这个涨落使得我们来到对角元的差值远大于非对角元的区域
>粉笔倒向哪个方向? 由这次实验涨落更大的方向决定

现在让电场含时, 比如在一个谐振腔中 $\vec{\varepsilon}(t)=\varepsilon_0(e^{i\omega t}+e^{-i\omega t})$ 
做法也是解 Schrodinger 方程
1. 取 $\mid \pm\rangle$ 基, 则此时外场的项会到非对角元 $$H=\begin{pmatrix}E-A & \mu\varepsilon(t) \\ \mu\varepsilon(t) & E +A\end{pmatrix}$$
2. 如果同样设解 $$C_{\pm}=\gamma_{\pm}e^{-iE_{\pm}t/\hbar}$$
3. 此时系数含时 $$i\hbar \dot{\gamma}_{\pm}=\mu\varepsilon(t) e^{\mp i 2At/\hbar}\gamma_{\mp}$$
4. 重要的事情是 $\gamma_{\pm}$ 对时间的依赖相对于指数因子 $e^{-i2At/\hbar}$ 是慢的 $$|\frac{\dot{\gamma_{\pm}}}{\gamma_{\pm}}|\ll2 A$$

