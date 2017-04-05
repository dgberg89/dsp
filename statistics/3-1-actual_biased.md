[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

from __future__ import print_function, division

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()
#resp.head()
#resp['numkdhh']
numkid_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
#print(numkid_pmf)
thinkplot.hist(numkid_pmf, label='numkdhh')
print("Actual mean: {:.4f}".format(numkid_pmf.Mean()))
print("Standard Dev: {:.4f}".format(numkid_pmf.Std()))

![Histogram](Numkid_Actual.tiff)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

numkid_biased_pmf = BiasPmf(numkid_pmf, label='observed')
thinkplot.hist(numkid_biased_pmf, label='numkdhh')
print("Observed mean: {:.4f}".format(numkid_biased_pmf.Mean()))
print("Standard Dev: {:.4f}".format(numkid_biased_pmf.Std()))

thinkplot.PrePlot(2)
thinkplot.Pmfs([numkid_pmf, numkid_biased_pmf])
thinkplot.Show(xlabel = 'NumKids', ylable = 'PMF')

print('The actual mean of number of kids per household is {:.4f}'.format(numkid_pmf.Mean()))
print('The actual mean of number of kids per household is {:.4f}'.format(numkid_biased_pmf.Mean()))
print('The Cohen effect statistic is {:.4f}'.format(cohen))

##The data shows that there is a significant difference between the actual data on number of kids per household and the biased data when asking the children themselves how many are in their household.  The mean of the actual data is 1.024 while the mean from the biased data is 2.404.  The standard deviation of both distributions respectively are 1.18 and 1.08 leading to a Cohen Effect Statistic of -1.213, showing that the difference between the groups is 1.2 standard deviations, not a huge difference, but still over one standard deviation.
