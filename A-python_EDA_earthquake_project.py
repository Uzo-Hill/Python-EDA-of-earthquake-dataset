#!/usr/bin/env python
# coding: utf-8

# # PYTHON PROJECT : EDA OF THE EARTHQUAKE DATASET
# 
# 
# 

# # Introduction:
# 
# Earthquakes are natural disasters that can cause significant damage to infrastructure and pose a threat to human lives. The study of earthquakes and their patterns is crucial for understanding their behavior, predicting future occurrences, and implementing effective mitigation strategies. With the availability of large earthquake datasets, exploratory data analytics using Python can play a vital role in uncovering valuable insights and patterns within the seismic data.
# 
# # Problem Statement
# 
# The objective of this project is to perform an exploratory data analytics on the earthquake dataset records between the year 1969 to 2018 and with magnitude 5.5 and greater. By leveraging Python's data analysis and visualization libraries, we aim to gain a comprehensive understanding of the earthquake patterns. Therefore, we have these tasks:
# 
# 1. What's the total number of earthquakes recorded?
# 2. What is the relationship between the earthquake magnitudes and depths, and how does it impact our understanding of the earthquake events?
# 3. What are the 10 largest earthquakes from 1969 - 2018?
# 4. Find how many times each category of the earthquake occurred?
# 5. Fetch the records for all aftershocks within a week of the initial earthquake for the top most great earthquake?
# 6. Find the count of the distinct cause of the earthquakes over the years?
# 7. Fetch the records where the earthquakes were caused by 'explosion' only with respect to the place, magnitude and year occurred?
# 8. Which years have the highest number of earthquake recorded?
# 9. Find the most recent earthquake caused by nuclear explosion?
# 10. Find the places with the highest record of earthquake occurrrence?
# 
# 

# In[ ]:





# ### Importing python libraries

# In[1]:


# Importing the necessary python libraries for our project

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# In[ ]:





# ### Importing the earthquake dataset

# In[2]:


# Importing the earthquake dataset

earthquake = pd.read_csv(r'C:\Users\DELL\Desktop\DATASETS\earthquake dataset.csv')


# ### EXPLORING THE DATASET

# In[3]:


# To display the top 5 rows


earthquake.head(5)


# In[ ]:





# In[4]:


# To display the last 5 rows of the data


earthquake.tail(5)


# In[5]:


# How many rows and columns are in the earthquake data?

earthquake.shape


# In[6]:


# Names of the dataset columns

earthquake.columns


# In[7]:


# to see statistics of the numerical columns in the dataset


earthquake.describe().T


# In[8]:


# to see all the information of columns in dataset

earthquake.info()


# In[ ]:





# ## DATA CLEANING AND TRANSFORMATION

# #### 1. We'll convert the 'occurred_on' column to datetime datatype

# In[9]:


# Converting the 'occurred_on' column to datetime dtype

earthquake['occurred_on'] = pd.to_datetime(earthquake['occurred_on'])


# In[10]:


earthquake.info()      # occurred_on column successfully converted to datetime format.


# #### 2. Extracting date, year, month_name and time columns from the 'occurred_on' column.

# In[11]:


earthquake['date'] = earthquake['occurred_on'].dt.date   # Extracting date column

earthquake['year'] = earthquake['occurred_on'].dt.year   # Extracting year column

earthquake['month_name'] = earthquake['occurred_on'].dt.month_name()  # Extracting month_name column

earthquake['time'] = earthquake['occurred_on'].dt.time  # Extracting time column


earthquake.head(1)


# #### 3. Creating a new column that would categorise the earthquakes based on their magnitude

# In[12]:


# Step1: Creating a function to categorise the earthquakes based on their magnitude

def magnitude(magnitude) :
    if magnitude >=8.0:
        return "Great earthquake"
    elif magnitude >= 7.0:
        return "Major earthquake"
    elif magnitude >= 6.0:
        return "Strong earthquake"
    else:
        return "Moderate earthquake"
    
    
# step2: Creating a new column containing the above categorisation function using the apply method.

earthquake['quake_category'] = earthquake['magnitude'].apply(magnitude)


# In[13]:


earthquake.head(2)      # New column 'quake_category' successfully created


# From the above codes, a new column 'quake_category' that categorised the earthquakes into **great, major, strong, and moderate** earthquakes has been created successfully.

# #### 4. Checking for missing values

# In[14]:


# Checking for missing values


earthquake.isnull().sum()


# The above result show that there are no missing or null values in our dataset.

# #### 5. Checking for duplicates

# In[15]:


# checking if any duplicate data present in the dataset

earthquake[earthquake.duplicated()]   # No duplicate was found in the dataset


# #### 6. Checking for outliers using the statistics method.

# In[16]:


# Checking for outlier

earthquake.describe()[['year', 'magnitude']]


# The min and max value for both the year the earthquakes occurred on and the magnitude agrees with that described in the original data, hence, no outlier was found.
# 
# Also standard deviation of 0.42 indicates that the magnitudes of the earthquakes tend to cluster relatively close to the mean value.
# 

