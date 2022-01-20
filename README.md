# Surf Shop in Oahu
SQLite and SQLAlchemy based analysis


## Overview

A client would like to analyze the feasibility of a Surf and Ice Cream Shop in tropical Oahu.  For the project to be viable, the year round temperatures and precipitation have to be favorable for the outdoors.  This analysis utilizes SQLite, SQLAlchemy, and pandas to read in temperature data for two months, June and Decemeber, to decide whether the weather is good for year-round patronage.  The descriptive statistics are provided in the images below for the June temperature data and the December temperature data.

### June Temps
![image](https://user-images.githubusercontent.com/59892063/150272503-df5605c0-7db7-4b2e-973c-d7180c16cdcf.png)

### December Temps
![image](https://user-images.githubusercontent.com/59892063/150272548-bfd3125d-1b7f-4690-9ee5-1d7e1c17ab81.png)

## Results

Fortunately, the weather in Hawaii is consistently perfect throughout the year.
- The average temperature in both June and December are almost identical.
- The standard deviation of the temperatures also shows minimal fluctuation from this ideal point.
- Unsurprisingly, the temperatures in December are slightly lower, but a few degrees, than in June.

## Summary
Overall, it is safe for the client to move forward with this venture. The temperatures are stable throughout the year in Hawaii, which means precipitation may contribute to some changes in customer level, but it is unlikely that there will be a quiet season in the shop.  This analysis could be improved by grouping the data by year to see if the average temperatures are consistently represenstative from year to year.  Additionally, comparing the precipitation with the temperatures for both months in a separate query would also improve the robustness of the analysis.
