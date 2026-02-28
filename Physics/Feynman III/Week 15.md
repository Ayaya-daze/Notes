最后提到了一些特别的东西: 哈密顿量的本征值只依赖于 $n$ , 不依赖于 $l$ 这是奇怪的
即当电子具有不同的空间构型居然具有相同的能量, 这源于动力学对称性

## 动力学对称性

当我们看到一些能量的简并的情形, 我们期待看到一些对称性应该存在, 他们可以把一个简并态变到另一个简并态而不改变哈密顿的本征值

在这里面的一种对称性是空间旋转对称性 $SO(3)$ 这使得本征值不依赖于 $m$ 
而我们在这里看到了更大的对称性, 这种对称性在经典情形我们也看到过

>开普勒定律告诉我们平方反比力下的粒子的轨道是封闭的椭圆, 但是椭圆需要的参数比圆多, 这在空间中选出了一个特殊的方向
>在这种情形我们知道有一个向量是守恒量, 从焦点指向近日点
>$$\vec{\mathcal{R}}=e^2\varepsilon$$
>这个矢量是守恒量源于更大的对称性, 在经典系统的表达为
>$$\vec{\mathcal{R}}=\frac{\vec{p}\times\vec{L}}{\mu}-e^2\frac{\vec{r}}{r}$$
>为了做把他变成量子系统的算符, 我们需要做量子化, 直接的方法是正则量子化
>$$\hat{\mathcal{R}}=\frac{\hat{p}\times\hat{L}-\hat{L}\times \hat{p}}{2\mu}-e^2\frac{\hat{r}}{|\hat{r}|}$$
>在这里需要提前做对称化, 因为这两个算符是不对易的, 因为 $\vec{p}$ 是矢量, 自然有对易关系
>$$[L_i,p_j]=i\epsilon_{ijk}p_k$$
>为了让量子化后的结果是 Hermite 算符, 则需要做对称化
>>大家自行完成计算验证
>有一些对易关系是不言自明的
>$$[L_i,\mathcal{R}_j]=i\epsilon_{ijk}\mathcal{R}_k\quad [H,\mathcal{R}_i]=0$$
>但是哈密顿与 $\mathcal{R}_i$ 的对易括号是 0 , 这个结果是神奇的 (check)
>这告诉我们存在一个新的对称性 (3个)
>首先它和 $L$ 不对易, 则当算符作用在 $L$ 的本征态上时, 会得到其他 $L$ 的本征态, 这会把不同 $L$ 的本征态联系在一起
>但是当它作用在哈密顿的本征态上时, 它又不会改变哈密顿的本征态, 即不会改变 $n$
>即由于这个算符的存在, 会使得不同 $l$ 的状态具有相同的 $n$ 
>并且, 当给定 $n$ 时, 对一个 $l$ 态作用 $\mathcal{R}$ , 可以得到所有的 $l$ 


>如果我们进一步去问, 这个对称性对应什么群
>我们知道: 当我们写下对易括号后, 就基本确定了这个群的局部性质
>这又是一个练习: 对这个线性组合
>$$\vec{A}_{\pm}=\frac{1}{2}(\vec{L}\pm \sqrt{\frac{\mu}{-2H}}\vec{\mathcal{R}})$$
>这个矢量的对易关系十分简单
>$$[{A_{\pm}}_{i},{A_{\pm}}_{j}]=i\epsilon_{ijk}{A_{\pm}}_{k}\quad [{A_{+}}_i,{A_{-}}_{j}]=0$$
>这构成了一个 $SO(3)$ 群

即氢原子的对称性为 
$$SO(3)\otimes SO(3)$$
生成元为 $\vec{A}_{\pm}$ 

>这个对称性和我们如何选取相互作用的势能密切相关, 这必须是 $1/r$ 
>同样, 如果我们加入相对论修正, 这个动力学对称性也会被破坏, 这会破坏牛顿势的形式
>精细结构就包含这一部分
>水星进动和精细结构差不多是一回事

