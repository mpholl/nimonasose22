def euler_step(x, f, h, pars):
    """
    performs one euler step
    x:      solution
    f:      right-hand-side
    h:      step-width
    pars:   parameters to be passed to f
    """
    return x + h*f(x, *pars)