#!/usr/bin/env python
# coding: utf-8

# # Weather Data Analysis
# 

# ![weather.jpg](attachment:weather.jpg)

# ## Introduction: Weather Data Analysis
# Weather refers to short-term atmospheric conditions of a region and can include indicators such as minimum/maximum temperature, humidity, or wind speed. Climate is the weather of a region averaged over a long period of time. Climate data covers details such as seasonal average temperatures or decade-long patterns of rains and contributes to climate prediction.
# 
# Weather data provides information about the weather and climate of a region. It tracks patterns and predicts trends.
# 
# Weather analysis begins with the observation and administration of the current state of the atmosphere,
# ocean, and land surface. Thus, many platforms, including
# satellites, radar, weather balloons, surface stations, and aircraft (both crewed and
# uncrewed) are crucial for generating reliable observations from accurate analyses.
# 
# Weather data is tremendously important to agriculture and infrastructure planning. Various industries use weather data for real-world business cases, such as travel planning, demand forecast, and supply chain management. The easy availability of weather data for practically any region makes it possible to incorporate it in diverse analytical cases.

# ## Objective
# The major objective of this Exploratory Data Analysis by Visualization is to examine historical weather data to extract insights and patterns, which include analyzing Temperature trends, Weather patterns, Wind speeds frequency, Relative Humidity and more.

# ### The Key Analysis Components
# 
# **Frequency Distribution:** This is conducted to observe and juxtapose the weather factor frequencies for each period of the year, especially when intensifying and when it is less pressurizing.
# 
# **Weather Situation:** This is conducted to reveal and study each weather/atmospheric situation with respect to the temperature and relative humidity as regards specific period/month of the year in order to mitigate the defaults that arises as the weather situation changes each period.

# ### Environment Set up

# In[1]:


# Import the packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Import csv file to read the data 

weather=pd.read_csv('Weather Data.csv')
weather


# ### Data Exploration

# In[3]:


# Check for the data details

weather.info()


# In[4]:


# Check for the data number of columns and rows

weather.shape


# In[5]:


# Check for the data index

weather.index


# In[6]:


# Check for the data Variables

column = weather.columns
for columns in column:
    print("~",columns)


# In[7]:


# Check for Null values

weather.isnull().sum()


# In[8]:


# Check for the data variable types

weather.dtypes


# In[9]:


# Check for; to familiarize with the Unique values for the variable "Weather"

Weather_Conditions= weather['Weather'].unique()
for Weather in Weather_Conditions:
    print("~",Weather)


# ### Data Processing

# In[10]:


# Rename specific columns for consistency

weather.rename(columns={'Rel Hum_%': 'Relative Humidity_%', 'Weather': 'Weather Situation'}, inplace=True)
weather


# In[11]:


# Format the "Date/Time" Variable to create new columns "Year" and "Month"
weather['Date/Time'] = pd.to_datetime(weather['Date/Time']).replace('Date/Time')

# Extract and create new columns for "Year" and "Month"
weather['Year'] = weather['Date/Time'].dt.year
weather['Month'] = weather['Date/Time'].dt.month
weather


# ### Exploratory Data Analysis/Visualization by Frequency Distribution

# In[12]:


# Relative Humidity Frequency Distribution over the Year

plt.figure(figsize=(10, 4))
sns.histplot(weather['Relative Humidity_%'], color='skyblue')
plt.title('Relative Humidity Dsitribution')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.show()


# In[13]:


# Temperature Frequency Distribution over the Year

plt.figure(figsize=(10, 4))
sns.histplot(weather['Temp_C'], color='skyblue')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.show()


# In[14]:


# Wind Speed Frequency Distribution over the Year

plt.figure(figsize=(12, 6))
sns.histplot(weather['Wind Speed_km/h'], color='skyblue')
plt.title('Wind Speed Distribution')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Frequency')
plt.show()


# #### Report:
# - the Relative Humidity has a high intensity and more frequent at 60 to 80 percentage within the year
# - the Temperature level is more consisted within the range of -5_C and 25_C, while the other temperature degrees occur for lesser period in the year
# - the Wind Speed has its way built up and more intensifying within 0_km/h to 20_km/h
# 

# ### Exploratory Data Analysis/Visualization by Weather Situation

# In[15]:


# Extract to analyze the data by the Weather Situation and Date/Time

weather_situation = weather[['Weather Situation', 'Date/Time']]
weather_situation


# In[16]:


# Observe the Weather Situation rate by the over all hours of the year

weather_group = weather_situation.groupby(['Weather Situation']).count().sort_values(['Date/Time'], ascending=False)
weather_group


# ANALYZING THE WEATHER SITUATION BASED ON THE RELATIVE HUMIDITY AND THE PERIOD (MONTH) OF THE YEAR

# **Weather Situation/Period when Humidity is Low:**

# In[17]:


# LOW HUMIDITY

low_humidity = weather[weather['Relative Humidity_%'] <= 25]
sns.countplot(x='Weather Situation', data=low_humidity)
plt.show()


# In[18]:


