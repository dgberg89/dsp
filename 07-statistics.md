# Statistics

# Table of Contents

[1. Introduction](#section-a)  
[2. Why We Are Using Think Stats](#section-b)  
[3. Instructions for Cloning the Repo](#section-c)  
[4. Required Exercises](#section-d)  
[5. Optional Exercises](#section-e)  
[6. Recommended Reading](#section-f)  
[7. Resources](#section-g)

## <a name="section-a"></a>1.  Introduction

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)

Use Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) book for getting up to speed with core ideas in statistics and how to approach them programmatically. This book is available online, or you can buy a paper copy if you would like.

Use this book as a reference when answering the 6 required statistics questions below.  The Think Stats book is approximately 200 pages in length.  **It is recommended that you read the entire book, particularly if you are less familiar with introductory statistical concepts.**

Complete the following exercises along with the questions in this file. Some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

## <a name="section-b"></a>2.  Why We Are Using Think Stats 

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  **You could import it, or you could write your own code to practice python and develop a deeper understanding of the concept.** 

Think Stats uses a higher degree of python complexity from the python tutorials and introductions to python concepts, and that is intentional to prepare you for the bootcamp.  

---

## <a name="section-c"></a>3.  Instructions for Cloning the Repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/metisgh/prework  
(Windows):  C:/ds/metis/metisgh/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/metisgh/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/metisgh/prework/ThinkStats2/code
```

---


## <a name="section-d"></a>4.  Required Exercises

*Include your Python code, results and explanation (where applicable).*

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

### Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 



### Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>> Using Bayes' Theorem, knowing that Elvis had a twin brother, we can calculate the probability that Elvis was an identical twin and not a fraternal twin.  The known data is:

    Population probability of being a fraternal twin:  1/125
    Population probability of being an identical twin:  1/300
    Once being an fraternal twin is known, probability of being twin boys: .5*.5 = .25 (50% chance of being a boy or girl)
    Once being an identical twin is known, probability of being twin boys:  .5 (can only be BB or GG)

    Using Bayes Theorem, we can figure out the probability:
    P(Identical|Twin Boys) = (P(Identical) * P(Twin Boys|Identical)) / (P(Identical) * P(Twin Boys|Identical)) + (not Identical) * P(Twin Boys|Not Identical))
    Below is the Python Code to solve this and the final answer:

    #Python code to figure out Elvis question/Bayes Theorem
    #Assume chance of girl or boy being born is 50/50

    prob_frat = 1 / 125
    prob_id = 1 / 300

    #if identical, prob of two boys = .5 (both have to be same sex so 50% identical girls, 50% identical boys)
    prob_id_giventwins = .5

    #if fraternal, prob of two boys = .25 (.5 first boy * .5 second boy)
    prob_frat_giventwins = .5 * .5

    #Calculate prob of Identical Twins|Given Twins using Bayes' Theorem
    #prob_id_T = (prob(id) * prob(T|id)) / ((prob(id) * prob(T|id)) + (prob(not id) * prob(T|not id))

    result = (prob_id_giventwins * prob_id) / ((prob_id_giventwins * prob_id) + (prob_frat * prob_frat_giventwins))

    print('''Given that Elvis had a twin brother who died at birth, the chances that Elvis was an identical twin given
    that the probabilities of fraternal twins are 1/125 and identical twins are 1/300 is {:.3f}.'''.format(result))```

>> Given that Elvis had a twin brother who died at birth, the chances that Elvis was an identical twin given
>> that the probabilities of fraternal twins are 1/125 and identical twins are 1/300 is 0.455.




---

### Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

The main difference between Frequentist and Bayesian approach to statistics is how both define and use probability.  Frequentists tend to believe that a parameter of a population is fixed and that the proper approach to conducting experiments on the parameter is through the creation of many different sampling distribtuions.  The statistics that describe those distributions will contain the true value of the fixed parameter.  The more sampling distributions there are, the less the error will be of the statistics that describe them.  A confidence interval can then be created that states "with x% confidence the actual mean of the population lies between A and B".  Probability is thus more tied to the frequency of different samples (thus the name Frequentists), the more samples taken the more accurate the confidence interval that contains the true mean.  There is no inital or past belief of what the parameter might have been for Frequentists, their analysis of the parameter is simply based on current sampling.  The parameter is fixed (unknown but fixed) but the data can be variate as many different sampling distributions are created.  Probabilities are then derived from these distributions to create the confidence intervals.

The Bayesian approach, however, treats the parameter itself as variate with the data fixed, with probabilities derived from the sample that attempt to pinpoint the range of the parameter.  The Bayesians start with a prior belief of what the parameter ought to be (i.e. if trying to find the mean of adult men's heights, prior knowledge that the mean is somewhere between 66 and 74 inches should be used) and then adjust that prior knowledge with results from the current experiment and analysis.  Then an actual probability is derived for what the statistic ought to be given both the past and current information.  So while a Frequentist might say "I have 95% confidence that the population statistic is between A and B", a Bayesian would say "There is a 95% probability that the population statistic is between A and B".  This is a subtle but important difference in how each school approaches statistical problems.


---

## <a name="section-e"></a>5.  Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

### Q7. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

### Q8. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

### Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
### Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
### Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

---

## <a name="section-f"></a>6.  Recommended Reading

Read Allen Downey's [Think Bayes](http://greenteapress.com/thinkbayes/) book.  It is available online for free, or you can buy a paper copy if you would like.

[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/) 

---

## <a name="section-g"></a>7.  More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.
