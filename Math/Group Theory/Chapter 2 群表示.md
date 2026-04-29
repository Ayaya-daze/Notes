# 群表示

## 基本概念

群表示的概念来自将群元素视为线性空间上的线性变换, 我们已经看到了很多例子, 下面给出一个一般的表述

> 为了方便, 下面先简单假设讨论有限群, 对非有限群的情况会特地区分

#### 定义
考虑群 $G$ , 一个群 $G$ 在线性空间 $V$ 上的线性表示是指一个同态

$$
\rho\colon G\to\mathrm{GL}(V)
$$

同态结构可以给出一些简单的性质

$$
\rho(1_G)=\mathrm{Id}_V\quad \rho(g^{-1})=\rho(g)^{-1}
$$

称 $V$ 是 $G$ 的表示空间, 在不混淆的情况, 也称 $V$ 是 $G$ 的一个表示

> 同样, 我们先假设 $V$ 是有限维的

称 $V$ 的维数为表示的维数, 不难看到, 若选择了 $V$ 上的一组基 $(e_i)$ 之后, $G$ 的线性表示能写成矩阵形式, 此时称为矩阵表示

从结构性的观点上看, 表示 $V$ 并不代表一个表示, 真正的关键是空间 $V$ 的同构类, 这导致我们应该也明确一个表示如何分类

#### 定义 同构/相似
若 $V$ 和 $V'$ 都是群 $G$ 的表示, 称他们相似/同构 isomorphic , 若存在线性空间的同构 $\tau \colon V\to V'$  满足

$$
\tau\circ \rho_s = \rho'_s \circ \tau \quad \forall s\in G
$$

特别的, 同构的表示具有相同的维数

先看群表示的一些例子, 从中可以看出有限群的一些结构

群 $G$ 的一个一维表示是一个函数

$$
\rho\colon G\to\mathbb{C}^{\times}
$$

由于 $G$ 是有限群, 这表明 $\rho(s)$ 都是 $\mathbb{C}$ 上的单位根(每个群元素都是有限阶的, 在同态下给出 $\mathbb{C}$ 上的代数方程), 特别的 $|\rho(s)|=1$ 

设群 $G$ 的阶为 $g$ , 且 $V$ 的维数为 $g$ , 选择由群元素 $t$ 标记的一组基 $(e_t)_{t\in G}$ 
对 $s\in G$ , 让 $\rho_s$ 将 $e_t$ 映至 $e_{st}$ . 这实际上定义了一个线性表示, 这称为 $G$ 的 regular representation

表示的维数等于 $G$ 的阶, 注意到实际上 $V$ 上的基可以被 $\rho_s$ 生成 $e_s=\rho_s(e_{1_G})$ , 即 $e_1$ 的像生成了 $V$ 的一组基

相反地, 取子空间 $W$ , 使其被其包含的向量 $w$ 在 $G$ 的表示的所有像下能形成 $W$ 的一组基

$$
W=\mathrm{Span}\{\rho_s(w):s\in G\}
$$

则 $W$ 同构于 $G$ 的 regular representation . 因为可以定义同构 $\tau:V\to W$ 合于 $\tau(e_s)=\rho_s(w)$ 

更一般地, 考虑群 $G$ 作用在有限集 $X$ 上, 让 $V$ 选择一组由 $X$ 中的元素标记的基 $(e_x)_{x\in X}$ 
定义表示 $\rho_s(e_{x})=e_{sx}$ 对 $s\in G$ , 如此给出的线性表示叫 permutation representation associated with $X$ 

> 上面的 $\rho_s$ 定义为什么是线性表示, 这来自于群作用的置换性, 因为 $\rho_{s}(e_t)=e_{st}$ 现在改变 $t$ 则 $\rho_s$ 在这组基下的像一一遍历了整个基, 所以这是一个同构, 并且可以看到在这组基下表示矩阵为置换矩阵
> 在下面群作用的例子是上面这个版本的推广 

## 子表示与不可约表示

#### 定义 子表示
设 $\rho \colon G\to \mathrm{GL}(V)$ 是线性表示, $W$ 是 $V$ 的线性子空间. 若 $W$ 在 $G$ 的作用下封闭, 即任意 $x\in W$  , 都有 $\rho_s(x)\in W$ 对任意 $s\in G$ , 则 $\rho_s^W=\rho_s \big|_W$ 是 $W$ 到自身的同构, 并且满足同态, 则

$$
\rho^W\colon G\to\mathrm{GL}(W)
$$

是 $W$ 的线性表示, 称其为 $V$ 的子表示

一个子表示的例子来自于正则表示, 取由 $x=\sum_{s\in G} e_s$ 生成的线性空间, 则限制在其上得到一个 1 维表示, 满足 $\rho_s x=x$ 对任意 $s\in G$ , 并且 $W$ 同构于单位表示

在区分出子表示后, 直觉上被子表示排除开的那一部分空间应该也对表示封闭, 这给出了一种对表示空间的分割方法

#### 定理
设 $\rho\colon G \to \mathrm{GL}(V)$ 是一个线性表示, 且子空间 $W$ 在表示下封闭, 则存在 $W$ 在 $V$ 中的补空间 $W^0$ 使其也对表示封闭

证:

> 证明的想法来自于线性代数, 即将这个补空间视作某种投影映射给出的子空间, 注意到补空间并非唯一, 而补空间实质上都是投影映射的核, 如果这个投影与任意表示都是交换的, 则表示对核也是封闭的, 故需要构造一个合适的投影

首先选取 $W$ 在 $V$ 中的任意补空间, 并给出一个投影 $p\colon V\to W$ , 则补空间 $W' =\ker p$
但是一般情况下

$$
p\rho_s \neq \rho_sp
$$

无法让交换性质满足, 这需要使用一种平均化的想法, 构造一个新的投影

$$
p^0 =\frac{1}{|G|}\sum_{s\in G}\rho_s^{-1}\cdot p\cdot\rho_s
$$

先证明这是投影, 由于 $p\colon V\to W$ , 且 $\rho_s$ 对 $W$ 封闭, 故这是一个投影, 然后再说明交换

对任意 $t\in G$ , 按照群本身的置换性质

$$
\rho_t^{-1} \cdot p^0\cdot \rho_t=p ^0\implies \rho_t \cdot p^0 =p^0\cdot \rho_t
$$

