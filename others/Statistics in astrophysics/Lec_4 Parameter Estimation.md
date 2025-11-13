这节课的目的是学会怎么将先验变为后验等

## 统计推断
回到之前抛硬币的问题:

>* 背景信息: 同一个硬币扔了 $N$ 次, 且每次扔硬币独立
>* 参数: 正面概率 $f\in [0,1]$
>* 分布: 二项分布, 即 $n$ 次正面结果的概率为 $$P(n\mid N,f)=\frac{N!}{n!(N-n)!}f^n(1-f)^{N-n}\quad n=1,2,\cdots,N$$

这样一个抛硬币的逆问题是: 

>* 观测数据 $D=(N,n)$ 即 $N$ 次抛硬币有 $n$ 次正面结果
>* 假设 $H$ : 一个假设族 $\{H_f\}$ 意思是正面的概率为 $f$ 
>* 目标: 求出后验概率, 即 $P(H\mid ID)$

对于连续型的随机变量, 后验概率的解释为 $$p(f\mid N,n)\mathrm{d}f=P(H_{f\in[f,f+\mathrm{d}f)}\mid DI)$$即后验概率分布

这在天文中有相同的问题: 超新星 supernova 的记录
超新星观测概率的推断: 根据已有的超新星观测数据, 能否推测未来观测到超新星爆发的概率?
* 原则上, 这需要恒星演化, 分布等知识
* 作为简单且合理的模型, 认为超新星爆发的发生率是常数, 因为我们的观测时间远短于超新星的寿命
即观测到的概率极小且观测次数很多
这可以被认为是一个近似 poisson 分布, 并且从历史记录上还可看见 poisson 分布的 clumps 现象

作为简化, 可以直接简化为 bernoulli 实验:
* 将时间分隔为每个区间超新星爆发次数在一次以内, 即时间间隔为100年
* 每个超新星爆发的观测率相同, 在 11 次实验中成功了 5 次
现在需要推断的参数即为观测成功率 $f$

在这个模型下, 预测下一个百年内观测到超新星爆发的概率:

回到 Bayes 定理: $$P(H\mid DI)=\frac{P(D\mid HI)P(H\mid I)}{P(D\mid I)}$$
在这个问题下: 

>* 先验: 实际上对此一无所知, 只知道他在 $[0,1]$ 之间, 所以 $f$ 的先验分布为 $$P(H\mid I_{0})=\begin{cases}1\quad 0\leq f \leq 1 \\ 0 \quad \text{otherwise}\end{cases}$$
>* 似然: 即为二项分布, 认为是二项分布 $$P(D\mid HI_0)\propto f^n(1-f)^{N-n}\quad f\in [0,1]$$
>* 后验: 通过 Bayes 公式计算得到: 正比于二项分布 $$P(H\mid DI_0)\propto f^n(1-f)^{N-n}\quad f\in[0,1]$$
>>注意: 似然和先验并不同, 注意概率的事件: 似然是样本 $D$ 即变量是 $n$ , 而后验是假设 $H$ 变量是 $f$

将似然归一化后, $$\int p(f\mid N,n,I_0)\mathrm{d}f =1$$得到 $$p(f\mid N,n,I_0)=\frac{(N+1)!}{n!(N-n)!}f^n(1-f)^{N-n}$$这实际上是 beta 分布 $B(n+1,N-n+1)$ 

## 理解后验
后验分布告诉了我们什么东西: 
* 没有数据时, 后验就是先验
* 当数据逐渐增加时, 后验的形状收到数据影响, 得到一个新的分布

统计结果在多大程度上依赖于先验?

>这里使用了两种先验进行模拟
>1. Gauss 先验: 即 $$P(H\mid I_1)\propto \exp\left[-\frac{1}{2}(\frac{f-0.5}{0.05})^2\right]$$
>2. 认为我们真的一无所知: Jeffreys' prior $$P(H\mid I_2)\propto \frac{1}{\sqrt{f(1-f)}}\propto B\left( \frac{1}{2},\frac{1}{2} \right)$$

可以看到: 当数据量增多时, 两种后验都趋于同一个分布

>总结: 
 >* 当数据极少时, 先验的影响较大
 >* 当数据很多时, 似然的影响较大
 >* 如果先验与真相排斥时, 这个收敛速度会减慢
 >* 对于极端值 $f=0,1$ 收敛速度极快, 而对一些中间值会慢些


## 参数估计

给定参数 $f$ 的后验分布后, 对 $f$ 的最佳估计是什么?这个估计有多可靠?

