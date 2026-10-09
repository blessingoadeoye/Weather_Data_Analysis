
#!/usr/bin/env python
# coding: utf-8

"""
====================================================================
WEATHER DATA ANALYSIS
EXPLORATORY DATA ANALYSIS AND VISUALIZATION
====================================================================

PROJECT OBJECTIVE

This project explores historical weather observations to identify
patterns in temperature, relative humidity, wind speed, and
recorded atmospheric conditions.

The investigation focuses on two main analytical components:

1. FREQUENCY DISTRIBUTION
   Examine the frequency of weather measurements to identify
   the ranges that occur most often.

2. WEATHER SITUATION
   Examine recorded atmospheric conditions across different
   humidity levels and periods of the year.

   Monthly temperature patterns are also investigated to
   understand how temperature ranges vary over time.

WORKFLOW STRUCTURE

    1. Environment Setup
    2. Initial Data Exploration
    3. Data Preparation
    4. Weather Variable Frequency Distributions
    5. Weather Situation Frequency
    6. Weather Situations by Humidity Level
    7. Monthly Temperature Analysis
    8. Analytical Conclusions

The workflow follows a progressive analytical approach:

    Inspect -> Prepare -> Analyze -> Interpret

====================================================================
"""


# ==================================================================
# STAGE 1 — ENVIRONMENT SETUP
# ==================================================================

"""
OBJECTIVE

Import the libraries required for data manipulation,
exploration, and visualization.

TOOLS

Pandas:
    Data loading, inspection, manipulation, and aggregation.

Matplotlib:
    Chart formatting and visualization.

Seaborn:
    Statistical plots and categorical comparisons.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------------
# 1.1 — Load the Weather Dataset
# ------------------------------------------------------------------

"""
APPROACH

Import the source CSV into a Pandas DataFrame.

The resulting DataFrame provides the foundation for the
subsequent inspection, preparation, and analysis.
"""

weather = pd.read_csv("Weather Data.csv")

weather


# ==================================================================
# STAGE 2 — INITIAL DATA EXPLORATION
# ==================================================================

"""
OBJECTIVE

Understand the dataset's structure and available variables
before proceeding with the analysis.

The initial exploration examines:

    - Dataset information
    - Number of observations and columns
    - Index structure
    - Available column names
    - Missing values
    - Variable data types
    - Recorded weather situations

These checks establish familiarity with the source data
and help guide the preparation stage.
"""


# ------------------------------------------------------------------
# 2.1 — Inspect Dataset Information
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

What information is available in the dataset, and how are
the individual variables represented?

APPROACH

Use info() to inspect the column names, non-null counts,
and existing data types.
"""

weather.info()


# ------------------------------------------------------------------
# 2.2 — Examine Dataset Dimensions
# ------------------------------------------------------------------

"""
APPROACH

Inspect the number of rows and columns to understand the
size of the dataset.
"""

weather.shape


# ------------------------------------------------------------------
# 2.3 — Examine the DataFrame Index
# ------------------------------------------------------------------

"""
APPROACH

Inspect the index associated with the imported observations.
"""

weather.index


# ------------------------------------------------------------------
# 2.4 — Identify Available Variables
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which variables are available for the weather investigation?

APPROACH

List the source columns individually for inspection.
"""

for column in weather.columns:
    print("~", column)


# ------------------------------------------------------------------
# 2.5 — Examine Missing Values
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Do any variables contain missing observations?

APPROACH

Count the missing values in each column before performing
the weather analysis.
"""

weather.isnull().sum()


# ------------------------------------------------------------------
# 2.6 — Inspect Variable Data Types
# ------------------------------------------------------------------

"""
APPROACH

Review the current data types, particularly the Date/Time
variable, which will be used for monthly comparisons.
"""

weather.dtypes


# ------------------------------------------------------------------
# 2.7 — Identify Recorded Weather Situations
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which atmospheric conditions are represented in the dataset?

