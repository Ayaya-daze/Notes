现实世界的数据分析通常包含了很多参数 $$\mathbf{\theta}=(\theta_1,\theta_2,\dots,\theta_n)$$实际上的假设包含模型和这些参数 $H =\{M,\theta\}$
此时的 Bayes 定理为 $$p(\theta\mid M D I)=\frac{p(D\mid \theta M I)p(\theta\mid MI)}{p(D\mid M I)}$$实际上的后验分布是一个在高维参数空间中的分布

## 多参数后验分布

以谱线拟合作为例子: 
模型是 Gauss 线 $$\phi(\lambda)=\alpha\exp\left[-\frac{(\lambda-\lambda_0)^2}{2w^2}\right]+\beta\quad\quad[\text{photon }\text{s}^{-1}]$$
在时间 $t$ 内, 期望的光子在宽度为 $m$ 的端口 $M$ 计数为 $$N_i=\langle n\rangle(x_i,t)=\int_{x_i-m/2}^{x_i+m/2} \phi(\lambda)t\mathrm{d}\lambda\simeq mt\left\{\alpha\exp\left[-\frac{(\lambda-\lambda_0)^2}{2w^2}\right]+\beta\right\}$$
而光子计数服从 poisson 分布 $$P(n_i=n(x_i)\mid N_i)=\frac{N_i^{n_i}\mathrm{e}^{-N_i}}{n_i!}$$
>区分这两个光子计数:
>1. 第一个说的是在光子在某个谱线附近的计数的期望, 这可以用光谱计算
>2. 第二个说的是真正打到的光子计数, 强度由第一个计算得到的期望控制


数值计算后验分布上: 比如选择 $A,w$ 进行拟合

>选择 Jeffrey‘s 先验
>这里并不是指某种形式的先验(我们还不知道二维的 Jeffrey‘s 先验长什么样子), 而是应该利用一些未知性
>例如标度不变性: $$p(L\mid I)\mathrm{d}L=p(L\eta\mid I)\eta \mathrm{d}L\implies p(L\mid I)\propto 1/L$$

并且假设两个参数是独立的 $p(A,w\mid I)\propto 1/Aw$
从而得到对数似然: $$p(\{n_i\}_{i=1}^M\mid A,w,I)=\prod_{i=1}^Mp(n_i\mid A,w,I)=\prod_{i}^M\frac{N_i^{n_i}e^{-N_i}}{n_i !}$$则对数后验为 (注意实际变量)$$p(A,w\mid \{n_i\}_{i=1}^M ,I)=\sum_{i=1}^M(n_i \ln N_i -N_i)-\ln Aw+\mathrm{const.}$$通过模拟可以得到后验分布, 此时是二维的分布

边缘化:
* 若只关心 $w$ , 则可以将 $A$ 作为冗余参数, 积掉

边缘化得到的参数并不足以重建二维分布, 这是因为两个变量的相关性丢失了

## 关联与简并
高维情形方差有自然的推广 $$\mathbf{C}(\mathbf{\theta})=\left\langle (\mathbf{\theta}-\langle\mathbf{\theta}\rangle) (\mathbf{\theta}-\langle\mathbf{\theta}\rangle)^{T}\right\rangle$$这是一个对称且(半)正定的矩阵, 称为协方差矩阵
这足以确定一个 Gauss 型分布的形状
将协方差矩阵做 Cholesky 分解 $$\mathbf{\Sigma}=\mathbf{L}\mathbf{L}^T$$设 $\mathbf{x}$ 服从标准的 Gauss 分布, 则
$$\mathbf{y}=\mathbf{L}\mathbf{x}+\mathbf{\mu}$$
即为原分布

>如何理解协方差?
>实际上反映了不同变量的某种相关性

通过将变量标准化, 得到的协方差矩阵称为相关系数矩阵
相关系数: 矩阵元定义为 $$\rho_{ij}=\frac{\left\langle( \theta_i -\langle\theta_i\rangle)(\theta_j-\langle \theta_j\rangle)\right\rangle}{\sigma_i \sigma_j}$$可以看到这是有界的
不相关性: 通常称两个变量是不相关的, 如果他们的相关系数为 $0$
这个条件等价于 $$\langle \theta_i\theta_i\rangle=\langle\theta_i\rangle\langle\theta_j\rangle$$但注意相关性并不意味着独立性, 或者只能认为在期望的意义上独立


>多元分析是必要的吗?
>对单参数情形的推断: 考虑比较不同 $A$ 下 $w$ 的分布, 可以发现对于不同的 $A$ , $w$ 的分布差异极大, 可以想象对于固定的变量, 实际上是给定了一个 delta 先验, 这实际上给后验带来了 bias 并且低估了不确定度


## 导出参数

当物理参数与模型参数不同时, 如何从模型参数中得到物理参数
  --实际上就是变量代换
例如 有变量代换关系 $y=f(x)$ 则有后验关系 $$p(x\mid DI)=p(y\mid DI)\left|\frac{\mathrm{d}f}{\mathrm{d}x}\right|$$
>这对多元情形是一致的 $\mathbf{y}=\mathbf{g}(\mathbf{x})$
>则分布由 Jacobian 传递 $$p(\mathbf{x}\mid DI)=p(\mathbf{y}\mid DI)\cdot |\nabla\mathbf{g}|$$

而误差的传递关系是类似的: $$\mathbf{y}\simeq\mathbf{g}(\mathbf{x}_0)+\nabla\mathbf{g}(\mathbf{x}_0)^T\cdot(\mathbf{x}-\mathbf{x}_0)$$
则 $$\delta\mathbf{y}\simeq\nabla\mathbf{g}(x_0)^T\delta\mathbf{x}$$
实际上协方差为 $$C(\mathbf{x})=\langle \delta\mathbf{x}\delta\mathbf{x}^T\rangle$$线性误差的传递: $$C(\mathbf{y})=\langle\delta\mathbf{y}\delta\mathbf{y}^T\rangle=\nabla\mathbf{g}(\mathbf{x}_0)^TC(\mathbf{x})\nabla\mathbf{g}(\mathbf{x}_0)$$

即使两组参数都是负相关, 而物理参数的计算参数不同, 也会出现不同的相关性, 这种现象也是我们期望的
这样能够更好地约束数据