在一个完全相对论性的系统里, 如果我们想对系统的所有对称性分类, 有一个非常简单的结果

## Coleman - Mandula 定理
在一些非常简单的假设下: 系统是相对论协变的, 这是一个非平庸的系统
可以证明: 相对论协变性允许的所有对称性分为两类

1. 时空对称性: 
	1. 平移
	2. 旋转
	3. boost
2. 内部对称性 internal symmetry
	1. 电荷守恒
	2. 重子数守恒, 轻子数守恒
	3. 等

区分的标准是: 如果把内部对称性的生成元叫 $Q$
则 $Q$ 必须和 $H,P,J$ 都对易, 意味着相对论所允许的所有对称性应该是一个直积
直积的时空部分是 poincare 群, 另一个部分是内部对称性的群

当然, 上面的动力学对称性的结果是 Coleman - Mandula 定理的 "反例", 当然这不是一个相对论性的系统
在一个相对论性的系统不存在势能这个东西, 如果有势能意味着相对论协变性必须被破坏掉

有一个简单的推论
这些内部对称性的生成元不能携带时空指标, 携带空间指标就不能和 $L$ 对易了
所以这是电荷是 Lorentz 标量的一个解释

## 宇称
在氢原子系统里看宇称的后果: 一个方便的定义是 $\vec{r}\to-\vec{r}$
则问前面找到的本征态如何变化, 只需要看波函数就好了
$$F_{nl}(|r|)Y_{lm}(\hat{r})$$
故宇称性质完全由球谐函数决定
$$\braket{\vec{x}|l,m}$$
则在宇称变换下
$$Y_{lm}\to (-1)^l Y_{lm}$$
这告诉我们宇称变换的性质通常与一些选择定则联系