从而对于任意 $x\in \ker p^0$ , 有

$$
p^0 (\rho_t(x))=\rho_t (p^0(x))=0\implies \rho_t(x)\in \ker p^0
$$

即对该补空间 $W^0=\ker p^0$ 封闭

如果 $V$ 上还配备了内积结构 $(\cdot|\cdot)$ , 则还可以采取平均化的手段定义群作用不变的内积

$$
(x|y)=\frac{1}{|G|}\sum_{t\in G}(\rho_tx|\rho_t y)
$$

这样, 由该内积诱导的正交补也是一个对表示封闭的子空间, 并且注意到该内积对表示不变, 意味着若 $V$ 的基为标准正交基, 则 $G$ 的矩阵表示为酉矩阵, 因为

$$
(\rho_s)_{ij} =(e_i|\rho_se_j)=(\rho_s^{-1}e_i|e_j)=(\rho_s^{-1})_{ji}^*\implies (\rho_s)_{ik}(\rho_s)_{jk}^*=(\rho_s)_{ik}(\rho_s^{-1})_{kj}=\delta_{ij}
$$

这正是酉矩阵的定义

接着, 对任意 $x\in V$ 我们都有分解 $x=w+w^0$ 满足 $w\in W,w^0\in W^0$ , 由 $\rho_s$ 的封闭性, 我们有

$$
\rho_s x=\rho_sw+\rho_sw^0
$$
每项各自仍在各自的子空间中, 这表明只需要知道 $W$ 和 $W^0$ 上的表示就足以确定 $V$ 上的表示

并且有自然的直和分解

$$
V= W\oplus W^0
$$

这告诉我们在 $W$ 和 $W^0$ 构造的基 $(w,w^0)$ 上, $W\oplus W^0$ 上的矩阵表示有自然的分块对角形式

$$
\begin{pmatrix}R_s&0\\0&R'_s\end{pmatrix}
$$

#### 定义 不可约表示
设 $\rho\colon G\to \mathrm{GL}(V)$ 是 $G$ 的线性表示, 称表示是不可约的或者简单(simple)的, 若对于非空的 $V$ , 除了 $\{0\}$ 和 $V$ 以外, 没有对 $G$ 封闭的子空间. 

根据上面的定理, 实际上在说 $V$ 不可能是两个子表示的直和, 除了 trivial 的分解. 一个 1 维表示显然是不可约的

不可约表示可以从一个表示逐步拆分, 做法是找表示的稳定子空间

#### 定理
任何表示都是不可约表示的直和

证: 做法是对表示的维数归纳, 对 $\dim V=0$ 的情况显然是成立的, 现在考虑 $\dim V\geq 1$ 

若 $V$ 是不可约的, 则已经证完了, 反之按照定义, 存在稳定子空间的直和分解

$$
V=V'\oplus V''
$$

并且 $\dim V',\dim V'' <\dim V$ , 根据归纳假设, 它们是不可约表示的直和, 完成证明

一般来说这样的直和分解不一定是唯一的, 例如对于表示 $\rho_s =\mathrm{Id}$ 可以一直做直和分解做到每个基生成的子空间上去, 但是基的选择不是唯一的. 但是后面会看到不可约子表示的数量不依赖于分解

## 表示的张量积

直和是对表示空间的分解的内在观点, 当然也可以构造更大的表示空间, 但是对于一般的两个空间, 例如在真实的物理问题中涉及的空间, 强行构造直和可能没有直观的理解. 另一种构造更大表示的方式是通过张量积, 也叫 Kronecker 积

#### 定义 张量积
对于线性空间 $V_1,V_2$ , 和线性空间 $W$ , 若配备映射 $(x_1,x_2)\mapsto x_1\cdot x_2$ 从 $V_1\times V_2 \to W$ 
称 $W$ 为 $V_1$ 和 $V_2$ 的张量积, 若满足

1.  $x_1\cdot x_2$ 对两个变量都是线性的
2. 若 $(e_{i_1})$ 是 $V_1$ 的一组基, $(e_{i_2})$ 是 $V_2$ 的一组基, 则 $(e_{i_1}\cdot e_{i_2})$ 是 $W$ 的一组基

这个空间存在, 且至多相差一个同构意义下唯一, 记作 $V_1\otimes V_2$

现在考虑表示 $\rho^1\colon G \to\mathrm{GL}(V_1)$ 和 $\rho^2\colon G\to\mathrm{GL}(V_2)$ , 对任意 $s\in G$ , 可以构造 $\rho_s\in\mathrm{GL}(V_1\otimes V_2)$

$$
\rho_s(x_1\cdot x_2)=\rho^1_s(x_1)\cdot \rho^2_s(x_2)\quad \forall x_1\in V_1,x_2\in V_2
$$

张量积空间的双线性性保证这是一个线性映射

> 一种验证方式是按照张量积的思路, 首先这个映射是 $V_1\times V_2$ 的双线性函数, 限制到张量积上给出唯一的线性映射. 这使用了张量积的泛性质:
> 张量积空间可以被使得 $V_1\times V_2$ 上的双线性函数线性化的空间唯一定义
> 另一种做法是按照上面的关系先定义所有基的像, 然后逐向量地定义其在 $\rho_s$ 下的像, 这样定义一个线性映射 

而表示满足对 $G$ 为同态和 $\rho_s$ 是同构都可以约化到原空间表示上进行 

将其记作

$$
\rho_s =\rho_s^1\otimes \rho_s^2
$$

若选择了各自的基, 则也可以写出张量积表示的矩阵表示

$$
\rho_s(e_{j_1}\cdot e_{j_2})=\sum_{i_1,i_2}r_{i_1j_1}(s)r_{i_2 j_2}(s)\, e_{i_1}\cdot e_{i_2}
$$

> 这看起来就不一定能写成一个简单矩阵了, 但是在张量积空间矩阵表示下这是一个矩阵
> 因为每个基实际携带了两个指标

### 张量积空间的对称与反对称化
考虑 $V_1=V_2=V$ 的情况, 我们有自然的 $V\otimes V$ 上的自同构

$$
\theta(e_i\cdot e_j)=e_j\cdot e_i \quad \forall i,j
$$

