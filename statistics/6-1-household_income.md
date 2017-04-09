[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```from __future__ import print_function, division

import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
import brfss
import thinkstats2
import thinkplot

def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)
    
def Mean(xs):
    return RawMoment(xs, 1)
    
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)
    
def Var(xs):
    return CentralMoment(xs, 2)
    
def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = np.sqrt(var)
    return CentralMoment(xs, k) / std**k
    
def Skewness(xs):
    return StandardizedMoment(xs, 3)

def Median(xs):
    cdf = thinkstats2.Cdf(xs)
    return cdf.Value(0.5)

def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    std = np.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp
    
 def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.loc[41, 'log_upper'] = log_upper
    
    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample
    
import hinc
income_df = hinc.ReadData()
log_sample = InterpolateSample(income_df, log_upper=6.0)
log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Config(xlabel='Household income (log $)',
               ylabel='CDF')
```               
![CDF](logincome_cdf.tiff)              
              
```sample = np.power(10, log_sample)
cdf = thinkstats2.Cdf(sample)
thinkplot.cdf(cdf)
thinkplot.Config(xlabel='Household income ($)',
               ylabel='CDF')
```               
![CDF](income_cdf.tiff)               
               
```Mean(sample), Median(sample)
Skewness(sample), PearsonMedianSkewness(sample)
cdf.Prob(Mean(sample))
```

```log_sample = InterpolateSample(income_df, log_upper=7.0)
Mean(sample), Median(sample)
Skewness(sample), PearsonMedianSkewness(sample)
cdf.Prob(Mean(sample))
```

The mean income of the sample is $74,278 while the median is $51,226.  The mean is above the median which means the distribution is skewed to the right.  Further support of this is the Skew value of 4.94 and the Pearson Skew value of .736, both positive.  The data shows that 66% of households have an income below the mean?  If the upper bound is moved from $1mm of income to $10mm, the distribution skews further to the right with the mean jumping to $124,267 and the skew numbers to 11.6 and .39 respectively.
