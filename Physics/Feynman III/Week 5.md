# Chapter 5 自旋 - 1
先继续上次的内容
首先是上次课数的概率 $$P(nA \to 0 A ) = n|a|^2 \Delta S \times P((n-1)A\to 0A) $$怎么解释这个概率, 实际上是一种条件概率的解释 $$P(nA \to 0A)=P(A\to (n-1)A)\times P((n-1)A\to 0A)$$对比这两个式子即可(之前也写过)

之前关于黑体辐射的解释:
光子的频率谱的 peak: 处在温度为 $T$ 的光子气体的典型频率是 $\frac{kT}{\hbar}\sim T$ 即 $$E\sim \omega \sim T$$请记住$$1 K \sim 10^{-4} eV$$所以马上可以回答一些问题

>电离氢原子需要的温度
>直接估算在 十万开左右

>我们房间里面的光子气体的数量
>$T\sim 100 K \sim 10^{-2}eV$ 回忆 Planck 公式 $$\frac{\mathrm{d}E}{\mathrm{d}\omega}\sim\frac{\hbar\omega}{e^{\hbar\omega/kT}-1}\times \omega^3$$简单的计算, 光子的数密度由 $T^3$ 控制 (能量和长度有相反的量纲, 而一个频率积掉了)
>记住 $1eV \sim 1 (\mu m)^{-1}$ (考虑一个能量为 $1eV$ 的光子的波长) : 你可以马上估算钠黄光光子的能量
>而屋子的体积 $V \sim 10^2 \times (10^6 \mu m)^3\sim 10^{20} (eV)^{-3}$ 数密度 $N \sim 10^{-6} eV^3$
>故光子数约为 $10^{14}$ 可以差几个数量级
>重要的是上面的几个物理关系得到的量纲关系, 加减乘除是简单的

>估计房子里所有可见光的光子的数量?


>这些 trick 很好用, 比如宇宙学里面 
>微波背景温度 $\sim 2.7 K$ , 则可以立即知道这种光子的波长, 于是可以推知: 探测这种光子所需要的天线的尺度

继续之前的量子场论

模式具有谐振子的形式 $$\frac{\mathrm{d}^2}{\mathrm{d}x^2}\phi_k + \omega^2 \phi_k =0$$后果是谐振子的能量是量子化的, 这不是一个经典的结果 $$E= \hbar \omega \left( n +\frac{1}{2} \right)$$你可以考虑降低盒子里的降低光强, 你就会在足够低时看见离散的光强
这里有一个理论假设: 电磁场的方程和谐振子的方程相同, 怎么量子化谐振子, 就该怎么量子化电磁场

>什么是量子化?
>我们相信: 量子力学是比经典力学更基本的理论, 即存在一个经典极限, 使得量子理论退化到经典情形, 但是从经典理论反推的量子理论不是唯一的
>量子化即: 找到一种量子理论, 使得它的经典极限退化到经典理论
>实际上量子化电磁场就是找到一个电磁场的量子理论, 使其在经典极限下退化到 Maxwell 方程 (在盒子里的电磁波)
>这么做对不对? 只要实验上验证了, 就可以相信他是对的

>如果你会做盒子里的电磁场的量子化, 你就可以像 Boltzmann 一样数光子的模式, 然后用 Boltzmann 分布, 得到盒子里的光子的平均占有数
>现在已经知道电磁场的量子化了, 那直接用 Boltzmann 分布即可, 即平均占有数应该计算这样的东西 $$1 + ne^{n\hbar \omega/kT}+\cdots \to \frac{1}{e^{\hbar \omega/kT}-1}$$注意这是指给定模式 (频率) 下, 光子处于这个模式的平均占有数, 已经对模式以外的东西做了积分, 所以这也是为什么叫平均占有数


>问: 经典的谐振子是因为他有一个 schrodinger 方程, 而电磁场里面有吗?
>量子场论里有一个极其丑陋的电磁场的 schrodinger 方程, 但没人会想去用