# In[ ]:





# ### DATA ANALYSIS

# #### 1. What's the total number of earthquakes recorded?

# In[17]:


# Total number of earthquakes recorded.

Total_number = earthquake['earthquake_id'].nunique()

print(f" A total of {Total_number} earthquakes of magnitude 5.5 or greater were recorded between the year 1969 - 2018.")


# In[ ]:





# #### 2. What is the relationship between the earthquake magnitudes and depths, and how does it impact our understanding of the earthquake events?¶ 

# In[38]:


# Investigate the relationship between the earthquakes magnitudes and depths using a scatter plot.


# Select the 'Magnitude' and 'Depth' columns
data = earthquake[['magnitude', 'depth']]

# Calculate the correlation coefficient
corr_coef = np.corrcoef(data['magnitude'], data['depth'])[0, 1]

# Plot a scatter plot
plt.scatter(data['magnitude'], data['depth'])
plt.xlabel('magnitude')
plt.ylabel('depth')
plt.title('Correlation between magnitude and depth (Correlation Coefficient: {:.2f})'.format(corr_coef))

plt.show()


# The positive sign of the correlation coefficient suggests that there is a tendency for magnitudes and depths to increase together, albeit weakly.
# 
# The corr_coef of 0.03 indicates that the relationship between earthquake magnitudes and depths is quite scattered and does not exhibit a strong linear pattern.
# 

# In[ ]:





# #### 3. What are the 10 largest earthquakes from 1969 - 2018?  

# In[22]:


# Top 10 largest earthquake 

largest_earthquake =earthquake.sort_values(by='magnitude',ascending=False) [['place','magnitude','cause','date']].head(10)

largest_earthquake


# #### Visualising 

# In[23]:


# Visualising the top 10 largest earthquakes using horizontal bar plot

sns.set(rc={'figure.figsize': (11, 6)})
sns.barplot(data=largest_earthquake, y='place', x='magnitude', color='darkblue')
plt.xlabel('magnitude', fontsize=16)
plt.ylabel('Place',fontsize=16)
plt.title('Top 10 Largest Earthquakes', fontsize=18)

# Display the chart
plt.show()


# The filtered dataframe and chart above shows the 10 largest 'great earthquakes' with the 9.1 magnitude near the coast of Japan the joint largest
# 
# alongside the 9.1 magnitude off the coast of Indonesia, which caused the devastating boxing day tsunami in 2004.
# 

# In[ ]:





# #### 4. Find how many times each category of the earthquake occurred? 

# In[24]:


# Calculate count and percentage

count = earthquake['quake_category'].value_counts()

percentage = earthquake['quake_category'].value_counts(normalize=True) * 100

# Create a new dataframe to store the results
result_earthquake = pd.DataFrame({'Count': count, 'Percentage': percentage})

# Print the result dataframe
 
print(result_earthquake)

# To visualise, we need to:
# 1. Reset index of result_earthquake to make 'quake_category' a column
result_earthquake = result_earthquake.reset_index()

# 2. Rename the columns for clarity
result_earthquake.columns = ['quake_category','count', 'Percentage']

# Plot a bar chart
plt.figure(figsize=(8, 6))
ax = sns.barplot(x='quake_category', y='Percentage', data=result_earthquake)
plt.xlabel('quake_category')
plt.ylabel('Percentage')
plt.title('Percentage of quake_category')

# Add data values to the bar plot
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, height, f'{height:.2f}%', ha='center')


plt.show()


# A total of 40 (0.17%) great earthquake was recorded.
# 
# Also, a total of 665 (2.88%) major earthquakes was recorded between 1969 - 2018.
# 

# In[ ]:





# #### 5. Find the records for all aftershocks within a week of the initial earthquake for the top most great earthquake?

# In[25]:


#Filter all aftershocks within a week of the initial 9.1 earthquake off the west coast of northern Sumatra on Dec 26th,2004.
# excludes the mainshock epicenter event.

aftershocks_df = earthquake[(earthquake['place'].str.contains("northern Sumatra")) & 
                 (earthquake['occurred_on'] > pd.to_datetime('2004-12-26 00:58:00')) & 
                 (earthquake['occurred_on'] <= pd.to_datetime('2005-01-02'))][['place', 'magnitude', 'occurred_on']]



aftershocks_df.head(10)    # A total of 28 aftershocks one week after the mainshock epicenter


# In[26]:


# Using the len() function to count the record of all aftershocks within a week of the December 26th,2004 
# earthquake off the west coast of Northern Sumatra, Indonesia.

record_count = len(aftershocks_df)

print(f"A total of {record_count} aftershocks occurred within a week of the initial 9.1 earthquake off the west coast of northern Sumatra, Indonesia.")


# In[ ]:





# #### 6. Find the count of the distinct cause of the earthquakes over the years?

# In[27]:


# Count of the earthquakes causes
cause_count = earthquake['cause'].value_counts().sort_values(ascending=False)
print(cause_count)

