# Financial Engineering
Python projects in financial engineering. In Python, unless otherwise stated.

## [Merton's Jump Diffusion Model]() (1976)
This is an application of **Monte Carlo methods** [1] to the pricing of options on stocks when the underlying asset has occasional jumps in the trajectories. Merton [2] describes such jumps as _"idiosynchratic shocks affecting an individual company but not the market as a whole"_. The jump component makes the distribution of prices _leptokurtic_ (high peak, heavy tails), a feature typical of market data.

[Link to Python module](/python-modules/jump_diffusion.py)

<img src = 'handbook/img/merton-jdm.png' alt = 'merton-jump-diffusion-model' width = '500'>

[1] Glasserman, P. (2003) _Monte Carlo Methods in Financial Engineering_, Springer Applications of Mathematics, Vol. 53

[2] Merton, R.C. (1976) _Option pricing when underlying stock returns are discontinuous_, Journal of Financial Economics, 3:125-144
