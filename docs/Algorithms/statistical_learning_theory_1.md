# Statistical Learning Theory - 1
In this blog, we mainly talk about statistical learning theory, which describes how a learning algorithm generalize and how to derive a generalization error bound for an algorithm. This is important because it shows why statistical learning is useful under i.i.d assumption.

## Introduction
The central question in statistical learning is:
> Why does minimizing training error reduce test error?

The answer is not obvious for the training error and testing error are two separate quantities which can in general be arbitrarily far apart. To answer this question, we will use a set of new tools. At the heart of these tools are concentration inequalities and union bound. We will talk about these tools below.

### Formal setup
In this post, we mainly talk about supervised learning setting. The problem is predicting an output $y\in Y$ given $x\in X$, for example, $X=R^d,Y=\{-1,1\}$.

- Let $H$ be a set of hypotheses, each $h\in H$ maps $X$ to $Y$, for example, $H=\{ x\to sign(w^Tx), w\in R^d \}$.

- Let $l:(X\times Y)\times H \to R$ be a loss function, for example, $l((x,y),h)=\mathbb{I}[y\neq h(x)]$ is the zero-one loss.

- Let $p^*$ be the underlying distribution of the input-output pair $X\times Y$.

Several definitions below:
- Expected risk
  
  $$
  L(h)=E_{(x,y)\sim p*}[l((x,y),h)]
  $$

  The expected risk is just an expectation of $h's$ loss with respect to $l$ over distribution $p^*$. Our goal is to get the best $h^*$ which satisfies:

  $$
  h^*=\arg min_{h\in H}L(h)
  $$

  Note that $h^*$ is not a random variable.
- Training example
  Training examples are a set of input-output pairs:

  $$
  (x^{(1)},y^{(1)}),(x^{(2)},y^{(2)}),...,(x^{(n)},y^{(n)})
  $$

  which are drawn i.i.d from $p^*$. Note that the training distribution and testing distribution are the same, and this is the source of statistial learning's power.
- Empirical risk
  Empirical risk

  $$
  \hat{L}(h)=\frac{1}{n}\sum_{i=1}^n l((x^{(i)},y^{(i)}),h)
  $$

  This is an unbiased estimation of expected risk. Note that empirical risk itself is a random variable that depends on training examples, so we can use many kinds of concentration inequalities to bound the range of it. By training, we mean to find an expirical risk minimizer (**ERM**):

  $$
  \hat{h}=\arg min_{h\in H} \hat{L}(h)
  $$

We want to get $h^*$, but $L(h)$ is difficult to solve because we do not know the distribution $p^*$. By ERM, our interest is the expected risk of $\hat{h}$, in other words, $L(\hat{h})$. 

We are interested in two quantities below:
- How does the expected and empirical risks compare for the ERM?
  
  $$
  L(\hat{h})-\hat{L}(\hat{h})
  $$

- How will the ERM doing with respect to $h^*$?
  
  $$
  L(\hat{h})-L(h^*)
  $$
  
  This is also known as **excess risk**