### moments estimation
一种方式是用矩评估: 在这个例子中
对均匀分布的先验的矩 $$\langle f^m\rangle =\int_0^1f^m p(f\mid N,n,I_0)\mathrm{d}f=\frac{(N+1)!(n+m)!}{n!(N+m+1)!}$$这表明均值 $$\mu_f =\langle f\rangle = \frac{n+1}{N+2}$$从而标准差 $$\sigma_f =\sqrt{\langle f^2\rangle-\langle f\rangle^2}=\sqrt{\frac{\mu_f(1-\mu_f)}{N+3}}$$在这种情况给出了参数 $f$ 的最佳估计 $\mu_f$

>但这和我们的直觉 $f_0=n/N$ 不同, 这个值去哪里了?
>这其实是另一种估计方式
>这其实是 $p(f)$ 的极值, 对于对称的分布, 这两者相同


>平均值的具体含义是什么: 下面会解释这一点
>* 假设未知参数的真值为 $\theta$ 
>* 给定数据 $D$ 和先验 $I$ , 我们可以用估计值 $\hat{\theta}$ 对 $\theta$ 做估计, 这给出估计误差 $\epsilon=\hat{\theta}-\theta$
>则偏差平方的期望为: $$\begin{align}\langle \epsilon^2\rangle&=\langle (\hat{\theta}-\theta)^2\rangle\\&=\langle\hat{\theta}^2-2\hat{\theta}\theta+\theta^2\rangle\\&=\hat{\theta}^2-2\hat{\theta}\langle \theta\rangle+\langle\theta^2\rangle\\&=(\hat{\theta}-\langle \theta\rangle)^2+\langle\theta^2\rangle-\langle\theta\rangle^2\end{align}$$
>
>即估计值为均值 $\langle \theta\rangle$ 时 , 这能够最小化 $\langle \epsilon^2\rangle$ 

但只有均值好吗?
* 这并没有一个标准答案, 取决于你想最小化什么
* 明显的问题:
		robustness: 对概率分布的拖尾十分敏感, 有的分布可能均值并不存在
		consistency: 对一个参数的非线性变换, 这种选择并不传递, 故在参数变换下最小平方误差期望的选择不同,即 $$\lambda(\langle\theta\rangle)\neq\langle\lambda(\theta)\rangle$$

### Laplace‘s Criterion
Laplace 认为并不用最小化 $\langle \epsilon^2\rangle$ , 而选择最小化 $\langle |\epsilon|\rangle$ 这给出了另一个参数估计 $\tilde{\theta}$:
这实际上要求估计值为中值, 因为 $$\langle |\epsilon|\rangle= \int_{-\infty}^{\tilde{\theta}}(\tilde{\theta}-\theta)p(\theta)\mathrm{d}\theta+\int_{\tilde{\theta}}^{+\infty}(\theta-\tilde{\theta})p(\theta)\mathrm{d}\theta$$对 $\tilde{\theta}$ 变分得到 $$\frac{\mathrm{d}\langle|\epsilon|\rangle}{\mathrm{d}\tilde{\theta}}=\int_{-\infty}^{\tilde{\theta}}p(\theta)\mathrm{d}\theta-\int_{\tilde{\theta}}^{+\infty}p(\theta)\mathrm{d}\theta$$这恰好是分布的中值

>中值作为估计值:
>* 对于拖尾有更高的 robustness
>* 对单调的参数变换满足 consistency 
>>(实际上这对百分位数都成立)
>>即使一, 二阶都不存在, 也可以使用此方法, 这个值总是有定义

>如何得到中值估计的置信区间?
>一般的选择是: 选择不同的百分位, 比如用 Gauss 分布一个 $\sigma$ 的  68%估计 :
>则低于$\mu-1\sigma$ 到 $\mu+1\sigma$ 给出了16 -50 -84 百分数

>对于看后验的峰这样的方法是什么估计方法?
>这种估计称为: maximum a posterior -- MAP (最大后验方法)
>但这有许多问题
>* 这个方法没有一个普适的最小化函数
>* 这个方法对于多峰和平顶的分布无能为力
>* 对噪声较敏感
>* 在重参数下不保持不变

而在现实问题中常常遇到奇异的多峰后验分布情形, 这时我们能做的是:
* 直接使用百分位数估计
* 直接给出不同估计方式的后验分布是 no-harm 的
* 如果十分奇异, 可以直接给出后验分布是最优的

>总结
>"The best way to convey to the experimenter what the data tell him is to show him a picture of the posterior distribution" -- G. E. P . Box & G. C. Tiao (1973)
>给出后验分布是最佳的

