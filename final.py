import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
student_df=df.loc[df['student_id']=="TRL_987"]

print(student_df.groupby('level')['attempt',as_index=False].mean())


fig = px.scatter( 
    x=student_df.groupby('level')['attempt',as_index=False].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],

    size="attempt",
    color="attempt",
    size_max=60)


fig.show()