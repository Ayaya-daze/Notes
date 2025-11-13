之前依据常识建立了一系列数学工具, 现在再通过常识做一些筛选

对于有效的数据, 哪一个模型是最好的?

## 假设检验
首先还是从 Bayes 定理开始 $$P(H\mid DI)=\frac{P(D\mid HI)P(H\mid I)}{P(D\mid I)}$$
考虑一个二元的假设检验情形:  两个互补的假设 $H,\overline{H}$ . Bayes 定理给出了两者的后验

当比较两个假设的后验时: 证据自然消失了, 此时后验比 $$O_H =\frac{P(H\mid DI)}{P(\overline{H}\mid DI)}=\frac{P(D\mid HI)}{P(D\mid \overline{H}I)}\cdot \frac{P(H\mid I)}{P(\overline{H}\mid I)}=\frac{P(H\mid DI)}{1-P(\overline{H}\mid I)}$$则, 我们认为
*  $O_H \gg 1$ 时, $H$ 更可信
*  $O_H\ll 1$ 时, $H$ 没有那么可信
*  $O_H\simeq 1$  时, 无法给出结论

对多模型 $\{H_i\}$, 也可以定义后验比 $$O_{ij}=\frac{P(H_i\mid DI)}{P(H_j\mid DI)}$$
> 如何解释后验比?
> 对于后验比选择的值, 一般没有一个黄金原则, 这和决策过程也有关系, 取决于你如何做出决策确定最佳的模型, 这不仅仅是概率的问题
> 但一般有些经验准则, 会用 $\log O_H$ 的数值刻画 (人的感知是对数的)

> Weber - Fechner law 感知的对数性
>>视星等的划分也基本是按照对数划分的

再次回到抛硬币的例子:
考虑一个公平的硬币和不公平的硬币, 现在无法区分这两块硬币, 我们需要做实验判断拿出的硬币是哪块硬币
则现在需要测试的就是一个二元的假设检验问题: 是 or 不是
公平的硬币抛出正面的概率是 1/2 , 而不公平的硬币抛出正面的概率是 1/4 .

我们通过假设检验, 做实验判断这两枚硬币:

假设 $H$ : 硬币是公平的, 以及其反面 $\overline{H}$ 

先验: 显然我们什么都不知道, 所以概率是 1/2 , 则后验比即为似然比
并且由于每次实验独立, 似然为 $$P(D\mid HI)=P(\{d_i\}\mid HI)=\prod_i P(d_i\mid HI)$$
则对数后验比的形式为 $$\ln O_H =\sum_i (\ln P(d_i\mid AI)-\ln(d_i\mid B I))$$

>可以看到实验给后验比的对数线性的贡献:每次做一次抛硬币实验: 出现正面后, 后验比增加
>而后验比越大, 表明 $A$ 更可信: 每有一次正面结果, $A$ 更可信, 因为 $B$ 更倾向
>这和我们的经验相符

>而如果加入不同的先验, 可以发现这仅仅是改变了零点: 需要更多的正面数据支持一个结果

但是这显然有问题! 这个比不能无限制地线性增大!

>假设前50次都是正面, 后验比表明 $A$ 更有可能, 但是你也不应该相信这是一个公平的硬币!
>问题在于: 开始的模型就错了, 我们一开始只放了两个假设: 但是显然可能有更多的假设
>所以我们需要设置一个机制, 能让我们对问题有合理的怀疑


>一个简单的方法是引入一个 “死”假设 $C$: 
>有一个很坏的硬币, 极有可能抛出正面, 比如 0.99 的概率, 但给他分配极低的先验 $\sim 10^{-6}$ , 现在的就变
>成了三个模型的假设检验问题

注意到假设 $A,B,C$ 是互斥且穷尽的 $A+B =\overline{C}$ 
这样可以得到 $C$ 的后验比 $$O_C =\frac{P(C\mid DI)}{P(\overline{C}\mid DI)}=\frac{P(C\mid DI)}{P(A\mid DI)+P(B\mid DI)}$$可以取一个全为正面的样本 $\hat{D}$ 
可以作出三个模型的后验比的图: 从图上看出:
有三个几乎线性的阶段
* 阶段 1 : $A \,\text{v.s.}\, B$  
* 阶段 2 : $A\,\text{v.s.}\, C$ , $C$ 的后验比超过了 $B$ 的后验比
* 阶段 3 : $C\,\text{v.s.}\,A$ , $C$ 占了主导

