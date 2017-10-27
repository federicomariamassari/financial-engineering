def jump_diffusion(S0=1, K=0.5, T=1, mu=0.12, sigma=0.3, Lambda=0.25,
                   a=0.2, b=0.2, Nsteps=252, Nsim=100, alpha=0.05):
    
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    tic = time.time()

    dt = T/Nsteps

    lognormal_mean = np.exp(a + 0.5*(b**2))
    lognormal_variance = np.exp(2*a + b**2) * (np.exp(b**2)-1)

    M = S0 * np.exp(mu*T + Lambda*T*(lognormal_mean-1))
    V = S0**2 * (np.exp((2*mu + sigma**2)*T \
        + Lambda*T*(lognormal_variance + lognormal_mean**2 - 1)) \
        - np.exp(2*mu*T + 2*Lambda*T*(lognormal_mean - 1)))

    simulated_paths = np.zeros([Nsim, Nsteps+1])
    simulated_paths[:,0] = S0

    normal_rv = np.random.normal(size=[Nsim, Nsteps])
    normal_rv2 = np.random.normal(size=[Nsim, Nsteps])
    poisson = np.random.poisson(Lambda*dt, [Nsim, Nsteps])

    for i in range(Nsteps):
        simulated_paths[:,i+1] = simulated_paths[:,i]*np.exp((mu
                               - sigma**2/2)*dt + sigma*np.sqrt(dt) \
                               * normal_rv[:,i] + a*poisson[:,i] \
                               + np.sqrt(b**2) * np.sqrt(poisson[:,i]) \
                               * normal_rv2[:,i])

    sns.set(palette='viridis')
    plt.figure(figsize=(10,8))
    ax = plt.axes()

    t = np.linspace(0, T, Nsteps+1) * Nsteps
    jump_diffusion = ax.plot(t, simulated_paths.transpose());

    plt.setp(jump_diffusion, linewidth=1);

    ax.set(title="Monte Carlo simulated stock price paths in Merton's jump \
diffusion model\n$S_0$ = {}, $\mu$ = {}, $\sigma$ = {}, $\mu_Y$ = {}, \
$\sigma_Y$ = {}, $\lambda$ = {}, $T$ = {}, Nsteps = {}, Nsim = {}"\
           .format(S0, mu, sigma, a, b, Lambda, T, Nsteps, Nsim), \
           xlabel='Time (days)', ylabel='Stock price')

    plt.show()

    toc = time.time()
    elapsed_time = toc - tic
    print('Total running time: {:.2f} ms'.format(elapsed_time*1000))
