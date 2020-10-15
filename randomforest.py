#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#download housing dataset from kaggle
data = pd.read_csv('housing.csv')

data.dropna(inplace=True)
data.head()

import seaborn as sns
sns.heatmap(data.corr(),vmin=0.1,vmax=0)

x = data.iloc[:,[1,3,5,7,-3]].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1, random_state=44,n_jobs=-1)

# n_estimators are the number of trees in the forest
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)

plt.plot(y_train[:len(y_pred)],color='blue')
plt.plot(y_pred,color='red')
plt.show()
regressor.score(x_test,y_test)
