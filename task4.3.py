import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import csv
from sklearn.metrics import mean_absolute_error , r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC





df = pd.read_csv("WeatherHistory.csv")
numerical_features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
numerical_features.remove('Temperature (C)')  # Remove the target variable if it's numerical
df = df.sort_values(by='Formatted Date', ascending=True)#sortting
X = df[numerical_features]
y = df['Temperature (C)']

# Handle missing values (if any)
#X.fillna(X.mean(), inplace=True)

# Normalize or standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



#Split the dataset into training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




regressors ={
    'Linear Regression':LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'K-Nearest Neighbors':KNeighborsRegressor(n_neighbors=5),
    'Random Forest':RandomForestRegressor(random_state=42),
 'Gradiant Boosting':GradientBoostingRegressor(random_state=42),
}
results=[]
for name, reg in regressors.items():
    reg.fit(X_train,y_train)
    y_pred= reg.predict(X_test)
    mae = mean_absolute_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)

plot_results = pd.DataFrame(results,columns=['Regressor','mae','r2'])
def plot_results(results):
    plt.figure(figsize=(10,6))
    plt.bar(results['Regressor'],results['mae'])
    plt.xlabel('Regressor')
    plt.ylabel('Mean Absolute Error')
    plt.title('Comparison of Regression Models')
    plt.xticks(rotation=45)
    plt.show()
#Choose a machine learning algorithm and train the model:
# Using RandomForestClassifier for classification
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
# error percentage
mAe = mean_absolute_error(y_test, y_pred)
print(f'Mean ABS Error: {mAe}')

plt.plot(X_test,y_test,color='red', label='real temperature')
plt.show()

plt.plot(X_test,y_pred,color='green', label='predected temperature')
plt.show()