## 选择定则 Selection Rule
只举一个例子: 在宇称变换下, 电磁相互作用控制的偶极跃迁必须满足
$$(-1)^{l_1-l_2}=-1$$
>偶极跃迁的意思是辐射的最低阶, 因为光子携带一个单位的角动量
>考虑跃迁
>$$l_1\to l_2$$
>这个过程的概率幅为
>$$\braket{n'l'm'|\vec{r}|nlm}$$
>在坐标表象下容易检查: 这个积分不等于 $0$ 当且仅当这个积分相差一个奇偶性, 而 $\vec{r}$ 是奇的, 则必须这两个波函数相差一个奇偶性


>为什么这个振幅形式是这样的?
>实际上是振幅
>$$\braket{n'l'm'|e^{-iHt}|nlm}\sim\braket{n'l'm'|1-iH\Delta t|nlm}$$
>这个哈密顿量必须含有电磁场的真空涨落, 这意味着哈密顿里面存在一个偶极项, 就会出来一个位置矢量

## 元素周期表

首先提几点
在氢原子中的电子的典型速度 $v/c\sim \alpha\sim1/137$
所以我们的计算精度不会超过 $\alpha$ 

对于原子序数为 $Z$ 的元素, 速度为 $Z\alpha$ , 则当 $Z\sim 100$ 时, 电子的相对论修正变得非常重要

相对论性的修正: "动质量" 
$$m\to\gamma m$$
则 bohr 半径会减小
$$\frac{\hbar^2}{me^2}\to \sqrt{1-v^2/c^2}\frac{\hbar^2}{me^2}$$
>这个结果可以解释为什么水银是液态的(?)

和 Hg 同一列的元素: Zn , Cd , Hg 

>为什么 Hg 的熔点很低, 这是一个典型的相对论效应: 为什么金属能形成晶体, 实际上来自于金属中的金属键
>容易液化意味着金属中的金属键不够强
>诚实地讲有两个原因, 不过其中一个原因是 Hg 的最外层电子的 Bhor 半径由于相对论效应会变得更小, 更不容易电离, 从而使得金属键更弱
>第二个原因叫 镧系收缩: Hg 中的一些电子对中心核的屏蔽作用很差, 导致电子的能级进一步下降

同样, 这列元素左边的元素: Cu, Ag , Au 他们的颜色也是相对论效应

另外元素周期表是有长度的, 实际上当周期表足够长, 就应该考虑完整的相对论效应了
这时候发生的事叫 Schwinger 效应, 比如对原子序数为 137 的元素, 在核内电场的大小已经足以产生 Schwinger 效应了
则至此以上的元素不可能稳定存在
现在已知原子序数最大为 118
实际上另外一点是: 这些重元素都是放射性的, 都有有限长的半衰期
也许你会反驳, 超过 137 的元素只是半衰期短一些
但是这里的本质差别在于控制衰变的相互作用: 
对前面的衰变由 $\alpha$ 衰变控制, 来自于隧穿, 是指数慢的
但是 Schwinger 效应是电磁相互作用, 所以他的半衰期会显著快于前一种

# Chapter 20 算符

实际上这章的内容已经被之前覆盖了
现在给之前用到的算符给一个良好定义

位置算符: 
去用经典的概率分布去刻画粒子的位置 $\mathcal{P}(x)$ , 结果是
$$\braket{x}=\int \mathrm{d}x \mathcal{P}(x)x$$
在量子力学里, 知道
$$\mathcal{P}(x)=|\psi(x)|^2$$
则立即知道
$$\braket{x}=\int \mathrm{d}x\braket{\psi|x|\psi}$$

这告诉我们算符在态上的期望值
$$\braket{\hat{x}}=\braket{\psi|\hat{x}|\psi}$$
即算符的定义为
$$\hat{x}\ket{\psi}=x\ket{\psi}$$
即在位置基础态下对角的一个算符, 则
$$\braket{y|\hat{x}|x}=x\delta(y-x)$$
这是一个不平庸的结果: $\ket{x}$ 实际上不是态空间里的态
即这个算符不是一个在量子力学下定义好的算符

>如果去问这里到底有什么问题: 就去把时空离散化为格子

对动量也有相同的结果, 这样就可以计算动量和位置的对易括号
$$[\hat{x},\hat{p}]=i\hbar$$

最后一节课讲一些别的东西: 

# Chapter 21 为什么两个铁球同时落地

一次特殊的报告会

为什么引力质量和惯性质量是成正比的?
这件事已经被牛顿讨论过了

为什么等效原理是对的?
Einstein 从等效原理出发得到的广义相对论

如果做一些简单的基础假设, 可以证明等效原理是可以被导出的事实

引力子: $m=0 ,s=2$ 我们并没有观测到过引力子, 但是如果波粒二象性是对的, 那么就应该有引力子
并且长程性表明为零质量, 而引力波的极化结果表明引力子有两个螺旋度

散射振幅: 需要相对论协变性的量子力学
而散射振幅应该是 Lorentz 不变的

大概路径
1. Green 函数方法
2. 双缝干涉 --> Feynman 图
3. 能动量守恒和质壳条件
4. 引力子的极化
5. Weinberg soft theorem (1964)


## Green 函数方法 (经典)

Maxwell 方程
$$\Box A_{\mu}=0\implies (-\frac{\partial^2}{\partial t^2}+\nabla^2)A_\mu$$
先忽略极化, 即考虑标量场, 给场加一个源 $f(t,\vec{x})$
$$\Box \phi =f(t,\vec{x})$$
知道 $\phi$ 的分布的方法就是去解这个方程

Grenn 函数方法的基本想法是先去解点源 
$$\delta^{(3)}(\vec{x})$$
取点源的场方程的解叫 Green 函数
$$\Box_xG(x,y)=\delta(x-y)$$
这任意点源的解可以用 Green 函数叠加得到
$$\phi=\int \mathrm{d}y G(x,y)f(y)$$
如何解, 意思是取算符的逆
$$G(x,y) =\frac{1}{\Box_x}\delta(x-y)$$
得到逆的方法是进入算符的对角基, 所以先用 Fourier 变换
$$G(x,y)\to G(k^\mu)\quad\delta(x,y)\to1\quad\Box_x\to-k_\mu k^\mu=E^2-\vec{k}^2$$
则 Green 函数为
$$G(k^\mu)=\frac{1}{E^2-\vec{k}^2}$$
实际上如果满足质壳条件, Green 函数已经炸了
当然, 一些正确的处理是在分母加上别的东西
$$G(k^\mu)=\frac{1}{E^2-\vec{k}^2\pm i\epsilon}$$
实际上这就是取了某种边界条件
确定物理意义的办法是去看不含时的解, 即
$$\Box G\to\nabla^2 G=\delta^{(3)}(0)$$
解是简单的
$$G\propto 1/r$$
推广到有质量场 $m\neq 0$
$$(\Box +m^2)\phi=0$$
同样, Green 函数也是质壳条件
$$G(k^\mu)=\frac{1}{E^2-m^2-\vec{k}^2}$$
## 双缝干涉

这个课一开始就是从双缝干涉得到量子力学的基本原理
双缝干涉的例子告诉了我们如何构造概率幅:
1. 对所有可能的路径求和
2. 每条路径的幅为传播幅 $\times$ 相互作用振幅, 比如 $\braket{S|1}a\braket{1|A}$ 这实际上就是 Feynman 图

比如说两个电子通过光子发生了散射, 由于相互作用的时间极短, 可以想象四个粒子都有相同的能量

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, decorations.markings, arrows.meta}