这导致 $\theta(x\cdot y)= y\cdot x$ 对 $x,y\in V$ , 并且 $\theta$ 无关基的选取, 合于 $\theta^2 =1$ , 根据 $\theta$ 的特征子空间, $V\otimes V$ 上有自然的直和分解

$$
V\otimes V= \mathbf{Sym}^2 (V)\oplus \mathbf{Alt}^2(V)
$$

其中 $\mathbf{Sym}^2(V)$ 满足任意 $z$ 有 $\theta (z)=z$ , 另一个就是 $\theta(z)=-z$ 
两个空间的一组基为

$$
(e_i\cdot e_j+e_j\cdot e_i)_{i\leq j}\in \mathbf{Sym}^2(V)\quad (e_i\cdot e_j-e_j\cdot e_i)_{i<j}\in \mathbf{Alt}^2(V)
$$
并且维数关系

$$
\dim \mathbf{Sym}^2 (V)=\frac{n(n+1)}{2}\quad \dim \mathbf{Alt}^2(V)=\frac{n(n-1)}{2}
$$

这两个空间在 $G$ 下封闭, 故将其称为表示的对称块与反对称块

以对称块为例子看看为什么封闭, 注意到 

$$
\rho_s \circ \theta=\theta \circ \rho_s
$$

 则任意 $x\in \mathbf{Sym}^2(V)$ , 有

$$
\theta(\rho_s(x))=\rho_s(\theta(x))=\rho_s(x)\implies \rho_s(x)\in\mathbf{Sym}^2(V)
$$

对反对称块是同理的, 即张量积空间的表示天然存在对称化与反对称化的直和分解

# 特征标

## 表示的特征

前面说到, 所关注的并非一个线性空间 $V$ 上的表示, 而是一族 $V$ 的同构类, 故也需要寻找表示得到的线性映射在 $V$ 的同构类上的性质. 即需要找到同构的表示之间的不变量. 对于矩阵表示, 一个熟知的不变量即为迹, 现在来正式定义它

#### 定义 特征
设 $\rho\colon G\to \mathrm{GL}(V)$ 是线性表示, 对任意 $s\in G$ , 定义

$$
\chi_\rho(s)=\mathrm{Trace} (\rho_s)
$$

称为表示的特征 character , 可以想像, 这几乎储存了表示的所有坐标无关的信息

不难验证, 特征有以下简单性质

1. $\chi_\rho(1_G) = n$ , $n$ 是表示的维数
2. $\chi_{\rho}(s^{-1})=\chi_{\rho}(s)^*$ 对任意 $s\in G$ 
3. $\chi_{\rho}(sts^{-1})=\chi_{\rho}(t)$ 对任意 $s,t\in G$ 

> 证明是简单的, 1. 来自于表示将 $1_G$ 打到单位, 2. 来自矩阵表示
> 3. 来自表示是同态

> 当然, 2. 的性质来自于矩阵是酉的, 这源于有限群

对于 3. 的性质, 可以将它抽象出来

#### 定义 类函数
将所有定义在 $G$ 上的函数 $f$ , 合于

$$
f(sts^{-1})=f(t)\quad s,t\in G
$$

的函数称为 类函数 class function

由两表示生成的直和与张量积空间的特征也可以直接得到

#### 命题 直和/张量积 表示的特征
设 $\rho_1 \colon G \to \mathrm{GL}(V_1)$ 和 $\rho_2 \colon G\to \mathrm{GL}(V_2)$ 是 $G$ 上的两个线性表示, $\chi_1,\chi_2$ 是对应的特征, 则

1. $\rho_1 \oplus \rho_2$ 的特征为 $\chi_1 +\chi_2$
2. $\rho_1\otimes \rho_2$ 的特征为 $\chi_1 \cdot \chi_2$

证:
证明是直接的, 对于 1. , 可以知道 $\rho_1\oplus \rho_2$ 的矩阵表示有分块对角形式

$$
\begin{pmatrix}R_s&0\\0&R'_s\end{pmatrix}
$$

则 

$$
\chi(s)=\sum_{i=1,2}\sum_{j} \lambda_{j_i}=\sum_{j_1}\lambda_{j_1}+\sum_{j_2}\lambda_{j_2}=\chi_1(s)+\chi_2 (s)
$$

对于 2. 同样放到矩阵表示上做

$$
\begin{align}\chi(s)=\sum_{i_1,i_2}R_{i_1i_1}(s)R_{i_2i_2}(s)&=(\sum_{i_1}R_{i_1i_1}(s))(\sum_{i_2}R_{i_2i_2}(s))\\&=\chi_1(s)\chi_2(s)\end{align}
$$

对于 $V\otimes V$ 上的表示, 由于有自然的直和分解

$$
V\otimes V=\mathbf{Sym}^2(V)\oplus \mathbf{Alt}^2(V)
$$

故可以写出在每个子空间上的表示, 做法是直接计算迹

例如 $\mathbf{Sym}^2(V)$  (以下记号是标准的)

考虑选择 $V$ 上的对角基 $(e_i)$ 那么

$$
\rho_s^{\otimes 2}(e_i\cdot e_j\pm e_j\cdot e_i)=\lambda_{i}\lambda_j (e_i\cdot e_j\pm e_j\cdot e_i)
$$

在新的张量积空间的基都是张量积表示的本征向量, 那么

$$
\chi_\sigma^{2}(s)=\sum_{i\leq j}\lambda_i\lambda_j=\sum_{i}\lambda_i^2+\sum_{i<j}\lambda_i\lambda_j
$$

做一点计算技巧

$$
2\sum_{i<j}\lambda_i\lambda_j=(\sum_i\lambda_i)^2-\sum_i\lambda_i^2
$$

即

$$
\chi_\sigma^2(s)=\frac{1}{2}(\sum_i\lambda_i^2+(\sum_i\lambda_i)^2)=\frac{1}{2}(\chi(s^2)+\chi(s)^2)
$$

利用直和分解, 可以求出反对称部分的特征

$$
\chi_\alpha^2(s)=\frac{1}{2}(\chi(s)^2-\chi(s^2))
$$

## Schur 引理
特征理论的一个重要结论是 Schur 引理

#### 命题 Schur 引理
设 $\rho^1\colon G\to \mathrm{GL}(V_1)$ 和 $\rho^2 \colon G\to\mathrm{GL}(V_2)$ 是 $G$ 的两个不可约表示, 设 $f\colon V_1\to V_2$ 合于

