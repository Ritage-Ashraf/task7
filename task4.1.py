import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import seaborn as sns
df = pd.read_csv("Weather Dataset.csv")
# Check for missing values
missing_values = df.isnull().sum()

# Remove duplicates
df = df.drop_duplicates()

# Convert the 'Formatted Date' column to datetime
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], errors='coerce')

# Recheck for missing values after conversion
missing_values_after = df.isnull().sum()
#sorting 
df = df.sort_values(by='Formatted Date', ascending=True)

plt.plot(df ['Formatted Date'], df ['Temperature (C)'] ,marker='o',ms=1 ,color='red')
plt.xlabel('time')
plt.ylabel('temperature')
plt.title('My plot')
plt.ylim(-15,35)
plt.show()

# histogram
plt.hist(df['Temperature (C)'] ,edgecolor='black',bins=(-10,0,10,20,30,40))
plt.title('Temperature Distribution')
plt.ylabel('Time')
plt.show()

plt.scatter(df['Apparent Temperature (C)'],df ['Humidity'])
plt.xlim(-15,35)
plt.ylim(0.25,1)
plt.show()


# Plot the heatmap
#heatmap
num_df = df.iloc[:,3:11]
corr = num_df.corr()
sns.heatmap(corr,cmap ='crest' , linewidth = 0.5 ,annot = True)
plt.show()