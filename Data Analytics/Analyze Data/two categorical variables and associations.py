# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:49:07 2023

@author: geron
"""

# crosstab() function used to create 2 way tables or crosstabulations between 2 categorical variables

import pandas as pd


npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)



# Proportions is dividing the frequencies in a contingency table by the total number of observations.  sum of frequencies.  


import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)

# print out special_authority_prop
print(special_authority_prop)



# marginal proportions - the proportions in each category of a single question

import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

# save the table of frequencies as special_authority_freq:
special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)

# calculate and print authority_marginals
authority_marginals = special_authority_prop.sum(axis=0)
print(authority_marginals)

# calculate and print special_marginals
special_marginals = special_authority_prop.sum(axis=1)
print(special_marginals)


# expected proportions.  Get by multiplying the marginal proportions for each category.  Then convert to frequency by 
#multiplying by sample size


import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print("observed contingency table:")
print(special_authority_freq)

# calculate the expected contingency table if there's no association and save it as expected
expected, pval, dof, expected=chi2_contingency(special_authority_freq)

# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))



# chi-square statistics - summarize 2 tables.  we find the squared difference between each value in the observed table
# and its corresponding value in the expected table and then device by the expected table.  results should be higher than sample size for strong assocation

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# calculate the chi squared statistic and save it as chi2, then print it:

chi2, pval, dof, expected=chi2_contingency(special_authority_freq)
print(chi2)