>问: 对谐振子为什么可以用 Boltzmann 分布?
>注意 Boltzmann 分布不是经典的
>为什么是对的?
>在统计力学中回答: 
>考虑一大堆球在盒子里相互作用, 问他们平衡下来的分布
>实际上就是计算相空间的密度(或者态空间的密度矩阵), 这就直接得到 Boltzmann 分布, 没有什么经典的假设
>那 bose , fermi 分布?
>注意到上面计算的是给定频率的平均占有数, 而不是给定态的分布, 这两者是不同的. 两者形式的相同带来了概念的混淆


回到主线:这章实际上就是在“科普”线性代数

>线性代数不是上帝放进量子力学中的, 而是我们自己推出来的

## Stern - Gerlach 实验
实验的描述见讲义

银原子, 自旋 $\frac{1}{2}\sim \mu$ 磁矩, 则磁场会给磁矩一个能量 $\Delta E = -\vec{\mu}\cdot \vec{B}$ 
考虑从 $+y$ 方向射出, 磁场方向为 $+z$ , 磁场会给磁矩一个力 
实验结果
* 银原子自旋不为 $0$ , 且存在量子化

>实验的小故事
>实验之后大家都发现了粒子有自旋, 这件事情最早知道的是 kionig , 他首先做了计算, 然后问 pauli , Pauli 直接否定了
>接着 ernfest 的两个学生也做了相同的计算, ern 鼓励他们把结果投出去
>这两个学生又去问了 boltzmann , boltzmann 给出了 pauli 相同的回答, 但文章已经发出去撤不回了
>所以现在大家都认为自旋的概念是

对自旋的理解: 
自旋的确可以理解为某种 内禀角动量, 这件事情不是很难理解:

> 常说角动量是空间旋转的效益, 但没有旋转也可以有角动量.
> 就像能量是运动的效应, 显然没有运动也可以有能量

自旋的取值 $$|\vec{s}|^2 =\hbar^2 s(s+1)\quad s= 0,1/2,1,\cdots$$然后问自旋在某个方向的取值, 这个取值也是量子化的 $$s_z = m\hbar \quad m=-s,-s+1,\cdots,s$$所以自旋 -  1/2 的情形有 $m =\pm 1$ , 而自旋 - 1  有 $m = -1, 0 ,1$  , 即这是一个三态系统

Stern - Gerlach -Feynman 偏振仪 polarizer / filter

同样引导银原子到一个带梯度的磁场中, 然后再加一个反向的磁场让他们聚拢起来, 并且加一些电场调控粒子的速度, 使得粒子在速度意义上回到初态

>Feynman 在 60 年代上的这节课, 如果他在今天上这节课他一定会讲量子电路
>所以我们把它叫做 qutrit -- 实际上这就是一种量子电路

>这个偏振器的要点: 粒子束进入偏振仪后可以走三种可能的路径, 但要求每条路径粒子获得相同的相位, 这不难做到

>游戏规则: 可以在偏振仪中加挡板, 得到不同的偏振仪
> $I(S)$ identify 即不加任何挡板
> $P_j(S)\quad j = \pm 1 ,0$ 在第 $j$ 条路不加挡板, 其他都加挡板
> 你可以发现在过了 $P$ 之后粒子束被纯化了 purify

新的记号 $\langle f\mid i\rangle$  这个 bra-ket 可以拆开
用 ket 标记粒子的三种状态 $\mid +s\rangle , \mid 0\rangle , \mid -s \rangle$ 
考虑这件事情, 在引出粒子束时, 我们总加一个 $P$ 而不加 $I$ 
刻画这个事情: 一开始粒子的状态不知道, 为 $\mid ?\rangle$ , 然后施加一个操作 $P_i(S)$ , 然后我们知道出来的粒子一定在 $\mid iS\rangle$ 态, 
然后继续往后面加偏振片 $P_j(S)$
即 $$\mid ? \rangle \xrightarrow {P_i(S)} \mid iS\rangle\xrightarrow{P_j(S)}\mid jS\rangle$$
然后可以得到 幅 $$\langle jS\mid iS\rangle =\delta_{ij}$$这个事情更奇妙的地方在于, 这和偏振的方向无关, 即可以把 $S$ 去掉  $$\langle j\mid i\rangle =\delta_{ij}$$
>实际上这里应该还有一个相因子, 但是我们总可以调整状态的相位抵消掉, 所以去掉了
>即重定义态 $$\mid iS \rangle \to e^{i\delta}\mid iS \rangle$$注意这里不是整体添加相位

