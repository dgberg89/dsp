import pandas as pd
    
Faculty = pd.read_csv('faculty.csv')
Faculty = Faculty.rename(columns = {'name' : 'Name', ' degree' : 'Degree', ' title' : 'Title', ' email' : 'Email'})
Faculty['Email'].to_csv('emails.csv', index=False)