APPROACH

Extract the distinct values from the Weather column.

These descriptions will be used to investigate the frequency
of weather situations and their relationship with humidity.
"""

weather_conditions = weather["Weather"].unique()

for condition in weather_conditions:
    print("~", condition)


# ==================================================================
# STAGE 3 — DATA PREPARATION
# ==================================================================

"""
OBJECTIVE

Prepare the source variables for the exploratory analysis.

The preparation focuses on:

    1. Renaming selected columns for consistency.
    2. Converting the Date/Time field to datetime format.
    3. Extracting the year and month for temporal analysis.

The original analytical variables are retained.
"""


# ------------------------------------------------------------------
# 3.1 — Standardize Column Names
# ------------------------------------------------------------------

"""
APPROACH

Rename the selected columns to make their meaning clearer
throughout the analysis.
"""

weather.rename(
    columns={
        "Rel Hum_%": "Relative Humidity_%",
        "Weather": "Weather Situation"
    },
    inplace=True
)

weather.head()


# ------------------------------------------------------------------
# 3.2 — Convert Date/Time to Datetime Format
# ------------------------------------------------------------------

"""
ANALYTICAL PURPOSE

The weather observations need to be organized by calendar
period to investigate monthly patterns.

APPROACH

Convert the Date/Time column into a Pandas datetime field.
"""

weather["Date/Time"] = pd.to_datetime(
    weather["Date/Time"]
)


# ------------------------------------------------------------------
# 3.3 — Extract Year and Month
# ------------------------------------------------------------------

"""
APPROACH

Create separate Year and Month variables from Date/Time.

These fields support the analysis of weather situations,
humidity levels, and temperature ranges across the year.
"""

weather["Year"] = weather["Date/Time"].dt.year

weather["Month"] = weather["Date/Time"].dt.month

weather.head()


# ==================================================================
# STAGE 4 — WEATHER VARIABLE FREQUENCY DISTRIBUTIONS
# ==================================================================

"""
ANALYTICAL OBJECTIVE

Examine the distributions of three important weather
measurements:

    - Relative humidity
    - Temperature
    - Wind speed

The purpose is to identify which measurement ranges appear
most frequently in the recorded observations.

Histograms are used because they display how numerical
observations are distributed across value intervals.
"""


# ------------------------------------------------------------------
# 4.1 — Relative Humidity Frequency Distribution
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which relative humidity levels occur most frequently
throughout the recorded period?

APPROACH

Plot the frequency distribution of Relative Humidity_%.
"""

plt.figure(figsize=(10, 4))

sns.histplot(
    data=weather,
    x="Relative Humidity_%",
    color="skyblue"
)