$$
\rho_s^2\circ f =f\circ \rho_s^1\quad\forall s\in G
$$

则有以下两条性质

1. 若 $\rho^1$ 和 $\rho^2$ 不是同构的, 则 $f=0$
2. 若 $V_1=V_2$ 且 $\rho^1=\rho^2$ , 则 $f$ 是一个 homothety (一个标量乘单位)

证: 
对 1. , 首先 $f=0$ 的情况是 trivial 的, 现在考虑 $f\neq 0$ , 由于两个表示不同构, 则 $f$ 的逆不存在, 现在需要这一点去逼出 $f=0$ , 为此, 考察 $W_1=\ker f$ , 则对任意 $x\in W_1$ , 有 $\rho_s^2(0)=f(\rho_s^1(x))$ 
即 $W_1$ 对表示封闭, 而 $\rho^1$ 是不可约表示, 这表明 $W_1=0$ 或者 $W_1=V_1$ , 后者已经被排除, 则只有 $W_1=0$ , 同样的方法可以说明 $\mathrm{im}\,f=V_2$ , 这表明 $f$ 是同构, 与题设矛盾

对 2. 相同的想法是由于这个性质对任意 $s\in G$ , 都成立, 这说明 $f$ 同构于自身, 或者说 $f$ 与任意 $\rho_s$ 都交换, 这预示着 $f$ 可能是一个标量单位, 但是最后可能的情况是考虑 $f$ 存在特征值的时候, 所以先考虑 $f$ 的任意一个特征值 $\lambda$ , 定义

$$
f'=f-\lambda\cdot\mathrm{Id}
$$

然后考虑 $f'$ 的核, 由于存在特征向量, $\ker f'\neq 0$ , 任取 $x\in \ker f'$ , 由于 $f'$ 仍与 $\rho$ 交换, 那么有

$$
\rho_s(f'(x))=f'(\rho_s(x))=0
$$

同样, 这导致 $\ker f'=V$ , 即 $f'=0$ , 所以 $f=\lambda\cdot\mathrm{Id}$ , 这实际上也证明了只存在一个特征值

> 由于特征值的关系, 实际上这个定理必须在域 $\mathbb{C}$ 上

#### 推论
设 $h$ 是 $V_1$ 到 $V_2$ 的线性映射, 定义

$$
h^0=\frac{1}{|G|}\sum_{t\in G}(\rho_t^2)^{-1}h\rho^1_t
$$

则 $h^0$ 满足 Schur 引理, 且对于第二点, $\lambda =\frac{1}{n}\mathrm{Tr}(h)$
证: 
只需要说明 $h^0$ 满足 Schur 引理的条件, 并求出特征值即可

这是因为

$$
(\rho_s^{2})^{-1}h^0\rho_s^1=\frac{1}{|G|}\sum_{t\in G}(\rho_{ts}^2)^{-1}h\rho^1_{ts}=h^0
$$

后一个等号来自于群的重排性质, 这满足 Schur 引理, 并且

$$
\mathrm{Tr}(h^0)=\frac{1}{|G|}\sum_{t\in G}\mathrm{Tr}(h)=\mathrm{Tr}(h)=n\lambda\implies \lambda =\frac{\mathrm{Tr}(h)}{n}
$$

将其改写为矩阵形式

$$
\rho_t^1=(r_{i_1j_1}(t))\quad \rho_t^2=(r_{i_2j_2}(t))
$$

则根据 $h$ 给出的矩阵, 给出了 $h^0$ 的矩阵表示

$$
(h^0)_{i_2i_1}=\frac{1}{|G|}\sum_{t\in G,j_1,j_2}r_{i_2j_2}(t^{-1})h_{j_2j_1}r_{j_1i_1}(t)
$$

右边对 $h_{j_1j_2}$ 线性, 在 Schur 引理 1. 的条件对任意映射下处处消失, 这表明系数为 0

> $\rho^1,\rho^2$ 不同构是事实, 可以在中间选任意一个映射 $h$ 按照上面的构造得到 Schur 引理

即: 在 Schur 引理 1. 的条件下, 有

$$
\frac{1}{|G|}\sum_{t\in G}r_{i_2j_2}(t^{-1})r_{j_1i_1}(t)=0
$$

对任意 $i_1,i_2,j_1,j_2$ 

在第二种情况, 有 $h^0=\lambda$ , 于是 $h^0_{i_2i_1}=\lambda \delta_{i_2i_1}$ , 则给出

$$
\lambda \delta_{i_1i_2}=\frac{1}{|G|}\sum_{t\in G,j_1,j_2}r_{i_2j_2}(t^{-1})h_{j_2j_1}r_{j_1i_1}(t)
$$

若改写为 $\lambda=\frac{1}{n}\sum\delta_{j_2j_1}h_{j_2j_1}$ 

$$
\frac{1}{|G|}\sum_{t,j_1,j_2}r_{i_2j_2}(t^{-1})h_{j_2j_1}r_{j_1i_1}(t)=\frac{1}{n}\sum_{j_1,j_2}\delta_{i_2i_1}\delta_{j_2,j_1}h_{j_2j_1}
$$

同样, 对任意映射 $h$ 的矩阵元 $h_{j_2,j_1}$ 这给出

$$
\frac{1}{|G|}\sum_{t}r_{i_2j_2}(t^{-1})r_{j_1i_1}(t)=\frac{1}{n}\delta_{i_2i_1}\delta_{j_2j_1}
$$

这两者给出

$$
\frac{1}{|G|}\sum_{t\in G}r_{i_2j_2}(t^{-1})r_{j_1i_1}(t)=\frac{1}{n}\delta_{i_2i_1}\delta_{j_2j_1}=\begin{cases}1/n&\quad \text{if }i_1=i_2\text{ and }j_1=j_2\\0&\quad \text{otherwise}\end{cases}
$$

这里 $r_{i_1j_1}$ 和 $r_{i_2j_2}$ 是两个不可约表示的矩阵表示, 这里省略了表示的记号 !

> [!note] 
> 注意到之前定义在 $G$ 上的函数 $\phi,\psi$ 的内积
>
>
> $$
\braket{\phi,\psi}=\frac{1}{|G|}\sum_{t\in G}\phi(t^{-1})\psi(t)=\frac{1}{|G|}\sum_{t\in G}\phi(t)\psi(t^{-1})
> $$
>
> 有 $\braket{\psi,\phi}=\braket{\phi,\psi}$ 并且这对两个位置都是线性的

上面的结果可以写为

$$
\langle r_{i_2j_2},r_{j_1i_1}\rangle=0\quad\mathrm{and}\quad\langle r_{i_2j_2},r_{j_1i_1}\rangle=\frac{1}{n}\delta_{i_2i_1}\delta_{j_2j_1}
$$

如果选择一组基, 使得 $r$ 是 unitary 的, 则上式即给出了一种正交归一性

## 特征的正交关系

首先约定一些记号, 若 $\phi,\psi$ 是 $G$ 上的复值函数, 则

$$
(\phi|\psi)=\frac{1}{|G|}\sum_{t\in G}\phi(t)\psi(t)^*
$$

> [!note]
> 这里 serre 写的内积是对左侧线性, 和一般 dirac 符号的约定不一样
> 但是我懒得改了


满足对 $\phi$ 线性, 对 $\psi$  semilinear , 并且正定

若 $\tilde{\psi}$ 满足关系 $\tilde{\psi}(t)=\psi(t^{-1})^*$ 则有

$$
(\phi|\psi)=\braket{\phi,\tilde{\psi}}
$$

特别地, 若 $\chi$ 是特征, 则 $\chi =\tilde{\chi}$ , 则对特征来说上面两种记号没有区别

#### 定理
1. 若 $\chi$ 是不可约表示的特征, 有 $(\chi|\chi)=1$ 
2. 若 $\chi$ 和 $\chi'$ 是不同构的两个不可约表示的特征, 则 $(\chi|\chi')=0$ 

