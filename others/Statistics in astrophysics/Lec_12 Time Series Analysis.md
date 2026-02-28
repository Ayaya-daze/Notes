时间序列
实际上一般是二维数据

* 没有对时间采样对假设性
* 数据之间也许不独立

目标是
* 找一些数据上的关联, 比如周期
* 预测未来的值

> 典型的时间序列
> 包括周期性的 periodic , 比如变星的光变曲线
> 爆发性的 burst , 比如 gamma 射线暴
> chirp 比如引力波
> 但是一般的真实数据并不是这样的
> 总之我们将面临的数据: 采样不均匀, 误差极大, 存在 gap , 探测极限等


>基本方法
>时域分析
>频域分析
>时-频域分析

# 傅立叶分析
傅立叶变换即


实际上是使用了周期性的基函数
频谱包含两部分: 振幅和相位


傅立叶变换的有很多性质
* 线性性
* 时间缩放
* 频率平移
* 时间平移
* 频率平移

同样也有对称性


卷积性质

事实上大自然有一大部分卷积过程

>Summary


在采样等间隔的情形 Fourier 变换是容易进行的, 此时为 DFT

Nyquist frequency
$$f_{Ny}$$

考虑一个 Gauss 在高频采样下得到的傅立叶变换

在低频区域可以复原原先函数的信息


但如果采样点较稀疏, 高频信息会混合, 在 Nyquist frequency 以外部分的信息丢失了

功率谱, 即描述了傅立叶基的权
$$P(f)=|H(f)|^2 + |H(-f)|^2$$

有 parseval's theorem

在离散情形也有估计

FFT: Fast Fourier Transform
将计算复杂度降低到 $\mathcal{O}(N\log N)$

对于真实数据, 同样采用的是 Bayes 方法

直接的 DFT 并不容易使用, 即使对于均匀采样也有噪声导致的问题

另一种策略为 periodogram

>
>对于采样的数据
>Schuster periodogram
>$$P_S(f)=\frac{2}{NV}[R(f)^2+I(f)^2]$$
>在没有噪声时等价于 DFT

例子: 
假设对一个周期函数加上 gauss 噪声

即使加了一个 gauss 噪声, 也能看出一个主要的频率

同样考虑 aliasing 效应

对于这种非均匀采样, 同样有periodogram

此时真实数据采样的有效数据比前面均匀采样的数量多

>为何非周期采样的效果有这么强
>Jaynes 证明了对于简单的单频率信号, 即使有 gauss 噪声, 此时的频率后验正比于 periodogram 的exp
>指数把这种效应更放大了

这种方法等价于 chi - squared 方法

>对于更多推广
>VanderPlas

# Localized & stochastic signals

对于爆发信号
$$y_B(t|)$$

同样, 对于 chirp 信号


这两种信号都是局域的, 此时傅立叶变换就不是一个好方法了

另一种方法为 spectrogram

>spectrogram
>即为短时的傅立叶变换


对于 chirp 类型的事件是有用的

>一个例子是 LIGO 的数据处理


## Wavelet Transform
实际上也是局域的傅立叶变换, 即选择一个特定的窗口函数
$$H_{w}(t_0;f_0,Q)=\int_{-\infty}^{\infty}$$

窗函数为小波函数

可以得到小波功率谱 scalogram

对于 burst 信号


对于 chirp 信号

表现得很好


# 随机过程 stochastic process
一个随机过程是一系列被时间标记的随机变量 $\{y(t):t\in\mathbb{R}\}$
* 无法被预测
* 不同点之间可能有关联

一些例子是
* AGN 的光变


## 自相关函数
描述不同点之间的关联, 可以引入相关函数
$$CF(\tau)=\frac{1}{\sigma_{f}\sigma_g}\underset{T\to\infty}{\lim}$$
同样有自相关函数


>ACF 的性质
>* $ACF(0)=1$
>* 对于
>* 实际上是功率谱的傅立叶变换


一个例子是有阻尼的随机游走
即为 
$$y(t+\Delta t)=y(t) e^{-\Delta t/\tau}$$

现在需要提取衰减信号, 做法是做离散版本自关联函数

模拟计算得到