\begin{document}
% 调节 scale 可以整体放大缩小
\begin{tikzpicture}[scale=1.3, line width=1pt,
    % --- 样式定义 ---
    photon/.style={decorate, decoration={snake, amplitude=2pt, segment length=4pt}},
    fermion/.style={postaction={decorate},
        decoration={markings,mark=at position 0.55 with {\arrow{Stealth[scale=1.2]}}}},
    label_text/.style={font=\small} % 字体大小
]

    % =========================================
    % 【左图：图 (a)】 左边电子先发射光子
    % 整体向左平移 2.5 单位
    % =========================================
    \begin{scope}[shift={(-2.5, 0)}]
        
        % --- 1. 定义坐标 (折线逻辑) ---
        % 左路电子：从下(-1) -> 往里折(-0.5) -> 往外弹(-1)
        % 注意 v_L (顶点) 的 Y 是 -0.5 (较早/较低)
        \coordinate (L_in)  at (-1.0, -2.0);
        \coordinate (L_v)   at (-0.5, -0.5); % 左顶点：低
        \coordinate (L_out) at (-1.0,  2.0);

        % 右路电子：从下(1) -> 往里折(0.5) -> 往外弹(1)
        % 注意 v_R (顶点) 的 Y 是 0.5 (较晚/较高)
        \coordinate (R_in)  at ( 1.0, -2.0);
        \coordinate (R_v)   at ( 0.5,  0.5); % 右顶点：高
        \coordinate (R_out) at ( 1.0,  2.0);

        % --- 2. 连线 ---
        % 左电子流
        \draw[fermion] (L_in) -- (L_v) node[midway, left] {$e^-$};
        \draw[fermion] (L_v) -- (L_out) node[midway, left] {$e^-$};
        
        % 右电子流
        \draw[fermion] (R_in) -- (R_v) node[midway, right] {$e^-$};
        \draw[fermion] (R_v) -- (R_out) node[midway, right] {$e^-$};

        % 交换光子 (左低 -> 右高)
        \draw[photon] (L_v) -- (R_v) node[midway, below right] {$\gamma$};
        
        % 图注
        \node[label_text] at (0, -2.5) {$A_1$};
    \end{scope}


    % =========================================
    % 【右图：图 (b)】 右边电子先发射光子
    % 整体向右平移 2.5 单位
    % =========================================
    \begin{scope}[shift={(2.5, 0)}]

        % --- 1. 定义坐标 ---
        % 注意这里 Y 坐标的反转
        
        % 左路电子：顶点变高了 (Y=0.5)
        \coordinate (L_in_2)  at (-1.0, -2.0);
        \coordinate (L_v_2)   at (-0.5,  0.5); % 左顶点：高 (晚)
        \coordinate (L_out_2) at (-1.0,  2.0);

        % 右路电子：顶点变低了 (Y=-0.5)
        \coordinate (R_in_2)  at ( 1.0, -2.0);
        \coordinate (R_v_2)   at ( 0.5, -0.5); % 右顶点：低 (早)
        \coordinate (R_out_2) at ( 1.0,  2.0);

        % --- 2. 连线 ---
        \draw[fermion] (L_in_2) -- (L_v_2);
        \draw[fermion] (L_v_2) -- (L_out_2);
        
        \draw[fermion] (R_in_2) -- (R_v_2);
        \draw[fermion] (R_v_2) -- (R_out_2);

        % 交换光子 (右低 -> 左高)
        \draw[photon] (R_v_2) -- (L_v_2) node[midway, below left] {$\gamma$};

        % 图注
        \node[label_text] at (0, -2.5) {$A_2$};
    \end{scope}

    % --- 可选：画个时间轴在最左边 ---
    \draw[->, thick, gray] (-4.5, -1) -- (-4.5, 1) node[midway, left] {Time};

