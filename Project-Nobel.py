import pandas as pd
import seaborn as sns
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# THAT İS A PROJECT ABOUT NOBEL PRİZES

# 1
nobel = pd.read_csv(r"C:\Users\PC\Desktop\nobel.csv.txt")
# 2
display("Num of Prizes", len(nobel))
display("Prizes won by sex", nobel['sex'].value_counts())
print("Prizes most won countries",
      (nobel['birth_country'].value_counts().sort_values(ascending=False)).head(10))
# 3

nobel['usa_born_winner'] = nobel['birth_country'] == "United States of America"
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)[
    'usa_born_winner'].mean()
print(prop_usa_winners)
# 4

sns.set()
plt.rcParams['figure.figsize'] = [11, 7]
ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)
ax.yaxis.set_major_formatter(PercentFormatter())
# plt.show()
# 5
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)[
    'female_winner'].mean()
# Plotting USA born winners with % winners on the y-axis
plt.rcParams['figure.figsize'] = [11, 7]
ax = sns.lineplot(x='decade', y='female_winner',
                  data=prop_female_winners, hue='category')
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
# 6
# Method1
print(nobel[nobel.sex == 'Female'].nsmallest(1, 'year'))
# Method2
print(nobel[nobel['female_winner']][['category', 'year']].head(1))
print(nobel[nobel['female_winner']][['full_name', 'category', 'year']].head(1))
# 7
prizesnoone=nobel.groupby('full_name').filter(lambda group: len(group)>=2)
print(prizesnoone)
#print(prizesnoone[['full_name','prize']]) # kimler ve ödülleri tek görmek istedim.
#8

# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
nobel['age']=nobel['year']-nobel['birth_date'].dt.year
print(nobel['age'])
sns.lmplot(x='year',y='age',data=nobel,lowess=True,aspect=2,line_kws={'color':'black'})
#plt.show()
#9
sns.lmplot(x='year',y='age',data=nobel,row='category')
#plt.show()
#10

enyaslı=nobel.nlargest(1,'age')
engenc=nobel.nsmallest(1,'age')
print(enyaslı)
display(engenc)
#11

