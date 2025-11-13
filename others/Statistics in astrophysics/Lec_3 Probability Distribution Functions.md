伯努利实验与二项分布
抛硬币问题:
考虑背景信息 $I$ :
* 抛出大量的硬币, 这些硬币都是全同的
* 用一个信息向量储存结果 $\textbf{d}=(d_{1},\cdots)$ , $d_{i}\in{0,1}$ 
* 用 $\mathbf{d}^{(n)}$ 表示前 $n$ 次结果的数据向量
 

问题的分析:

无差别原则: $$P(d_{i}=0\mid I)=P(d_{i}=1\mid I)=\frac{1}{2}\quad P(\mathbf{d}^{(n)}\mid I)=2^{-n}$$
这样给定前 $n-1$ 次结果 $\mathbf{d}^{(n-1)}$ $$P(\mathbf{d}_{(n)}\mid \mathbf{d}^{(n-1)},I)=$$即$$P(\mathbf{d}_{(n)}\mid \mathbf{d}^{(n-1)},I) = P(d_{n}\mid I)=\frac{1}{2}$$这表明之前的抛掷硬币结果并不影响后面的结果, 即可以认为它们是统计独立的

$A$ 和 $B$ 是在 $I$ 下是统计独立的, 当且仅当 $$P(A\mid BI)=P(A\mid I)$$当然也有其他写法

推广到一组事件 $\{A_{i}\}_{i=1}^{n}$ 称为在 $I$ 下两两独立,


然后推广抛硬币问题, 认为抛硬币事件各自独立, 而且认为抛出正面的概率为 $f$ , 这就是 $n$ 次伯努利实验
从而获得 $n$ 次正面的概率为 $$P(n\mid N,f,I)= P(\sum_{i=1}^Nd_{i} = n \mid N ,f ,I) = \frac{N!}{n!(N-n)!}f^n(1-f)^{N-n}$$这个分布叫做二项分布

描述一个分布, 也可用一些抽象的统计量描述, 一个常用的统计量是 矩 (moment)
m - moment $\langle X^m\rangle = \sum_{i}p(x_{i})x_{i}^m$ 
例如: 期望是 1阶矩, 方差是中心矩 (减去一阶矩后的二阶矩)

>二项分布的矩
>期望(中心) 
>方差
>标准差


Poisson 计数模型

考虑极端情况: 看一个源的亮度
假设一个源, 单位时间产生 $N$ 个光子, 每个光子被探测器接收到的几率为 $r$ 
则单位时间内有 $n$ 个光子穿过探测器的概率服从二项分布
实际上考虑上面的连续情况, 即 $\phi = Nr$ 通量是常值 ($N$ 很大 $r$ 很小)
在上面的极限下 $$\frac{N!}{(N-n)!}r^n$$
则二项分布在极限下变为 $$p(n\mid\phi)=\frac{\phi^ne^{-\phi}}{n!}$$即为 poisson 分布

>possion 分布的性质
>均值
>方差
>标准差


在真实情况中, 还要考虑探测器的效率, 假设探测器的效率为 $\eta$ (忽略探测器探测不同光子需要时间的影响, 即认为它们是独立的)

则单位时间内从 $n$ 个光子中得到 $c$ 次计数也服从二项分布

现在我们知道通量 $\phi$ , 探测器的效率 $\eta$ , 则探测器计数 $c$ 的概率为 $$p(c\mid \eta ,\phi)=\sum_{n=0}^\infty p(c\mid n, \eta,\phi)p(n\mid \eta,\phi)=\sum p(c\mid n,\eta)p(n\mid \phi)=\frac{(\eta \phi)^c}{c!}e^{-\eta\phi}$$这里是考虑了因果关系 $\phi\to n\overset{\eta}{\to} c$
即一个新的 poisson 分布
这是poisson 分布的一个性质: thinning , 还有一个性质是 superposition 

poisson 噪声
* 天文中的光子通量一般较低, 可以应用 poisson 分布
* 在 photon-limited 情况: 忽略背景, 探测器的效应等问题, 只关注源放出的光子数
	* 则信号强度 $S=\phi t$ 即光子数的期望
	* 噪声 $N=\sqrt{\phi t}$ 即光子数的标准差
	* 信噪比 $S/N=\sqrt{\phi t}$ 
天文中解决方案: 更大的望远镜提高通量, 且增长曝光时间


sky - limited 情况: 天空背景的信号较强, 即添加天空的信号 $\phi_{sky}$ 
	信号 $S = \phi t$ 
	噪声 $N=\sqrt{\phi_{sky}t}$ 
	从而信噪比 $$S/N=\frac{\phi}{\sqrt{\phi_{sky}}}\sqrt{t}$$此时更加困难, 由于 $\phi_{sky}>\phi$ , 所以应该在更暗的时候观测

Gaussian 分布
$$p(x\mid\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})=\mathcal{N}(\mu,\sigma)$$注意到 gauss 分布只有一阶和二阶矩, 其他都消失

二项分布: 当 $N\to\infty$ 时, 即高阶矩越来越小, 最后消失
poisson 分布: 当 $\phi\to\infty$ 时

Herschel's derivation 

考虑观察恒星的位置的不确定度 $\rho(x,y)$ 
* 独立性: 认为位置的两个自由度独立 $$\rho(x,y)\mathrm{d}x\mathrm{d}y=f(x)\mathrm{d}xf(y)\mathrm{d}y$$
* isotropy : 概率分布旋转不变 $$\rho(x,y)\mathrm{d}x\mathrm{d}y=g(r,\theta)r\mathrm{d}r\mathrm{d}\theta$$则$g(r,\theta)=g(\sqrt{x^2+y^2})$

这有通解 $f(x)\sim \exp(-\alpha x^2)$ 

3d 情况 : 比如 maxwell 速度分布

中心极限定理
见ppt


反例: 洛伦兹分布(柯西分布)

percentile

从概率分布中采样

生成一个 gauss 分布?
np 有直接的代码, 但是能不能自己构造一个方法
或者说用均匀分布生成任意的分布

考虑一个均匀分布的随机变量 $u$ 
取常数 $m$ , 
ppt

采样逆变换

考虑 cdf $$F(x)=\int_{-\infty}^{x}p(x')\mathrm{d}x'$$均匀采样纵坐标 $u\in[0,1)$ , 计算反函数 $x=F^{-1}(u)$ 
这要求 cdf 有逆或者存在, 这时候有将 cdf 进行插值

在一些情况可以考虑变量代换

将 $p(x)$ , 变为 $g(y=r(x))$ 
* 若 $r(x)$ 是单调增的 $$G(y)=F[r^{-1}(y)]\quad g(y)=p(r^{-1}(y))\frac{\mathrm{d}r^{-1}(y)}{\mathrm{d}y}$$
*  若 $r(x)$ 是单调减的 $$G(y)=1-F[r^{-1}(y)]\quad g(y)=-p(r^{-1}(y))\frac{\mathrm{d}r^{-1}(y)}{\mathrm{d}y}$$
* 统一地 $$g(y)=p(r^{-1}(y))|\frac{\mathrm{d}r^{-1}(y)}{\mathrm{d}y}|$$

例子: gaussian 
此时不存在初等的 cdf , 可以尝试采样二维 gaussian 分布 $$r\exp(-\frac{r^2}{2})\mathrm{d}r\mathrm{d}\theta$$这样就有可积的 cdf 了$$u\sim \exp(-\frac{r^2}{2})\quad v \sim\frac{\theta}{2\pi}$$从而有随机数 box -muller

poisson 分布的到达时间分布 服从指数分布

poisson 分布的 clump
