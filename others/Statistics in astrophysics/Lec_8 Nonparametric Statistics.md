这节课是应用的第一节课
问题是: 对于一个未知的函数 $f(x)$ , 获得了有限的数据 $D$ , 并且只有一个较弱的先验背景 $I$
因为没有一个具体的函数形式, 需要一个 flexible 的函数作为代表
这需要增加一个较弱或者一类型的约束, 比如 光滑性, 非负性等
需要让数据来度量复杂度, 这个过程就是非参数统计

>这并不代表模型中不带参数, 反而一般是模型有很多参数

## 模型构造和表达

回到问题:
给定数据 $D$ 和背景信息 $I$ , 我们能对感兴趣的函数 $f(x)$ 做出什么论断
* 变量 $x$ 可以是离散的也可以是连续的, 或者是多维的

现在的后验实际是一个函数的先验 $$p(f\mid DI)\propto p(D\mid f I)p(f\mid I)$$
在计算后验时, 需要
* 在已知信息 $I$ 选择一族合适的代表族 $f$ 
* 确定先验和似然

>数据的使用策略
>1. 若函数的形式已经知道了, 实际上就是推断函数的参数, 回到参数推断
>2. 若函数的形式不确定, 但是有一个有限的选择范围, 这回到模型选择
>3. 若完全什么都不知道, 则这就是非参数统计

回到光谱的例子:
若有一个锐利的谱线 $$\phi(\lambda)=\sum_{i=1}^M \alpha_i \delta(\lambda-\lambda_i)$$
实际上 CCD 测量到的是在背景下的每个像素的光子计数, 并带着点源的扩散 
比如在像素 $i$ 处的光子数期望值为
$$\mu_i =\braket{n_i}= \sum_{j=1}^M A_j \exp\left[-\frac{(x_i-\lambda_j)^2}{2w^2}\right]+B$$
比如有三条发射线 $(A_i,\lambda_i)$ , 获得了仪器的点扩散函数 $w$, 且测得背景强度 $B$
此时的似然是多个独立的 poisson 过程 
$$p(D\mid fI)=\prod_i^{N_p}\frac{\mu_i^{n_i}\mathrm{e}^{-\mu_i}}{n_i !}$$

### Case1 参数推断
如果已经函数形式
$$\phi(\lambda)=\sum_{i=1}^3 \alpha_i \delta(\lambda-\lambda_i)$$
三条发射线, 则也可以计算出期望
$$\mu_i =\braket{n_i}= \sum_{j=1}^3 A_j \exp\left[-\frac{(x_i-\lambda_j)^2}{2w^2}\right]+B$$
所以现在的参数为
$$\theta =\{A_1,A_2,A_3,\lambda_1,\lambda_2,\lambda_3\}$$
得到对数似然 
$$\log \mathcal{L}(\theta) = \sum_{i=0}^{20}(n_i \ln \mu_i -\mu_i -\ln {n_1!})$$
使用均匀先验
$$\pi(\theta) =\text{const}$$
和
$$\{A_1,A_2,A_3\}\in[0,100]\quad \{\lambda_1 ,\lambda_2,\lambda_3\}\in [0,20]$$
后验:
$$\ln\mathcal{P}(\theta)=\sum_{i=0}^{20}(n_i \ln \mu_i -\mu_i)+\text{const}$$


> 代码中计算似然时, 可能出现参数的简并现象, 
> 这是因为没有设置参数之间的关系导致的, 可以强行加一些大小关系让他们退简并, 否则实际上你有几个等价的参数会让后验分布多一些相同的峰