证: 
考虑表示 $\rho$ , 及其特征 $\chi$ , 若 $\rho$ 的矩阵表示为 $(r_{ij}(t))$ 则

$$
(\chi|\chi)=\braket{\chi,\chi}=\sum_{ij}\braket{r_{ii},r_{jj}}
$$

按照 Schur lemma 的结果 

$$
\braket{r_{ii},r_{jj}}=\frac{1}{n}\delta_{ij}\implies(\chi|\chi)=\frac{1}{n}\sum_{ij}\delta_{ij}=1
$$

对于 2. , 同样可以由 Schur lemma 得到 (这同样利用了两个不同构的不可约表示的矩阵元关系 ,当然不是下面这个)

$$
\frac{1}{|G|}\sum_{t\in G}r_{i_2j_2}(t^{-1})r_{j_1i_1}(t)=\frac{1}{n}\delta_{i_2i_1}\delta_{j_2j_1}=\begin{cases}1/n&\quad \text{if }i_1=i_2\text{ and }j_1=j_2\\0&\quad \text{otherwise}\end{cases}
$$

当然, 上面都是对同一个群 $G$ 的表示而言的

#### 定理
设 $V$ 是 $G$ 的线性表示, 特征 $\phi$ , 考虑 $V$ 有不可约表示的直和分解

$$
V=W_1\oplus \cdots\oplus W_k
$$

则, 若 $W$ 是特征 $\chi$ 的不可约表示, 同构于 $W$ 的 $W_i$ 的数量为特征的标量积 $(\phi|\chi)=\braket{\phi,\chi}$

证: 这几乎是上面定理的直接结果, 考虑 $V$ 的特征的直和分解

$$
\phi =\chi_1+\cdots+\chi_k
$$

用 $\chi$ 做内积, 与 $W$ 同构的特征得到 1 , 不同构的得到 0 , 即

$$
(\phi|\chi)=\sum_{W_i \text{同构于} W}(\chi_i|\chi)=\sum_{W_i\text{同构于}W}1
$$


##### 推论
同构于 $W$ 的数量 $W_i$ 不依赖于具体的分解

这实际上是来自于 $(\phi|\chi)$ 不依赖于具体的分解

##### 推论
两个具有相同特征的表示是同构的

> 记住特征相同的意思是: 定义在一个群 $G$ 上的函数相同, 而不是一个数、
> 同时该命题的意思是: 如果有一个群 $G$ , 它的两个表示如果具有相同的特征, 则它们是同构的

证明的方式是把表示分解为不可约表示, 然后逐分量比较

上面的讨论中的精神是: 总是将一个表示分解为不可约表示的直和

$$
V=m_1W_1\oplus \cdots\oplus m_hW_h\quad m_i\in \mathbb{Z}_{\geq 0}
$$

> 特别地, 张量积可以用相同的符号计算, 例如 $W_i\otimes W_j$ 这两个不可约表示的张量积的特征也可以进行分解
>
>
> $$
\chi_i\cdot\chi_j=\sum_km_{ij}^k \chi_k
> $$

正交归一性给出

$$
(\phi|\phi)=\sum_{i=1}^{h}m_i^2
$$

这立即导致下面的结果

#### 定理
若 $\phi$ 是表示 $V$ 的特征, 则 $(\phi|\phi)$ 是正整数, 且满足 $(\phi|\phi)=1$ 当且仅当 $V$ 是不可约的

证明是显然的

借助 Schur lemma 给出的正交归一性, 我们可以给出一个表示的不同分解方式

## 表示的分解

### 正则表示的分解

继承前面的记号, 用 $\chi_1,\cdots,\chi_h$ 表示 $G$ 的所有不可约特征, 用 $n_1,\cdots ,n_h$ 标记表示的维度, 注意 $n_i=\chi_i(1)$

并记 $R$ 为 $G$ 的正则表示, 注意到正则表示上自然诱导出一组基 $(e_t)_{t\in G}$ 即 $\rho_se_t =e_{st}$ 
若 $s\neq 1$ , 则有 $st\neq t$ 对任意 $t$ : 这表明在该基上, $\rho_s$ 的矩阵表示的对角项是 0, 特别地, 我们有

$$
\mathrm{Tr}(\rho_s)=0
$$

> 注意这里还没有内积, 由于正则表示实际上都是置换, 那么
>
>
> $$
\rho_s(e_t)=e_{st}\neq e_t
> $$
>
> 即不存在对角项

而对于 $s=1$ , 有

$$
\mathrm{Tr}(\rho_s)=\mathrm{Tr}(1)=\dim R=|G|
$$