# Visualizing
sns.set(font_scale=1.4)
ax = cause_count.plot(kind='bar', figsize=(7, 6), rot=0, color="red")
plt.xlabel("Cause", labelpad=14)
plt.ylabel("Count of Causes", labelpad=14)
plt.title("Count of Distinct Earthquake Cause", y=1.02)

# Adding data value labels
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

plt.show()


# Majority of the earthquakes were caused by the earth's tectonic activities i.e by natural earthquake with a count of 22942 (99.23%).

# In[ ]:





# #### 7. Fetch all records where the earthquakes were caused by 'explosion' only?

# In[28]:


# Records where the earthquakes were caused by 'explosion' only.

cause_by_explosion = earthquake.loc[earthquake['cause'] == 'explosion', ['place', 'year', 'magnitude']]


cause_by_explosion


# All 4 earthquakes caused by **'explosion'** only were all moderate earthquakes, 2 in France and 2 at the former Soviet Union.

# In[ ]:





# #### 8. Which years have the highest number of earthquake recorded?

# In[29]:


earthquake_by_year =earthquake.groupby(['year']).size().reset_index(name='count').sort_values(by='count',ascending=False).head(10)

earthquake_by_year


# #### Visualising

# In[30]:


plt.figure(figsize=(12, 6))
sns.set(font_scale=1.4)

# Create a horizontal bar chart
ax = sns.countplot(data=earthquake, orient="h", y="year", color="skyblue",
                   order=earthquake['year'].value_counts().iloc[:10].index)

# Add data value labels to the bars
for p in ax.patches:
    width = p.get_width()
    plt.text(width + 18, p.get_y() + p.get_height() / 2, f'{int(width)}', ha='center', va='center')

plt.title("Top 10 Earthquakes by Year", y=1.02)

# Remove grid lines
plt.grid(visible=False)

plt.show()


# In the above horizontal bar plot, it is evident that the year **2011** has the most record of earthquake occurrence.

# In[ ]:





# #### 9. Find the most recent earthquake caused by nuclear explosion?

# In[31]:


get_ipython().set_next_input('what is the most recent earthquake caused by nuclear explosion');get_ipython().run_line_magic('pinfo', 'explosion')

nuclear_explosion = earthquake.loc[earthquake['cause'] == 'nuclear explosion', 
                                  ['place','magnitude', 'occurred_on']].sort_values(by='occurred_on', ascending = False).head(1)

nuclear_explosion


# In[ ]:





# #### 10. Find the places with the highest record of earthquake occurrrence?

# In[36]:


# Group the data by the 'place' column and count the occurrences
region_counts = earthquake.groupby('place').size().sort_values(ascending=False).head(20)


region_counts


# #### Visualising earthquake occurrence by region

# In[37]:


# Visualize the earthquake occurrences by regions using a bar chart

plt.figure(figsize=(10, 6))
region_counts.plot(kind='bar', width=0.8)

plt.xlabel('Region')
plt.ylabel('Number of Earthquakes')
plt.title('Earthquake Occurrences by Region')

# Remove grid lines
plt.grid(visible=False)

plt.xticks(rotation=90, fontsize=12)  # Adjust the font size of x-axis tick labels

plt.show()


# The bar chart shows that Vanuatu, Fiji region, Tonga are the leading regions with a relatively high number of earthquake occurrences.
# 
# This suggests that these regions experiences a significant amount of seismic activity.
# 

# In[ ]:





# ### Conclusion

# his python exploratory data analysis project has provided valuable insights into the earthquake dataset of magnitude 5.5+ and spanning from 1969 to 2018. By leveraging Python's libraries such as pandas, numpy, matplotlib,seaborn and the Jupyter notebooks, we were able to gain a deeper understanding of the seismic activity during this extensive time period.
# 
# Throughout the analysis, we explored various aspects of the dataset, including the frequency, categories based on the magnitude of the earthquakes and their geographical distribution. We observed that the dataset contains a wide range of earthquake magnitudes, with some exceptionally strong events occurring over the years.
# 
# Geographically, we found that earthquakes are not evenly distributed around the world. Certain Oceania regions, such as Vanuatu, Fiji region, Tonga, Papua New Guinea,Solomon Island and asian regions such as Japan, Indonesia experienced a higher concentration of seismic activity. This information can be crucial for disaster preparedness and risk assessment in vulnerable areas.
# 
# We also investigated the earthquake causes and potential correlations between the earthquakes magnitudes and depth.Further research could be conducted to explore other relationships such as geological phenomena, climate factors, or other external variables in more detail.
# 
# This earthquake dataset project serves as a foundation for further investigations, such as predictive modeling or advanced statistical analyses. By continuing to explore and analyze earthquake datasets, we can make significant strides in mitigating the impact of earthquakes and ensuring the safety and well-being of communities worldwide.

# In[ ]:





# ### Reference

# - Socratica. (2019, March 4). SQL SELECT Tutorial-Part 2: SQL Tutorial for Beginners [https://youtu.be/PkJKzR_sClM]. YouTube. https://www.youtube.com/watch?v=PkJKzR_sClM

# In[ ]:




