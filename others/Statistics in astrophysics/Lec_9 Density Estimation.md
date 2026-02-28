在很多时候, 不能去估计数据本身, 只能去估计一些其他结构

目标: 从样本中推断出一个未知的概率分布


## 直方图

一种对未知分布 $f(x)$ 对估计方式是切片 $h(x)$
$$h(x) = \sum_{k=1}^M h_k\Pi(x;x_{k-1},x_k)$$
这里
$$\Pi(x;x_a,x_b) =\begin{cases}1\quad x_a \leq x<x_b \\ 0\quad \text{otherwise}\end{cases}$$
则可以定义概率 $\pi_k = h_k v_k$ , 这里 $v_k = x_{k}-x_{k-1}$
对计数有 $\{n_k\}_{k=1}^M :\hat{h}_k =n_k /(N v_k)$ 其中 $N =\sum_{k=1}^M n_k$


但是如何选择 bins 数量?

>一个经验法则为 Scott's 法则:
>对 $N$ 个点,假设是 Gauss 分布带有标准差 $\hat{\sigma}$ 则选择间隔
>$$v_{\text{scott}} = 3.49 \hat{\sigma} N^{-1/3}$$
>对于非 Gauss 分布, 一个推广是采取百分位数, 即 Freedman -Diaconis rule
>$$v_{\text{FD}}=2(q_{75}-q_{25})N^{-1/3}$$

可以看到 Scott 法则在 Gauss 情形很适用, 但对长尾分布不太好, 同样 fd 对长尾分布较好, 但同样在较尖锐的分布的刻画也并不好
所以需要一个更有效的方式去估计 bins

>Knuth method
>同样采用等宽的 bin $v$ , 共 $M$ 个, 假设数据的范围是 $V$
>可以直接通过推断直方图模型的参数得到
>$$h(x)=\frac{M}{V}\sum_{k=1}^{M} \pi_k \Pi(x;x_{k-1},x_k)\quad \quad \sum_{k=1}^{M} \pi_k =1$$
>这样就是我们熟悉的问题:
>给定数据 $D =\{x_i\}_{i=1}^N$ , 对给定的 $M$ , 有计数 $n_k=\mathrm{card}\{x_i\in[x_{k-1},x_k)\}$ 满足 $N =\sum_k n_k$
>要做的就是在给定数据 $D$ 下优化 $M$
>例如最大化后验 $P(M\mid DI)$

实现的算法是这样的:
考虑自由参数 $\{\pi_k\}_{k=1}^M$ 
Bayes 定理给出
$$\begin{align}p(\pi ,M\mid DI)&\propto p(D\mid \pi,MI)p(\pi,M \mid I)\\&=p(D\mid \pi,MI)p(\pi\mid MI)p(M\mid I)\end{align}$$
$M$ 的后验可以通过 marginalization 得到
$$p(M\mid DI) = \int p(\pi,M\mid DI)\mathrm{d}\pi$$
对于 $M$ 使用均匀先验, 对 $\pi$ 使用多峰 Jeffreys 先验
$$p(M\mid I) = \text{const.} \quad p(\pi\mid MI) =\frac{\Gamma(M/2)}{\Gamma(1/2)^M} \prod_{k=1}^M \pi_k^{-1/2}$$

似然是容易计算的, 因为若 $x_i \in [x_{k-1},x_k)$ , 则 $p(x_i\mid \pi,MI)=h_k=(M/V)\pi_k$
即
$$p(D\mid \pi,MI)=(\frac{M}{V})^N \prod_{k=1}^M\pi_k^{n_k}$$

从而得到对数后验
$$\begin{align}\log p(M\mid DI)&=N\log M +\log \Gamma(M/2)-M\log \Gamma(1/2)\\& -\log \Gamma(N+M/2)+\sum_{k=1}^M \log \Gamma(n_k+1/2)+\mathrm{const.}\end{align}$$

得到的效果与前面两个差不多

但是还可以做得更好

>自适应分块: Bayes 块 -- Scargle(1998)
>对于固定宽度的网格
>* 丢失了局部的结构
>* 对于稀疏区域的数据使用较低效(浪费太多网格)
>* 在数据变化剧烈的区域表现不佳
>而对于 Bayes 块
>* 将区块的长度变为可变的, 自适应的
>* 这可以通过最大后验得到
>* 自适应方法能够捕捉到锐利的特征, 并且减少在稀疏区域的浪费
>这个算法最初是为了天文上的时间序列分析而引入的, 比如寻找 gamma 射线暴, 这就是一个极端的例子: gamma 射线爆发生的频率极低, 但信号强度极高, 这需要在一般区域使用较宽的网格, 而在疑似信号区域使用更细的网格捕捉特征

