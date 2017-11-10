# Financial Engineering
Python projects in financial engineering.

## [Merton's Jump Diffusion Model](https://nbviewer.jupyter.org/github/federicomariamassari/financial-engineering/blob/master/handbook/01-merton-jdm.ipynb) (1976)
This is an application of **Monte Carlo methods** [1] to the pricing of options on stocks when the underlying asset has occasional jumps in the trajectories. Merton [2] describes such jumps as _"idiosynchratic shocks affecting an individual company but not the market as a whole"_. The jump component makes the distribution of prices _leptokurtic_ (high peak, heavy tails), a feature typical of market data.

The model builds on the _standard Brownian motion_, which can also be generated using the [willow tree](https://github.com/federicomariamassari/willow-tree).

[Link to Python module](/python-modules/jump_diffusion.py)

<img src = 'handbook/img/merton-jdm.png' alt = 'merton-jump-diffusion-model' width = '500'>

[1] Glasserman, P. (2003) _Monte Carlo Methods in Financial Engineering_, Springer Applications of Mathematics, Vol. 53

[2] Merton, R.C. (1976) _Option pricing when underlying stock returns are discontinuous_, Journal of Financial Economics, 3:125-144

## Dependencies
`financial-engineering` requires Python 3.5+, and is built on top of the following libraries:
- **NumPy**: v. 1.13+
- **SciPy**: v. 0.19+
- **Matplotlib**: v. 2.0+
- **Seaborn**: v. 0.8+

## Installation
The source code is currently hosted on GitHub at: https://github.com/federicomariamassari/financial-engineering.
Either clone or download the git repository. To clone the repository, on either Terminal (macOS) or Command Prompt (Windows) enter the folder inside which you want the repository to be, possibly changing directory with `cd <desired path>`, and execute:
```shell
$ git clone https://github.com/federicomariamassari/financial-engineering.git
```

## Contributing
This is a small but continuously evolving project open to anyone willing to contribute—simply fork the repository and modify its content. Any improvement, in terms of code speed and readability, or inclusion of new models (such as those from Glasserman's book), is more than welcome. For git commits, it is desirable to follow [Udacity's Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/).

Feel free to bookmark, or "star", the repository if you find this project interesting. Thank you for your support!