这个结果叫做正交归一条件

第二件事: 如果中间加入一个 $I$ 挡板, 会发生什么, 但由于做了三条路径获得的相位都相同, 实际上就是什么都没做
$$\mid iS\rangle \xrightarrow{} \begin{cases}+T \\0T \\ -T\end{cases} \to \mid jS\rangle$$然后得到幅的关系, (操作在线性代数中就是一个算符) $$\langle jS\mid I(T)\mid iS\rangle = \sum_{k=\pm1,0}\langle jS\mid kT\rangle \langle kT\mid iS\rangle$$因为这对任意的态 $S$ 都成立, 有 $$ I = \sum_{k=\pm1,0}\mid kT\rangle \langle kT\mid$$
> 可以理解成一堆插口 (映射) 的角度理解这个等号:
> 这是一个映射的等式, 意思是你在左右两边放 braket , 最后得到的复数都是相同的
> 这在之前接触过: 矢量等式为什么是对的? 实验上观测到的都是标量
> 实际上同样这里隐藏了投影的矢量

上面这个条件叫做完备性条件, 再次, 甚至可以抹去 $T$ $$\boxed{ I = \sum_{k=\pm1,0}\mid k\rangle \langle k\mid}$$

那么现在对任意一个态 $\mid \phi \rangle$ , 像在线性代数中一样, 用一个完备的基去展开 $$\mid\phi\rangle = \sum_{i=\pm1,0}\mid iS\rangle\langle iS\mid \phi\rangle$$注意 $\langle iS \mid \phi \rangle$ 实际上是一个复数, 即 $\mid \phi\rangle$ 在上面这组基下的坐标, 叫它 $c_i^S$ 
下面做一个无聊的事情: 坐标变换
如果再考虑在 $T$ 上展开, 就有新的坐标 $c_j^T$ $$\mid\phi\rangle = \sum_{j=\pm1,0}\mid jT\rangle\langle jT\mid \phi\rangle$$在一个坐标中插入完备性条件 $$\langle iS \mid \phi\rangle = \sum_{j=\pm1,0}\langle iS\mid jT\rangle\langle jT\mid \phi\rangle=\sum_{j=\pm1,0}R_{ij}^{ST}\langle jT\mid\phi\rangle$$即 $$c_i^S = \sum_{j=\pm 1,0}R_{ij}^{ST}\times c_j^T$$上面都是对 ket 做的, 你也可以对 bra 做同样的事情, 比如一个 bra $\langle \chi\mid$ 
然后有 $$\langle \chi \mid \phi \rangle =\sum_{k,j}\langle \chi\mid k\rangle\langle k\mid j\rangle\langle j\mid \phi\rangle=\sum_{j,k}D_k^S\delta_{kj}R_j^S=\sum_{j}D_j^S R_j^S$$这和在做一个矢量的内积很相似

## 幺正性 unitarity -- 概率守恒

>这不是量子力学基本原理的推论
>这是一个额外的假设, 可以有幺正性的理论, 也有不幺正的
>比如你考虑一个小球, 找到这个小球的概率总为 1, 但比如中子, 如果你的理论里面没有中子衰变, 那么可能过一段时间找到中子的概率就不为 1了