考虑 $N_b$ 个网格: 宽度 $\mathbf{T}=\{T_k\}_{k=1}^{N_b}$ , 网格数据 $D_k\subset D$
目标是对 $(N_b ,\mathbf{T})$ 在给定数据 $D$ 下联合优化
基础同样是 Bayes 公式
$$p(N_b,\mathbf{T}\mid DI)\propto p(D\mid N_b,\mathbf{T}I)p(\mathbf{T}\mid N_b,I)p(N_b\mid I)$$

对数似然
$$\ln p(D\mid N_b,\mathbf{T}I)=\sum_{k=1}^{N_b}\ln p(D_k \mid T_k I)$$

先验: 对 $\mathbf{T}$ 使用均匀先验, 但对 $N_b$ 应该选择一个更倾向于更少网格数对先验
$$P(N_b\mid I)\propto \gamma^{N_b}\quad 0<\gamma <1\quad 1\leq N_b\leq N$$
这样可以可以通过幂律惩罚过多的网格数

对于似然, 就需要引入假设
一种方式是采用 poisson 形式
考虑对每个块采用 poisson 过程 , 对于 $k$ 块的分布为 $\text{Poisson}\,\lambda_kT_k$
$$\begin{align}\ln \mathcal{L}^{(k)} &= \ln\mathcal{L}(n_k , T_k)=\ln p(n_k\mid N_b,T_kI)\\&=n_k\ln \lambda_k -\lambda_k T_k +\text{const.}\end{align}$$
最大化为 $\hat{\lambda}_k = n_k/T_k$

>这个假设源于光子计数: 每个 pixel 对计数都是 poisson 过程

最终的似然函数为
$$\ln \mathcal{L}_{\max} = \sum_{k=1}^{N_b} \ln \mathcal{L}_{\max}^{(k)}=\sum_{k=1}^{N_b}n_k(\ln n_k-\ln T_k)+\mathrm{const.}$$
>实际上这里在写出似然的时候已经做了一个优化过程, 我们找了一个假定为 poisson 过程下最可能的似然函数

同样也可以采用 Gauss 形式, 对 $k$ 个块服从 $\mathcal{N}(\mu_k , \sigma_k^2)$
似然
$$\ln\mathcal{L}(\{x_i,\sigma_i\}\mid N_b,TI)=-\frac{1}{2}\sum_{k=1}^{N_b}\sum_{i\in k}(\frac{x_i-\mu_k}{\sigma_i})^2+\text{const.}$$
最大化得到 $\hat{\mu_k}=S_{1,k}/S_{0,k}$ 这里 $S_{n,k}=\sum_{i\in k}x_i^n/\sigma_i^2$

>同样, 这源于假定每个data产生都来自于一个 gauss 分布


>Scargle 在 2013 年完善了上面的方法, 并提出了更多的方法
>更多细节可以看 Scargle (2013)


可以看到在新方法下, bin 的数量明显变小, 并且成功捕捉到了较小的尖峰

>一个成功的应用是 Mondal et al. 在 2021 年利用此方法分析了 gamma射线暴的光变曲线, 并得到了射线暴的各个阶段


>Summary: Histogram
>用分段常数的方式从采样中估计密度


但直方图仍有一些问题:
* 这仍然依赖于 bin 的起始位置, 对平移没有 robustness
* 对边界有 bias 并且不连续, 
* 对范围有敏感性
* 在高维情形很难处理


## 连续估计
### Kernel density estimator

第一种方法是 Kernel density estimator (KDE)
* 对每个样本放一个小包
* 加上所有的包
* 不存在 bin 的边界

estimator 为
$$\hat{f}_h(x) = \frac{1}{N h^D}\sum_{i=1}^N K(\frac{d(x_i,x)}{h})$$
其中 $K(x)$ 为 kernel function
$h$ 为带宽, 控制这个包的弥散
$d(x_i,x_j)$ 为距离函数, 通常用 Euclidean 距离

可以看到结果明显依赖于带宽 $h$ 的选择, 反而和核函数的选择无关, 这回到了我们前面选择 bin 宽度的问题
小的带宽会导致噪声影响过大, 使得过拟合, 而大的带宽会导致欠拟合

这里同样可以有 Scott's rule 以及对 Gauss型分布的 Silverman‘s rule
$h_{Scott}=1.06\hat{\sigma} N^{-1/5}$  $h_{Silverman} =0.9 \min(\hat{\sigma},\frac{q_{75}-q_{25}}{1.34})N^{-1/5}$