plt.title("Relative Humidity Distribution")
plt.xlabel("Relative Humidity (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


"""
RESULT

The analysis identified relative humidity values
between approximately 60% and 80% as occurring more
frequently during the year.

INTERPRETATION

This concentration indicates that observations within the
60–80% humidity range were prominent in the recorded data.

The distribution provides a starting point for examining
how weather situations vary across humidity levels.
"""

# ------------------------------------------------------------------
# 4.2 — Temperature Frequency Distribution
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which temperature ranges appear most frequently in the
weather observations?

APPROACH

Use a histogram to examine the distribution of Temp_C.
"""

plt.figure(figsize=(10, 4))

sns.histplot(
    data=weather,
    x="Temp_C",
    color="skyblue"
)

plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


"""
RESULT

The analysis result shows that temperatures were more
frequently recorded between approximately -5°C and 25°C.

Temperature values outside this range occurred less
frequently in the dataset.

INTERPRETATION

The observations suggest that the recorded temperature
distribution was concentrated within a broad range
covering cold to moderately warm conditions.

Monthly comparisons are examined later to understand
when different temperature ranges were observed.
"""

# ------------------------------------------------------------------
# 4.3 — Wind Speed Frequency Distribution
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which wind-speed ranges are most common in the dataset?

APPROACH

Visualize the distribution of Wind Speed_km/h.
"""

plt.figure(figsize=(12, 6))

sns.histplot(
    data=weather,
    x="Wind Speed_km/h",
    color="skyblue"
)

plt.title("Wind Speed Distribution")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


"""
RESULT

The analysis result identified wind speeds between
approximately 0 and 20 km/h as occurring more frequently.

INTERPRETATION

The frequency distribution shows a greater concentration
of observations within the lower wind-speed range.

This helps describe the wind conditions represented
throughout the recorded period.
"""


# ------------------------------------------------------------------
# 4.4 — Frequency Distribution Summary
# ------------------------------------------------------------------

"""
KEY FINDINGS

Relative Humidity:
    More frequent observations around 60–80%.

Temperature:
    More frequent observations around -5°C to 25°C.

Wind Speed:
    More frequent observations around 0–20 km/h.

ANALYTICAL SIGNIFICANCE

Together, these distributions establish the commonly
observed ranges of three important atmospheric variables.

The next stage examines the recorded weather descriptions
rather than the numerical measurements alone.
"""


# ==================================================================
# STAGE 5 — WEATHER SITUATION FREQUENCY
# ==================================================================

"""
ANALYTICAL OBJECTIVE

Examine the occurrence of different atmospheric conditions
across the recorded observations.

The analysis groups weather descriptions and counts how
frequently each situation appears.

This provides an overview of the weather categories
represented in the dataset.
"""


# ------------------------------------------------------------------
# 5.1 — Extract Weather Situation Records
# ------------------------------------------------------------------

"""
APPROACH

Select the Weather Situation and Date/Time variables.

These fields allow the recorded weather descriptions
to be grouped and counted.
"""

weather_situation = weather[
    ["Weather Situation", "Date/Time"]
]

weather_situation


# ------------------------------------------------------------------
# 5.2 — Rank Weather Situations by Frequency
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which recorded weather situations occur most frequently?

APPROACH

Group observations by Weather Situation, count their
occurrences, and sort from highest to lowest.
"""

weather_group = (
    weather_situation
    .groupby("Weather Situation")
    .count()
    .sort_values(
        "Date/Time",
        ascending=False
    )
)

weather_group


"""
INTERPRETATION

This summary establishes the relative frequency of the
weather situations represented in the source records.

The next stage examines how these weather situations
are distributed across different humidity ranges.
"""


# ==================================================================
# STAGE 6 — WEATHER SITUATIONS BY HUMIDITY LEVEL
# ==================================================================

"""
ANALYTICAL OBJECTIVE

Investigate how recorded weather situations differ
across relative humidity levels.

This considers four humidity
categories:

    Low Humidity:
        25% or below

    Fair Humidity:
        Above 25% through 60%

    High Humidity:
        60% through 70%

    Very High Humidity:
        70% through 100%

For each category, two questions are examined:

    1. Which weather situations are most common?
    2. During which months are these observations recorded?

The analysis combines categorical weather descriptions
with calendar-month frequency comparisons.
"""


# ------------------------------------------------------------------
# 6.1 — Low Humidity: Weather Situations
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which weather situations are most frequently observed
when relative humidity is low?

APPROACH

Filter observations where relative humidity is at most
25%, then count the recorded weather situations.
"""

low_humidity = weather[
    weather["Relative Humidity_%"] <= 25
]

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Weather Situation",
    data=low_humidity
)