同样考虑之前的仪器 $$\boxed{P_+(S)}\to \boxed{P_+(T)}\to \boxed{P_-(S)}$$实验表明, 幅 $$\langle -S\mid +T\rangle \langle +T \mid +S\rangle \quad \text{可以不为 0}$$如果概率守恒(粒子不消失)
$$1 = P(+S\to +T)+P(+S\to0T)+P(-S\to -T)$$而这里面的任何一个概率都是一个幅的模, 比如 $P(+S\to -T) =\langle-T\mid +S\rangle^*\langle -T\mid +S\rangle$
可以得到这个等式的后果: 首先 $$\langle \phi\mid\phi\rangle = 1 =\sum_i \langle\phi \mid i\rangle\langle i \mid \phi\rangle$$ 而考虑幺正性 $$1 = \sum_i \langle i\mid \phi\rangle^*\langle i \mid\phi\rangle$$这两个等式要同时成立, 可以有一种方法 $\langle i\mid \phi\rangle^* = \langle\phi\mid i\rangle$ 

> 这不是推导, 只是一个幺正性的解释

>feynman 使用了一种迷惑的记号, 例如电子双缝干涉 $\langle f \mid i \rangle$ , 不要将它理解为内积, 因为这两个状态是带时间的
>正确的理解是把时间也放进来, 即 $$\langle n+1\mid \mathcal{U}\mid n\rangle$$这里 $\mathcal{U}$ 是时间演化算符

# Chapter 6 自旋 - 1/2

>正确地理解自旋 1/2 这些系统的方式是旋量 (spinor)
>某种意义上这是 “最量子” 的系统, 因为它没有经典极限, 所有得到的都是量子效应
>对于二态系统, 即 qubit

上次课认识到: 自旋不是一种旋转效应, 比如电子散射时, 电子的自旋角动量可以和空间角动量交换, 即自旋角动量也是真正的角动量

先简单复习旋转

>三维旋转: 保持欧氏距离不变的所有线性变换全体 (反射有时候也可以看作旋转)
>下面我们只考虑连续的旋转, 即排除反射
>所谓连续: 即有一个参数连续变化控制旋转,并且可以连续地回到恒等, 毫无疑问一个可取的参数是旋转角
>三维空间一个非平庸的结果是: 任何旋转都有旋转轴 (有特征向量)
>反射显然不是连续的, 一般地, 这叫做 parity

旋转的性质
* 旋转的复合是旋转 $R_2R_1= R$ 
* 旋转的乘法不交换 $R_2R_1\neq R_1 R_2$ 

>旋转对称性是一种重要的对称性
>当提到对称性时, 不仅指系统在这种操作下不变, 更是确确实实做了这样的操作

>旋转的表示: 旋转矩阵
>好处在于不用抽象地讨论旋转, 而把它具体到一个矩阵上, 即
>$$\mathcal{R}\mapsto D_{ij}[\mathcal{R}]$$一般叫 $D_{ij}(\mathcal{R})$ 为旋转 $R$ 的表示矩阵 representation
>表示的意义不仅是拿出一堆矩阵表示旋转, 更是可以找到两种东西对应的运算律: 你可以用矩阵乘法模仿旋转的复合
>矩阵表示非常强大: 足以表示任何非交换的对称性
>旋转的复合 $$D_{ij}[R_2\circ R_1]=\sum_k D_{ik}[R_2]D_{kj}[R_1]$$另一个意义上是: 先表示再复合和复合再表示是交换的

>连续的三维旋转全体构成群 $SO(3)$
>三维空间的旋转的群表示不一定是 $3\times 3$ 阶 , 实际上和自旋有关, 自旋 $s$ 的旋转矩阵是 $(2s+1)\times (2s+1)$ 阶
>对于 $3\times 3$ 的旋转矩阵 $D^T=D^{-1}$ , 但这不一定对其他旋转矩阵成


>定番笑话: $SO(n)$ 和 $SU(n)$

