关心的是空间点过程
常常关心的是一些分布的随机样本点
目标是特征

不一定是欧式几何中的空间统计, 也不一定是标量场的统计

# Spatial clustering description

一种方式是在空间格点中计数 $N$

估计密度 $n=V/N$  , 可以定义平均密度 $\bar{n}=\braket{n}=\braket{N}/V$ 同样有 overdensity $\delta =\frac{n-\bar{n}}{\bar{n}}$

## Counts - in -cells
现在从一个计数的得到一个分布 $p(N|V)$ 对于不同的格点 $V$

对于一个随机的样本, CiC 的结果是 Poisson 分布

则随机样本的 overdensity 的方差 $\sigma_V^2=\mathrm{Var}(N)/\braket{N}$


对于一般的样本, 一般是一个 poisson 成分加上在格子中的 clustering 成分

这里 $\xi(\mathbf{r})$ 是两点相关函数

### 2 - point correlation function
考虑距离为 $\mathbf{r}$ 的两个体积元, 问期望有多少点对

一般的形式为
$$\mathrm{d}\mathcal{P}_{12}=\bar{n}^2(1+\xi(\mathbf{r}))\mathrm{d}V_1\mathrm{d}V_2$$
$\xi$ 即两点相关函数
* $\xi>0$ 两点是相关的
* $\xi=0$ 两点是无关的
* $\xi$<0 两点负相关

注意到局域的数密度为
$$n(\mathbf{x})=\bar{n}(1+\delta(\mathbf{x}))$$
则成对点的期望
$$\begin{align}\mathrm{d}\mathcal{P}_{12}&=\braket{n\mathrm{d}V_1\cdot n\mathrm{d}V_2}\\&=\\&=\bar{n}^2[1+\braket{\delta\delta}]\end{align}$$
即相关函数的定义为
$$\xi(\mathbf{r})=\braket{\delta(\mathbf{x+r})\delta(\mathbf{x})}$$

>在真实的数据中, 这个平均值的计算容易收到选择效应影响
>比如角向的选择效应与完备度, 径向也存在不均匀性
>处理这些东西需要一个随机样本做参照

>比如一个被画了一些mask的天区, 需要一个随机样本作为参照
>这些随机样本可以将一些边界的效应修正

则可以从计数中得到分布函数
去问距离为 $\Delta r$ 的点对有多少 $\widehat{DD}$ , 对随机样本也这样做 $\widehat{RR}$ , 也可以去用随机样本的数据样本做点对 $\widehat{DR}$
进行归一化
$$DD = \frac{\widehat{DD}}{N_D(N_D-1)/2}\quad RR=\frac{\widehat{RR}}{N_R(N_R-1)/2}\quad DR=\frac{\widehat{DR}}{N_R N_D}$$
则相关函数的估计为
$$\hat{\xi}_{PH}=\frac{DD}{RR}-1$$
* 经常被用在周期性的盒子里, 经常在模拟中使用
* 问题是受边界条件影响很大

并且模拟此时 $RR$ 的结果是解析的
$$RR = \frac{4\pi}{3}\frac{(r+\Delta r)^3-r^3}{V}$$

在真实的数据中, 需要考虑 $DR$ 项

Landy - Szalay estimator
$$\hat{\xi}_{LS}=\frac{DD-2DR+RR}{RR}$$
也有 Hamilton estimator


>真实的两点关联函数为
>在尖尖处对应重子声波振荡, 这是一个用于标定宇宙膨胀的

同样可以做各向异性的测量, 把距离按视线方向分解

$$\mathbf{s}_{\parallel}$$

可以定义夹角

>测量的结果是
>则可以用来测距, 或者检验广义相对论

对于大量数据, 还可以做一些压缩方式, 比如多极展开
比如按 Legendre 展开
$$\xi_l(s)=\frac{2l+1}{2}\int_{-1}^1\xi(s,\mu)\mathcal{L}_l(\mu)\mathrm{d}\mu$$
然后去看这个谱的分布

在数据不够好的时候, 也可以做径向压缩, 得到投影相关函数
$$w_p()$$

角向也可以做


另一种做法是计算 marked 2PCF
即按照一些物理量分布的权重给不同点加权
$$\mathcal{M}(\mathbf{r})=\frac{1+W(\mathbf{r})}{1+\xi(\mathbf{r})}$$
* 当 $\mathcal{M}>1$ 时, 