### Case2 模型选择
现在不知道函数的具体形式: 不知道有几条峰, 故可以假设有 $M$ 条
$$\phi(\lambda)=\sum_{i=1}^M \alpha_i \delta(\lambda-\lambda_i)$$
对于这样的模型, 期望计算为
$$\mu_i^{(M)} =\mu(x_i;M)= \sum_{j=1}^M A_j \exp\left[-\frac{(x_i-\lambda_j)^2}{2w^2}\right]+B$$
现在模型的参数为 
$$\theta_M =\{\lambda_1,\cdots,\lambda_M,\theta_1,\cdots,\theta_M\}$$
同样赋予均匀先验, 这时实际上是在进行模型选择
模型证据为
$$\mathcal{Z}_{M}=\int \mathcal{L}(\theta_M;M)\pi(\theta_M)\mathrm{d}\theta_M$$
在相同的模型先验下, 则后验比为 Bayes 因子
$$\ln O_{lm}=\ln B_{lm} = \ln \mathcal{Z}_l -\ln \mathcal{Z}_m$$

### Case 3 非参数统计
这时需要寻求一个不知道函数形式的解
一个一般的方法是去做离散化
$$\phi(\lambda)=\sum_{j=1}^M\alpha_j \delta(\lambda -\lambda_j) \quad \lambda_j =\lambda_{\min}+(j-\frac{1}{2})\Delta \lambda$$
即在每点都放一个源, 然后就可以去做模型比较, 但这很低效, 因为你在一直加参数
即这时候有非常多的参数, 由于维数诅咒, 这通常遇到计算上的困难, 并且非常依赖于先验, 对结果的限制也更弱

>一个更好的策略是找一些弱的假设
>这需要人为从数据里面找一些已知的结构, 或者找一个合适的先验

对于光滑函数的假设, 可以做一个 基函数展开, 一些紧, 局域性的函数展开
$$f(x)\simeq \sum_{h=1}^{M_b} c_h b_n(x)$$
一般的基函数有高斯, Bspline , 球谐函数, 小波函数, Chebyshev 多项式等

比如此时采用 Gauss 型的基函数时
$$\mu_i = \sum_{j=1}^{M_b} A_j \exp[-\frac{(x_i-x_j)^2}{2w^2}] + B$$

>而对于基函数的 knots 的选取实际上是由模型选择确定
>但是一般会采用 $w$ 大小的格点, 即
>$$x_j =x_{\min}+(j-1)w$$

现在的参数为
$$\theta =\{A_j\}_{j=1}^{M_b}$$
一般会赋予非负的均匀先验

>问题是
>1. 有参数的后验分布并不是 Gauss 型, 甚至不对称
>2. 有的参数出现简并

从拟合图中可以得到一些额外的信息: 可以看到有几个峰在占主导, 其他的峰很弱, 这暗示我们可能需要减少参数数量

>即使这样, 也存在一些问题:
>1. knots 的放置和数量也含有一些任意性
>2. 结果显然和 basis function 和 knots 有关
>3. 参数可能存在简并
>可能需要一些非均匀的先验来调整这个过程


## 高斯过程回归

现在直接考虑做函数的先验 
$$p(f\mid I)\sim \mathcal{N}(m,\mathbf{K})$$
即对输入的坐标 $X=\{x_1,\cdots,x_n\}$ , 使得得到的值服从 Gauss 分布
$$f(X)\sim \mathcal{N}(m(X),\mathbf{K}(X,X))$$
>这在即使实际结果不是 Gauss 型的时候也很有用
>在中心化数据之后会取 $m=0$ 作为简化


可以定义 kernel  matrix 核矩阵
$$\mathbf{K}=\begin{pmatrix}k(x_1,x_1) &\cdots& k(x_1,x_n)\\\vdots & \ddots &\vdots\\ k(x_n,x_1)&\cdots&k(x_n,x_n)\end{pmatrix}$$

>核函数 kernel $k(x_i,x_i;\mathbf{\theta})$ 与超参数 $\theta$
>一般会用 Gauss 型的径向基函数作为核函数 $\{\sigma,l\}$
>$$k(x_i,x_j)=\sigma^2 \exp\left[-\frac{(x_i-x_j)^2}{2l^2}\right]$$
>或者周期性的核函数 $\{\sigma,l,p\}$
>$$k(x_i,x_j)=\sigma^2 \exp\left[-\frac{2\sin^2(\pi |x_i-x_j|/p)}{l^2}\right]$$
>线性 $\{\sigma_b ,\sigma,c\}$
>$$k(x_i,x_j)=\sigma_b^2 +\sigma^2 (x_i-c)(x_j-c)$$
>总之有各种 核函数