#### 命题
正则表示的特征 $r_G$ 由下式给出

$$
\begin{aligned}&r_{\mathbf{G}}(1)=g,&&\text{order of G,}\\&r_{\mathbf{G}}(s)=0&&if\,s\neq1.\end{aligned}
$$

##### 推论
任何不可约表示 $W_i$ 都包含在正则表示中, 并且容易给出它的数量 $n_i$

$$
\braket{r_G,\chi_i}=\frac{1}{|G|}\sum_{s\in G}r_G(s^{-1})\chi_i(s)=\chi_i(1)=n_i
$$

##### 推论
继续上面的结果

*  $n_i$ 满足关系 $\sum_{i=1}^h n_i^2=|G|$
* 若 $s\in G$ 且 $s\neq 1$ , 则有 $\sum_{i=1}^h n_i \chi_i(s)=0$

证:
这几乎是上面的结果, 只需要对正则表示取不可约分解即可

为了计算不可约表示的分解, 我们先考察不可约表示的数量

### 不可约表示的数量

#### 命题
设 $f$ 是 $G$ 上的一个类函数, 且 $\rho \colon G\to \mathrm{GL}(V)$ 是一个线性表示, 取 $\rho_f$ 是一个 $V$ 上的线性映射, 定义为

$$
\rho_f =\sum_{t\in G} f(t)\rho_t
$$

若 $V$ 是一个维数为 $n$ , 特征为 $\chi$ 的不可约表示, 则 $\rho_f$ 是一个单位, 且系数为

$$
\lambda =\frac{1}{n}\sum_{t\in G} f(t)\chi(t)=\frac{g}{n}(f|\chi^*)
$$

这是 Schur lemma 的一个推论, 只需要计算

$$
\rho_s^{-1}\rho_f\rho_s=\sum_{t\in G}f(t)\rho_s^{-1}\rho_t \rho_s=\sum_{t\in G}f(s^{-1}ts)\rho_{s^{-1}ts}=\rho_f
$$

故满足 Schur lemma 的结果, 表明 $\rho_f$ 是一个单位, 取 trace 得到

$$
n\lambda =\sum_{t\in G} f(t)\chi(t)=g (f|\chi^*)
$$

引入 $G$ 上的类函数的空间 $H$ , 则不可约特征都是 $H$ 中的元素

#### 定理
不可约表示的特征 $\chi_1,\cdots ,\chi_h$ 构成 $H$ 的正交基

证: 之前已经证明了不同构的不可约表示的特征之间是正交的, 现在只需要证明这套正交系统生成 $H$ , 那么只需要证明: $H$ 中任意正交于 $\chi_i^*$ 的元素都是 0.

考虑 $f\in H$ , 对于表示 $\rho$ 定义 

$$
\rho_f =\sum_{t\in G} f(t)\rho_t
$$

按照上面的定义, $f$ 正交于所有 $\chi_i^*$ , 而若 $\rho$ 是不可约表示,  则由上面的结果, $\rho_f=0$ 因为系数都是 0.
从而得出 $\rho_f$ 总是 0 , 那么考虑正则表示 $R$ , 计算 $\rho_f$ 在基向量上的像

$$
\rho_f e_1 =\sum_{t\in G}f(t)\rho_t e_1=\sum_{t\in G}f(t)e_t =0
$$

这就表明对所有 $t\in G$ 都有 $f(t)=0$ 完成证明

当然我们也可以从另一个角度证明: $\rho_f$ 满足 Schur 引理的要求, 若取 $\rho$ 是一个不可约表示的话
则

$$
n\lambda = \sum_{t\in G}f(t)\chi(t)=g(f|\chi^*)
$$

后续证明相同

同样, 回忆起对于一个群 $G$  , 可以按共轭关系对群做等价类的分解, 我们有如下结果

#### 定理
群 $G$ 的不可约表示数量等于 $G$ 的共轭类的数量
证: 考虑群 $G$ 的共轭类 $C_1,\cdots,C_k$ , 称一个函数 $f$ 是类函数, 当且仅当它在共轭类上为常数, 则它被每个共轭类上的值, 共 $k$ 个值决定. 这表明 $H$ 的维数是 $k$ , 另一方面, 该维数也等于 $G$ 的不可约表示的数量

#### 命题
让 $s\in G$ , 且 $c(s)$ 为 $s$ 所在共轭类的元素的数量, 则

* 我们有 $\sum_{i=1}^h\chi_i^*(s)\chi_i(s) = g/c(s)$
* 对 $t\in G$ 与 $s$ 不共轭, 有 $\sum_{i=1}^h \chi_{i}^*(s)\chi_i(t)=0$

证: 考虑 $s$ 所在共轭类上的示性函数, 并且按照不可约表示分解

$$
f_s =\sum_{i=1}^h \lambda_i\chi_i\quad \lambda_i =(f_s|\chi_i)=\frac{c(s)}{g}\chi_i^*(s)
$$

则有对 $t\in G$

$$
f_s(t)=\frac{c(s)}{g}\sum_{i=1}^h \chi_i^*(s)\chi_i(t)
$$

这给出命题的结果

##### 例子
考虑 $G$ 是三个元素的置换群, 有 $g=3! =6$  , 按照类函数 $H$ 的想法, 我们需要先找出一些类函数, 首先给出 $G$ 共轭类划分与其代表元: 单位 $e$, 三个对换 $t$, 两个轮换 $c$ , 我们有 $t^2=1,c^3 =1,tc =c^2t$ 
我们知道这里存在两个一维特征: 单位 $\chi_1$ 和置换的符号 $\chi_2$ , 从而表明还存在另一个特征 $\theta$ 
首先有维数关系 $1^2+1^2+n^2=6 \implies n=2$ , 还有一个二维表示的特征, 实际上根据正则表示的特征

$$
r_G =\chi_1+\chi_2+2\theta
$$

可以确定特征在每个共轭类上的值, 首先 $\theta(1)=2$ , 再代入 $t$ , 有

$$
1-1+2\theta(t)=0\implies \theta(t)=0
$$

同样

$$
1+1+2\theta(c)=0\implies \theta(c)=-1
$$

这给出了特征的完整刻画

### 表示的正则分解
现在考虑构造一个比不可约分解更稀疏的直和分解, 并且我们要求这种分解是唯一的

