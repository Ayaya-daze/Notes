# 群

## 群的基本知识
##### 定义 群
$G$ 是一个集合, 在 $G$ 中定义了乘法 $\times \colon G\times G\to G$ , 若乘法满足下面的条件
1. 封闭性: 任意 $f,g\in G$ , 有 $f g\in G$ 
2. 结合律: 任意 $f,g,h\in G$ , 有 $(fg)h=f(gh)$ 
3. 单位元: 存在 $e\in G$ , 使得任意 $f\in G$ , 有 $ef=fe=f$ 
4. 逆元: 任意 $f\in G$ , 存在 $g\in G$ , 使得 $fg=gf=e$ 
则称 $(G,\times)$ 为一个群

>[!notes]
>可以验证, 在上述定义下, 群的幺元与逆元唯一

最简单的群只有一个元素, 即幺元, 称为平凡群

##### 定义 群的阶数
称群 $G$ 作为集合的基数 $|G|$ 为群的阶数

##### 定义 子群
若 $G$ 为群, 而 $H$ 为 $G$ 的子集, 若满足下述条件
1. $1_G\in H$
2. 对乘法封闭
3. 对逆封闭
则称 $H$ 为 $G$ 的子群, 即 $(H,\times)$ 也为群

>[!notes]
>实际上, 子群的条件可以合并为一条: 
>$$\forall h_1,h_2,\quad h_1 h_2^{-1}\in H$$



$G$ 有自然的子群 $G$ 和 $\{1\}$ , 称后者为平凡子群, 对于 $H\subsetneq G$ 的子群为真子群

##### 定义 群的中心
对任意群 $G$ , 定义
$$Z_G:=\{z\in G:\forall g\in G,zg=gz\}$$
即和 $G$ 的任意元素都交换的元素, 这是一个子群

##### 定义 半群与幺半群
继续拆解群的定义, 若只保留结合律, 则为半群, 若保留结合律, 幺元存在的性质, 则有幺半群

>[!example]
>下面有一些典型的群

##### 定义 群的生成
若 $G$ 为群, $S$ 为 $G$ 的子集, 则定义 $\braket{S}$ 为所有形如 $s_1^{a_1}\cdots s_m^{a_m}$ 的元素构成的子集, 其中 $m\in \mathbb{Z}_{\geq 0},s_i\in S$ 而 $a_i\in\mathbb{Z}$ , 这构成一个群, 且为 $G$ 的子群 , 称为 $S$ 生成的子群
从定义上, $\braket{S}$ 是包含 $S$ 的最小子群, 若 $G=\braket{S}$ , 则称 $S$ 生成 $G$ 或 $S$ 是 $G$ 的一族生成元
若 $G$ 能被有限子集生成, 则称为有限生成的

##### 定义 - 命题 群的直积
设 $(G_i)_{i\in I}$ , 其中 $I$ 为非空集, 则在集合的积 $\prod_{i\in I}G_i$ 上定义乘法
$$(x_i)_{i\in I}\cdot(y_i)_{i\in I}\coloneqq (x_iy_i)_{i\in I}$$
即元素逐分量相乘, 则 $\prod_{i\in I}G_i$ 构成群, 幺元为 $(1_{G_i})_{i \in I}$ , 逆元为 ${(x_i)_{i\in I}}^{-1}=({x_i}^{-1})_{i\in I}$
若所有 $G$ 都为同一个群的情形, 积记为 $G^I$

>[!notes]
>群结构的验证:
>对于结合律只需要逐分量验证:
>$$((x_i)_{i\in I}\cdot (y_i)_{i\in I})\cdot (z_i)_{i\in I}=(x_i y_i)_{i\in I}\cdot (z_i)_{i\in I}=(x_i y_i z_i)_{i\in I}=\cdots=(x_i)_{i\in I}\cdot ((y_i)_{i\in I}\cdot (z_i)_{i\in I})$$


## 同态与同构
在群上也可构造对应的态射

##### 定义 群同态
设 $f\colon G\to G'$ 为群之间的映射, 若 $f$ 与乘法相容, 即下述条件, 则称 $f$ 为群同态
$$f(xy)=f(x)f(y)\quad x,y\in G$$

>[!notes]
>该定义与环同态类似, 但更有一些简化的地方
>如未要求 $f$ 保持幺元, 实际上这是自动的
>对于半群和幺半群, 也有对应的同态