>除了标量场, 其他场也可以做相关函数
>比如速度场, 形变场(张量场) , Lyman $\alpha$ 森林分布, 温度场, 极化场


### tools
第一个介绍的是老师写的

# Clustering models from 
现在去理解宇宙学中计算得到的相关函数有什么含义

Hierarchical universe -- 1900s
认为宇宙是一个分层的结构
今天我们对宇宙结构的理解也差不多, 并且主导宇宙的相互作用都是引力, 所以每层的结构也很像

怎么给宇宙建模? 

>Neyman - Scott process - 1953
>认为宇宙的第一级结构是一些随机分布的星系团, 
>然后在第二级结构给每个星系团按照 Gauss 分布分配星系
>halo model
>$$\xi = \xi_{2h} +\xi_{1h}$$
>2 - halo term 考察 haloes 之间的关联
>1 - halo term 考察 haloes 内部的关联
>在无噪声的情形, 2 - halo terms 是 0
>$$\xi_{1h}\propto \int \rho(\mathbf{x})\rho(\mathbf{x+r})\mathrm{d}^3x$$
>这样


对于真实宇宙, 按上面的结果计算
1 - halo term : 一个 universal 的密度分布
* Navarro - 
* E

2 - halo term : 有偏的采样, 偏差反映了暗物质密度分布
$$\xi_{2h}(r)\approx b_1^2\xi_m(r)$$

对于暗物质分布, 可以通过 CMB 的分布得到
涨落大小为 $10^{-5}$ 
来源于宇宙早期的量子涨落, 这是 Gauss 随机场即涨落的分布是 gauss分布

### Gauss 随机场
这是一个多维 gauss 分布
$$p(\mathbf{\delta})=\frac{1}{(2\pi)^{n/2}|\mathbf{M}|^{1/2}}\exp\left[-\frac{1}{2}\mathbf{\delta}^T\mathbf{M}^{-1}\delta\right]$$
协方差矩阵实际上是两点相关函数


>即一个均匀的 Gauss 随机场可以由它的两点分布函数完全决定


### Fourier 空间中的密度场

则一个 gauss 场的 fourier 变换后 还是 gauss 场

问: 这个 gauss 场的协方差矩阵是什么, 则可以用原 gauss 场计算

在各向同性的假设下

即

于是可以定义功率谱, 即相关函数的 fourier 变换

得到

即这个协方差矩阵是对角的, 不同的模式之间是不相关的 (对 gauss 分布甚至是独立的)

### gauss 随机场生成
考虑在 k 空间生成不同的 guass 分布 (不同模式是独立的)

gauss 分布可以使用 Box - Muller 变换得到

做逆变换即可得到 gauss 场



CMB 的结果接近于 $\alpha=-1$ 的功率谱

### 窗函数
对于有限的观测窗口, 观测到的实际上相差一个窗函数

在 k 空间变为卷积

这个结果将 k 空间不同模式的不相关性破坏了

一般会使用带权的结果作为 estimator

如果做 FFT 需要均匀采样 即做 particle assignment

>一种方式是 NGP
>CIC


最后的功率谱是


按照不同的网格进行这么做


宇宙学上的功率谱

同样可以做角向的功率谱, 即做球谐函数展开

对于各向同性场

这就是 CMB 的结果

# Beyond  2 - point
引力会让分布不再 gaussian

分布会变得更奇怪, 2 点相关函数不能提取分布的所有信息了

>一个例子是
>此时这两种情形分布的功率谱是一致的
>实际上差别在相位上

一种推广是去做多点相关函数

比如 3 点相关函数

并且在傅立叶空间也有对应物

同样有 拓扑结构的统计
按照空间点按照半径的连接结构和半径的关系

同样的东西比如最小生成树

也有去找宇宙中的空洞的方法

上面的拓扑方法需要连续分布, 对于离散场需要做一个 estimator 得到连续场的估计

>实际上这些方法在地理中使用得更多
>因为地理在估计地形的时候不能在所有位置采样
>一些方法比如三角化, 这在计算机图形学中使用
>三角化方法也有一些问题, 比如三角化方法不唯一, 一种好的方法是三角剖分 Delaunay Triangulation
>这种方法在不存在四点共圆的情形时三角化的方法是唯一的
>是 Vorono

这种方法也常用于宇宙学中的密度估计

## 层级估计
不去做点的估计, 而是直接正向建模场, 再去拟合场本身
