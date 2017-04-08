[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

    from __future__ import print_function, division

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline
    import nsfg
    import first
    import analytic
    import thinkstats2
    import thinkplot
    import scipy.stats
    
    #Distribution for men's heights
    mu = 178
    sigma = 7.7
    dist = scipy.stats.norm(loc=mu, scale=sigma)

    #Convert inches to centimeters
    def inTOcm(x, y):
        low_bound = x * 2.54
        high_bound = y * 2.54
        return(low_bound, high_bound)

    low_cm, high_cm = inTOcm(70, 73)
    low_percent = (dist.cdf(low))
    high_percent = (dist.cdf(high))
    print("The percent of men below 5'10\" is {:.4f}".format(low_percent))
    print("The percent of men below 6'1\" is {:.4f}".format(high_percent))
    print("Therefore, the percent of men between 5'10\" and 6'1\" is {:.4f}".format(high_percent - low_percent))
    
To determine the percent of men between 5'10" and 6'1", you need to compute the total percentages of men below 5'10 (177.8cm) and then below 6'1" (185.42cm).  The difference between the two is the percentage of men between those two heights and thus available for Blue Man Group.  Using the CDF function allows you to come up with these percentages, the final answer of which is .3427 or 34.27% of all men. 