plt.title("Weather Situations at Low Humidity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 6.2 — Low Humidity: Monthly Distribution
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

During which months are low-humidity observations
recorded most frequently?
"""

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=low_humidity
)

plt.title("Monthly Frequency of Low Humidity")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


"""
RESULT

The analysis result found that clear and partly cloudy
conditions were most prominent during low humidity.

These observations were particularly evident between
March and June.

INTERPRETATION

The results describe an association between lower
relative humidity and clear or partly cloudy conditions
within the recorded observations.
"""


# ------------------------------------------------------------------
# 6.3 — Fair Humidity: Weather Situations
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

How do weather situations vary when relative humidity
falls within the fair-humidity range?

APPROACH

Select observations above 25% and up to 60% humidity.
"""

fair_humidity = weather[
    (weather["Relative Humidity_%"] > 25)
    & (weather["Relative Humidity_%"] <= 60)
]

plt.figure(figsize=(10, 4))

fair_humidity_plot = sns.countplot(
    x="Weather Situation",
    data=fair_humidity
)

fair_humidity_plot.set_xticklabels(
    fair_humidity_plot.get_xticklabels(),
    rotation=45,
    ha="right"
)

plt.title("Weather Situations at Fair Humidity")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 6.4 — Fair Humidity: Monthly Distribution
# ------------------------------------------------------------------

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=fair_humidity
)

plt.title("Monthly Frequency of Fair Humidity")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


"""
RESULT

The result identified both clear and cloudy
conditions within the fair-humidity range.

These conditions appeared across the year, with greater
frequency reported between March and July.

INTERPRETATION

Fair humidity was associated with a wider mixture of
recorded clear and cloudy weather situations.
"""


# ------------------------------------------------------------------
# 6.5 — High Humidity: Weather Situations
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which weather situations become more prominent at
higher relative humidity levels?

APPROACH

Select observations between 60% and 70% humidity.
"""

high_humidity = weather[
    (weather["Relative Humidity_%"] >= 60)
    & (weather["Relative Humidity_%"] <= 70)
]

plt.figure(figsize=(10, 4))

high_humidity_plot = sns.countplot(
    x="Weather Situation",
    data=high_humidity
)

high_humidity_plot.set_xticklabels(
    high_humidity_plot.get_xticklabels(),
    rotation=90
)

plt.title("Weather Situations at High Humidity")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 6.6 — High Humidity: Monthly Distribution
# ------------------------------------------------------------------

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=high_humidity
)

plt.title("Monthly Frequency of High Humidity")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


"""
RESULT

The query result found cloudy conditions to be
more prominent in this humidity range, although clear
conditions were also recorded.

These observations appeared during different parts
of the year.

INTERPRETATION

The comparison suggests that cloudier conditions
were more prominent within the higher humidity band.
"""


# ------------------------------------------------------------------
# 6.7 — Very High Humidity: Weather Situations
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

Which atmospheric conditions occur when relative
humidity reaches very high levels?

APPROACH

Select observations between 70% and 100% humidity.
"""

very_high_humidity = weather[
    (weather["Relative Humidity_%"] >= 70)
    & (weather["Relative Humidity_%"] <= 100)
]

plt.figure(figsize=(10, 4))

very_high_humidity_plot = sns.countplot(
    x="Weather Situation",
    data=very_high_humidity
)

very_high_humidity_plot.set_xticklabels(
    very_high_humidity_plot.get_xticklabels(),
    rotation=90
)

plt.title("Weather Situations at Very High Humidity")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 6.8 — Very High Humidity: Monthly Distribution
# ------------------------------------------------------------------

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=very_high_humidity
)

plt.title("Monthly Frequency of Very High Humidity")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


"""
RESULT

The analysis result observed very high humidity
during the early months of the year, with greater
prominence toward the end of the year.

The original report associated this later-year
pattern with winter conditions.

INTERPRETATION

The monthly distribution demonstrates that very high
humidity was not equally represented across the year.
"""


# ------------------------------------------------------------------
# 6.9 — Humidity and Weather Situation Summary
# ------------------------------------------------------------------