最后由于有大量极端数据. 死假设 $C$ “复活”了

>总结
>* 二元情形: 后验比 = 似然比 $\times$ 先验比
>	对独立的数据, 后验比的对数是线性依赖的
>	先验设置了某种拦截机制
>* 决策通常在对数尺度进行
>* 极端数据可以"复活"死假设
>* 多模型分析: 后验之间相互耦合, 配对原则并不普适
>* 可以做局部的二元推断: 识别两种占主导的模型


## 备选假设

再次回到抛硬币的问题
>如何测试一个硬币是不是公平的?
>$f$ 是一个连续的分布, 考虑 $f=\frac{1}{2}$ 显然是一个糟糕的说法, 显然连续变量取任何值的概率都是 $0$
>正确的说法是考虑一个区间$$\Omega =\{f\in [0,1]\mid |f-1/2|\leq \epsilon\}$$ 而他互补的假设为 $$\overline{H}=\{f\in\Omega^c\}$$现在问题变成了一个区间, 实际的 $f$ 已经成了一个冗余参数 nuisance parameter 
>考虑区间的时候你总应该把它积分掉, 这个过程即为 边缘化 marginalizatino

从而后验比 $$O_H=\frac{P(D\mid HI)P(H\mid I)}{P(D\mid\overline{H}I)P(\overline{H}\mid I)}=\frac{\int_\Omega p(D\mid f,I)p(f\mid I)\mathrm{d}f}{\int_{\Omega^c} p(D\mid f,I)p(f\mid I)\mathrm{d}f}$$
>在现实世界, 备选假设 $\overline{H}$ 的定义不是一个显然的东西. 通常一个说法的反面并不是良定义的
>* 一个假设的反面难以被表达: 假设: 一条直线 的反面是什么意思?
>* 为了计算后验比, 常常会找出一个备选假设

这个合适的假设叫零假设 null hypothesis
当然, 忽视或错误地选择空假设会导致严重的问题

>一个有趣的例子: 上世纪的特异功能的流行
>英国叫 stewart 的女士声称自己有心灵感应的能力, 实验是这样的:
>实验员给代理人翻牌, 然后翻, stewart 在另一个房间翻牌, 同时另一位实验员来记录
>进行了近 3万次实验, stewart 猜对了 9k 次左右
>用伯努利分布 $p\simeq 0.2$来估计她猜对的次数 $\langle n\rangle \simeq 7420 \pm 77$ , 高了几十个标准差
>她是真的有心灵感应吗?

现在来描述这个问题 假设 $H_t$ : 她有超能力 , 零假设 $H_0$: 她没有超能力
这里遇到了和抛硬币一样的问题: 需要假设多大的正确概率 $f$ 才能确定她有超能力?
可以是一个值,  也可以是一个区间

不妨设先验是一个正态分布 $$p(f\mid I)\propto \exp \left[-\frac{(f-0.2)^2}{2\times 0.004^2}\right]\quad f\in[0,1]$$我们用高于 $5\sigma$ 的 $f$ 值来代表 $H_t$ , 即
假设 $$H_t =\{f>0.22\}\quad H_0=\{f\leq 0.22\}$$
先验比 $$\frac{P(H_t\mid I)}{P(H_o\mid I)}\simeq 2.9\times 10^{-7}$$
可以发现: 先验极其拒绝这件事情

似然为二项分布: $$p(D\mid f,I)=\propto f^n(1-f)^{N-n}$$
对实验的数据计算得到
后验比 $$O_{t0}\simeq 10^{28}$$这是一个非常大的后验比, 表明:
极强的证据支持 stewart 有心灵感应的能力

>这对吗?