现在有一个一般的问题: 一个 $n$ 维空间, 如何表示旋转?
> 任意态空间, 有基础态 $\mid iS\rangle$ 
> 第一件事是任意状态都可以用上面的基展开 $$\mid \phi \rangle = \sum_i \mid iS\rangle \langle iS\mid \phi\rangle=\sum_j \mid jT\rangle \langle jT\mid\phi \rangle $$从而有坐标变换关系
> 注意做这件事情的时候, 态是不变的, 在转的是坐标基的方向: 被动变换


现在对二态系统做这件事
策略: 把任意的旋转分解为简单的旋转, 在这里使用的是欧拉角 $(\alpha,\beta,\gamma)$
$$\mathcal{R}(\alpha,\beta,\gamma)=\mathcal{R}_z(\gamma)\mathcal{R}_x(\beta)\mathcal{R}_z(\alpha)$$
>强调这是被动变换, 上面旋转作用的不是同一个轴, 轴被旋转了
>一般地书为了强调一点会把两个 $z$ 做不同的 label

>主动变换上面要加负号 (每次旋转贡献一个符号)

现在只需要求沿两个特定方向的旋转, 为了方便, 取一组好的坐标基 (基础态) $\mid \pm z\rangle$ 
可以期待绕 $z$ 方向的矩阵是对角的, 但 $x$ 方向的不是, 但可以想办法将 $x$ 转到 $z$ 方向: 只需要绕 $y$ 轴转, 即 $$\mathcal{R}_x(\beta)=\mathcal{R}_y(-\frac{\pi}{2})\mathcal{R}_z(\beta)\mathcal{R}_y(\frac{\pi}{2})$$
这仍是困难的, 但利用旋转的复合性质$$\mathcal{R}_y(\pm\frac{\pi}{2}) \to \mathcal{R}_y(\pi)\to \mathcal{R}_y(2\pi)\to \mathcal{R}_z(2\pi)$$
最终问题归结于计算 $\mathcal{R}_z(2\pi)$

>$SO(3)$ 的群表示分类是简单的, 就是按照自旋分类

>上面开根号的操作肯定得到的结果是不一样的, 不同的根号给出不同的矩阵, 但是他们通过某种坐标变换联系在一起: 故事的结局是: 自旋 1/2 的旋转表示是唯一的

Step.1 绕 $z$ 轴的任意旋转 $\mathcal{R}_z(\alpha)$
从 $S$ 旋转到 $T$
符号约定 $$C_i =\langle iS\mid \phi\rangle \quad C_j' =\langle jT\mid \phi\rangle$$
由于 $z$ 轴有显然的对称性 $$|C_{\pm}'| = |C_{\pm}|$$ 即 $$\begin{cases}C_+' =e^{i\lambda}C_+ \\ C_-' =e^{i\mu}C_-\end{cases}$$一个重要的观察是整体的相因子是不重要的, 需要的只是相对相位, 故可以乘整体的相因子 $e^{-i(\lambda+\mu)/2}$ 得到
$$\begin{cases}C_+' =e^{i(\lambda-\mu)/2}C_+ \\ C_-' =e^{-i(\lambda -\mu)/2}C_-\end{cases}$$ 重定义相位 $$\begin{cases}C_+' =e^{i\lambda}C_+ \\ C_-' =e^{-i\lambda}C_-\end{cases}$$
>问题的重点是整体的相因子是不必要的

这样表明这个矩阵是对角的, 下一个问题是求 $\lambda(\alpha)$ , 这是简单的: 只要做两次旋转, 这表明 $$e^{i\lambda(\alpha)}e^{i\lambda(\beta)} =e^{i\lambda(\alpha+\beta)}$$这表明 $\lambda(\alpha)$ 是线性函数, 即 $$\lambda(\alpha) = m\alpha$$接下来的任务是确定 $m$ 的值, 我们期待 $m\in\mathbb{R}$ 

回到三维旋转, 我们知道转 $2\pi$ 会回到恒等, 我们在这里也期待同样的事情, 即 $$e^{i m \times 2\pi}=1$$最简单的取法是取 $m=+1$ , 这样取的后果是对转 $\pi$ 角的旋转 $$\begin{pmatrix}e^{i\pi} & 0 \\ 0 &e^{-i\pi}\end{pmatrix}=\begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix}$$这是不对的, 转 $\pi$ 角显然会改变一些物理态, 但上面表示这是一个平庸的操作(没有改变物理态)
即 $$e^{im\times 2\pi}\neq 1$$

