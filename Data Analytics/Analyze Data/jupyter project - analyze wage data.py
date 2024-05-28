# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:50:54 2023

@author: geron
"""

Analyze Wage Data with Python
Task Group 1 - Import and Clean
Task 1
Display the first five lines of df_wages.

import pandas as pd

df_wages = pd.read_csv('wages.csv')

# Preview the data
df_wages.head()
Index	Occupation title (click on the occupation title to view its profile)	Year	Employment	Average hourly wage	Industry average	Similar occupation average
0	0	Management Occupations - Top Executives - Chie...	2021	200480	$102.41	$59.31	$57.94
1	1	Management Occupations - Top Executives - Gene...	2021	2984920	$55.41	$59.31	$57.94
2	2	Management Occupations - Top Executives - Legi...	2021	44590	NaN	$59.31	$57.94
3	3	Management Occupations - Advertising, Marketin...	2021	22520	$68.68	$59.31	$69.77
4	4	Management Occupations - Advertising, Marketin...	2021	278690	$73.77	$59.31	$69.77
Task 2
Rename the Occupation title (click on the occupation title to view its profile) column to Occupation title.

col_mapper = {'Occupation title (click on the occupation title to view its profile)':'Occupation title'}
df_wages = df_wages.rename(mapper = col_mapper, axis=1)

# show output
df_wages.head()
Index	Occupation title	Year	Employment	Average hourly wage	Industry average	Similar occupation average
0	0	Management Occupations - Top Executives - Chie...	2021	200480	$102.41	$59.31	$57.94
1	1	Management Occupations - Top Executives - Gene...	2021	2984920	$55.41	$59.31	$57.94
2	2	Management Occupations - Top Executives - Legi...	2021	44590	NaN	$59.31	$57.94
3	3	Management Occupations - Advertising, Marketin...	2021	22520	$68.68	$59.31	$69.77
4	4	Management Occupations - Advertising, Marketin...	2021	278690	$73.77	$59.31	$69.77
Task 3
Drop any redundant or otherwise unnecessary columns from df_wages. Make a note of why these columns are suitable for dropping!

drop_column_labels = ['Index', 'Year']
df_wages = df_wages.drop(labels=drop_column_labels, axis=1)

# show output
df_wages.head()
Occupation title	Employment	Average hourly wage	Industry average	Similar occupation average
0	Management Occupations - Top Executives - Chie...	200480	$102.41	$59.31	$57.94
1	Management Occupations - Top Executives - Gene...	2984920	$55.41	$59.31	$57.94
2	Management Occupations - Top Executives - Legi...	44590	NaN	$59.31	$57.94
3	Management Occupations - Advertising, Marketin...	22520	$68.68	$59.31	$69.77
4	Management Occupations - Advertising, Marketin...	278690	$73.77	$59.31	$69.77
Task 4
Display column information including names, # non-null entries, and data types.

df_wages.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 824 entries, 0 to 823
Data columns (total 5 columns):
 #   Column                      Non-Null Count  Dtype 
---  ------                      --------------  ----- 
 0   Occupation title            824 non-null    object
 1   Employment                  824 non-null    int64 
 2   Average hourly wage         764 non-null    object
 3   Industry average            824 non-null    object
 4   Similar occupation average  765 non-null    object
dtypes: int64(1), object(4)
memory usage: 32.3+ KB
Task Group 2 - Column Transformations
Task 5
Use pandas to split the information in the Occupation title column into new columns Industry, Level, and Occupation.

title_split = df_wages['Occupation title'].str.split('-', expand=True)
df_wages['Industry'] = title_split[0]
df_wages['Level'] = title_split[1]
df_wages['Occupation'] = title_split[2]

# show output
df_wages[['Occupation title', 'Industry', 'Level', 'Occupation']].head()
Occupation title	Industry	Level	Occupation
0	Management Occupations - Top Executives - Chie...	Management Occupations	Top Executives	Chief Executives
1	Management Occupations - Top Executives - Gene...	Management Occupations	Top Executives	General and Operations Managers
2	Management Occupations - Top Executives - Legi...	Management Occupations	Top Executives	Legislators
3	Management Occupations - Advertising, Marketin...	Management Occupations	Advertising, Marketing, Promotions, Public Re...	Advertising and Promotions Managers
4	Management Occupations - Advertising, Marketin...	Management Occupations	Advertising, Marketing, Promotions, Public Re...	Marketing Managers
Task 6
Remove any leading and trailing whitespaces in the columns Industry, Level, and Occupation.

df_wages['Industry'] = df_wages['Industry'].str.strip()
df_wages['Level'] = df_wages['Level'].str.strip()
df_wages['Occupation'] = df_wages['Occupation'].str.strip()
Task 7
Replace the '$' character in the columns Average hourly wage, Industry average, and Similar occupation average with an empty character '' (no space between the single quotes!).

df_wages['Average hourly wage'] = df_wages['Average hourly wage'].str.replace('$', '', regex=False)
df_wages['Industry average'] = df_wages['Industry average'].str.replace('$', '', regex=False)
df_wages['Similar occupation average'] = df_wages['Similar occupation average'].str.replace('$', '', regex=False)

# show output
df_wages[['Average hourly wage', 'Industry average', 'Similar occupation average']].head()
Average hourly wage	Industry average	Similar occupation average
0	102.41	59.31	57.94
1	55.41	59.31	57.94
2	NaN	59.31	57.94
3	68.68	59.31	69.77
4	73.77	59.31	69.77
Task 8
Convert the data types of the columns Average hourly wage, Industry average, and Similar occupation average from object to float.

df_wages['Average hourly wage']  = df_wages['Average hourly wage'].astype(float)
df_wages['Industry average'] = df_wages['Industry average'].astype(float)
df_wages['Similar occupation average'] = df_wages['Similar occupation average'].astype(float)

# show output
df_wages.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 824 entries, 0 to 823
Data columns (total 8 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Occupation title            824 non-null    object 
 1   Employment                  824 non-null    int64  
 2   Average hourly wage         764 non-null    float64
 3   Industry average            824 non-null    float64
 4   Similar occupation average  765 non-null    float64
 5   Industry                    824 non-null    object 
 6   Level                       824 non-null    object 
 7   Occupation                  824 non-null    object 
dtypes: float64(3), int64(1), object(4)
memory usage: 51.6+ KB
Task Group 3 - Comparison to Industry Average
Task 9
Calculate the difference between the average hourly wage and the industry average. Assign the difference to a new column Industry wage difference.

df_wages['Industry wage difference'] = df_wages['Average hourly wage'] - df_wages['Industry average']

df_wages[['Occupation', 'Average hourly wage', 'Industry average', 'Industry wage difference']].head()
Occupation	Average hourly wage	Industry average	Industry wage difference
0	Chief Executives	102.41	59.31	43.10
1	General and Operations Managers	55.41	59.31	-3.90
2	Legislators	NaN	59.31	NaN
3	Advertising and Promotions Managers	68.68	59.31	9.37
4	Marketing Managers	73.77	59.31	14.46
Task 10
Divide Industry wage difference by Industry average to convert the difference to a percent change. (You might want to multiply by 100 at the end to display as a percentage).

Assign the result to new column called Industry wage pctchg.

df_wages['Industry wage pctchg'] = df_wages['Industry wage difference']/df_wages['Industry average'] * 100

df_wages[['Industry', 'Occupation','Level', 'Average hourly wage', 'Industry average', 'Industry wage pctchg']].head()
Industry	Occupation	Level	Average hourly wage	Industry average	Industry wage pctchg
0	Management Occupations	Chief Executives	Top Executives	102.41	59.31	72.669027
1	Management Occupations	General and Operations Managers	Top Executives	55.41	59.31	-6.575620
2	Management Occupations	Legislators	Top Executives	NaN	59.31	NaN
3	Management Occupations	Advertising and Promotions Managers	Advertising, Marketing, Promotions, Public Rel...	68.68	59.31	15.798348
4	Management Occupations	Marketing Managers	Advertising, Marketing, Promotions, Public Rel...	73.77	59.31	24.380374
Task 11
Sort df_wages by the Industry wage pctchg column from highest to lowest. Assign the result to the variable highest_industry_pctchg.

highest_industry_pctchg = df_wages.sort_values(by='Industry wage pctchg', ascending=False)

highest_industry_pctchg[['Industry', 'Occupation','Level', 'Industry wage pctchg']].head(10)
Industry	Occupation	Level	Industry wage pctchg
329	Healthcare Practitioners and Technical Occupat...	Cardiologists	Healthcare Diagnosing or Treating Practitioners	288.538813
460	Personal Care and Service Occupations	Makeup Artists, Theatrical and Performance	Personal Appearance Workers	269.820656
328	Healthcare Practitioners and Technical Occupat...	Anesthesiologists	Healthcare Diagnosing or Treating Practitioners	263.515982
305	Healthcare Practitioners and Technical Occupat...	Oral and Maxillofacial Surgeons	Healthcare Diagnosing or Treating Practitioners	241.872146
331	Healthcare Practitioners and Technical Occupat...	Emergency Medicine Physicians	Healthcare Diagnosing or Treating Practitioners	240.981735
342	Healthcare Practitioners and Technical Occupat...	Orthopedic Surgeons, Except Pediatric	Healthcare Diagnosing or Treating Practitioners	236.118721
330	Healthcare Practitioners and Technical Occupat...	Dermatologists	Healthcare Diagnosing or Treating Practitioners	232.305936
339	Healthcare Practitioners and Technical Occupat...	Radiologists	Healthcare Diagnosing or Treating Practitioners	231.187215
344	Healthcare Practitioners and Technical Occupat...	Surgeons, All Other	Healthcare Diagnosing or Treating Practitioners	226.872146
335	Healthcare Practitioners and Technical Occupat...	Obstetricians and Gynecologists	Healthcare Diagnosing or Treating Practitioners	225.136986
Task Group 4 - Computer Jobs
Task 12
Lastly, let's take advantage of some of our earlier column transformations to zoom in on interesting industries.

Use the separate Industry column you created in Task 5 to investigate occupations in the 'Computer and Mathematical Occupations' industry. Filter df_wages for this specific industry and create a new DataFrame named cs_math_occupations.

cs_math_occupations = df_wages[df_wages['Industry'] == 'Computer and Mathematical Occupations']
Task 13
Sort cs_math_occupations by Average hourly wage from highest to lowest, and display the results. What do you notice?

cs_math_occupations_sorted = cs_math_occupations.sort_values(by='Average hourly wage',ascending=False)

# show output
cs_math_occupations_sorted.head(10)
Occupation title	Employment	Average hourly wage	Industry average	Similar occupation average	Industry	Level	Occupation	Industry wage difference	Industry wage pctchg
70	Computer and Mathematical Occupations - Comput...	30840	68.58	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Computer and Information Research Scientists	20.57	42.845241
83	Computer and Mathematical Occupations - Mathem...	23040	60.24	48.01	49.90	Computer and Mathematical Occupations	Mathematical Science Occupations	Actuaries	12.23	25.473860
75	Computer and Mathematical Occupations - Comput...	50440	58.58	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Database Architects	10.57	22.016247
78	Computer and Mathematical Occupations - Comput...	1364180	58.17	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Software Developers	10.16	21.162258
73	Computer and Mathematical Occupations - Comput...	168830	58.01	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Computer Network Architects	10.00	20.828994
69	Computer and Mathematical Occupations - Comput...	157220	54.46	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Information Security Analysts	6.45	13.434701
84	Computer and Mathematical Occupations - Mathem...	1770	54.05	48.01	49.90	Computer and Mathematical Occupations	Mathematical Science Occupations	Mathematicians	6.04	12.580712
87	Computer and Mathematical Occupations - Mathem...	105980	52.24	48.01	49.90	Computer and Mathematical Occupations	Mathematical Science Occupations	Data Scientists	4.23	8.810664
68	Computer and Mathematical Occupations - Comput...	505150	49.14	48.01	47.89	Computer and Mathematical Occupations	Computer Occupations	Computer Systems Analysts	1.13	2.353676
86	Computer and Mathematical Occupations - Mathem...	31370	47.81	48.01	49.90	Computer and Mathematical Occupations	Mathematical Science Occupations	Statisticians	-0.20	-0.416580
 