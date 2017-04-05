[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

    from __future__ import print_function, division

    import pandas as pd
    import numpy as pd
    import matplotlib.pyplot as plt
    %matplotlib inline
    import nsfg
    import first

    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    #Calculate Cohen Effect Size for pregnancy length differences between firsts and others:

    diff = firsts.prglngth.mean() - others.prglngth.mean()
    var_firsts = firsts.prglngth.var()
    var_others = others.prglngth.var()
    n_f, n_o = len(firsts.prglngth), len(others.prglngth)

    pooled_var = (n_f * var_firsts + n_o * var_others) / (n_f + n_o)
    cohen_prglngth = diff / np.sqrt(pooled_var)
    print(cohen_prglngth)

    #Calculate statistics and Cohen Effect Size for birthweight differences between firsts and others:

    mean_twf = firsts.totalwgt_lb.mean()
    var_twf = firsts.totalwgt_lb.var()
    std_twf = firsts.totalwgt_lb.std()

    mean_two = others.totalwgt_lb.mean()
    var_two = others.totalwgt_lb.var()
    std_two  = others.totalwgt_lb.std()

    diff1 = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
    var_firsts = firsts.totalwgt_lb.var()
    var_others = others.totalwgt_lb.var()
    n_f, n_o = len(firsts.totalwgt_lb), len(others.totalwgt_lb)

    pooled_var1 = (n_f * var_firsts + n_o * var_others) / (n_f + n_o)
    cohen = diff1 / np.sqrt(pooled_var1)

    print('The mean and Std of first babies\' weight is {:.3f} and {:.3f}.'.format(mean_twf, std_twf))
    print('The mean and Std of non-first babies\' weight is {:.3f} and {:.3f}.'.format(mean_two, std_two))
    print('The Cohen Effect Size is {:.4f}.'.format(cohen))

##The results show that weights of first babies are 7.201 lbs with a standard deviation of 1.421 lbs and weights of other babies are 7.326 lbs with a standard deviation of 1.394 lbs.  The Cohen Effect Size is -.0887 standard deviations, which is small.  Conclusion is that weights of first babies are ever so slightly lower than those of non-first babies with the results have little statistical significance.

##Relative to the difference in pregnancy length between firsts and others, there is a slightly bigger difference in weight than in length.  The Cohen Effect Size for length is .0288 standard deviations, about 1/3 of the size of that for weight, but still very small overall.