# The Period of the Year

sns.countplot(x='Month', data=low_humidity)
plt.show()


# **Report:** The weather situation is mostly clear, and then partially cloudy within the 
#             months of march-june when the Relative Humidity is less than 25%

# **Weather Situation/Period when Humidity is Fair:**

# In[19]:


# FAIR HUMIDITY

fair_humidity = weather[(weather['Relative Humidity_%'] > 25) & (weather['Relative Humidity_%'] <=60)]
fair_hum_plot = sns.countplot(x='Weather Situation', data=fair_humidity)
fair_hum_plot.set_xticklabels(fair_hum_plot.get_xticklabels(), rotation=45)
plt.show()


# In[20]:


# The Period of the Year

sns.countplot(x='Month', data=fair_humidity)
plt.show()


# **Report:** There is quite both the clear and cloudy weather when the humidity is at the fair level. 
#             However, these seem to occur all through the year, but most effectful within the months of march-july when the Relative Humidity is between 25% and 60%

# **Weather Situation/Period when Humidity is High:**

# In[21]:


# HIGH HUMIDITY

high_humidity = weather[(weather['Relative Humidity_%'] >= 60) & (weather['Relative Humidity_%'] <= 70)]
high_hum_plot = sns.countplot(x='Weather Situation', data=high_humidity)
high_hum_plot.set_xticklabels(high_hum_plot.get_xticklabels(), rotation=90)
plt.show()


# In[22]:


# The Period of the Year

sns.countplot(x='Month', data=high_humidity)
plt.show()


# **Report:** The weather situation is mostly cloudy, yet averagely clear when the humidity level is high, and this happens mostly during the early period if the year, the mid and partly towards the end of the way when the Relative Humidity is between 60% and 70%

# **Weather Situation and Period when the Humidity is Very High:**

# In[23]:


# VERY HIGH HUMIDITY

very_high_humidity = weather[(weather['Relative Humidity_%'] >= 70) & (weather['Relative Humidity_%'] <=100)]
plt.figure(figsize=(10, 4))
vhigh_hum_plot = sns.countplot(x='Weather Situation', data=very_high_humidity)
vhigh_hum_plot.set_xticklabels(vhigh_hum_plot.get_xticklabels(), rotation=90)
plt.show()


# In[24]:


# The Period of the Year

sns.countplot(x='Month', data=very_high_humidity)
plt.show()


# **Report:** The Humidity level is visible in the early months of the year, while it is mostly intensified towards the end of the year, mostly due to the winter.

# ANALYZING THE WEATHER DATA BASED ON THE TEMPERATURE (TEMP_C) AND THE PERIOD (MONTH) OF THE YEAR

# In[25]:


# COLD TEMPERATURE

cold_temperature = weather[weather['Temp_C'] <= 10]
sns.countplot(x='Month', data=cold_temperature)
plt.show()


# In[26]:


# LOW TEMPERATURE

low_temperature = weather[(weather['Temp_C'] >= 10) & (weather['Temp_C'] <= 20)]
sns.countplot(x='Month', data=low_temperature)
plt.show()


# In[27]:


# FAIR TEMPERATURE

fair_temperature = weather[(weather['Temp_C'] >= 20) & (weather['Temp_C'] <= 30)]
sns.countplot(x='Month', data=fair_temperature)
plt.show()


# In[28]:


# HIGH TEMPERATURE

high_temperature = weather[(weather['Temp_C'] >= 30) & (weather['Temp_C'] <= 40)]
sns.countplot(x='Month', data=high_temperature)
plt.show()


# ## Conclusion
# - The Exploratory Data Analysis (EDA) of the weather dataset unveiled several significant insights into the atmospheric conditions over the specified period. Through a combination of juxtapositions, measurements and visualizations, we have gained a deeper understanding of different weather patterns each with respect to its responsible factor. 
# - Also, about the Weather temporal patterns; the temperature analysis shows the variance in temperate range with respect to a given period (month) of the year which in the long run alters the relative humidity, as well the weather atmospheric situation at each given period, thus allowing us to identify the frequency and duration of specific atmospheric states. 
# - Instances of cloudy/clear skies, snowy conditions and foggy weather patterns were explored, thereby enhancing our ability to anticipate and prepare for specific weather phenomena, contributing to improved decision-making.

# ## Implication
# - Weather Data Analysis are important because they are used to protect lives and property by deriving forecasts. Forecasts based on temperature and precipitation are important to agriculture, and therefore to traders within commodity markets. 
# - Also, Temperature forecasts are used by utility companies to estimate demand over coming days, supply chain management and customer demand planning — to ensure that the right product is at the right place at the right time.

# ## Limitation
# The atmospheric system, Unlike the tides and the orbit of planets, has an intrinsic limit that represents a natural and ultimate boundary beyond which prediction is no longer possible. Also, weather forecasting relies on Numerical Weather Prediction (NWP) models that simulate the atmosphere's behavior based on mathematical equations. However, these models have limitations in representing small-scale features, such as local wind patterns, precipitation, and atmospheric turbulence.
