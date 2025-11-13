从积规则中得到 (Bayes 公式)$$\begin{align}&p(D\mid \theta M I)\cdot p(\theta\mid MI)=p(\theta\mid DMI)\cdot p(D\mid MI)\\ &\mathcal{L}(\theta) \times \pi(\theta)\quad\quad=\quad \quad\mathcal{P}(\theta)\times \mathcal{Z}\end{align}$$
可以看到两者的关系:
1. 已经有的是似然 $\mathcal{L}(\theta)$ 和 先验 $\pi(\theta)$ 
2. 要求的是后验 $\mathcal{P}(\theta)$ 和 证据 $\mathcal{Z}$
两者分别在参数推断和模型选择中发挥作用

## Monte - Carlo 积分
在计算后验时, 可能计算很困难. 而做积分的时候, 通常都没有封闭形式. 并且高维时更加困难

目标是计算积分 $$\int_a^b f(x)\mathrm{d}x$$一种方法是在区间 $[a,b]$ 中均匀采样 $\{X_i\}_{i=1}^n$ , 那么计算的均值 $$\mu =\sum_{i=1}^n f(X_i)\times\frac{1}{b-a}$$实际上就是积分值
通过数值模拟, 可以发现相对误差随 $N^{-1/2}$ 降低
但是均匀分布对点的利用效率太低了, 可以按一定的分布进行取样 -- 重要性采样

>重要性采样
>按恰当的分布 $q(x)$ 进行取样, 再计算 monte - carlo 积分
>要求在 $f(x)\neq 0$ 的位置都有 $q(x)>0$ 保证采样准确$$\int_a^b f(x)\mathrm{d}x = E(\frac{f(X)}{q(X)})\simeq \frac{1}{N}\sum_{i=1}^N\frac{f(X_i)}{q(X_i)}$$
>显然当采样函数为均匀分布时, 即为第一种情况


>总结 Monte Carlo 的优劣
>优点:
>1. 简单且适用于高维
>2. 无偏且一致, 误差服从 $N^{-1/2}$
>3. 容易并行计算: 可以在不同处理器上独立采样
>
>缺点:
>1. 效率极度依赖采样函数 $q(x)$
>2. 优化采样函数有时是困难甚至不可能的, 在高维更是这样


## Markov Chain Monte Carlo
考虑一种更优化的方案

想法: 构造一种随机游走, 在值更大的地方会呆更长时间, 让随机变量自己去决定采样函数!