注意到一件事 $H_0 \neq \overline{H_1}$ : 零假设并不是反面假设! 
我们有很多死假设
*  $H_1$ : 记录出错了: 记录员写错了, 读错了...
*  $H_2$ : 数据被选择过
*  $H_3$ : stewart 作弊了
* ....

原则上你可以对任意一个死假设, 然后计算先验比

对于一个很怀疑这个假设的人: 他可以设立先验, 对任意死假设 $H_i$ 都应该比待测假设可信 $$P(H_i\mid I)> P(H_t\mid I)$$并且他们的似然是可比的, 则对任意 $i$ , 有 $$O_{it}=\frac{P(D\mid H_i I)}{P(D\mid H_t I)}\cdot\frac{P(H_i\mid I)}{P(H_t\mid I)}>1$$并且这个后验比随着极端数据的增多而增大, 这表明这些死假设比待测假设都更可信!

> 如果实验者想作弊说明这件事情: 他们不会成功
> 反而是增加了死假设的后验比
> 即使 $P(H_t\mid I)>0$ , $H_t$ 也不会被接受

>问题是: 上面是一个不相信超能力的人设置的先验, 如果是一个相信的人就会从同一个数据中能获得不同的结论
>那么
>数据到底告诉了我们什么?

>再看一个例子
>药物的安全性:
>一个叫 Oscar 的人公开宣称某种药物不安全 (即数据)
>现在我们尝试去计算这件事对药物是否安全, 在不同人下得出的结论


>现在有持不同观点 (先验) 的人
>Alice/Carol 相信药物是安全的 $P(S\mid I) =0.9$
>Bob/Dave 相信药物是不安全的 $P(S\mid I)=0.1$

>而似然 $$P(D\mid SI)\quad P(D\mid \overline{S}I)$$
>实际上似然反映了这四个人对 Oscar 这个人对可信度:
>>Alice: Oscar 这个人很正义, 且很少犯错 $P(D\mid SI)=0.01\quad P(D\mid \overline{S}I)=1$
>>Bob: Oscar 这个人正义, 但有时会犯错 $P(D\mid SI)=0.1\quad P(D\mid \overline{S}I)=1$
>>Carol: Oscar 这个人只是想博人眼球 $P(D\mid SI)=0.9\quad P(D\mid \overline{S}I)=1$
>>Dave: Oscar 只是想故意对着干 $P(D\mid SI)=0.99\quad P(D\mid \overline{S}I)=0.01$

现在来计算后验: 
计算证据(边缘化) $$P(D\mid I)=P(DS\mid I)+P(D\overline{S}\mid I)=P(D\mid SI)P(S\mid I)+P(D\mid \overline{S}I)P(\overline{S}\mid I)$$
最后的结果
>Alice: $P(S\mid DI) =0.083$
>Bob: $P(S\mid DI) =0.011$
>Carol: $P(S\mid DI) =0.890$
>Dave: $P(S\mid DI) =0.917$
>>即使是拥有着相同先验的两个人, 在不同的似然下也会得到及其不同的结果!!!

>对相同的数据, 不同的先验和似然都会导致结论不同


## 模型比较

上面模型的比较都是一个单一的模型, 实际上模型还带着一些参数

实际上的模型为 $H =\{M,\theta\}$ 此时的 Bayes 定理为 $$p(\theta M\mid DI)=\frac{p(D\mid MI\theta)p(\theta M\mid I)}{P(D\mid I)}$$

但此时发现: 后验比会更复杂
如果定义: 即模型下的证据$$E(M) =p(D\mid MI)=\int p(\theta D\mid MI)\mathrm{d}\theta=\int p(D\mid \theta MI)p(\theta\mid MI)\mathrm{d}\theta$$
再对参数做边缘化得到模型的后验 $$P(M\mid DI)=\int p(\theta M\mid DI)\mathrm{d}\theta=\int \frac{p(D\mid MI\theta)p(\theta M\mid I)}{P(D\mid I)}\mathrm{d}\theta$$注意到 $$p(\theta M\mid I)=p(\theta\mid MI)P(M\mid I)$$从而后验 $$P(M\mid DI)=\frac{P(M\mid I)}{P(D\mid I)}E(M)$$

