from pandas import DataFrame
from sklearn import linear_model
import matplotlib.pyplot as plt
import statsmodels.api as sm
my_data = {'Fertilizer': [100,200,300,400,500,600,700],
           'Rainfall': [10, 20, 10, 30, 20, 20, 30],
           'Yield': [40, 50, 50, 70, 65, 65, 80]
           }
df = DataFrame(my_data,columns=['Fertilizer','Rainfall','Yield'])

print (df)
plt.scatter(df['Fertilizer'], df['Yield'], color='red')
plt.title('Fertilizer Vs Yield', fontsize=14)
plt.xlabel('Fertilizer', fontsize=14)
plt.ylabel('Yield', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['Rainfall'], df['Yield'], color='green')
plt.title(' RainFall Vs Yield', fontsize=14)
plt.xlabel('RainFall', fontsize=14)
plt.ylabel('Yield', fontsize=14)
plt.grid(True)
plt.show()


X = df[['Fertilizer','Rainfall']]
Y = df['Yield']
reg = linear_model.LinearRegression()
reg.fit(X, Y)
print('Intercept: \n', reg.intercept_)
print('Coefficients: \n', reg.coef_)
predictions = reg.predict(X)
print('predictions: \n', predictions)

X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)