\end{tikzpicture}
\end{document}
```

两个过程为 1 粒子发生光子 或者 2 粒子发射光子

可以想象在每次相互作用时, 在相互作用的顶点上能量, 动量是不是守恒的
如果能动量守恒, 有
$$E_{\gamma} = E_1-E_3\quad \vec{p}_{\gamma} =\vec{p}_1-\vec{p}_3$$
质壳条件
$$E_1^2=p_1^2+m_1^2\quad E_2^2=p_2^2+m_2^2$$

现在来检查光子的质壳条件

$$(E_1-E_3)^2=(\vec{p_1}-\vec{p_3})^2=|p_1|^2+|p_3|^2-2p_1p_3\cos\theta$$
如果 $\theta$ 是可以连续调节的, 那么光子的质壳条件经常是不满足的
但是这并不奇怪, 我们知道散射过程的时间极短, 所以能量具有不确定度, 那么在质壳条件的范围内表明动量也有不确定度
这可以解释这一点

于是我们有两种选择
1. 放弃能动量守恒, 但保证在壳条件. 这就是量子力学的微扰论
2. 放弃在壳条件, 坚持顶点上的能动量守恒

Feynman 选择第二条路: 如果将两种路径相加, 可以得到一个 Lorentz 不变的表达式
$$A_1+A_2\propto\frac{1}{E_{\gamma}^2-|\vec{k}_\gamma|^2}$$

只要两个点的距离是类空的, 讨论哪个过程谁先谁后就是有歧义的, 应该做的是把两个过程加在一起
并且这个结果正比于光子的 Green 函数, 正比的原因是我们忽略了发射和吸收的幅, 只有传播幅
即 Green 函数的另一个物理意义是刻画了场所对应的粒子的传播

完整的写法是
$$A_1+A_2=\frac{Q_1Q_2}{E_\gamma^2-|k_{\gamma}|^2}$$
>对这个结果做 Fourier 变换就得到了所熟知的 Coulomb 力

Feynman 的洞见是, 这个振幅中的传播幅恰好是 Green 函数, 并且这三部分幅都是 Lorentz 不变的
我们有一个自始至终都协变的理论

>为什么发射, 吸收的幅的强度正比于电荷? 这是我们对电荷的定义

这就是 Feynman 规则

即这种方式的构造可以给我们不在壳的粒子, 如果在壳, 振幅是发散的

>这个发散是有明确的物理意义的, 如果有在壳条件, 计算散射的结果应该是所有过程做时间的积分, 如果是一个有限长的时间, 光子是可以不在壳的, 而如果光子在壳, 则表明光子可以传播非常长的时间, 这个积分往往是发散的
>并且这个发散的留数是两种情况振幅的乘积, 这叫在壳因子化 ?

>你能看到的光子都不可能是在壳的, 这个世界不存在在壳的光子
>你看到的光子总是传播了有限长的时间, 在壳只是一种理论近似
>世界上最在壳的光子是 CMB 光子

## 引力子的极化

不再仔细提光子的极化
光子的极化矢量 
$$\epsilon^{+}_i =\begin{pmatrix}1\\i\\0\end{pmatrix}\quad \epsilon^{-}_i =\begin{pmatrix}1\\-i\\0\end{pmatrix}$$
前面已经提到过, 如果想去构造一种 Lorentz 不变的极化四矢量, 这是不可能的
$$\epsilon_{\mu}\to \Lambda_{\mu}^\nu\epsilon_\nu +\alpha p_{\mu}$$
引力子的极化是类似的 $\epsilon_{\mu\nu}(p)$
则在 Lorentz 变换下, 会出现多余的成分
$$\xi_{\mu}p_\nu+\xi_{\nu}p_{\mu}$$
>极化矢量的指标是对称的, 自旋 2 是两个自旋 1 的全对称化

我们可以推广, 比如自旋 3 的无质量粒子: $\epsilon_{\mu\nu\rho}$
则在 Lorentz 变换下
$$\xi_{\mu\nu}p_{\rho} +\text{全对称项}$$
>对于光子的情形, 一个简单的回答是: 光子的极化矢量总是和动量垂直

Weinberg (1964) 任意散射过程 ($N\to N'$)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, decorations.markings, arrows.meta, calc}

\begin{document}
% scale: 整体缩放, 1.0 比较适中，想大一点改 1.2
\begin{tikzpicture}[scale=1.3, line width=1pt,
    % --- 样式定义 ---
    photon/.style={decorate, decoration={snake, amplitude=2pt, segment length=4pt}},
    fermion/.style={postaction={decorate},
        decoration={markings,mark=at position 0.6 with {\arrow{Stealth[scale=1.2]}}}},
    % 硬过程Blob (灰色圆球)
    hard_blob/.style={circle, draw=black, fill=gray!30, minimum size=1.2cm, inner sep=0pt},
    % 图注文字样式
    caption/.style={text width=3cm, align=center, font=\small, yshift=-2.5cm}
]

    % =========================================
    % 【图 1】 ISR: 初态辐射 (入射腿发射)
    % 向左平移 4 个单位
    % =========================================
    \begin{scope}[shift={(-4, 0)}]
        \node[hard_blob] (b1) at (0,0) {Hard};
        
        % 1. 正常的腿 (右下入，两上出)
        \draw[fermion, shorten >= -1pt] (1, -1.8) -- (b1.315);
        \draw[fermion, shorten <= -1pt] (b1.135) -- (-1, 1.8);
        \draw[fermion, shorten <= -1pt] (b1.45)  -- (1, 1.8);

        % 2. 发射光子的腿 (左下入)
        \coordinate (in_start) at (-1, -1.8);
        \coordinate (emit_pos) at (-0.7, -1.0); % 发射点位置

        % 第一段：从无穷远 -> 发射点
        \draw[fermion] (in_start) -- (emit_pos);
        % 第二段：从发射点 -> Blob
        \draw[fermion, shorten >= -1pt] (emit_pos) -- (b1.225);
        
        % 3. 光子 (向左飞出)
        \draw[photon] (emit_pos) -- (-1.8, -0.5) node[midway, left] {$\gamma$};

        % 标签
        \node[caption] at (0, 0) {(a) Initial State\\ Radiation};
    \end{scope}


    % =========================================
    % 【图 2】 FSR: 末态辐射 (出射腿发射)
    % 居中 (不平移)
    % =========================================
    \begin{scope}[shift={(0, 0)}]
        \node[hard_blob] (b2) at (0,0) {Hard};

        % 1. 正常的腿 (两下入，左上出)
        \draw[fermion, shorten >= -1pt] (-1, -1.8) -- (b2.225);
        \draw[fermion, shorten >= -1pt] (1, -1.8)  -- (b2.315);
        \draw[fermion, shorten <= -1pt] (b2.135) -- (-1, 1.8);

        % 2. 发射光子的腿 (右上出)
        \coordinate (emit_pos_2) at (0.7, 1.0); % 发射点
        \coordinate (out_end)    at (1.2, 1.8);

        % 第一段：Blob -> 发射点
        \draw[fermion, shorten <= -1pt] (b2.45) -- (emit_pos_2);
        % 第二段：发射点 -> 无穷远
        \draw[fermion] (emit_pos_2) -- (out_end);

        % 3. 光子 (向右飞出)
        \draw[photon] (emit_pos_2) -- (1.8, 0.5) node[midway, right] {$\gamma$};

        % 标签
        \node[caption] at (0, 0) {(b) Final State\\ Radiation};
    \end{scope}


    % =========================================
    % 【图 3】 Internal: 硬区域直接发射
    % 向右平移 4 个单位
    % =========================================
    \begin{scope}[shift={(4, 0)}]
        \node[hard_blob] (b3) at (0,0) {Hard};

        % 1. 所有的腿都是直的
        \draw[fermion, shorten >= -1pt] (-1, -1.8) -- (b3.225);
        \draw[fermion, shorten >= -1pt] (1, -1.8)  -- (b3.315);
        \draw[fermion, shorten <= -1pt] (b3.135) -- (-1, 1.8);
        \draw[fermion, shorten <= -1pt] (b3.45)  -- (1, 1.8);

        % 2. 光子从 Blob 表面长出来
        % 从右侧 (角度0) 出来
        \draw[photon] (b3.0) -- (1.5, 0) node[right] {$\gamma$};

        % 标签
        \node[caption] at (0, 0) {(c) Internal/Hard\\ Emission};
    \end{scope}

    % --- 时间轴 (公用) ---
    \draw[->, thick, gray] (-5.5, -1.5) -- (-5.5, 1.5) node[midway, left] {Time};

\end{tikzpicture}
\end{document}
```