> Gauss 过程的超参数
> 比如对于径向分布函数 $\theta =\{\sigma,l\}$
> 幅度 $\sigma$ : 控制了竖直的振幅
> 长度尺度 $l$ : 调整波动

给定训练集 $(X,Y)=(x_i,y_i)_{i=0}^n$
得到测试集之后就可以去做超参数的优化
$$p(\theta\mid X,Y)\propto p(Y\mid X,\theta)\cdot p(\theta)$$
证据(边缘化后的似然)即为
$$p(Y\mid X,\theta) =\int p(Y\mid f,X,\theta)p(f\mid X,\theta)\mathrm{d}f$$
>>这里在确实是在函数空间做积分
>>但是数值上并不会遇到这一点, 因为数值上遇到的函数总是一个有限维的, 即我们对函数空间做了离散化
>>意思是你在谈 $f$ 的时候总是在谈他在一个测试集 $X^*$ 上的行为

这样给定训练集 $(X,Y)$ 和测试集 $X^*$ 我们有
$$\begin{bmatrix}Y\\f(X^*)\end{bmatrix}\sim\mathcal{N}\left(0,\begin{bmatrix}\mathbf{K}(X,X)&\mathbf{K}(X,X^*)\\\mathbf{K}(X^*,X)&\mathbf{K}(X^*,X^*)\end{bmatrix}\right)=\mathcal{N}\left(0,\begin{bmatrix}\mathbf{K}&\mathbf{K}_*\\\mathbf{K}_*^T & \mathbf{K}_{**}\end{bmatrix}\right)$$
即预测的"后验分布"为
$$p(f(X^*)\mid Y) \sim\mathcal{N}(\mathbf{K}_*^T \mathbf{K}^{-1}Y,\mathbf{K}_{**}-\mathbf{K}_{*}^T\mathbf{K}^{-1}\mathbf{K}_{*})$$
从而给出测试集上的预测

甚至可以加入误差
加入 Gauss 误差
$$y =f(x)+\epsilon \quad \epsilon \sim \mathcal{N}(0,\sigma_y^2)$$
从而
$$\begin{bmatrix}Y\\f(X^*)\end{bmatrix}\sim\mathcal{N}\left(0,\begin{bmatrix}\mathbf{K}+\sigma_y^2 \mathbf{I}&\mathbf{K}_*\\\mathbf{K}_*^T & \mathbf{K}_{**}\end{bmatrix}\right)$$
预测值
$$p(f(X^*)\mid Y) \sim\mathcal{N}(\mathbf{K}_*^T (\mathbf{K} + \sigma_y^2\mathbf{I})^{-1}Y,\mathbf{K}_{**}-\mathbf{K}_{*}^T(\mathbf{K} +\sigma_y^2 \mathbf{I})^{-1}\mathbf{K}_{*})$$


> Why does Gaussian process work ?
> * 真实的数据常常不是 Gauss 过程产生的
> * 实际的噪声也不是 Gauss 型的
> 回到问题中的数据携带了多少信息


## 最大熵原理

>信息熵
>需要找到一个量来度量: 不确定的大小, 这应该是一个概率分布
>* 假设这个函数存在
>* 连续性
>* 单调性
>* 一致性


> Shannon's Theorem
> 上面的函数存在且唯一
> $$H_n =-\sum_{i=1}^n p_i\log p_i$$
> 这被称为信息熵

假设唯一所知的是 
$$\sum_{i=1}^{n}p_i =1$$
尝试最大化信息熵得到实际的概率分布实际上就得到了
$$p_i =\frac{1}{n}$$
即无差别原理
如果进一步假设我们知道期望和方差
如果假设这是一个连续的分布
则可以得到 Gauss 分布