考虑 $G$ 的不可约表示 $W_1,\cdots,W_h$ 有特征 $\chi_1,\cdots,\chi_h$ , 维数 $n_1,\cdots,n_h$ . 若考虑

$$
V=U_1\oplus\cdots\oplus U_m
$$

是 $V$ 的一个直和分解, 若用 $V_i$ 表示前者的一些直和, 它由那些同构的 $W_i$ 直和得到则有

$$
V=V_1\oplus \cdots\oplus V_h
$$

这几乎就是正则分解

#### 定理
分解 $V=V_1\oplus \cdots \oplus V_h$ 不依赖于最初选择的 $V$ 的不可约表示分解
且投影 $p_i \colon V\to V_i$ 在该分解下由下式给出 (注意 $\chi_i$ 的定义来自前面)

$$
p_i =\frac{n_i}{g}\sum_{t\in G}\chi_i^*(t)\rho_t
$$

证: 先证第二条, 可以用该公式来定义 $V_i$ , 考虑映射

$$
q_i =\frac{n_i}{g}\sum_{t\in G}\chi_i^*(t)\rho_t
$$

由于特征是一个 类函数, 可以使用上面的结果, 这表明 $p_i$ 限制在一个特征为 $\chi$ 维度为 $n$ 的不可约表示 $W$ 上的限制是一个单位(将 $\rho$ 限制在它的不可约子表示上是不可约的), 并且系数为 

$$
\frac{n_i}{n}(\chi_i|\chi)=\begin{cases}1 \quad \chi_i=\chi\\ 0\quad \chi_i\neq \chi\end{cases}
$$

即 $q_i$ 是某个同构于 $W_i$ 不可约表示上的单位, 并且在其他地方取 0 . 于是可用该像来定义 $V_i$
如果对 $x\in V$ 做分解

$$
x=x_1+\cdots+x_h
$$

于是有

$$
q_i(x)=q_i(x_1+\cdots+x_h)=x_i
$$

故这是一个投影

现在对 $V$ 的分解方式有更多了, 第一种分解方式是正则分解

$$
V=V_1\oplus \cdots\oplus V_h
$$

算法只需要用前文定义的投影 $p_i$ 来构造出 $V_i$ (这需要先找出不可约特征标)
如果有必要的话, 就可以对每个 $V_i$ 做不可约表示的分解, 则至多同构于 $W_i$ 的意义下有如下结果

$$
V_i=W_i\oplus\cdots\oplus W_i
$$

后面这一步的分解就不是唯一的了

##### 例子
考虑群 $G=\{1,s\}$ , 这个群有两个不可约的一维表示 $W^+,W^-$ 合于 $\rho_s=+1,\rho_s=-1$ 
故正则分解为

$$
V=V^+\oplus V^-
$$

则两个投影显式构造为

$$
p^+ x=\frac{1}{2}(x+\rho_s x)\quad p^- x =\frac{1}{2}(x-\rho_s x)
$$

### 表示的显式分解
继续保持上一节的记号, 上一节我们显式构造出来了一个正则分解, 现在我们可以引入一个方法, 它能显式构造 $V_i$ 至多相差一个同构的不可约表示分解 $W_i$ 
在标准基 $(e_1,\cdots,e_n)$ 下记 $W_i$ 为 $(r_{\alpha\beta}(s))$ , 同时有 $\chi_i =\sum_{\alpha}r_{\alpha\alpha}(s)$ 和 $n=n_i=\dim W_i$ 

对每个 $\alpha,\beta$ 对, 可以定义投影 (这实际上是比使用特征更精细的投影)

$$
p_{\alpha\beta}=\frac{n}{g}\sum_{t\in G}r_{\beta\alpha}(t^{-1})\rho_t
$$

则我们有如下结果

#### 定理
(a) 映射 $p_{\alpha\alpha}$ 是一个投影, 且在 $V_j,j\neq i$ 上为 0 , 它的像 $V_{i,\alpha}\subset V_i$ , 且 $V_i$ 是  $V_{i,\alpha},\alpha=1,\cdots, n$ 的直和
我们有

$$
p_i=\sum_{\alpha}p_{\alpha\alpha}
$$

(b) 线性映射 $p_{\alpha\beta}$ 在 $V_j,j\neq i$ 上为 0 , 同样在 $V_{i,\gamma},\gamma\neq \beta$ 上也为 0 . 这是一个 $V_{i,\beta}$ 到 $V_{i,\alpha}$ 的同构

(c) 让 $x_1$ 是 $V_{i,1}$ 的非零元, 且 $x_{\alpha}=p_{\alpha 1}(x_1)\in V_{i,\alpha}$ , 则 $x_{\alpha}$ 是线性无关的且张成一个子空间 $W(x_1)$ 在 $G$ 下稳定且维数为 $n$ , 对每个 $s\in G$ , 有

$$
\rho_s(x_{\alpha})=\sum_{\beta}r_{\beta\alpha}(s)x_{\beta}
$$

(d) 若 $(x_1^{(1)},\cdots,x_1^{(m)})$ 是 $V_{i,1}$ 的一组基, 则表示 $V_i$ 是上面子表示 $W(x_1^{(1)}),\cdots, W(x_1^{(m)})$ 的直和

证: 
首先将该算子作用在 $W_i$ 上, 我们有

$$
\frac{n}{g}\sum_{t\in G}r_{\beta\alpha}(t^{-1})\rho_t(e_\gamma)=\frac{n}{g}\sum_{\delta}\sum_{t\in G}r_{\beta\alpha}(t^{-1})r_{\delta\gamma}(t)e_{\delta}
$$

后一个等号来自不可约表示的矩阵表示
按照前面的结果, 里面是一个双 delta, 再求和求掉一个

$$
p_{\alpha\beta}(e_\gamma)=\begin{cases}e_{\alpha}\quad \beta=\gamma \\0\quad \beta\neq \gamma\end{cases}
$$

可以看到这将 $W_i$ 的基中选择 $e_\beta$ 的部分, 并将其打到 $e_\alpha$ 上
同样, 作用在 $W_j,j\neq i$ 上会直接给出 0 (按照 Schur lemma 给出的不可约表示矩阵元的正交关系)
由于 $V$ 有不可约表示分解, 可以看到投影算子会保留 $W_i$ 的一些成分, 完全去掉 $W_j$ 中的成分