>应该取 $m$ , 当 $\alpha$ 从 $0$ 到达 $2\pi$ 时, 旋转矩阵**才**第一次到达平庸的结果
>即当 $\alpha=2\pi$ 时 , 任意旋量第一次回到自己
>正确的取法是 取 $$m=\frac{1}{2}$$(这也就是为什么自旋 1/2 叫做自旋 1/2)
>在自旋 1 时, $m = 1$
>对不同的自旋重复上面的故事, 会发现:
>即转过 $\pi$ 角后, 任何整数自旋获得平庸相位 $1$ , 任何半整数自旋获得非平庸相位 $-1$

从而 $$D[\mathcal{R}_z(\alpha)]=\begin{pmatrix}e^{+i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix}$$

> 这就是为什么称自旋 1/2 系统转一圈不会回到自己
> 这是一个奇怪的问题: 恒等变换的表示矩阵不是 $1$ , 而是 $-1$ !
> 矛盾在于我们所求的不是一个表示, 而是一个投影表示

>投影表示
>回到表示的定义: 表示要求矩阵的乘法忠实地复现旋转的复合
>一方面 $D[\mathcal{R}_z(2\pi)]=1$ 但 $D[\mathcal{R}_z(\pi)]\cdot D[\mathcal{R}_z(\pi)] =-1$
>问题来源于态之间可以获得一个整体的相因子
>这种表示称为投影表示 projection rep.
>即乘法之间可以差一个相因子 $$D[\mathcal{R}_2\mathcal{R}_1]=e^{i\phi(\mathcal{R}_2,\mathcal{R}_1)}D[\mathcal{R}_2]D[\mathcal{R}_1]$$

>这和之前的自旋- 统计定理相容: 
>整数自旋 $e^{i\phi}=+1$
>半整数自旋 $e^{i\phi}=-1$
>可以想象交换粒子实际上就是乘了一个旋转矩阵, 这样每个费米子贡献 $-1$ 

于是 $\mathcal{R}_z(2\pi) =-\mathbf{1}_{2\times 2}$ , 那么 $$\mathcal{R}_y(2\pi) =\mathcal{R}(-\mathbf{1})\mathcal{R}^{-1}\implies \mathcal{R}_y(2\pi) = -\mathbf{1}$$
回到之前, 我们要对这个矩阵开根号: 

> 绕 $y$ 转 $\pi$ 角: 可以期待这个矩阵是一个只有非对角元非 0 的矩阵 (交换两个态) , 并且这是一个纯相位
> $$\begin{cases}C_-'=e^{i\beta}C_+\\ C_+' =e^{i\gamma}C_- \end{cases}$$重复上面的故事, 我们得到 $$\mathcal{R}_y(\pi)=\begin{pmatrix}0 & 1 \\ -1 &0\end{pmatrix}$$


最后再次开根号, 一种可能的解是 $$\mathcal{R}_y(\frac{\pi}{2})=\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix}$$
并且 $\mathcal{R}_y(-\frac{\pi}{2})=\mathcal{R}_y(\frac{\pi}{2})^\dagger$ 

>为什么这是一个旋转变换(二维的)? 
>简单的回答是: 我们就是在找一个非平庸的旋转
>或者可以理解为这里隐含了幺正性

从而得到绕 $x$ 轴任意旋转的矩阵 $$D[\mathcal{R}_x(\alpha)]=D\left[ \mathcal{R}_y( -\frac{\pi}{2} )\mathcal{R}_z(\alpha)\mathcal{R}_y\left( -\frac{\pi}{2} \right)\right]= \begin{pmatrix}\cos(\alpha/2)&i\sin(\alpha/2)\\ i\sin(\alpha/2) &\cos(\alpha/2) \end{pmatrix} $$