即粒子在散射过程中发射一个光子

这个过程在光子动量 $q\to 0$ 下是简单的, 即软极限

如果让光子的动量趋于 0 , 则发射过程线上的光子是在壳的
则可以想象
$$\underset{q\to 0}{\lim} \mathcal{M}(q)\to\frac{1}{q}$$
我们应该把每种过程的幅加在一起
有三种可能
1. 光子从初态发射
2. 光子从末态发射
3. 光子从中间态发射

那么前两种的振幅在 $q\to 0$ 下行为与 $1/q$ 相同, 但中间的过程不是这样, 因为中间过程的光子不是在壳的 
则中间过程的幅在 $q\to0$ 时 表现为 $\mathcal{O}(q^0)$ 故可以忽略这种情况

在 $q\to 0$ 下

第一种情况: 第 $i$ 个粒子发射光子
幅正比于中间过程的 Green函数 乘上发射光子的幅
$$\frac{Q_i\epsilon^\mu(p_i)_{\mu}}{(p_i-q)^2-m_i^2}\to\frac{Q_i\epsilon^\mu(p_i)_\mu}{-2p_i\cdot q}$$
>收缩光子极化矢量的指标只能是 $p_i$ 

第二种情况是类似的, 在 $q\to 0$ 时得到
$$\to \frac{Q_j(\epsilon p_j)}{2p_j\cdot q}$$
总的幅为
$$\underset{q\to 0}{\lim}\mathcal{M}=\mathcal{M}_0\left\{\sum_{i\in\text{入射}}\frac{-Q_i (p_i\cdot\epsilon)}{2p_i\cdot q}+\sum_{j\in\text{出射}}\frac{Q_j(p_j\cdot\epsilon)}{2 p_j\cdot q}\right\}$$
问题是 $p\cdot \epsilon$ 不是一个 Lorentz 标量
唯一的要求是要求多变出来的量为 0 , 我们知道多变出来的量是动量
那么 Lorentz 不变性要求
$$\sum_{i\in\text{入射}}-Q_{i} +\sum_{j\in\text{出射}}Q_j=0$$
这就是电荷守恒