##### 定义 群同构
设 $f\colon G\to G'$ 为群同态, 若存在群同态 $g\colon G'\to G$ 合于 $gf=\mathrm{id}_G$ 和 $fg=\mathrm{id}_{G'}$ , 则称 $f$ 为群同构, $g$ 为 $f$ 的逆

##### 命题 
设 $f\colon G\to G'$ 为群同态, 同时 $f$ 还是作为集合的双射, 则 $f$ 是群同构

证: 所做之事不过验证 $f$ 由集合映射定义的逆也是群同态
即需考察 
$$f\left(f^{-1}(f(g)f(h))\right)=f(g)f(h)=f(gh)$$
这说明 ( $f$ 是集合意义上的同构)
$$f^{-1}(f(g)f(h))=gh=f^{-1}(f(g))f^{-1}(f(h))$$
即 $f^{-1}$ 是同态

## 循环群

##### 定义 循环群
由单个元素生成的群称为循环群

##### 命题
设 $G$ 为循环群, 由元素 $\sigma$ 生成
* 若 $G$ 无穷, 则有同构 $\mathbb{Z}\overset{\sim}{\operatorname*{\rightarrow}}G$ , 映 $k$ 为 $\sigma^k$ 
* 若 $G$ 有限, 记 $n=|G|$ , 则有同构 $\mathbb{Z}/n\mathbb{Z}\overset{\sim}{\to} G$ , 映 $k+n\mathbb{Z}\to\sigma^k$ 
且在有限的情形, $|G|=\min\{k\in\mathbb{Z}_{\geq 1}\colon \sigma^k =1\}$ 

证:
我们总有满射 $\mathbb{Z}\to G$ 映 $k$ 为 $\sigma^k$ , 现在讨论单射性质
若这个映射是单的, 则为群同构, 此时 $G$ 无穷, 否则这个映射不是单的
若 $G$ 是有限集, 即存在 $l\in \mathbb{Z}_{\geq 1}$ 合于 $\sigma_l=1$ , 那么取 $n =\min\{k\in \mathbb{Z}_{\geq 1}:\sigma^k=1\}$ . 满射仍然满足, 现在证单性:
若 $n> k\geq l>0$ 且 $\sigma^k=\sigma^l$ , 这表明 $\sigma^{k-l}=1$ , 由上文, $k-l=0$ 表明单性, 于是我们有同构 $\mathbb{Z}/n\mathbb{Z}\overset{\sim}{\to} G$ 
同样验证同态: 
$$(k+ n\mathbb{Z})+(l+n\mathbb{Z})=(l+k)+n\mathbb{Z}\to \sigma^k\cdot\sigma^l=\sigma^{k+l}$$
这确实是同态, 于是给出群同构

>[!notes] 
>这个命题表明了循环群的结构, 同样可以预见这与数论有很多联系

##### 命题 
设 $n$ 为非零整数, 则同余类 $a+n\mathbb{Z}$ 生成加法群 $\mathbb{Z}/n\mathbb{Z}$ 当前仅当 $a$ 和 $n$ 互素

证:
由于加法群 $\mathbb{Z}/n\mathbb{Z}$ 由同余类 $1+n\mathbb{Z}$ 生成, 故 $a+n\mathbb{Z}$ 也生成 $\mathbb{Z}/n\mathbb{Z}$ 表明 $1+n\mathbb{Z}\in \braket{a+n\mathbb{Z}}$ . 即存在 $k\in \mathbb{Z}$ 合于 $1=ka\quad \mathrm{mod} n$ , 该方程有解的充要条件是 $\mathrm{gcd}(a,n)=1$

##### 推论
设 $G$ 是有限循环群, $n\coloneqq |G|$ , 则 $G$ 的生成元个数为 $\varphi(n)$ 

## 陪集分解

考虑群 $G$ 和子群 $H$ , 对 $x,y\in G$ , 在这之上可以定义一种关系:
* 若存在 $h\in H$ 合于 $x=hy$ , 则 $x\sim_{\text{左}} y$ 
* 若存在 $h\in H$ 合于 $x=yh$ , 则 $x\sim_{\text{右}} y$

上述定义关系实际为等价关系

##### 引理 
上面定义的两个关系为 $G$ 上的等价关系

证:
简单验证即可
* 自反性: $1\in H$ , 则 $x=1x$ 即 $x\sim x$ 
* 对称性: $h\in H$ , 则 $x=hy\implies y=h^{-1}x$ 子群性质保证 $y\sim x$
* 传递性: $g,h\in H$ 合于 $x=gy,y=hz$ , 那么 $x=g(hz)=(gh)z$ 即 $x\sim z$ 
可以看到, 等价关系来自于子群性质

而任何等价关系将集合划分为等价类, 于是对所有 $g\in G$ , 有如下 $G$ 的子集
$$Hg:=\{hg:h\in H\},\quad gH:=\{gh:h\in H\}$$

这两个等价类有特殊的名字

##### 定义 左/右陪集
设 $H$ 为群 $G$ 的子群, 则右陪集是形如 $Hg$ 的子集, 左陪集是形如 $gH$ 的子集, 其中 $g\in G$

>[!notes]
>验证陪集为上面等价关系得到的等价类
>同样, 只验证左乘版本, 右乘版本是相同的
>等价关系给出的等价类: 由于 $g1=g\in gH$ , 故选取 $g$ 为代表元的话, 等价类为 $C_g$
>任意 $y\sim g$ 满足: 存在 $h\in H$ 合于 $gh=y$ , 这表明 $C_g \subset gH$ 
>同样的理由, 任何 $y\in gH$ , 满足 $h\in H,\quad y=gh\implies y\sim g$ , 即 $gH\subset C_g$
>恰好表明两者相同

由于陪集实则为等价关系定义出的等价类, 具有等价类的性质, 即任意两个等价类之间无交或相同, $G$ 能分解为陪集的无交并
这些等价关系给出的商集也有对应的符号

##### 定义
设 $H$ 为群 $G$ 的子群, 记
$$H\backslash G:=\left\{\text{右陪集 }Hg:g\in G\right\},\quad G/H:=\left\{\text{左陪集 }gH:g\in G\right\}$$

若对任意子集 $A\subset G$ , 记 $A^{-1}\coloneqq \{a^{-1}\colon a\in A\}\subset G$

##### 引理
设 $g\in G$ , 则有 $(Hg)^{-1}=g^{-1}H$

证:
任意 $a\in Hg$ , 即存在 $h\in H$ 合于 $a=hg$ , 则 $a^{-1}=g^{-1} h^{-1}\implies (Hg)^{-1}\subset g^{-1}H$ 
同样的理由 $a=g^{-1}h\implies a^{-1}=h^{-1}g\implies a=(h^{-1}g)^{-1}\in (Hg)^{-1}\implies g^{-1}H\subset (Hg)^{-1}$ 

##### 定义 - 命题 子群的指数
设 $H$ 为群 $G$ 的子群, 映射 $Hg\mapsto(Hg)^{-1}$ 给出从 $H\backslash G$ 到 $G/H$  的双射, 因此两者作为集合有相同的基数, 记为 $(G:H)$ , 称为 $H$ 在 $G$ 中的指数

证:
只需要验证这是一个双射, 首先验证良定义: 像与代表元的选取无关
由前者引理 $(Hg)^{-1}=g^{-1}H$ 于是这是一个右陪集到左陪集到映射, 设 $g\in Hg'$ 即 $g=h'g'$,那么 
$$x\in g^{-1}H\implies x=g^{-1}h=(h'g')^{-1}h=g'^{-1}h'^{-1}h\implies x\in g'^{-1}H$$
反之亦然, 表明 $Hg$ 和 $Hg'$ 被打到同一左陪集, 故映射是良定义的, 并且由陪集的性质
而 $g^{-1}\in G$ , 故这是满射, 同时, 若 $g^{-1}H=g'^{-1}H$ , 这表明 $g^{-1}=g'^{-1}h\implies g=h^{-1}g'\implies Hg=Hg'$ 故这是单的

##### 定理 (J.- L. Lagrange)
若 $H$ 是群 $G$ 的子群, 则有
$$|H| \cdot (G:H)=|G|$$
对于无穷群, 则理解为集合的基数

证: 
要点在于要给出双射
$$H\times (H\backslash G) \overset{1:1}{\to} G$$ 
双射的构造是自然的
$$(h,C)\to hx_{C} $$
这里 $h_{C}$ 是从等价类里面选取的一个代表元, 现在证明这是双射 (这个映射与代表元的选取有关, 但不管怎么选都是双射)
满性: 陪集分解表明任意 $g\in G$ , 存在一个等价类 $C$ 合于 $g\in C$ , 即 $g$ 可被表为 $g=hx_{C}$ 的形式
单性: 若 $h'x_{C'}=hx_C\implies x_{C'}=h'^{-1}hx_{C}$ , 这表明 $x_{C'}$ 和 $x_C$ 属同一个等价类, 则 $x_{C}=x_{C'}$ , 那么消去律表明 $h=h'$ 
两者作为集合存在双射, 即有相同的基数, 这给出上面的等式

##### 推论 
若 $G$ 是有限群, 则所有子群 $H$ 的阶数 $|H|$ 都整除 $|G|$

这是 Lagrange 定理的直接结果, 包括下面

##### 定义 元素的阶
设 $\sigma$ 为群 $G$ 的元素, 定义 $\mathrm{ord}\coloneqq |\braket{\sigma}|$ , 称为 $\sigma$ 的阶

##### 推论
设 $G$ 是有限群, $n\coloneqq |G|$ , 则对任何 $\sigma\in G$ , 有 $\mathrm{ord}{\sigma}\mid n$ 

##### 推论
若 $G$ 是有限群, $|G|$ 是素数, 则 $G$ 是循环群

证: 设 $|G|=p$ 是素数, 那么任取 $g\in G\setminus\{1\}$ , 用其生成一个循环群 $\braket{g}$ , 那么 $|\braket{g}|\mid G$  , 但 $\mathrm{ord} g\neq 1$ , 这表明 $G=\braket{g}$ 

##### 命题
设 $H$ 为群 $G$ 的子群, $K$ 为群 $H$ 的子群, 则 $(G:K)=(G:H)(H:K)$

证: 同样利用陪集分解, 不断把子群做分解, 对每个陪集 $C\in H\backslash G$ 和 $D\in K\backslash H$ 选取代表元 $x_C$ 和 $y_D$ , 故有如下陪集分解
$$G=\bigsqcup_{C\in H\backslash G}Hx_C\quad H=\bigsqcup_{D\in K\backslash H}Ky_D$$
于是
$$G=\bigsqcup_{(C,D)}Ky_Dx_C$$
这表明
$$(G:K)=|(H\backslash G)\times(K\backslash H)|=(G:H)(H:K)$$


# 群作用

##### 定义 群作用
群 $G$ 在非空集 $X$ 上的左作用即为满足下述性质的映射 $a\colon G\times X\to X$
$$\begin{align}&a(g_1g_2,x)=a(g_1,a(g_2,x))\quad g_1,g_2\in G,x\in X\\& a(1_G,x)=x\quad x\in X\end{align}$$
通常记 $a(g,x)$ 为乘法 $gx$ 或 $g\cdot x$ , 因此条件实则在说这种映射和群结构相容
改变 $g$ 的位置, 同样可以定义右作用, 但一般习惯使用左作用

##### 定义 轨道与稳定化子
设群 $G$ 作用到 $X$ 上, 对所有的 $x\in X$ , 定义其
* 轨道 $Gx\coloneqq\{gx: g\in G\}$ , 又称为 $G$ - 轨道
* 稳定化子 $\mathrm{Stab}_G(x)\coloneqq \{g\in G:gx=x\}\subset G$ 

稳定化子 $\mathrm{Stab}_G(x)$ 自动是 $G$ 的子群

>[!notes] 子群验证
>同样验证等价的条件即可, 对任意 $g_1,g_2\in\mathrm{Stab}_G(x)$ , 考察 $g_1g_2^{-1}$ 
>由于 $gx=x\implies x=g^{-1}x$ , 则 $g_1g_2^{-1}x=g_1(g_2^{-1}x)=g_1x=x$
>即 $g_1g_2^{-1}\in\mathrm{Stab}_G(x)$

##### 定义 - 命题 
设群 $G$ 作用在非空集 $X$ 上. 在 $X$ 上定义二元关系 $\sim_G$ 合于 $x\sim_G y$ 当且仅当存在 $g\in G$ 使得 $y=gx$ , 则
1. $\sim_G$ 是等价关系
2. 对 $\sim_G$ 的等价类即为 $X$ 中的 $G$ - 轨道
对应的商集记为 $G\backslash X$ , 对于右作用也有对应结果, 对应的商集记为 $X/G$ 

证:
首先证明等价关系
* 自反性: $x=1x$ , 则 $x\sim_G x$
* 对称性: $y=gx\implies x= g^{-1}y$ , 即 $y\sim_G x$
* 传递性: 若 $x\sim_G y,y\sim_G z$ , 那么 $y=g_1x,z=g_2y\implies z=g_2(g_1x)=(g_2g_1)x$ 即 $x\sim_G z$ 
然后再说明给出的等价类即为轨道
对于包含代表元 $x$  的等价类 $C$ , $y\in C\implies y\sim_G x\implies y=gx\implies y\in Gx$ 相反的方向是相同的

##### 推论 轨道分解
设群 $G$ 作用在非空集 $X$ 上, 则 $X$ 是所有 $G$ - 轨道的无交并

这是因为轨道是等价类, 于是有自然的等价类分解

##### 定义
设群 $G$ 作用在非空集 $X$ 上
* 若 $\bigcap_{x\in X} \mathrm{Stab}_G(x)=\{1_G\}$ , 则称此作用忠实
* 若对所有的 $x$ 皆有 $\mathrm{Stab}_G(x)=\{1_G\}$ , 则称此作用自由
* 若 $X$ 仅有一个轨道, 即对所有 $x,y\in X$ 皆有 $g\in G$ 合于 $y=gx$ , 则称此作用传递

##### 引理
设群 $G$ 左作用于 $X$ 上, 对 $x\in X$ , 记 $H\coloneqq \mathrm{Stab}_G(x)$ , 则有双射
$$\begin{array}{c}G/H\xrightarrow{1:1}Gx\\gH\mapsto gx\end{array}$$

证: 
同样先证明这是良定义的: 若 $g'=gh$ 那么 $g'x=ghx=g(hx)=gx$ , 即像只与陪集本身有关
轨道的定义导致这个映射是满的, 对于单性, 若 $gx=g'x$ , 则 $g'^{-1}g\in H$ , 这表明两者同属同一等价类

>[!notes] 理解
>这个引理的意思是说 $G$ 轨道的分解和按照稳定子的陪集分解是相同的
>因为每个 $x$ 的轨道上的点从 $x$ 出发可以相差一个任意的 $x$ 的稳定子, 这个东西不能被轨道上的元素探测到
>这也是轨道的构造
>这个结果立即导致 轨道 - 稳定子公式, 实际上就是特殊的 Lagrange 定理, 取稳定子为子群, 那么有
>$$|G|=|H|\cdot(G:H)=|H|\cdot|Gx|$$


若 $X$ 是有限非空集, 则它有且仅有有限多个 $G$ - 轨道, 记作 $Gx_1,\cdots ,Gx_n$ , 记 $H_i\coloneqq \mathrm{Stab}_{G}(x_i)$ , 于是有轨道分解 $X=\bigsqcup_{i=1}^nGx_i$  , 则于上面的引理一同导致
$$|X| =\sum_{i=1}^n (G\colon H_i)$$
同样有一个基于轨道分解给出的关于群的计数的结果

##### 命题 Burnside 引理
设有限群 $G$ 作用于有限非空集 $X$ , 对于所有 $g\in G$ , 定义 $X^g\coloneqq \{x\in X: gx=x\}$ , 则
$$|G\backslash X|\cdot |G|=\sum_{g\in G}|X^g|$$
证: 证明基于轨道分解
首先需要使用一个引理: 取 $x_0\in X$ , 则 $\mathrm{Stab}_G(gx_0)=g\mathrm{Stab}_G(x_0)g^{-1}$ , 那么 $|\mathrm{Stab}_G(gx_0)|=|\mathrm{Stab}_G(x_0)|$ 
先考虑传递作用, 即只有一条轨道 $|G\backslash X| =1$ , 那么轨道分解给出
$$\sum_{g\in G}|X^g|=\sum_{x\in X}|\mathrm{Stab}_G(x)|=|\mathrm{Stab}_G(x_0)|\cdot(G:\mathrm{Stab}_G(x_0))=|G|$$
>第一步是因为考虑固定 $g$ 去问 $g$ 作用下不变的 $x$ 和固定 $x$ , 去问作用使 $x$ 不变的 $g$ 是一样的
>第二步是因为作用传递导致稳定化子大小相同, 而 $\sum_{x\in X}1=|X|=|Gx_0|=(G:\mathrm{Stab}_G(x_0))$

对于一般的作用, 可以做轨道分解 $Gx_i$ (注意 $G$ 有限故轨道也有限)
$$X=\bigsqcup_{i}Gx_i$$
从而对 $X_i=Gx_i$ 
$$\sum_{g\in G}|X^g|=\sum_{i}\sum_{g\in G}|X_i^g|=n|G|$$
而 $n=\sum_{i}1$ 即为轨道的数量, 即为 $|G\backslash X|$ 


##### 引理
群 $G$ 在 $X$ 上的作用忠实, 当且仅当对应的同态 $A:G\to\mathfrak{S}_X$ 为单

证:
若作用忠实, 即 $\bigcap_{x\in X}\mathrm{Stab}_G(x)=\{1\}$ , 那么考虑同态 $A(g)=A(g')$ , 则 $A(gg'^{-1})=1$ 即  $gg'^{-1}\in\bigcap_{x\in X}\mathrm{Stab}_G(x)$
从而 $gg'^{-1}=1\implies g=g'$ 
反之若 $A$ 单, 即任意 $g\in \bigcap_{x\in X}\mathrm{Stab}_G(x)$ , $A(g)=1\implies g=1$ 

##### 定理 A.Cayley
任何群 $G$ 都能嵌入为 $\mathfrak{S}_G$ 的子群

证: 考虑 $G$ 以群乘法作用在 $G$ 自身上, 则 $g_1x=g_2x\leftrightarrow g_1=g_2$ , 即对任意 $x$ , $\mathrm{Stab}_G(x)=\{1\}$ 即作用自由, 从而作用忠实, 即对应的同态是单射, 且 $G\subset \mathfrak{S}_G$ 可以作为子群嵌入


# 轨道分解的应用

##### 定义 不动点
设 $G$ 作用在 $X$ 上, 记 $X^G := \{x\in X:\forall g,gx=x\}$ , 其元素称为 $X$ 在 $G$ 作用下的不动点
不动点也等于只有一个元素的轨道

##### 定义 p - 群
设 $p$ 为素数, 若 $|G|=p^m$ , 其中 $m\in\mathbb{Z}_{\geq 0}$, 则称 $G$ 为 p - 群

##### 命题 
设 p - 群 $G$ 作用在有限集 $X$ 上, 则
$$|X|=|X^G|\quad (\mathrm{mod} \,p)$$
证:
同样证明依赖轨道分解, 先将有限集做轨道分解 $Gx_1,\cdots Gx_n$ , 而不动点对应只有自己的轨道, 总数为 $|X^G|$
$$|X|=|X^G|+\sum_{i}|Gx_i|=|X^G|+\sum_{i}(G:\mathrm{Stab}_G(x_i))$$
而 Lagrange 定理给出 $(G:\mathrm{Stab}_G(x_i))|\mathrm{Stab}_G(x_i)|=|G|$ , 而 $\mathrm{Stab}_G(x_i)\neq G$ 因为不是不动点, 故 $(G:\mathrm{Stab}_G(x_i))$ 是 $p$ 的倍数, 于是
$$|X|=|X^G|\quad (\mathrm{mod}\,p)$$
 
##### 命题
设 $G$ 为非平凡的 p - 群, 则 $Z_G\neq \{1\}$
证:
考虑 $G$ 到自身的群作用, 那么有 $|G|=|G^G|\quad (\mathrm{mod}p)$ 这里 $G^G=\{h\in G:\forall g\in G,g\cdot h=h\}$ 
若是共轭作用 $g\cdot h=ghg^{-1}$ , 那么 $ghg^{-1}=h\implies gh=hg$ , 故 $G^G$ 为 $G$ 的中心, 则 $|G|=|Z_G|=0\quad (\mathrm{mod}p)$
从而 $Z_G\neq\{1\}$

##### 定理 A. - L. Cauchy
设 $G$ 为有限群, $p$ 为 $|G|$ 的素因数, 则存在 $g\in G$ 使得 $\mathrm{ord}(g)=p$
证:

>证明的方式是一个构造性的证明, 直觉较少, 但可以如下理解:
>实际上在寻找 $g\in G$ 合于 $g^p=1$ , 直接找是困难的, 但是可以找 $g_1\cdots g_p=1$ 的所有元素, 注意到轮换作用在其上的不动点就是要找的 $p$ . 现在来具体写这一点

考虑 $\mathbb{Z}/p\mathbb{Z}$ 在集合 $X=\{(g_1,\cdots,g_p):g_1\cdots g_p=1\}$ 上的轮换作用, 具体地说, 将集合的下标视作 $\mathbb{Z}/p\mathbb{Z}$ 的元素, 作用为
$$a(k+p\mathbb{Z},(g_i))\mapsto g_{i+k}$$
那么若 $(g_i)_i\in X$ , 则 
$$g_2\cdots g_p g_1=g_1^{-1}(g_1 g_2\cdots g_p)g_1=g_1^{-1}g_1=1$$
即集合对群作用封闭, 考虑该作用的不动点, 得到
$$g_1=g_2=\cdots=g_p=g\quad g^p=1$$
不动点集为 $X^{\mathbb{Z}/p\mathbb{Z}}$ , 由于 $(1)_i=\in X^{\mathbb{Z}/p\mathbb{Z}}$ , 故非空, 只需要证它有 $(1)_i$ 之外的其他元素, 由于确定了 $p-1$ 个元素后, 总可以唯一得到剩下一个元素, 所以 $X$ 的大小等价于 $G^{p-1}$ 的大小, 由前一定理得到, 对 p - 群 $\mathbb{Z}/p\mathbb{Z}$ 作用, 有
$$|G^{p-1}|=|X|=|X^{\mathbb{Z}/p\mathbb{Z}}|=0\quad\mathrm{mod} \,p$$
于是 $X^{\mathbb{Z}/p\mathbb{Z}}$ 有 $(1)_i$ 之外其他元素

##### 定义 Sylow p - 子群
设 $G$ 为有限群, $p$ 为素数. 满足 $|P|=p^a$ 的子群 $P$ 称为 $G$ 的 p - 子群, 其中 $a\in\mathbb{Z}_{\geq 0}$; 若进一步有 $p^{a}\parallel|G|$  , 则称 $P$ 为 $G$ 的 Sylow p - 子群

#### 定理 Sylow 定理
一共有三个定理

待写


# 置换的循环分解的应用

##### 定义 轮换
设 $X$ 为非空集, $a_1,\cdots,a_m$ 是 $X$ 中相异的元素 ($m\in\mathbb{Z}_{\geq 1}$) , 下面取同余类将 $i$ 等同于 $\mathbb{Z}/m\mathbb{Z}$ 的元素, 则具有下面形式的置换
$$\begin{align}&\sigma\colon X\to X\\&\sigma(a_i)=a_{i+1}\quad i\in\mathbb{Z}/m\mathbb{Z}\\&\sigma(x)=x\quad x\in X\setminus\{a_1,\cdots,a_m\}\end{align}$$
称为 $X$ 上的 m - 循环或轮换, 也记为 $\sigma=(a_1\,\cdots\,a_m)\in\mathfrak{S}_X$ , 对于 $m=2$ 时, 也称为对换

##### 定义
给定集合 $X$ 的循环 $(a_1\cdots a_n)$ 和 $(b_1\cdots b_m)$ , 若 $\{a_1,\cdots,a_n\}\cap\{b_1,\cdots,b_m\}=\emptyset$ , 则称这两个循环不交

##### 引理
设循环 $\sigma,\tau\in\mathfrak{S}_X$ 不交, 则 $\sigma\tau=\tau\sigma$
证: 两个各自保持轮换对象之外的元素不变, 故交换性是显然的

##### 命题 循环分解
设 $n\in \mathbb{Z}_{\geq 1}$ , 而 $\sigma \in \mathfrak{S}_n$ , 则 $\sigma$ 分解为两两不交的循环的积
$$\sigma=(a_{1,1}\cdots a_{1,\ell_1})(a_{2,1}\cdots a_{2,\ell_2})\cdots(a_{m,1}\cdots a_{m,\ell_m})$$
且满足 $\sum_{i=1}^m\ell_i=n$ , 而且这些循环是唯一的, 至多差一个重排
证:
让 $\sigma$ 生成的有限群 $\braket{\sigma}$ 作用在 $\{1,2,\cdots,n\}$ 上, 于是有轨道分解 (这是有限集故分解有限)
$$\{1,2,\cdots,n\}=C_1\sqcup C_2\sqcup\cdots\sqcup C_m$$
对每个轨道, 取代表元 $a_i\quad 1\leq i\leq m$ , 然后取最小的 $l_i\in \mathbb{Z}_{\geq 1}$ 合于 $\sigma^{l_i}(a_i)=a_i$ , 于是定义 
$$a_{i,k}=\sigma^{k-1}(a_{i,1})$$
则 $\sigma$ 在其上的作用是
$$a_{i,1}\mapsto a_{i,2}\mapsto\cdots\mapsto a_{i,l_{i}}\mapsto a_{i,1}$$
限制到这个集合上变为循环作用, 且若 $1<m<n<l_i$ 有 $a_{i,m}=a_{i,n}$ , 则 $\sigma^{m-n}(a_{i,1})=a_{i,1}$ 与 $l_i$ 的最小性矛盾
并且轨道的定义使这个集合就是轨道, 于是 $|C_i|=l_i$ 即 $\sigma$ 在子集 $C_i$ 上的作用可以看作作用在
$$(a_{i,1},a_{i,2},\cdots,a_{i,l_i})$$
上的轮换作用, 并且轨道不交, 于是轮换也无交
对于唯一性, 因为轨道分解是唯一的, 至多相差我们对代表元的选取, 即相差一个重排

##### 命题
设 $\sigma$ 有如上述命题的循环分解, 则
$$\begin{align}&\mathrm{sgn}(\sigma)=(-1)^{\sum_{i=1}^{m}(\ell_{i}-1)}\\&\mathrm{ord}(\sigma)=\mathrm{lcm}(\ell_1,\ldots,\ell_m)\end{align}$$
证:由于符号是同态, 所做问题即为计算上面的轮换作用的符号, 考察 $\xi_i:=(a_{i,1} a_{i,2}\cdots a_{i,l_i})$ , 只需要计算该轮换的符号, 注意到轮换有分解
$$(a_{i,1} a_{i,2}\cdots a_{i,l_i})=(a_{i,1}a_{i,l_i})(a_{i,2}\cdots a_{i,l_i})$$
该分解可以递归地做下去, 那么 $\mathrm{sgn}\,\xi_i=(-1)^{l_i -1}$
而对于 $\mathrm{ord}\,\sigma$ , 按照上面的分解, 有
$$\sigma^k =\xi_{i}^k\cdots \xi_{l_i}^k=\mathrm{Id}\Leftrightarrow \xi_{i}^k=\mathrm{Id}\quad \forall i$$
这立即导致 $\mathrm{ord}(\sigma)=\mathrm{lcm}(\ell_1,\ldots,\ell_m)$

# 正规子群与商群

##### 定义 正规子群
若 $G$ 的子群满足以下条件
$$\forall g\in G,gHg^{-1}=H$$
则称 $H$ 为 $G$ 的正规子群, 也记为 $H\lhd G$
注:
* 正规性要求 $gHg^{-1}\subset H$ 对所有 $g$ 成立, 用 $g^{-1}$ 替代 $g$ 则可以得到反向包含关系
* 同样, 等价的要求是 $gH=Hg$ , 或者放宽为 $gH\subset Hg$ , 因此正规子群的陪集不必分左右

>[!example]
>正规子群的几个典型例子:
>1. 若 $G$ 是交换群, 则 $G$ 的所有子群都正规


##### 定义 单群
若 $G$ 不是平凡群, 且没有 $\{1\},G$ 之外的正规子群, 则称 $G$ 为单群

##### 引理
设 $H$ 和 $K$ 是 $G$ 的子群, 则 $HK=KH$ 当且仅当 $HK$ 为 $G$ 的子群
证: 直接证明即可
若 $HK=KH$ , 考虑任意 $h_1k_1,h_2k_2$ , 则 $h_1k_1(h_2k_2)^{-1}=h_1k_1k_2^{-1}h_2^{-1}$ 利用 $HK=KH$ 移动 $h_2$ 到最左边, 表明这是 $HK$ 的元素, 故 $HK$ 为 $G$ 的子群 
反之, 对任意 $h_1k_1$ , 存在$h_2k_2$ 合于 $h_1k_1h_2k_2=1$ 那么 $h_1k_1=k_2^{-1}h_2^{-1}\in KH$ 表明 $HK\subset KH$ , 反过来的包含关系也是显然的, 于是 $HK=KH$  

##### 命题 
设 $H$ 是 $G$ 的子群, $K$ 为 $G$ 的正规子群, 则 $HK=KH$ , 而且有 $HK$ 是 $G$ 的子群
证:
只需要证 $HK=KH$ 即可, 由于 $gKg^{-1}=K$ 对所有 $g$ 成立, 那么考虑任意 $hk$ 存在 $k'$ 合于 $hkh^{-1}=k'\implies hk=k'h\in KH$ 从而 $HK\subset KH$ ,反过来的包含关系也是显然的, 由前者也知 $HK$ 是 $G$ 的子群

##### 定义 中心化与正规化
对任意子群 $K\subset G$ , 可以其中心化子和正规化子, 为 $G$ 的子群
$$Z_G(K):=\{g\in G:\forall x \in K,gxg^{-1}=x\}$$
和正规化子
$$N_G(K):=\{g\in G:gKg^{-1}=K\}$$


##### 定义 - 命题 群同态的核
设 $f\colon G\to G'$ 为群同态, 记
$$\ker(f):=\{g\in G:f(g)=1_{G'}\}$$
则 $\ker(f)\lhd G$ , 称之为群同态 $f$ 的核
证: 只需要证明核正规, 考虑任意 $g\in G$ , 若 $a\in \ker(f)$ , 则 $f(gag^{-1})=f(g)f(a)f(g^{-1})=f(g)f(g)^{-1}=1_{G'}$
从而 $g\ker(f)g^{-1}\subset \ker{f}$ 
对任意 $a\in\ker(f)$ , 则 $a=g(g^{-1}ag)g^{-1}\in g\ker(f)g^{-1}$ 得到反向包含关系

##### 命题
设 $f\colon G\to G'$ 为群同态, $N:=\ker(f)$ . 若 $x,y\in G$ ,则 $f(x)=f(y)$ 当且仅当 $xN=yN$ .
特别地 $f$ 是单同态当且仅当 $N=\{1_G\}$
证:
直接证明即可, 若 $f(x)=f(y)$ , 那么 $f(x)f(y)^{-1}=f(xy^{-1})=1_{G'}\implies xy^{-1}\in\ker(f)$ 这表明 $xN=yN$ 
反之, 若 $xN=yN$ , 那么 $xy^{-1}\in\ker(f)$ 得到之前的结果
故若 $f$ 是单同态, 则 $\forall x\in\ker{f}$ , 有 $x=1_G\implies N=\{1_G\}$

##### 定义 - 命题 商群
设 $N\lhd G$ , 在 $G/N$ 上定义二元运算
$$xN\cdot yN=xyN$$
这是良定义的, 这只与陪集有关, 而无关代表元的选取
1. 此运算使 $G/N$ 构成群, 其幺元和取逆为$$1_{G/N}=1_GN\quad (xN)^{-1}=x^{-1}N$$
2. 映 $x$ 为 $xN$ 的商映射 $q\colon G\to G/N$ 是群同态, 且 $\ker(q)=N$

群 $G/N$ 称为 $G$ 对 $N$ 的商群
证:
首先说明这是良定义的, 考虑 $x'=xn$ , 那么 $(x'y)N=(xny)N=(xyn')N=(xy)N$ , 其中用到了 $H$ 正规的条件, 对 $y$ 用相同的条件也可以, 可以看到这里用到正规子群的群元素可以在封闭的条件下穿过其他元素, 代价是变为子群中的其他元素, 其他群性质的验证全部归结于 $G$ 本身的群性质, 故不再赘述
接着证明这是同态:
$$q(xy)=(xy)N=xN\cdot yN=q(x)q(y)$$
同时
$$q(x)=xN=1_GN\implies x\in N\implies \ker(q)\subseteq N$$
反向包含是显然的, 于是有 $\ker(q)=N$

##### 命题
设 $f\colon G\to G'$ 为群同态, 而 $N\lhd G$ 合于 $N\subset \ker(f)$ , 则存在唯一的同态 $\overline{f}\colon G/N \to G'$ 使得 $f=\overline{f}q$ , 或表述为以下交换图
![[attachments/EAlg-Notes-2.webp|300]]

[[EAlg-Notes-2.pdf#page=462&rect=179,456,261,511|📖]]
称这样的 $\overline{f}$ 为 $f$ 诱导的同态

证: 
由于 $q$ 是满同态, 故 $\overline{f}$ 的像被交换性质 $f=\overline{f}\circ q$ 唯一确定, 方法是找陪集中的任意一个代表元, 并追踪其在 $f$ 下的像.
不过需要首先说明这是良定义的, 我们取 $x,x'\in x'N\implies xx'^{-1}\in N$ , 而 $N\subseteq \ker(f)$  , 这给出
$$f(xx'^{-1})=1_{G'}=f(x)f(x')^{-1}\implies f(x)=f(x')$$
这同时论证了存在性与唯一性, 即该映射作为集合存在和唯一, 下面再说明其与群结构相容
$$\overline{f}((xy)N)=f(xy)=f(x)f(y)=\overline{f}(xN)\overline{f}(yN)$$

##### 推论 
设 $f\colon G\to G'$ 为群同态, $N\lhd G,N'\lhd G'$ 而 $f(N)\subset N'$, 则存在唯一的群同态 
$$\overline{f}\colon G/N\to G'/N'$$
使下图交换
![[attachments/EAlg-Notes-2 1.webp|300]]

[[EAlg-Notes-2.pdf#page=462&rect=183,190,285,254|📖]]
这里 $q,q'$ 为商同态
证:
沿着原先的思路, $\overline{f}$ 在每个陪集上的值被代表元唯一确定, 即交换图 $\overline{f}\circ q=q'\circ f$ , 同时要验证映射是良定义的, 实际上这需要  $f(N)\subseteq N'=\ker(q')$ . 与原命题精神一致.
由于指定了函数值, 同态性也与前者一样只需类似验证即可

##### 命题
设 $f\colon G\to G'$ 为群同态, 则诱导同态 $\overline{f}\colon G/\ker(f)\to G'$ 给出群同构 $G/\ker(f)\overset{\sim}{\to}\mathrm{im}(f)$ , 从而有 $(G:\ker(f))=|\mathrm{im}(f)|$
证:
这实际上是前面两个命题的应用, 先说明核正规, 再证明同构
核正规: 
$$\forall h\in G,\forall g\in\ker(f)\implies f(hgh^{-1})=f(h)1_{G'}f(h)^{-1}=1_{G'}\implies hgh^{-1}\in\ker(f)\implies h\ker(f)h^{-1}\subset \ker(f)$$
而对任意 $g\in\ker(f)$ , 取 $h^{-1}gh\in\ker(f)\implies g=h(h^{-1}gh)h^{-1}\in h\ker(f)h^{-1}$ 证明双边包含关系
同时 $\ker(f)\subseteq\ker(f)$ 自动满足, 故诱导同态存在, 下面证这是同构
单: 
$$\overline{f}(x\ker(f))=1_{G'}\implies f(x)=1_{G'}\implies x\in \ker(f)\implies q(x)=x\ker(f)=1_{G}\ker(f)$$
满:
$$\forall f(x)\in \mathrm{im}(f)\implies \overline{f}(x\ker(f))=f(x)$$
故这是同构

##### 命题 
设 $f\colon G\to G'$ 为满同态, 则有双射
![[attachments/EAlg-Notes-2 2.webp|500]]

[[EAlg-Notes-2.pdf#page=463&rect=88,172,380,279|📖]]

此双射满足如下性质
1. $H'_1\subset H'_2\leftrightarrow f^{-1}(H'_1)\subset f^{-1}(H'_2)$
2. 若 $H'\lhd G'$ 对应到 $H\lhd G$ , 则合成同态 $G\overset{f}{\to} G'\overset{\text{商}}{\to}G'/H'$ 诱导出群同构 $G/H\overset{\sim}{\to} G'/H'$
3. 当 $f$ 取为对某个 $N\lhd G$ 的商同态 $G\to G/N$ 时, 上述群同构进一步有形式 $$G/H\overset{\sim}{\to}(G/N)/(H/N)$$其中 $N\subset H\lhd G$

证:
首先验证两个双射
对一个双射, 由于 $f$ 是满同态, 
需要验证逆映射确实得到一个群
$$f^{-1}(H')=\bigcup_{y\in H'}f^{-1}(y)$$
那么 
$$\forall x,y\in f^{-1}(H')\implies f(xy^{-1})=f(x)f(y)^{-1}\in H'\implies xy^{-1}\in f^{-1}(H')$$
从而这是一个子群, 那么由 $f$ 的满性可以得到该映射的满性, $1_{G'}\in H'$ 显然有 $f^{-1}(H')\supseteq\ker(f)$
再来验证单性
$$f(H_1)=f(H_2)\implies \forall x_1\in H_1,\exists x_2\in H_2,f(x_1)=f(x_2)\implies f(x_1x_2^{-1})=1_{G'}\implies x_1x_2^{-1}\in \ker(f)\subset H_2$$
那么就有 $x_1\in H_2$ , 同理可证反向包含关系, 最后即 $H_1=H_2$  故这是单射
对第二个映射, 先说明 $f$ 将正规子群打到正规子群
$$H\lhd G\implies f(g)f(H)f(g)^{-1}=f(gHg^{-1})=f(H)\implies f(H)\lhd G'$$
这里 $g$ 是根据 $f$ 的满性任意选出来的, 故映射良定义
满性: 考虑 $f^{-1}(H')$ , 只需要证明这是正规子群, 由
$$f(g)H'f(g)^{-1}=H'\implies \forall h\in H',\exists h'\in H',f(g)hf(g)^{-1}h'^{-1}=1_{G'}$$
从而
$$\forall a\in f^{-1}(h),\exists b\in f^{-1}(h'^{-1}),gag^{-1}b\in\ker(f)\subseteq f^{-1}(H')$$
即 
$$\forall h\in f^{-1}(H'),\forall g\in G,ghg^{-1}\in f^{-1}(H')\implies f^{-1}(H')\lhd G$$
这同时说明了满性, 而单性由上一个双射关系继承
接着再验证每个性质:
若 $H_1'\subset H_2'$ 自然有 $f^{-1}(H_1')\subset f^{-1}(H_2')$ , 若 $f^{-1}(H_1')\subset f^{-1}(H_2')$ , 即任意 $y\in H_1'$ 有 $f^{-1}(y)\subseteq f^{-1}(H_2')$ , 任取 $x_0\in f^{-1}(y)$ 有 $y=f(x_0)\in H_2'$ 即 $H_1'\subset H_2'$
第二条性质, 直接使用前面的命题即可
最后, 当 $f\colon G\to G/ N$ 时,若 $H$ 合于 $\ker(f)=N\subset H$ , 那么 $N$ 也对 $H$ 正规, 上述符号合法, 接着看 $f$ 在 $H$ 上的值
$$\forall x\in H,f(x)=xN$$
由陪集的性质, 这实则给出 $N$ 作为 $H$ 的子群的所有陪集, 正规性表明这是一个商群 $H/ N$ 于是得到命题结果

>这实际上在刻画一件事情, 映射丢失的信息即为 $\ker(f)$ 
>这个精神不仅在这里出现, 可以说出现映射的地方就会有这个精神存在

##### 命题
设 $H,K\subset G$ 为子群, $H\subset N_{G}(K)$ , 则 $K\lhd HK$ , $H\cap K\lhd H$ , 而且有群同构
$$\begin{align}H&/(H\cap K)\overset{\sim}{\to} HK/K\\&h(H\cap K)\to hK\end{align}$$
其中 $h\in H$

证:
逐个验证即可
$$\forall hk\in HK, hkK(hk)^{-1}=hKh^{-1}=K$$
其中使用了 $H\subset N_{G}(K)$ , 这给出 $K\lhd HK$ (子群的说明是简单的)
同样由 $H$ 正规化 $K$ , 并且 $H\lhd H$ 
$$\forall g\in H\cap K,\forall h\in H,\exists k\in K,hgh^{-1}=k\implies k\in K\implies H\cap K\lhd H$$
同样这是子群的说明也是简单的
最后说明群同构 $H/(H\cap K)\to HK/K$ , 定义为 $h(H\cap K)\to hK$ 
满性: 
$$\forall hkK\in HK/K,hkK=hK$$
这给出满性, 对于单性
$$h_1K=h_2K\implies h_1h_2^{-1}\in K\implies h_1h_2^{-1}\in H\cap K\implies h_1(H\cap K)=h_2(H\cap K)$$


# 群的半直积

##### 定义 - 命题 半直积
设 $H$ 和 $N$ 为群, $\varphi\colon H\to \mathrm{Aut}(N)$ 为群同态, 记 $h\in H$ 对 $\varphi$ 的像为 $\varphi_h\colon N\to N$ , 在 $N\times H$ 上定义二元运算
$$(n,h)(n',h'):=(n\varphi_h(n'),hh')$$
这给出群结构, 称为 $H$ 和 $N$ 相对于 $\varphi$ 的半直积, 记为 $N\rtimes_{\varphi}H$ 满足
$$1_{N\rtimes H}=(1_N,1_H),\quad(n,h)^{-1}=\left(\varphi_{h^{-1}}(n^{-1}),h^{-1}\right)$$
群 $N$ 和 $H$ 分别通过 $n\mapsto(n,1_{H})$ 和 $h\mapsto (1_N,h)$ 嵌入为 $N\rtimes H$ 的子群, 而 $(n,h)=(n,1_H)(1_N,h)$
对所有 $n\in N,h\in H$ 均成立, 进一步 $N\lhd N\rtimes H$

证:
先验证这确实是一个群:
$$((n_1,h_1)(n_2,h_2))(n_3,h_3)=(n_1\varphi_{h_1}(n_2),h_1h_2)(n_3,h_3)=(n_1\varphi_{h_1}(n_2)\varphi_{h_1h_2}(n_3),h_1h_2h_3)$$
需要关心的只有第一个坐标, 首先 $\varphi_{\cdot}$ 是群同态: $\varphi_{h_1h_2}=\varphi_{h_1}\varphi_{h_2}$ , 故为 $n_1\varphi_{h_1}(n_2)\varphi_{h_1}(\varphi_{h_2}(n_3))$ 而
$$n_1\varphi_{h_1}(n_2\varphi_{h_2}(n_3))=n_1\varphi_{h_1}(n_2)\varphi_{h_1}(\varphi_{h_2}(n_3))$$
与结合律相容
$$(1_N,1_H)(n,h)=(1_N\varphi_{1_H}(n),h)=(1_N\mathrm{Id}(n),h)=(n,h)$$
以及
$$(n,h)(1_N,1_H)=(n\varphi_{h}(1_N),h)=(n,h)$$
最后
$$(\varphi_{h^{-1}}(n^{-1}),h^{-1})(n,h)=(\varphi_{h^{-1}}(n^{-1})\varphi_{h^{-1}}(n),h)$$
以及
$$(n,h)(\varphi_{h^{-1}}(n^{-1}),h^{-1})=(n\varphi_{h}(\varphi_{h^{-1}}(n^{-1})),1)=(n\varphi_{hh^{-1}}(n^{-1}),1)=(1,1)$$

>注意这里有两个同态 $\varphi_{\cdot}$ 是一个打到同态的同态

子群的嵌入是显然的, 这里不会存在两个坐标的交叉

最后
$$(n',h')(n,1_H)(n',h')^{-1}=(n'\varphi_{h'}(n),h')(\varphi_{h'^{-1}}(n'^{-1}),h'^{-1})=(n'\varphi_{h'}(n)n'^{-1},1_H)\in N$$

>半直积初看难以理解, 可以用二维平移群和旋转群来理解: $h$ 旋转, $n$ 平移:
>旋转的角度是直接相加的, 但是平移向量需要先旋转到新坐标系再相加