"""
KEY FINDINGS

LOW HUMIDITY
    Clear and partly cloudy conditions were prominent.
    More observations occurred around March–June.

FAIR HUMIDITY
    Clear and cloudy conditions were both represented.
    More observations occurred around March–July.

HIGH HUMIDITY
    Cloudy conditions became more prominent, while
    clear conditions remained present.

VERY HIGH HUMIDITY
    Observations appeared in the early months and
    were particularly prominent toward year-end.

ANALYTICAL SIGNIFICANCE

The investigation reveals differences in recorded
weather situations across humidity levels.

It also demonstrates how monthly comparisons can
provide additional context for atmospheric patterns.
"""


# ==================================================================
# STAGE 7 — MONTHLY TEMPERATURE ANALYSIS
# ==================================================================

"""
ANALYTICAL OBJECTIVE

Investigate how different temperature ranges are
distributed across the months of the year.

The original analysis divides temperature into four
categories:

    Cold:
        10°C or below

    Low:
        10°C through 20°C

    Fair:
        20°C through 30°C

    High:
        30°C through 40°C

Each category is examined separately to identify
the months in which its observations occur.

Monthly countplots provide a consistent approach
for comparing the frequency of each temperature band.
"""


# ------------------------------------------------------------------
# 7.1 — Cold Temperature: Monthly Frequency
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

During which months are temperatures of 10°C or below
most frequently recorded?
"""

cold_temperature = weather[
    weather["Temp_C"] <= 10
]

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=cold_temperature
)

plt.title("Monthly Frequency of Cold Temperatures")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 7.2 — Low Temperature: Monthly Frequency
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

How are temperatures between 10°C and 20°C
distributed across the year?
"""

low_temperature = weather[
    (weather["Temp_C"] >= 10)
    & (weather["Temp_C"] <= 20)
]

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=low_temperature
)

plt.title("Monthly Frequency of Low Temperatures")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 7.3 — Fair Temperature: Monthly Frequency
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

During which months are temperatures between
20°C and 30°C recorded?
"""

fair_temperature = weather[
    (weather["Temp_C"] >= 20)
    & (weather["Temp_C"] <= 30)
]

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=fair_temperature
)

plt.title("Monthly Frequency of Fair Temperatures")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 7.4 — High Temperature: Monthly Frequency
# ------------------------------------------------------------------

"""
ANALYTICAL QUESTION

During which months are temperatures between
30°C and 40°C recorded?
"""

high_temperature = weather[
    (weather["Temp_C"] >= 30)
    & (weather["Temp_C"] <= 40)
]

plt.figure(figsize=(10, 4))

sns.countplot(
    x="Month",
    data=high_temperature
)

plt.title("Monthly Frequency of High Temperatures")
plt.xlabel("Month")
plt.ylabel("Observation Count")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------
# 7.5 — Monthly Temperature Analysis Summary
# ------------------------------------------------------------------

"""
INTERPRETATION

The monthly comparisons examine how the occurrence
of different temperature ranges changes across
the recorded calendar periods.

When considered alongside the temperature histogram,
these charts provide two complementary perspectives:

    1. The overall distribution of temperature values.

    2. The monthly frequency of selected temperature
       categories.

Together, they help describe temporal variation
in the recorded temperature observations.
"""


# ==================================================================
# STAGE 8 — ANALYTICAL CONCLUSIONS
# ==================================================================

"""
CONCLUSION

The exploratory analysis examined historical weather
observations through frequency distributions, categorical
comparisons, and monthly patterns.

The frequency distributions highlighted prominent
ranges for three atmospheric measurements:

    Relative humidity:
        Approximately 60–80%.

    Temperature:
        Approximately -5°C to 25°C.

    Wind speed:
        Approximately 0–20 km/h.

The weather-situation analysis further examined the
conditions recorded at different humidity levels.

Clear and partly cloudy conditions were prominent
under low humidity, while cloudier conditions were
more evident in the higher humidity range.

Monthly comparisons showed that humidity categories
and temperature ranges varied across the year.

Together, these findings provide a descriptive
understanding of the recorded atmospheric conditions
and their temporal patterns.
"""
