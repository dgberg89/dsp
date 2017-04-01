import re
import csv
import pandas as pd
    
Faculty = pd.read_csv('faculty.csv')
Faculty.shape

#Part 1, Question 1
Faculty = Faculty.rename(columns = {'name' : 'Name', ' degree' : 'Degree', ' title' : 'Title', ' email' : 'Email'})
#For stripping '.' and ' ', there are a few methods:
#Using lambda and strip, only first '.' is stripped so not good enough:
#Faculty[' degree'] = Faculty[' degree'].apply(lambda x: x.strip('.'))
#Below line works but I'm unclear on the regex and inplace syntax in the middle:
#Faculty['Degree'].replace(regex=True,inplace=True,to_replace=r'\.',value=r'')
#The below lines work and make sense to me:
Faculty['Degree'] = Faculty['Degree'].str.replace(r'\.', '')
Faculty['Degree'] = Faculty['Degree'].str.replace(r'\d+', '')
Faculty['Degree'] = Faculty['Degree'].str.replace(r' ', '')
Faculty['Degree'].unique()

Faculty.groupby('Degree').count()

print(Faculty[Faculty['Degree'].str.contains('PhD')].count())
print(Faculty[Faculty['Degree'].str.contains('ScD')].count())
print(Faculty[Faculty['Degree'].str.contains('MD')].count())
print(Faculty[Faculty['Degree'].str.contains('MPH')].count())
print(Faculty[Faculty['Degree'].str.contains('BSEd')].count())
print(Faculty[Faculty['Degree'].str.contains('MS')].count())
print(Faculty[Faculty['Degree'].str.contains('JD')].count())
print(Faculty[Faculty['Degree'].str.contains('MA')].count())

#Part 1, Question 2
Faculty['Title'].unique()
Faculty['Title'] = Faculty['Title'].str.replace(r' is ', ' of ')
Faculty['Title'].unique()

Faculty.groupby('Title').count()

#Part 1, Question 3
email_list = Faculty['Email'].tolist()
print(email_list)

#Part 1, Question 4
Faculty[['Email_User_Name', 'Email_Domain']] = Faculty['Email'].str.rsplit('@', expand=True, n=1)
Faculty['Email_Domain'].unique()