也有更好的方法: cross - validation
选择某种似然函数进行最大化, 例如 leave - one -out (LOO) : 扔掉一个点之后不影响整体分布
$$CV_{LL} = \frac{1}{N}\sum_{i=1}^{N}\log \hat{f}_{h,-i}(x_i)$$
这里 $\hat{f}_{h,-i}$ 是扔掉第 $i$ 个数据的似然估计

同样可以去做 MISE, 最小化误差平方
$$CV_{MISE}(h) =\braket{\int(\hat{f}_h-f)^2\mathrm{d}x}$$


这种方法的结果很好, 除了某些太小的 feature 没有捕捉到, 同时这给出了一个连续的分布

这种方法也能很好处理数据的误差

> 测量误差
> 假设真实的分布为 $h(u)$ , 误差的分布为 $g(\epsilon)$ , 则分布 $f(x=u+\epsilon)$ 由如下结果给出
> $$f(x) =(h*g)(x) =\int h(u)g(x-u)\mathrm{d}u$$
> > 实际上 KDE 本身就是 convolution
> 这样假设误差具有加性, 且分布已知, 我们可以直接在 KDE 上反卷积, 得到真实分布
> 注意: 这种方法可能会增加误差
> 

KDE 在高维有自然的推广
$$\hat{f}_{\mathbf{H}}(\mathbf{x}) = \frac{1}{N} \sum_{i=1}^N |\mathbf{H}|^{-1/2} K(\mathbf{H^{1/2}}(\mathbf{x}-\mathbf{x}_i))$$

通常有 pre - whitening: 将数据变为具有单位协方差的数据

但是这种算法不能避免 Curse of dimensionality
这时可以采用一些降维的方法

>Summary
>这是一种通过点之间的核函数获得分布的非参数方法
>带宽 $h$ 的合适选择有时比核函数的形式更重要
>带宽选择的准则通常是 $h\propto N^{-1/(D+4)}$
>通过 cross - validation 可以优化带宽
>反卷积可以在误差已知时消除误差
>

### k - NN 方法

另一种方法为 k - nearest neighbor ( k - NN) estimator

这基于近邻估计
$$\hat{f}_k(x) = \frac{k}{N V_D(d_k)}$$
$d_k$ 是距离第 $k$ 个最近点点距离
$V_D(d_k)$ 是半径为 $d_k$ 的球体积

这是一种自适应地平滑方式, 能够自动选择核函数

在高维时仍然需要数据清洗

同样, 这里需要选择 $k$ , 一般不能选择太小的 $k$ , 否则受噪声影响较大

经验上选取 $k\simeq [N^{4/(4+D)}]$
然后用一个似然函数去做最大化优化, 比如 LOO 似然方法

结果也不错

## 基于 AI

### 神经密度模型
目标: 从数据中学习一个高维的, 平滑的分布

神经网络是一个非常普适的函数近似
两种比较直观的方法
* Normalizing flow: 从一个非常简单的分布出发 (比如 Gauss ) , 去学习一个双射, 可逆的映射, 把这个分布映射为数据的分布, 通过变量代换即可得到分布
* Autoregressive model: 想法比较相同, 逐次去做上面的过程
* 也有许多方法

#### Normalization flow
从一个简单的分布开始 $z_0 \sim \mathcal{N}(0,1)$
去做一系列可逆, 可微的变换
$$ z_k = f_k(z_{k-1})\quad ,\quad x =z_K =f_K \circ f_{K-1}\circ \cdots\circ f_1 (z_0)$$

一般要求可微, 这样就可以去做梯度下降
这样通过变量代换 
$$p_X(x) = p_Z(z_0) \prod_{i=1}^K|\det J_{f_i}(z_{i-1})|^{-1}$$
训练目标是最大化似然 
$$\underset{\theta}{\min}\frac{1}{N}\sum_{j=1}^{N}\log p_X(x_j;\theta)$$

> zephyr: 使用 normalization flow 去测光红移的推断 (Sun et al. 2023)

#### Autoregressive 
逐步去做条件分布
$$p(x_1,x_2,\cdots,x_D)=\prod_{i=1}^D p(x_i\mid x_1,x_2,\cdots,x_{i-1})$$
对每个条件分布可以使用神经网络得到
直观: 从先前给定的数据可以预测下一个数据
采样: 逐步采样
最后将这些条件分布乘在一起

## Simulation - based inference
目标: 当似然不容易得到的时候, 直接通过模拟数据去推断后验
idea : 在模拟数据对 $(\theta, x)$ 上用神经网络去代替似然


>一个应用例子是 SimBig (Hahn et al. 2022)
>在模拟数据上学习, 在现有宇宙的观测数据上得到宇宙学参数的分布