在之前我们使用了 $V_i$ 为一系列不可约表示的同构类的直和, 在这里我们将其理解为一系列投影算符的像的直和, 我们需要证明这两者一致

按照定义

$$
V_{i,\alpha}=\mathrm{Im} p_{\alpha\alpha}
$$

(注意 label $i$ 出现是因为我们使用了 $W_i$ 的表示矩阵构造投影) 
按照上面的计算, 实际上 $p_{\alpha\alpha}$ 保持了 $W_i$ 上的基 $e_\alpha$ 和打到 $W_i$ 的同构类上的对应的基, 把这些所有的基收集起来, 就得到整个 $V_i$ , 即

$$
V_i=\bigoplus_{\alpha} V_{i,\alpha}
$$

对应的就有完整的投影, 当然这实际上就是上面正则分解的投影方式

$$
p_i=\sum_{\alpha}p_{\alpha\alpha}
$$

如果已经理清了 $V_i$ 的结构, 所以投影 $p_{\alpha\beta}$ 在 $V_j$ 上都是 0 , 同时按照数基的方式, 这是一个同构

$$
p_{\alpha\beta}\colon V_{i,\beta}\to V_{i,\alpha}
$$

所做的只不过是将基的 label 从 $\beta$  切换到 $\alpha$

进一步, 若非零元 $x_1\in V_{i,1}$ (它是所有 $W_i$ 的同构类的 $1$ 方向坐标子空间的直和) , 按上面的同构, 将其打到 $V_{i,\alpha}$ 上

$$
x_{\alpha}=p_{\alpha1}(x_1)
$$

则 $x_{\alpha}$ 是线性无关的, 只需要先回到直和分解再回到各自子表示的基上就可证明
同样, 这也表明张成的子空间在 $G$ 下封闭 (实际上想象一下就是同时转动指标 $\alpha$, 不同组分之间只相差一些同构带来的冗余, 不影响这个转动) 

$$
\rho_s(x_\alpha)=\rho_s \frac{n}{g}\sum_{t\in G}r_{1\alpha}(t^{-1})\rho_t(x_1)=\frac{n}{g}\sum_{st\in G}r_{1\alpha}((st)^{-1}s)\rho_{st}(x_1)=\frac{n}{g}\sum_{t\in G}\sum_{\beta}r_{1\beta}(t^{-1})r_{\beta\alpha}(s)\rho_t(x_1)=\sum_{\beta}r_{\beta\alpha}(s) x_\beta
$$

(d) 的结果就是我们前面叙述的, 当然我们只需要说明 $W(x_1^{(1)})$ 等是子表示, 这直接来自于 c 的结果

## 本章主线

这一章的核心问题可以理解为: 给定有限群 $G$ 的表示 $V$ , 如何把 $V$ 分解成不可约表示. 前面的 Schur 引理、特征标、正则表示和投影算子都是围绕这个问题展开的.

这件事大致分成三层. 第一层是存在性: 通过平均化证明子表示存在 $G$-稳定补空间, 从而任意表示都可以拆成不可约表示的直和. 第二层是计数: 具体的不可约分解不唯一, 但每种不可约表示出现的次数唯一. Schur 引理说明不可约表示之间的 $G$-等变映射非常刚性, 不同构时为零, 同构时为标量, 由此推出矩阵元正交关系和不可约特征标正交关系. 若

$$
V\cong m_1W_1\oplus\cdots\oplus m_hW_h
$$

则重数由

$$
m_i=(\chi_V|\chi_i)
$$

给出.

第三层是构造: 特征标不仅可以计算重数, 还可以构造投影算子. Serre 所说的正则分解是

$$
V=V_1\oplus\cdots\oplus V_h
$$

其中 $V_i$ 是所有同构于不可约表示 $W_i$ 的部分合在一起. 这个分解唯一, 但 $V_i$ 内部继续拆成若干个 $W_i$ 副本的方式不唯一. 对应投影为

$$
p_i=\frac{n_i}{g}\sum_{t\in G}\chi_i^*(t)\rho_t
$$

这里 $\chi_i^*(t)$ 只是复数 $\chi_i(t)$ 的共轭, 不是新定义的函数记号.

正则表示 $R$ 不是任意表示 $V$ , 也不是给 $V$ 选一组基. 它是特殊表示 $\mathbb{C}[G]$ , 满足

$$
\rho_s(e_t)=e_{st}
$$

它的作用是作为研究所有不可约表示的全局工具. 它分解为

$$
R\cong n_1W_1\oplus\cdots\oplus n_hW_h
$$

其中 $n_i=\dim W_i$ , 由此得到

$$
\sum_i n_i^2=|G|
$$

正则表示还帮助证明不可约特征标构成类函数空间的正交基, 从而不可约表示个数等于共轭类个数. 类函数在这里有两个角色: 一方面特征标本身是类函数, 因为 $\chi(sts^{-1})=\chi(t)$ ; 另一方面不可约特征标构成整个类函数空间的一组正交基, 因此可以作为类函数空间的坐标系.

最后, 若要把 $V_i$ 继续显式拆出具体的 $W_i$ 副本, 需要使用更精细的矩阵元投影

$$
p_{\alpha\beta}=\frac{n_i}{g}\sum_{t\in G}r_{\beta\alpha}(t^{-1})\rho_t
$$

并且

$$
p_i=\sum_\alpha p_{\alpha\alpha}
$$

直观上, $p_i$ 是按不可约类型投影, 抓出整个 $W_i$-等型分量; 而 $p_{\alpha\beta}$ 是按不可约表示内部的坐标方向投影, 用来进一步显式拆出具体的 $W_i$ 副本.

因此本章的总地图是

![[attachments/tikz/group-theory-ch2-representation-decomposition-map.png]]

$$
\text{完全可约}
\to
\text{Schur 引理}
\to
\text{矩阵元正交}
\to
\text{特征标正交}
\to
\text{重数公式}
\to
\text{正则表示}
\to
\text{类函数空间}
\to
\text{正则分解投影}
\to
\text{显式分解投影}.
$$

更口语地说, 先证明表示能拆; 再用 Schur 引理说明不可约块之间互不干扰; 再用特征标计算每种块出现几次; 最后用投影算子把对应的块真正构造出来.