从而有模型的后验比 $$O_{ij}=\frac{E(M_i)}{E(M_j)}\cdot\frac{P(M_i\mid I)}{P(M_j\mid I)}=B_{ij}\frac{P(M_i\mid I)}{P(M_j\mid I)}$$
可以看到模型下的证据比 $B_{ij}$ 出现在了后验中, 这称为 Bayes 因子

再次回到抛硬币:

现在比较两个模型 
* $M_1$ : 出现正面的几率是常数 $f$
* $M_2$ : 出现正面的几率未知

假设两个模型的先验相同, 则后验比即位证据比

参数的先验: 
* $p(f\mid M_1 I)=\delta(f-\hat{f})$
* $p(f\mid M_2 I)=\begin{cases}1\quad 0\leq f\leq 1 \\ 0\quad \text{else}\end{cases}$

后验比 $$O_{21}=\frac{\int_0^1 f^n(1-f)^{N-n}\mathrm{d}f}{\hat{f}^n(1-\hat{f})^{N-n}}=\frac{n!(N-n)!}{(N+1)!}\hat{f}^{-n}(1-\hat{f})^{-N+n}$$
这是一个二项分布的倒数, 即 $$O_{21}=\left[(N+1)\text{Binomial}(n,N,\hat{f})\right]^{-1}$$
进行模拟, 可以发现后验比是这样的行为: 
* 当 $\hat{f}$ 的值恰好是 $n/N$ 附近时, 到达极小值, 即 $M_1$ 更被偏好

这实际上是一个原则的体现: Occam's razor

> Occam's razor 
> ***The simplest explanation is usually the best one***
> 都能解释数据时, 更简单的模型更被青睐
> 当仅用一个固定值就能解释数据时, 就没有必要使用更多自由度的均匀分布
> 人们将此解读为 
> ***Entities are not to be multiplied without necessity*** 


在大样本的极限下, 后验比为 $$O_{21}\sim \sqrt{\frac{2\pi f_0(1-f_0)}{N}}(\frac{f_0}{\hat{f}})^n(\frac{1-f_0}{1-\hat{f}})^{N-n}\quad f_0=\frac{n}{N}$$
对 $\hat{f}\sim n/N$ 时 $$O_{21} \propto \frac{1}{\sqrt{N}}$$
又遇见了根号分之一

>Occam‘s razor 来源于哪里?
>考虑一个更简化但普遍的情况:
>* $M_1$ : 一个没有自由参数的模型
>* $M_2$ :一个有参数 $\theta$ 的模型
>* 对两种模型的选择没有先验的偏好

不妨假设, 模型参数是均匀分布的, 似然是 Gauss 的
即 $$p(\theta\mid M_2 I)=\frac{1}{\theta_{\max}-\theta_{\min}}\quad \quad p(D\mid M_2\theta I) = p(D\mid \theta_0 M_2 I) \exp\left[-\frac{(\theta-\theta_0)^2}{2\sigma_{\theta}^2}\right]$$这样, 模型参数的证据为 $$E(M_2) =\int p(D\mid M_2\theta I)p(\theta\mid M_2I)\mathrm{d}\theta=\frac{p(D\mid \theta_0M_2I)\cdot \sqrt{2\pi}\sigma_{\theta}}{\theta_{\max}-\theta_{\min}}$$
$M_1$ 的参数的证据 $E(M_1) =P(D\mid M_1 I)$

后验比 $$O_{21}=\frac{p(D\mid \theta_0M_2 I)}{P(D\mid M_1 I)}\cdot \frac{\sqrt{2\pi}\sigma_{\theta}}{\theta_{\max}-\theta_{\min}}$$
一般来说, 由于 $\theta$ 的存在, 会偏好于 $M_2$ , 但当参数的自由范围极大时, 这个效应被压低, $M_1$ 更受到偏好
因子 $$\frac{\sqrt{2\pi}\sigma_{\theta}}{\theta_{\max}-\theta_{\min}}$$称为 Occam 因子