>The Metropolis- Hasting algorithm
>在原先的分布下采样, 但并不直接取样, 而是以采样点为初值条件 burn in 进行随机游走, 则这个点在随机游走过程中待在某个位置的时间与所求函数形状应该较接近
>目标: $f(x)$
>采样函数 $q(x'\mid x)$ 比如说可以使用局域的 gaussian 
>具体算法: 给定初始点 $x_1$ , 对于每步 $i$ , 按照采样函数 $q(x'\mid x_i)$ 进行下一步游走, 同时计算接受率 $$r=\frac{f(x')}{f(x_i)}\cdot \frac{q(x_i\mid x')}{q(x'\mid x_i)} $$依据概率 $\min(1,r)$ 来接受下一步 $x_{i+1}=x'$ , 否则拒绝移动并停留 $x_{i+1}=x_i$
>重复这个过程, 得到一个 Markov 链
>>实际上接受率包含了两部分贡献: 
>>1. $f(x')/f(x_i)$ 这比较了积分值, 点应该更倾向于向函数值更大的方向移动
>>2. $q(x_i\mid x')/q(x'\mid x_i)$ 同样, 点应该更倾向于向更可能移动的方向移动


可以使用 emcee , PyMC , zeus 包调用 mcmc 方法
一个例子: 
考虑之前的谱线 $$N_i =A\exp\left[-\frac{(x_i-\lambda_0)^2}{2w^2}\right]+B$$对于未知参数 $A,w$ 
对数后验函数为 $$\ln p(A,w\mid \{n_i\}_{i=1}^M ,I)=\sum_{i=1}^M(n_i \ln N_i -N_i)-\ln Aw+\mathrm{const.}$$
>当然这里已经给出了后验分布, mcmc 实际上在干的是在已知的后验分布上采样, 但是这里 mcmc 找到了一个很好的 $q(x)$ 
>它几乎就是原先的函数 $f(x)$, 这使得我们在计算积分时有 $$\begin{align}\int f(x)\cdot g(x)\mathrm{d}x=E(\frac{f(X)g(X)}{q(X)})&\simeq \frac{1}{N}\sum_{i=1}^N\frac{f(X_i)g(X_i)}{q(X_i)}\\&\simeq\frac{1}{N}\sum_{i=1}^{N}g(X_i)\end{align}$$

>问题:
>1. 这个算法并不一定能保证收敛, 容易被 local minimum 影响
>2. 如果 burn in 阶段不够长就会有 bias , 但不能估计 burn in 的界
>3. 点之间的关联较强, 有效的点数量较少
>4. 结果的效率依赖于采样函数
>5. 并行的效率较低


同样 HM 算法极其容易受到候选分布 proposal $q$ 的影响: $q$ 决定了点能跑多远以及怎么跑

另一种方法是 Hamiltonian Monte Carlo

>某种意义上, mcmc 在干的实际上就是搜索函数的极大值, 这让我们想起物理上势能极小值的对应, 一种想法就是将物理上的整套动力学移植过来, 即某种参数空间的动力学

类比势场 $$U(\theta)=-\ln\mathcal{P}(\theta)$$把随机游走直接用 Hamilton 动力学过程代替 $$H(\theta,p)=U(\theta)+K(\theta)=U(\theta)+\frac{1}{2}p^TM^{-1}p$$
$M$ 是质量矩阵, 要求是正定的, 动量 $p$ 由初始给定
这实际上也是某种梯度下降, 因为粒子的运动实际上由力支配 $$\mathbf{F}=-\nabla U(\theta)=\nabla \ln \mathcal{P}(\theta)$$

>HMC 算法
>1. 给定初始的位置 $\theta$ , 并从分布 $\mathcal{N}(0,M)$ 中采样动量 $p$
>2. 做 $L$ 步某种内插的动力学演化, 由步长 $\epsilon$ 按以下算法决定候选状态 $(\theta',p')$ $$\begin{align}&p \leftarrow p-\frac{\epsilon}{2}\nabla U(\theta)\\&\theta\leftarrow \theta + \epsilon M^{-1}p\\&p\leftarrow p-\frac{\epsilon}{2}\nabla U(\theta)\end{align}$$
>3. 最后按照能量决定 $(\theta',p')$ 的接受概率 $$\rho =\min (1,\exp\left[-H(\theta',p')+H(\theta,p)\right])$$
>4. 重复, 得到样本点在参数空间的动力学演化


>HMC 的优劣
>优点:
>1. 在计算先验的时候更有效率, 有规律地游走而不是随机游走
>2. 样本之间的关联更低
>3. 更适合高维的问题
>
>缺点:
>1. 需要梯度, 要求可微
>2. 更多需要参数: 步长 $\epsilon$ , 路径长度 $L$ , 质量矩阵 $M$

>No - U - Turn Sampler (NUTS) - Hoﬀman & Gelman (2014), JMLR, 15:1593–1623 ( https://arxiv.org/abs/1111.4246)
>* 自动决定路径长度, 步长和质量矩阵也可以在 warm - up 阶段自动调整
>* 更加灵活: 连续模型
>* 应用广泛: PyMC , Stan , Numpyro 包
>* 可扩展性高: 在多参数的情形也有效率

>一个应用例子是:
>在计算机上模拟星系, 问题是引力的反解是困难的, 我们并不知道宇宙的初值条件, 我们能做的就是设置一个处置条件, 然后跑模拟. 第一个实现的计算就借助了 HMC 方法在我们可以接受的时间内反解出了初值条件
>当然这种方法要求求解动力学方程, 即需要可微性

>总结: MCMC 方法
>1. 输入: 未归一化的后验函数 (对 HMC 还需要梯度)
>2. 输出: 依据后验的采样点
>3. How it works: 一个更容易到达高概率区域的 Markov 过程
>4. 限制: 对于分散的分布( 多峰分布 )很难采样, 并没有给出证据

## Nested Sampling
由 Skilling 在 04 年引入:
* 能够为模型比较计算证据
* 后验采样实际上仅仅作为副产物输出

优点是:
* 对于多峰分布以及高简并的后验分布也能用
* 很少的参数
* 有效, 且对高维也可行

*几乎立即在宇宙学中使用*

想法是: 
在参数空间采样时, 分布需要用采样点表示, 在高维时十分糟糕, 所以并不考虑采样参数点 -- 而是采样等值面
一旦采样出等值面, 积分也自动得到了 - 要做的只是一个一维积分

>>你几乎可以立即意识到, 这就是在做 Lebesgue 积分
>>遗憾的是, 这种算法是在 Lebesgue 积分提出近100年后才提出
>>Lebesgue 积分即为 $$\int f(x)\mathrm{d}x =\int_0^\infty\mu\{x\colon f(x)>y\}\mathrm{d}y$$


这种算法需要采样出等值面, 首先来做一些准备工作
定义 $X(\lambda)$ 为先验 $\pi(\theta)$ 在似然比 $\lambda$ 大对部分, 即 $$X(\lambda)=\int_{\mathcal{L}(\theta)>\lambda}\pi(\theta)\mathrm{d}\theta\implies\mathrm{d}X=\pi(\theta)\mathrm{d}\theta$$
这样 $$\mathcal{Z}=\int \mathcal{L}(\theta)\pi(\theta)\mathrm{d}\theta=\int_o^1\tilde{\mathcal{L}}(X)\mathrm{d}X\quad 
\mathcal{P}(X)=\frac{\tilde{\mathcal{L}}(X)}{\mathcal{Z}}$$
这里 $\tilde{\mathcal{L}}(X)$ 对定义的 $X\in [0,1]$ 满足 $$\tilde{\mathcal{L}}(0)=\mathcal{L}_{\\max}\quad\tilde{\mathcal{L}}(1)=0$$
所以 Nested sampling 算法需要采样出等值面
具体算法是这样的
1. 先依据先验 $\pi(\theta)$ 采 live point $n_{\text{live}}$ 
2. 依据这些点得到的最小的似然 $\mathcal{L}^\star$ 排除一个死点
3. 再依据新的先验采一个活点, 按照先验 $$\pi^\star(\theta)\simeq\begin{cases}\pi(\theta)\quad \text{if}\quad \mathcal{L}(\theta)>\mathcal{L}^\star\\0\quad \text{otherwise}\end{cases}$$
4. 可以证明, 活点分布的体积压缩率 $t$  (即 $X_{i+1}=tX_i$) 满足分布 $$p(t)=n_{\text{live}}t^{n_{\text{live}}-1}\quad \langle \log t\rangle =-1/n_{\text{live}}$$
>你可能会疑惑为什么 $X_0=1$ , 实际上这是一种近似, 在活点数量足够多的时候, 采样点就很容易接近 $X=1$ 处, 这样得到误差的概率就会比较小, 而实际计算中 $t$ 也是按照分布取的, 比如取期望值

即死点位置演化 $$X_0=1\quad X_{i+1}=tX_i$$
则可以在死点上做证据积分 $$\mathcal{Z}=\sum_{i}\mathcal{L}_i^\star\Delta X_i\quad \Delta X_i=(1-t)X_i$$最终算法在剩余上界 $$\mathcal{Z}_{\text{rem}}\simeq \mathcal{L}_{\max}X_i\ll \mathcal{Z}_{\text{current}}$$时停止, 即估计的差值极小
最后加上 $$\langle \tilde{\mathcal{L}}\rangle\cdot X_n$$作为停止值,  $\langle \tilde{\mathcal{L}}\rangle$ 意识是在活点上取平均的似然, 即"封顶"

 >后验实际上是副产物:
 >每次运算实际上都是在似然 $\mathcal{L}_i^\star$ 处移去了一个壳层 $\Delta X_i$
 >而死点是在壳层中均匀采样的, 后验的权重为 $w_i=\mathcal{L}_i^\star\Delta X_i$ (实际上就是后验在死点处的近似值) 但是由于这些点并不是按照后验采样, 需要做重采样
 >在终止时的活点也可以作为权重 $w_j =\mathcal{L}_j X_n/n_{\text{}live}$
 >由 $\mathcal{Z}$ 去做归一化 $\tilde{w_i}=w_i/\mathcal{Z}$
 >以上面的权再去采样即可得到似然的样本 (即在原先的点上再按照权去抽样)
 
 >Nested sampling 的特点:
 >1. 在低概率区域由死点采样
 >2. 并不知道死点具体对应的 $X$ 的值, 但是可以给出他们在 $X$ 空间的期望体积
 >3. 在高概率区域由活点采样
 >4. 准确性和收敛速度依赖于活点数量
 
 Nested sampling 可以用 UltraNest , dynesty , PyPolyChord , PyMultiNest 等调包
  
