[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```from __future__ import print_function, division

import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
import nsfg
import thinkstats2
import thinkplot
import first

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

age = live.agepreg
weight = live.totalwgt_lb

thinkplot.Scatter(age, weight, alpha = .1)
thinkplot.Show(xlabel = 'AgePreg', ylabel = 'Birth Weight')
#thinkplot.HexBin(ages, weights)
```

![Scatter](ageweight_scatter.tiff)

```bins = np.arange(15, 45, 5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)
#for i, group in groups:
    #print(i, len(group))
ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)
    thinkplot.Config(xlabel = 'AgePreg', ylabel = 'Birth Weight')
print('Pearson\'s correlation is {:.3f}'.format(Corr(age, weight)))
print('Spearman\'s correlation is {:.3f}'.format(SpearmanCorr(age, weight)))
```
![Percentile](ageweight_percentile.tiff)

From the scatterplot there does not seem to be a discernible pattern between mother's age and birth weight.  The mean weight seems to center around the same number regardless of age, though there are outliers.  The correlations support this analysis with both Pearson and Spearman corr close to 0.  The graph of percentiles also supports this with ages increasing somewhat with the mothers' ages between 20 and 25, but then flatteing out and even decreasing with ages from 37 and older. 