## Appendix
接着之前的计算, 可以得到绕 $y$ 轴任意旋转的矩阵 $$D[\mathcal{R}_y(\beta)]=D\left[\mathcal{R}_x(-\frac{\pi}{2})\mathcal{R}_z(\beta)\mathcal{R}_x(\frac{\pi}{2})\right]=\begin{pmatrix}\cos(\beta/2) & \sin(\beta/2) \\ -\sin(\beta/2) & \cos(\beta/2)\end{pmatrix}$$与之前的结果相容.
即我们可以写出最后用欧拉角表示的旋转, 但这个没什么用, 用的最多的还是绕三个坐标轴的转动
$$\begin{align}&D[\mathcal{R}_x(\alpha)]=\begin{pmatrix}\cos(\alpha/2)&i\sin(\alpha/2)\\ i\sin(\alpha/2) &\cos(\alpha/2)\end{pmatrix}\\&D[\mathcal{R}_y(\beta)]=\begin{pmatrix}\cos(\beta/2) & \sin(\beta/2) \\ -\sin(\beta/2) & \cos(\beta/2)\end{pmatrix}\\& D[\mathcal{R}_z(\alpha)]=\begin{pmatrix}e^{+i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix}\end{align}$$
最后我们来计算任意方向角 $(\theta,\phi)$ 处的自旋态用 $z$ 轴的基础态的表示, 以向上态为例
要做的实际上就是把这个方向转到 $z$ 轴, 由于原坐标只给了它的 $z$ 方向, 另外两个方向是任意选取的, 不妨取它的 $x$ 轴躺在我们 $x-y$ 平面上, 为了确定这个方向, 写出法平面方程 $$x\sin\theta\cos\phi+y\sin\theta\sin\phi+z\cos\theta=0$$然后取 $z=0$ 得到方向 $$\tan\psi=-\frac{y}{z}=-\cot(\phi)\implies \psi =\pi/2 -\phi$$
 故先将坐标绕 $x$ 轴转 $-\theta$ 度, 再绕 $z$ 轴转 $\psi$ 度, 就把坐标架转到了原始位置, 直接计算
 $$\begin{align}&\langle +z\mid +(\theta,\phi) \rangle=\sum_i\langle +z\mid i z'\rangle\langle iz'\mid +(\theta,\phi)\rangle=e^{i(\frac{\pi}{4}-\frac{\phi}{2})}\cos\frac{\theta}{2}\\ &\langle -z\mid +(\theta,\phi)\rangle =e^{i(\frac{\pi}{4}+\frac{\phi}{2})}\sin\frac{\theta}{2}\end{align}$$即我们得到 $$\mid +(\theta,\phi)\rangle=e^{i(\frac{\pi}{4}-\frac{\phi}{2})}\cos\frac{\theta}{2}\mid +z\rangle+e^{i(\frac{\pi}{4}+\frac{\phi}{2})}\sin\frac{\theta}{2}\mid -z\rangle$$对反方向的态也可以通过相同的方式得到
另一种方式, 负方向态实际上是 $(\pi-\theta,\phi+\pi)$ 的向上态, 直接代入得到 $$\mid +(\pi-\theta,\phi+\pi)\rangle =e^{-i(\frac{\pi}{4}+\frac{\phi}{2})}\sin\frac{\theta}{2} \mid+z\rangle +e^{i(\frac{3\pi}{4}+\frac{\phi}{2})}\cos\frac{\theta}{2}\mid -z\rangle$$而直接计算得到 $$\mid -(\theta,\phi)\rangle=e^{i(\frac{3\pi}{4}-\frac{\phi}{2})}\sin\frac{\theta}{2}\mid +z\rangle+e^{i(-\frac{\pi}{4}+\frac{\phi}{2})}\cos\frac{\theta}{2}\mid -z\rangle$$两者相差一个整体相因子 $e^{i\pi}$ 
这与前面的说法一致
