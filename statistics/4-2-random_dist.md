[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

    from __future__ import print_function, division
    
    import pandas as pd
    import numpy as np
    import matlpotlib.pyplot as plt
    %matplotlib inline
    import nsfg
    import first
    import thinkstats2
    import thinkplot
    
    random = np.random.random(1000)
    random_pmf = thinkstats2.Pmf(random)

    # Plot PMF of random sample
    thinkplot.Pmf(random_pmf)
    thinkplot.Config(xlabel='Random Numbers', ylabel='PMF')
    
![PMF](pmf_random.tiff)
    
    # Plot CMF of random sample
    random_cdf = thinkstats2.Cdf(random)
    thinkplot.Cdf(random_cdf)
    thinkplot.Config(xlabel='Random Numbers', ylabel='CDF')
    
![CDF](cdf_random.tiff) 
 
The distribution of 1000 random numbers is uniform.  It is hard to see this from the PMF function as because of the amount of elements, the entire graph is filled, making a discernible pattern hard to read.  The CDF function, however, shows an almost straight line which proves that the distirbution is uniform. 