现在再来看一个通过引力子的散射过程, 做完全相同的分析
同样, 对结果做 Lorentz 变换, 仍然应该得到一个等式
如果每个粒子参与引力相互作用的强度为 $\kappa_i$ 

同样的结果为
$$\sum_{i\in\text{入射}}-\kappa_i p_i+\sum_{j\in\text{出射}}\kappa_jp_j=0$$
不同的在于需要动量去做一个指标收缩
而动量守恒要求
$$\sum_{i\in\text{入射}} p_i+\sum_{j\in\text{出射}}p_j=0$$
这几乎就要求所有的 $\kappa$ 都相同, 这就是等效原理
我们可以做同样的事情到零质量的自旋 3 粒子,那么就再需要一个动量指标做收缩, 这和动量守恒的结果不相容
即: 长程相互作用不能由自旋 3 及以上的无质量粒子传递

>为什么 $\kappa$ 是相互作用粒子的质量?

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, decorations.markings, arrows.meta}

\begin{document}
% ▼▼▼【参数调节区】▼▼▼
% scale: 整体大小 (1.5 倍)
% line width: 线条粗细 (1pt)
\begin{tikzpicture}[scale=1.5, line width=1pt,
    % 样式定义
    photon/.style={decorate, decoration={snake, amplitude=2pt, segment length=5pt}},
    fermion/.style={postaction={decorate},
        decoration={markings,mark=at position 0.6 with {\arrow{Stealth[scale=1.2]}}}}
]

    % ▼▼▼【坐标调节区 - 这里的数值决定了"折角"的大小】▼▼▼
    
    % --- 上半部分 (Top) ---
    % 入射点 (左上，Y=1.8) -> 撞击点 (中间，Y=0.6) -> 出射点 (右上，Y=1.8)
    % 注意：1.8 和 0.6 的差距越大，折角越明显！
    \coordinate (in_top)    at (-1.5,  1.8); 
    \coordinate (v_top)     at (0,     0.6);   
    \coordinate (out_top)   at (1.5,   1.8);  

    % --- 下半部分 (Bottom) ---
    % 入射点 (左下，Y=-1.8) -> 撞击点 (中间，Y=-0.6) -> 出射点 (右下，Y=-1.8)
    \coordinate (in_bottom) at (-1.5, -1.8); 
    \coordinate (v_bottom)  at (0,    -0.6);   
    \coordinate (out_bottom) at (1.5, -1.8);  

    % ▼▼▼【连线区】▼▼▼
    
    % 上路电子 (折线)
    \draw[fermion] (in_top) -- (v_top) node[midway, above=2pt] {$e^-$};
    \draw[fermion] (v_top) -- (out_top) node[midway, above=2pt] {$e^-$};
    
    % 下路电子 (折线)
    \draw[fermion] (in_bottom) -- (v_bottom) node[midway, below=2pt] {$e^-$};
    \draw[fermion] (v_bottom) -- (out_bottom) node[midway, below=2pt] {$e^-$};

    % 中间交换光子
    \draw[photon] (v_top) -- (v_bottom) node[midway, right] {$\gamma$};

\end{tikzpicture}
\end{document}
```