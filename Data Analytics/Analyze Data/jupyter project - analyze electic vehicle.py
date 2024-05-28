# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:45:29 2023

@author: geron
"""

Analyze Electric Vehicle Stations in Python
View Solution Notebook
View Project Page
Task Group 1 - Import and Explore
Task 1
Import the CSV file stations.csv and assign it to the variable stations.

import pandas as pd
stations = pd.read_csv('stations.csv')

# show output
stations.head()
fuel	state	owner	access	number_of_stations
0	biodiesel	AL	government	private	8
1	biodiesel	AL	private	public	2
2	biodiesel	AR	government	private	1
3	biodiesel	AR	private	public	16
4	biodiesel	AZ	government	private	74
What is the structure of this dataset? Toggle to check!
Task 2
When we start working with a new dataset, it's a good idea to get some summaries of the different columns, so that we know what kinds of values they contain.

Call .value_counts() on fuel to see the different kinds of fuel included in the dataset.

stations['fuel'].value_counts()
electric                  260
compressed natural gas    210
propane                   105
ethanol                    97
biodiesel                  70
liquefied natural gas      50
hydrogen                   27
Name: fuel, dtype: int64
Task 3
Call .value_counts() on owner to see the different kinds of owners included in the dataset.

stations['owner'].value_counts()
private            413
government         288
utility company    108
joint               10
Name: owner, dtype: int64
Task 4
Call .value_counts() on access to see the different kinds of access included in the dataset.

stations['access'].value_counts()
public     415
private    404
Name: access, dtype: int64
What did we discover using value counts? Toggle to check!
Task 5
Call .describe() on number_of_stations.

stations['number_of_stations'].describe()
count     819.000000
mean       34.741148
std       118.665095
min         1.000000
25%         2.000000
50%         5.000000
75%        20.500000
max      2423.000000
Name: number_of_stations, dtype: float64
Task 6
There's a pretty large maximum in the output to Task 5. Sort stations by number_of_stations from largest to smallest. What do the top 5 rows have in common?

stations = stations.sort_values(by='number_of_stations',ascending=False)
stations.head()
fuel	state	owner	access	number_of_stations
301	electric	CA	private	public	2423
456	electric	NY	private	public	1173
500	electric	TX	private	public	778
329	electric	FL	private	public	659
510	electric	VA	private	public	497
Task 7
Sort stations by number_of_stations from smallest to largest. What do the top 5 rows of the new sorted DataFrame have in common?

stations = stations.sort_values(by='number_of_stations',ascending=True)
stations.head()
fuel	state	owner	access	number_of_stations
117	compressed natural gas	GA	utility company	public	1
165	compressed natural gas	MN	government	private	1
166	compressed natural gas	MN	government	public	1
169	compressed natural gas	MN	utility company	private	1
361	electric	IN	utility company	private	1
What did we discover using sorting? Toggle to check!
Task Group 2 - Public Access Electric Charging
Task 8
Electric vehicles have become more and more crucial to plans around climate change. Let's take a closer look at stations that anyone can access.

Create a Boolean mask that is True for any row of stations where access is public.

is_public_access = stations['access'] == 'public'
Task 9
Create a Boolean mask that is True for any row of stations where fuel is electric.

is_electric = stations['fuel'] == 'electric'
Task 10
Use the Boolean masks from Tasks 8 and 9 to filter stations down to only rows that are both public-access and electric-fuel. Assign the result to the variable public_electric.

public_electric = stations[is_public_access & is_electric]
Task 11
Sort public_electric by number_of_stations from smallest to largest. Display the top 5 rows (corresponding to the smallest numbers of stations.)

public_electric = public_electric.sort_values(by='number_of_stations')
public_electric.head()
fuel	state	owner	access	number_of_stations
479	electric	RI	government	public	1
293	electric	AR	utility company	public	1
454	electric	NY	joint	public	1
451	electric	NV	utility company	public	1
403	electric	MN	utility company	public	1
Task 12
While we can't be sure that this trend continues, it certainly looks as if publicly-owned (government/utility) stations are less common than privately owned (which we saw in Task 6).

Let's compare privately- and publicly-owned stations. Create a Boolean mask that is True for each row of public_electric where owner is private.

is_privately_owned = public_electric['owner'] == 'private'
Task 13
Use the Boolean mask from Task 12 to filter public_electric down to only privately-owned rows. Assign the result to the variable privately_owned.

privately_owned = public_electric[is_privately_owned]
privately_owned.head()
fuel	state	owner	access	number_of_stations
430	electric	NE	private	public	26
325	electric	DE	private	public	30
539	electric	WY	private	public	34
491	electric	SD	private	public	37
282	electric	AK	private	public	37
Task 14
Let's check how many states have privately-owned, publicly-accessible electric charging stations. Call .describe() on the state column of privately_owned.

privately_owned['state'].describe()
count     51
unique    51
top       NE
freq       1
Name: state, dtype: object
What did we discover in Task 14? Toggle to check!
Task 15
Let's compare this to the publicly-owned stations. Use the Boolean mask you created in Task 12 to filter public_electric down to only rows with non-private ownership. Assign the result to the variable not_privately_owned.

not_privately_owned = public_electric[~is_privately_owned]
not_privately_owned.head()
fuel	state	owner	access	number_of_stations
479	electric	RI	government	public	1
293	electric	AR	utility company	public	1
454	electric	NY	joint	public	1
451	electric	NV	utility company	public	1
403	electric	MN	utility company	public	1
Task 16
Let's check how many states have publicly-owned, publicly-accessible electric charging stations. Call .describe() on the state column of not_privately_owned.

not_privately_owned['state'].describe()
count     83
unique    49
top       NC
freq       3
Name: state, dtype: object
What did we discover in Task 16? Toggle to check!
Task 17
Let's investigate publicly-owned stations a bit further. Call .describe() on the number_of_stations column of not_privately_owned.

not_privately_owned['number_of_stations'].describe()
count     83.000000
mean      17.927711
std       44.294409
min        1.000000
25%        1.000000
50%        6.000000
75%       17.000000
max      361.000000
Name: number_of_stations, dtype: float64
Task 18
The maximum number of stations is quite a bit larger than the 75th percentile. Let's look at the rows between these values.

Create a Boolean mask that is true in each row of not_privately_owned where the number_of_stations is bigger than 17 (the 75th percentile).

gt_17 = not_privately_owned['number_of_stations'] > 17
Task 19
Filter not_privately_owned down to only rows with number_of_stations bigger than 17. Assign the result to the variable above_17.

above_17 = not_privately_owned[gt_17]
above_17.head()
fuel	state	owner	access	number_of_stations
423	electric	NC	utility company	public	18
398	electric	MI	utility company	public	19
521	electric	WA	government	public	19
508	electric	VA	government	public	19
367	electric	KS	utility company	public	21
Task 20
Sort above_17 by number_of_stations and output the entirety of the result.

above_17.sort_values(by=['number_of_stations'],ascending=False)
fuel	state	owner	access	number_of_stations
299	electric	CA	government	public	361
453	electric	NY	government	public	145
311	electric	CT	government	public	106
484	electric	SC	government	public	63
305	electric	CO	government	public	59
418	electric	NC	government	public	50
475	electric	PA	government	public	46
303	electric	CA	utility company	public	40
460	electric	OH	government	public	39
327	electric	FL	government	public	32
331	electric	FL	utility company	public	31
390	electric	ME	government	public	31
384	electric	MD	government	public	30
438	electric	NJ	government	public	26
394	electric	MI	government	public	22
378	electric	MA	government	public	22
367	electric	KS	utility company	public	21
398	electric	MI	utility company	public	19
508	electric	VA	government	public	19
521	electric	WA	government	public	19
423	electric	NC	utility company	public	18
What did we discover in Task 20? Toggle to check!
Task Group 3 - West Coast
Task 21
In Task 20 we found that CA has

the largest number of government-owned public-access electric stations
the largest number of utility-owned public-access electric stations
In Task 6, the full sorted DataFrame shows that CA also has the most privately-owned public-access electric stations.

What about the rest of the west coast?

Create two Boolean masks:

the first should be True whenever the state column of public_electric is WA (Washington)
the second should be True whenever the state column of public_electric is OR (Oregon)
is_wa = public_electric['state'] == 'WA'
is_or = public_electric['state'] == 'OR'
Task 22
Filter public_electric down to only those rows where state is either WA or OR. Assign the result to the variable WA_or_OR.

WA_or_OR = public_electric[ is_wa | is_or]
Task 23
Sort WA_or_OR first by owner and then, within each owner, by number_of_stations. Display the full output.

WA_or_OR.sort_values(by=['owner','number_of_stations'],ascending=False)
fuel	state	owner	access	number_of_stations
525	electric	WA	utility company	public	4
473	electric	OR	utility company	public	1
523	electric	WA	private	public	402
471	electric	OR	private	public	282
521	electric	WA	government	public	19
469	electric	OR	government	public	16
What did we discover in Task 23? Toggle to check!
That's the end of the project, but you can always add more cells below to explore the dataset further!